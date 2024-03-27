import machine, uos, utime, ds1302, onewire, ds18x20, bme280 
from machine import Pin, I2C, ADC
from esp8266_i2c_lcd import I2cLcd
from time import sleep
recv_buf="" # receive buffer global variable
print(), ("Machine: \t" + uos.uname()[4]), ("MicroPython: \t" + uos.uname()[3])
i2c=I2C(1,sda=Pin(14), scl=Pin(15), freq=400000)    #initializing the I2C method 
boton=Pin(22, Pin.IN, Pin.PULL_UP) #Pantalla LCD"""
pantalla=I2C(0, sda=machine.Pin(20),scl=machine.Pin(21),freq=400000)
lcd=I2cLcd(pantalla,0x27,2,16)
lcd.backlight_off()
led_b=machine.Pin(7,machine.Pin.OUT)#LED
led_g=machine.Pin(8,machine.Pin.OUT)#LED
led_r=machine.Pin(9,machine.Pin.OUT)#LED
led_g.value(0), led_b.value(0), led_r.value(0)
led_g.value(1)
relay_uno = Pin(18,machine.Pin.OUT)#Relay
relay_uno.on()
relay_dos = Pin(19,machine.Pin.OUT)
relay_dos.on()
lcd.backlight_on()#LCD
lcd.clear()
lcd.move_to(03,0)
lcd.putstr("Iniciando")
lcd.move_to(04,1)
lcd.putstr('sistema')
utime.sleep(5)
lcd.clear()
uart0 = machine.UART(0, baudrate=115200)
print(uart0)
def Rx_ESP_Data():
    recv=bytes()
    while uart0.any()>0:
        recv+=uart0.read(2)
    res=recv.decode('utf-8')
    return res
def Connect_WiFi(cmd, uart=uart0, timeout=3000):
    print("CMD: " + cmd)
    uart.write(cmd)
    utime.sleep(7.0)
    Wait_ESP_Rsp(uart, timeout)
    print()
def Send_AT_Cmd(cmd, uart=uart0, timeout=3000):
    print("CMD: " + cmd)
    uart.write(cmd)
    Wait_ESP_Rsp(uart, timeout)
    print()
def Wait_ESP_Rsp(uart=uart0, timeout=3000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        print(resp.decode())
    except UnicodeError:
        print(resp)
lcd.clear()
lcd.move_to(02,0)
lcd.putstr("Configurando")
lcd.move_to(02,1)
lcd.putstr('conexion-wifi')
Send_AT_Cmd('AT\r\n')          #Test AT startup
Send_AT_Cmd('AT+GMR\r\n')      #Check version information
Send_AT_Cmd('AT+CIPSERVER=0\r\n')      #Check version information
Send_AT_Cmd('AT+RST\r\n')      #Check version information
Send_AT_Cmd('AT+RESTORE\r\n')  #Restore Factory Default Settings
Send_AT_Cmd('AT+CWMODE?\r\n')  #Query the Wi-Fi mode
Send_AT_Cmd('AT+CWMODE=1\r\n') #Set the Wi-Fi mode = Station mode
Send_AT_Cmd('AT+CWMODE?\r\n')  #Query the Wi-Fi mode again
Connect_WiFi('AT+CWJAP="Beeline_2G_F1F558","fW3MKUtFoP"\r\n', timeout=5000) #Connect to AP
Send_AT_Cmd('AT+CIFSR\r\n',timeout=5000)    #Obtain the Local IP Address
Send_AT_Cmd('AT+CIPMUX=1\r\n')    #Obtain the Local IP Address
utime.sleep(1.0)
Send_AT_Cmd('AT+CIPSERVER=1,80\r\n')    #Obtain the Local IP Address
utime.sleep(1.0)
print ('Starting connection to ESP8266...')
lcd.clear()
lcd.move_to(03,0)
lcd.putstr("Iniciando")
lcd.move_to(03,1)
lcd.putstr('sensores')
ds = ds1302.DS1302(Pin(2), Pin(5), Pin(4))
ds.date_time([2022, 01, 16, 0, 00, 07, 0])
foto=ADC(28)
ds_pin = machine.Pin(13)
tem_tierra = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = tem_tierra.scan()
tierra=ADC(26)
resolucion=3.3/65535
resol=5.4/65535
#maximo=3.28
#minimo=1.0
tempint=ADC(4)
pir_uno= Pin(10, Pin.IN, Pin.PULL_DOWN)
pir_dos= Pin(11, Pin.IN, Pin.PULL_DOWN)
lcd.clear()
lcd.move_to(03,0)
lcd.putstr("Iniciando")
lcd.move_to(03,1)
lcd.putstr("Server-Web")
utime.sleep(10)
lcd.clear()
lcd.move_to(04,0)
lcd.putstr("Sistema")
lcd.move_to(03,1)
lcd.putstr("Iniciado")
#utime.sleep(5)
#led_g.value(1)
lcd.clear()
lcd.backlight_off()
lcd.clear()
count=0
led_g.value(0)
def pulsar(pin):
    global count
    count=count+1
    if(count >7):
        count=0
    if (count ==0):
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(00,0)
        lcd.putstr("Fecha:")
        lcd.move_to(06,0)
        lcd.putstr(str(D)+"/"+str(M)+"/"+str(Y))
        lcd.move_to(01,1)
        lcd.putstr("Hora:")
        lcd.move_to(07,1)
        lcd.putstr(str(hr)+":"+str(m)+":"+str(s))
        utime.sleep(10)
        lcd.clear()
        lcd.backlight_off()
    if (count ==1):
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(01,0)
        lcd.putstr("Temp-ambiente")
        lcd.move_to(05,1)
        lcd.putstr(str(temperatura))
        utime.sleep(10)
        lcd.clear()
        lcd.backlight_off()
    if (count ==2):
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(03,0)
        lcd.putstr("Hum-ambente")
        lcd.move_to(05,1)
        lcd.putstr(str(humedad))
        utime.sleep(10)
        lcd.clear()
        lcd.backlight_off()
    if (count ==3):
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(01,0)
        lcd.putstr("Pre-atmosfera")
        lcd.move_to(03,1)
        lcd.putstr(str(presion))
        utime.sleep(10)
        lcd.clear()
        lcd.backlight_off()
    if (count ==4):
        lcd.backlight_on()
        lcd.clear()
        lcd.move_to(01,0)
        lcd.putstr("Intensidad-Luz")
        lcd.move_to(06,1)
        lcd.putstr(str(luz)+"%")
        utime.sleep(10)
        lcd.clear()
        lcd.backlight_off()
    if (count ==5):
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(03,0)
        lcd.putstr("Temp-Terreno")
        lcd.move_to(04,1)
        lcd.putstr(str(tem_tierra.read_temp(rom)) +"C")
        utime.sleep(10)
        lcd.clear()
        lcd.backlight_off()
    if (count ==6):
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(01,0)
        lcd.putstr("Humedad-Terreno")
        lcd.move_to(04,1)
        lcd.putstr(str(hum_tierra) +"%")
        utime.sleep(10)
        lcd.clear()
        lcd.backlight_off()
boton.irq(handler=pulsar, trigger=Pin.IRQ_FALLING)
#led_g.value(0)
led_b.value(1)
while True:
    (Y,M,D,day,hr,m,s)=ds.date_time()
    print("Fecha y Hora"); print(ds.day(),ds.month(),ds.year(), sep="/");print(ds.hour(),ds.minute(),ds.second(), sep=":")
    temperaturaint=27-((tempint.read_u16()*resolucion)-0.706)/0.001721
    print("Temperatura Interna:"+str(temperaturaint)+"C")
    luz=round((foto.read_u16()/65535)*100,2)
    print("Intensidad de la Lus:" +str(luz)+"%")
    tem_tierra.convert_temp()
    for rom in roms:
        print("Temperatura del suelo:" +str(tem_tierra.read_temp(rom)-2)+"C")
    hum_tierra=round(((tierra.read_u16()*resol)*(-21.6449))+116.8827,2)
    print("Humedad de la tierra:" + str(hum_tierra) + "%")
    if hum_tierra<=30:# se enciende con OFF y se apaga con ON
        relay_uno.off()
    elif hum_tierra>=31:
        relay_uno.on()
    utime.sleep(2)
    bme = bme280.BME280(i2c=i2c)        #BME280 object created
    temperatura = bme.values[0]
    print("temperatura:" +str(bme.values[0]))#reading the value of temperature
    presion = bme.values[1]            #reading the value of pressure
    print("presion:" +str(bme.values[1]))
    humedad = bme.values[2]            #reading the value of humidity
    print("humedad:" +str(bme.values[2]))
    utime.sleep(2)
    if pir_uno.value() or pir_dos.value() == 1:
       led_b.value(0)
       led_r.value(1)
       print("movimiento")
    else:
       led_r.value(0)
       led_b.value(1) 
       print("no movimiento")
    res =""
    #led.value(1)#Encender Led
    res=Rx_ESP_Data()
    utime.sleep(2.0)
    if '+IPD' in res: # if the buffer contains IPD(a connection), then respond with HTML handshake
        id_index = res.find('+IPD')
        print("resp:")
        print(res)
        connection_id =  res[id_index+5]
        print("connectionId:" + connection_id)
        print ('! Incoming connection - sending webpage')
        uart0.write('AT+CIPSEND='+connection_id+',1800'+'\r\n')
        utime.sleep(1.0)
        uart0.write('HTTP/1.1 200 OK'+'\r\n')
        uart0.write('Content-Type: text/html'+'\r\n')
        uart0.write('Connection: close'+'\r\n')
        uart0.write(''+'\r\n')
        uart0.write('<!DOCTYPE HTML>'+'\r\n')
        uart0.write('<html><head>'+'\r\n')
        uart0.write('<title>CPA Carlos Manuel de Cespedes</title>'+'\r\n')
        uart0.write('<meta http-equiv=\"refresh\" content=\"10\">'+'\r\n')
        uart0.write('<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\'\r\n')
        uart0.write('<link rel=\"icon\" href=\"data:,\">'+'\r\n')
        uart0.write('<style>'+'\r\n')
        uart0.write('html {font-family: Arial; display: inline-block; text-align: center;}'+'\r\n')
        uart0.write('p {  font-size: 1.2rem;}'+'\r\n')
        uart0.write('body {  margin: 0;}'+'\r\n')
        uart0.write('.topnav { overflow: hidden; background-color: #000033; color: white; font-size: 1.7rem; }'+'\r\n')
        uart0.write('.content { padding: 20px; }'+'\r\n')
        uart0.write('.card { background-color: white; box-shadow: 2px 2px 12px 1px rgba(140,140,140,.5); }'+'\r\n')
        uart0.write('.cards { max-width: 700px; margin: 0 auto; display: grid; grid-gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }'+'\r\n')
        uart0.write('.reading { font-size: 1.7rem; }'+'\r\n')
        uart0.write('.card.temperature { color: #0e7c7b; }'+'\r\n')
        uart0.write('.card.humidity { color: #17bebb; }'+'\r\n')
        uart0.write('.card.pressure { color: hsl(113, 61%, 29%); }'+'\r\n')
        uart0.write('.card.gas { color: #5c055c; }'+'\r\n')
        uart0.write('</style>'+'\r\n')
        uart0.write('</head>'+'\r\n')
        uart0.write('<body{width:100%;}>'+'\r\n')
        uart0.write('<div class=\"topnav\">'+'\r\n')
        uart0.write('<h3>CPA Carlos Manuel de Cespedes</h3>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('<h2 style=color:#006666>Estacion meteorologica y analisis del suelo<center></h2>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('<div class=\"content\">'+'\r\n')
        uart0.write('<div class=\"cards\">'+'\r\n')
        uart0.write('<div class=\"card temperature\">'+'\r\n')
        uart0.write('<h4>Temperatura</h4><p><span class=\"reading\">' +str(temperatura)+ '</p>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('<div class=\"card temperature\">'+'\r\n')
        uart0.write('<h4>Humedad</h4><p><span class=\"reading\">' + str(humedad) + '</p>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('<div class=\"card temperature\">'+'\r\n')
        uart0.write('<h4>Presion</h4><p><span class=\"reading\">' + str(presion) + '</p>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('<div class=\"card temperature\">'+'\r\n')
        uart0.write('<h4>Luz en %</h4><p><span class=\"reading\">' + str(luz) + "%"'</p>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('<div class=\"card pressure\">'+'\r\n')
        uart0.write('<h4>Temperatura del Tierreno</h4><p><span class=\"reading\">' + str(tem_tierra.read_temp(rom)) + "C"'</p>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('<div class=\"card pressure\">'+'\r\n')
        uart0.write('<h4>Humedad del tierreno</h4><p><span class=\"reading\">' + str(hum_tierra) + "%"'</p>'+'\r\n')
        uart0.write('</div>'+'\r\n')
        uart0.write('</div></div>'+'\r\n')
        uart0.write('</body></html>'+'\r\n')
        utime.sleep(2.0)
        Send_AT_Cmd('AT+CIPCLOSE='+ connection_id+'\r\n') # once file sent, close connection
        utime.sleep(2.0)
        recv_buf="" #reset buffer
        print ('Waiting For connection...')         
