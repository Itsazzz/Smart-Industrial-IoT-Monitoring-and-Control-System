import serial  # import serial pacakge
import mysql.connector
from datetime import datetime
import time
arduino = serial.Serial('COM3', 9600, timeout=.1)
count = 0
cost_per_kWh = 0.12
date = datetime.now().strftime('%Y-%m-%d')
conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
                    # cursor = conn.cursor()
cur = conn.cursor()
cur.execute("SELECT * FROM iotdata where date='"+date+"'")
data1 = cur.fetchone()
if data1 is None:
    total_energy_kWh = 0.0
    total_cost = 0.0

else:
    total_energy_kWh = float(data1[8])

    total_cost = float(data1[9])






time_now = datetime.now().strftime("%H:%M:%S")
#date = datetime.now().strftime('%Y-%m-%d')
while True:
    data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
    if data:
        data = data.decode('utf-8')
        data_v = str(data)

        print(data_v)
        data=str(data_v)
        data =  data.split(",")
        print(data)

        voltage = float(data[0].replace(' V', ''))
        current = float(data[1].replace(' A', ''))

        # Calculate power in watts (W)
        power = voltage * current  # P = V * I (in watts)

        # Calculate energy in kWh (assuming 1-second intervals)
        energy_kWh = (power / 1000) * (1 / 3600)  # Energy in kWh for each second

        # Accumulate total energy consumed
        total_energy_kWh += energy_kWh

        # Calculate the cost of energy used (in USD)
        total_cost = total_energy_kWh * cost_per_kWh
        u=f"{total_energy_kWh:.6f}"
        c=f"{total_cost:.4f}"

        # Display the results
        print(f"Voltage: {voltage:.2f} V, Current: {current:.2f} A")
        print(f"Power: {power:.2f} W, Energy (Units): {total_energy_kWh:.6f} kWh, Cost: ${total_cost:.4f}")





        time_now = datetime.now().strftime("%H:%M:%S")
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
                    # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM iotdata where date='"+date+"'")
        data1 = cur.fetchone()
        if data1 is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO iotdata VALUES ('','"+str(date)+"','" + str(data[0]) + "','" + str(data[1]) + "','" + str(
                    data[2]) + "','"+str(data[3])+"','"+str(data[4])+"','"+str(time_now)+"','"+str(u)+"','"+str(c)+"')")
            conn.commit()
            conn.close()

        else:
            time_now = datetime.now().strftime("%H:%M:%S")
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
            cursor = conn.cursor()
            cursor.execute("update iotdata set voltage='" + str(data[0]) + "',current='" + str(data[1]) + "',load_temperature='" + str(data[2]) + "',envi_temp='" + str(data[3]) + "',envi_humidity='" + str(data[4]) + "',time='"+str(time_now)+"',unit='"+str(u)+"',amount='"+str(c)+"' where date='" + str(date) + "' ")
            conn.commit()
            conn.close()

        conn2 = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
        # cursor = conn.cursor()
        cur2 = conn2.cursor()
        cur2.execute("SELECT * FROM iotdata1")
        data2 = cur2.fetchone()
        if data2[1] == '1':
            time.sleep(2)
            arduino.write(b'1')
            time.sleep(0.5)
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
            cursor = conn.cursor()
            cursor.execute("update iotdata1 set status='0' where id='1' ")
            conn.commit()
            conn.close()

        elif data2[1] == '2':
            time.sleep(2)
            arduino.write(b'2')

            time.sleep(0.5)
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
            cursor = conn.cursor()
            cursor.execute("update iotdata1 set status='0' where id='1' ")
            conn.commit()
            conn.close()
        elif data2[1] == '3':
            time.sleep(2)
            arduino.write(b'3')
            time.sleep(0.5)
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='cyberiot')
            cursor = conn.cursor()
            cursor.execute("update iotdata1 set status='0' where id='1' ")
            conn.commit()
            conn.close()



























