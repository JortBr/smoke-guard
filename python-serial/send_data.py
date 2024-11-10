import serial
import requests
import time

# Configuratie van de seriële poort
arduino_port = 'COM3'  # Aanpassen naar jouw seriële poort (bijvoorbeeld COM3 op Windows)
baud_rate = 9600
try:
    ser = serial.Serial(arduino_port, baud_rate)
    print(f"Succesvol verbonden met {arduino_port}")
except serial.SerialException as e:
    print(f"Fout bij het verbinden met de seriële poort {arduino_port}: {e}")
    exit()

# API endpoint op de VM
api_url = 'http://192.168.153.127:5000/record'  # Vervang 192.168.1.100 met het IP-adres van je VM

while True:
    try:
        # Controleer of er data beschikbaar is om te lezen van de seriële poort
        if ser.in_waiting > 0:
            # Lees de data van de seriële poort
            counter = ser.readline().decode().strip()
            print(f"Counter ontvangen: {counter}")

            # Controleer of de ontvangen waarde een geldig nummer is
            try:
                counter_int = int(counter)
                print(f"Verstuurde counter: {counter_int}")

                # Stuur een POST-verzoek naar de API
                response = requests.post(api_url, json={"counter": counter_int})
                print("Response van server:", response.json())

            except ValueError:
                print(f"Ongeldige data ontvangen: {counter}")
            except requests.exceptions.RequestException as e:
                print(f"Fout bij het verzenden naar de API: {e}")
        
        else:
            print("Geen data beschikbaar op de seriële poort...")
        
        time.sleep(1)  # Vertraging om overbelasting van de seriële poort en de API te voorkomen

    except Exception as e:
        print(f"Er is een onverwachte fout opgetreden: {e}")
        break  # Stop de lus als er iets fout gaat