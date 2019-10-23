# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:34:37 2019

@author: user
"""

from flask import Flask, render_template, request
from Car_price import preprocessing,predict

app = Flask(__name__)



@app.route('/')
def index():
    item_condition=['New','Used','Recon'] 
    brand=['AUDI','BENTLEY','BMW','CHERY','MERCEDES BENZ','PERODUA','MITSUBISHI','HYUNDAI','NISSAN','PROTON','PEUGEOT','TOYOTA','HONDA','MINI','SUBARU','MAZDA','NAZA','KIA','VOLKSWAGEN','LEXUS','SSANGYONG','SUZUKI','FORD','PORSCHE','CITROEN','ISUZU','JAGUAR','LAND ROVER','MASERATI','CHEVROLET','INOKOM']
    mileage=['0 - 4 999', '90 000 - 94 999', '60 000 - 64 999','45 000 - 49 999', '70 000 - 74 999', '100 000 - 109 999','80 000 - 84 999', '190 000 - 199 999', '20 000 - 24 999','120 000 - 129 999', '10 000 - 14 999', '5 000 - 9 999','40 000 - 44 999', '110 000 - 119 999', '55 000 - 59 999','95 000 - 99 999', '130 000 - 139 999', '200 000 - 249 999','15 000 - 19 999', '30 000 - 34 999', '170 000 - 179 999','75 000 - 79 999', '180 000 - 189 999', '35 000 - 39 999','65 000 - 69 999', '50 000 - 54 999', '85 000 - 89 999','150 000 - 159 999', '140 000 - 149 999', '25 000 - 29 999','300 000 - 349 999', '250 000 - 299 999', '160 000 - 169 999']
    variant=['TFSI','GT V8','sDrive20i (CKD)','PREMIUM','200 K ELEGANCE (CKD)','EZi','LITE','THETA II HIGH SPEC','LUXURY','ELEGANCE BASE LINE','THP','ALTIS V','VTEC','COUNTRYMAN','2.0I-P','2WD HIGH SPEC','GLS','CRDi','CC TSI (CBU)','T F-SPORT','II RX270 XDi','PREMIER','ECOBOOST','S 718','EXCLUSIVE','4x4 SINGLE CAB','S PREMIUM LUXURY','V8 SUPERCHARGED','Levante','4WD','PRIMA GL']
    car_type=['4D SEDAN', '4D WAGON', 'DUAL CAB PICKUP', '4D HATCHBACK','2D HATCHBACK', '4D VAN', 'WINDOW VAN', '4D DOUBLE CAB PICK-UP','2D COUPE', '2D ROADSTER', 'SINGLE CAB P/UP', '4D COUPE','2D CONVERTIBLE', 'SEMI PANEL VAN', '2D CABRIOLET', '4D MPV']
    transmission=['7 SP AUTOMATIC G-TRONIC', '5 SP MANUAL', '6 SP AUTOMATIC','5 SP AUTOMATIC', 'CONTINUOUS VARIABLE', '4 SP AUTOMATIC','6 SP AUTOMATIC TIPTRONIC', '7 SP AUTOMATIC TIPSHIFT','CVT AUTO 7 SP SEQUENTIAL', 'AUTOMATIC CONSTANTLY VARIABLE (CVT)','9 SP AUTOMATIC 9G-TRONIC', '4 SP AUTO SPORTS MODE','CONTINUOUS VARIABLE TRANSMISSION', 'CVT AUTO 6 SP SEQUENTIAL','CONSTANTLY VARIABLE (CVT)', '8 SP AUTOMATIC']
    fuel_type=['PETROL','DIESEL']
    front_brakes=['DC','DS','DV','NSD','VD','Vented Disc(330 mm)','Ventilated Disc','Ventilated Discs']
    rear_brakes=['DC','DS','DV','NSD','VD','Vented Disc(330 mm)','Disc','Ventilated Discs','Discs','DR','Drum','Drums','Hydraulic Disc','Solid Disc']
    return render_template('front_view.html',item_condition=item_condition,brand=brand,mileage=mileage,variant=variant,car_type=car_type,transmission=transmission,fuel_type=fuel_type,front_brakes=front_brakes,rear_brakes=rear_brakes)

@app.route('/prediction',methods=['POST'])
def cardata():
    if request.method=='POST':
        item_condition=request.form.get("condition")
        brand=request.form.get("brand")
        mil=request.form.get("mileage")
        variant=request.form.get("var")
        car_type=request.form.get("type")
        transmission=request.form.get("trans")
        engine_cc=request.form.get("engine")
        peak_power=request.form.get("power")
        fuel_type=request.form.get("fuel")
        height=request.form.get("height")
        fuel_tank=request.form.get("tank")
        front_brakes=request.form.get("f_brakes")
        rear_brakes=request.form.get("r_brakes")
        
    d=[item_condition,brand,mil,variant,car_type,transmission,engine_cc,peak_power,fuel_type,height,fuel_tank,front_brakes,rear_brakes]
    X=preprocessing(d)
    y=predict(X)

    return render_template('success.html',y=y,item_condition=item_condition,brand=brand,mil=mil,variant=variant,car_type=car_type,transmission=transmission,engine_cc=engine_cc,peak_power=peak_power,fuel_type=fuel_type,height=height,fuel_tank=fuel_tank,front_brakes=front_brakes,rear_brakes=rear_brakes)
	

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=50025)
