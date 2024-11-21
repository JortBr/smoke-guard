import serial
import requests
import time

# Configuratie
arduino_port = "COM3"
baud_rate = 9600
api_url_fetch = "http://192.168.153.127:5000/check_limit?device_id=1"
api_url_log = "http://192.168.153.127:5000/log_cigarette"

# Verstuurt get verzoek naar de api voor gegevens en zet de gegevens om naar json.
def fetch_data_from_api():
    try:
        response = requests.get(api_url_fetch)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

# Verstuurt een post verzoek naar de api met de waarde van het aantal sigaretten.
def send_to_api(counter_int):
    try:
        # Verstuur de counter naar de API
        response = requests.post(api_url_log, json={"counter": counter_int})
        if response.status_code == 200:
            print("Data succesvol verzonden naar API:", response.json())
        else:
            print(f"Fout bij verzenden naar API: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Fout bij het verzenden naar de API: {e}")

def send_data_to_arduino(ser, data):
    try:
        message = f"{data['cigarettes_taken']},{data['daily_limit']}\n"
        ser.write(message.encode())
        print("Data verzonden naar Arduino:", message)

        # Lees de reactie van Arduino
        response = ser.readline().decode('utf-8', errors='ignore').strip()
        if response.startswith("status:"):
            print("Arduino reactie:", response)
        else:
            print(f"Onverwachte reactie van Arduino: {response}")
    except serial.SerialException as e:
        print(f"Error in serial communication: {e}")

if __name__ == "__main__":
    try:
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        print(f"Succesvol verbonden met {arduino_port}")

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                print(f"Reactie van Arduino ontvangen: {line}")

                # Wanneer de knop wordt ingedrukt op Arduino, haal de API-gegevens op
                if line.isdigit():  # Controleer of het een geldig nummer is
                    counter = int(line)
                    api_data = fetch_data_from_api()
                    if api_data:
                        print("Data ontvangen van API:", api_data)
                        send_data_to_arduino(ser, api_data)

                        # Verstuur de counter naar de API
                        send_to_api(counter)  # Verzend de counter naar de API

            time.sleep(1)  # Verminder belasting
    except serial.SerialException as e:
        print(f"Fout bij seriële communicatie: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Seriële poort gesloten.")
