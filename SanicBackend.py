#!/usr/bin/env python3
# pylint: disable=C0116,C0103,C0115,C0209

import serial
from sanic import Sanic,json
from sanic.response import file

#ser = serial.Serial('COM15',baudrate=115200)
# ser = serial.Serial('/dev/ttyACM0',baudrate=115200)
ser = serial.Serial('/dev/tty.usbserial-57670823091',baudrate=115200)

app = Sanic("Q101HM")

@app.exception(Exception)
async def catch_anything(request, exception):
    print("Exception:",exception)
    return json({"success":False,"message":"E99 : Unhandled Exception!","RAW":""})

@app.get("/emergencystop",name="emergencystop")
async def emergencystop(request):
    if request.args.get("devid").upper() != "09DF2712":
        return json({"success":False,"message":"E00 : Invalid Device ID!","RAW":request.args.get("devid").upper()})
    
    resplist = []
    for i in range(64):
        ser.reset_input_buffer()
        ser.write(b'\x8F2'+i.to_bytes(1, 'big')+b'\x00\x00')
        data = ser.read(5)
        resplist.append(' '.join([f"{i:02X}" for i in data]))
    return json({"success":True,"message":"success","RAW":resplist})

@app.get("/setvolt",name="setvolt")
async def setvolt(request):
    if request.args.get("devid").upper() != "09DF2712":
        return json({"success":False,"message":"E00 : Invalid Device ID!","RAW":request.args.get("devid").upper()})

    ch = int(request.args.get("ch"))-1
    if ch<0 or ch>=64:
        return json({"success":False,"message":"E01 : Invalid channel number!","RAW":request.args.get("ch")})

    volt = float(request.args.get("V"))
    volt = int(volt/10*65535)
    if volt<0 or volt>65535:
        return json({"success":False,"message":"E02 : Invalid voltage setting!","RAW":request.args.get("V")})

    ser.reset_input_buffer()
    ser.write(b'\x8F2'+ch.to_bytes(1, 'big')+volt.to_bytes(2, 'little'))
    data = ser.read(5)
    resp = ' '.join([f"{i:02X}" for i in data])
    return json({"success":True,"message":"success","RAW":resp})


@app.get("/getvolt",name="getvolt")
async def getvolt(request):
    if request.args.get("devid").upper() != "09DF2712":
        return json({"success":False,"message":"E00 : Invalid Device ID!","RAW":request.args.get("devid").upper()})

    ch = int(request.args.get("ch"))-1
    if ch<0 or ch>=64:
        return json({"success":False,"message":"E01 : Invalid channel number!","RAW":request.args.get("ch")})

    #getvolt
    ser.reset_input_buffer()
    ser.write(b'\x8F0'+ch.to_bytes(1, 'big')+b'\x00\x00')
    data = ser.read(5)
    resp1 = ' '.join([f"{i:02X}" for i in data])
    volt = (int.from_bytes(data[3:],"little"))/65536.0*10

    #getcurr
    ser.reset_input_buffer()
    ser.write(b'\x8F1'+ch.to_bytes(1, 'big')+b'\x00\x00')
    data = ser.read(5)
    resp2 = ' '.join([f"{i:02X}" for i in data])
    curr = (int.from_bytes(data[3:],"little"))/65536.0*100

    return json({"success":True,"message":"success","volt":volt,"amp":curr,"RAW":[resp1,resp2]})

@app.route('/')
async def index(request):
    return await file('./dist/index.html')

@app.route('/<filename:path>')
async def serve_file(request, filename):
    return await file(f'./dist/{filename}')

@app.middleware('response')
async def add_cors_headers(request, response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=6661,single_process = True)
