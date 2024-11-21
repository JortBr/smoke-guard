from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

db =  mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
        return "API is running!"

@app.route('/get_records', methods=['GET'])
def get_records():
        try:
                db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM records")
                records = cursor.fetchall()
                db.close()
                return jsonify(records)
        except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route("/record", methods=["POST"])
def record():
        data = request.get_json()
        counter = data.get("counter")

        cursor = db.cursor()
        cursor.execute("INSERT INTO records (counter) VALUES (%s)", (counter,))
        db.commit()
from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

db =  mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
        return "API is running!"

@app.route('/get_records', methods=['GET'])
def get_records():
        try:
                db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM records")
                records = cursor.fetchall()
                db.close()
                return jsonify(records)
        except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route("/record", methods=["POST"])
def record():
        data = request.get_json()
        counter = data.get("counter")

        cursor = db.cursor()
        cursor.execute("INSERT INTO records (counter) VALUES (%s)", (counter,))
        db.commit()
from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

db =  mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
        return "API is running!"

@app.route('/get_records', methods=['GET'])
def get_records():
        try:
                db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM records")
                records = cursor.fetchall()
                db.close()
                return jsonify(records)
        except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route("/record", methods=["POST"])
def record():
        data = request.get_json()
        counter = data.get("counter")

        cursor = db.cursor()
        cursor.execute("INSERT INTO records (counter) VALUES (%s)", (counter,))
        db.commit()
from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

db =  mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
        return "API is running!"

@app.route('/get_records', methods=['GET'])
def get_records():
        try:
                db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM records")
                records = cursor.fetchall()
                db.close()
                return jsonify(records)
        except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route("/record", methods=["POST"])
def record():
        data = request.get_json()
        counter = data.get("counter")

        cursor = db.cursor()
        cursor.execute("INSERT INTO records (counter) VALUES (%s)", (counter,))
        db.commit()
from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

db =  mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
        return "API is running!"

@app.route('/get_records', methods=['GET'])
def get_records():
        try:
                db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM records")
                records = cursor.fetchall()
                db.close()
                return jsonify(records)
        except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route("/record", methods=["POST"])
def record():
        data = request.get_json()
        counter = data.get("counter")

        cursor = db.cursor()
        cursor.execute("INSERT INTO records (counter) VALUES (%s)", (counter,))
        db.commit()
from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

db =  mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
        return "API is running!"

@app.route('/get_records', methods=['GET'])
def get_records():
        try:
                db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM records")
                records = cursor.fetchall()
                db.close()
                return jsonify(records)
        except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route("/record", methods=["POST"])
def record():
        data = request.get_json()
        counter = data.get("counter")

        cursor = db.cursor()
        cursor.execute("INSERT INTO records (counter) VALUES (%s)", (counter,))
        db.commit()
from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

db =  mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
        return "API is running!"

@app.route('/get_records', methods=['GET'])
def get_records():
        try:
                db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
                cursor = db.cursor(dictionary=True)
                cursor.execute("SELECT * FROM records")
                records = cursor.fetchall()
                db.close()
                return jsonify(records)
        except Exception as e:
                return jsonify({"error": str(e)}), 500

@app.route("/record", methods=["POST"])
def record():
        data = request.get_json()
        counter = data.get("counter")

        cursor = db.cursor()
        cursor.execute("INSERT INTO records (counter) VALUES (%s)", (counter,))
        db.commit()
       cursor.close()


        return jsonify({"status": "success", "counter_received": counter})

@app.route("/add_record", methods=["POST"])
def add_record():
        try:
                data = request.get_json()
                print(f"Ontvangen data: {data}")
                date = data.get("date")
                id = 1
                cigarettes_smoked = data.get("cigarettes_smoked")
                counter = data.get("counter")

                cursor = db.cursor()
                cursor.execute("SELECT cigarettes_smoked FROM Records WHERE id = %s", (id,))
                result = cursor.fetchone()

                if result:
                        current_cigarettes_smoked = result[0]
                else:
                        current_cigarettes_smoked = 0

                cursor.execute("SELECT * FROM Records WHERE id = %s AND date = %s", (id, date))
                existing_record = cursor.fetchone()

                if existing_record:
                        new_cigarettes_smoked = current_cigarettes_smoked + counter
                        cursor.execute("""UPDATE Records SET counter = %s, cigarettes_smoked = %s WHERE id = %s AND date = %s""", (counter, new_cigarettes_smoked, id, date))
                        db.commit()
                        response = {"message": "Record bijgewerkt!", "cigarettes_smoked": new_cigarettes_smoked}
                else:
                        new_cigarettes_smoked = current_cigarettes_smoked + counter
                        cursor.execute("""INSERT INTO Records (id, date, cigarettes_smoked, counter) VALUES (%s, %s, %s, %s)""", (id, date, cigarettes_smoked, counter))
                        db.commit()
                        response = {"message": "Record toegevoegd!"}
                cursor.close()               return jsonify(response), 200
        except Exception as e:
                return jsonify({"error": str(e)}), 400

@app.route("/log_cigarette", methods=["POST"])
def log_cigarette():
    try:
        data = request.get_json()
        counter_increment = data.get("counter")  # We gaan ervan uit dat dit steeds +1 is bij een druk op de knop

        # Verkrijg de huidige datum
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Query de daily limit voor de gebruiker
        cursor = db.cursor()
        cursor.execute("SELECT daily_limit FROM limits WHERE user_id = 1")
        limit_result = cursor.fetchone()

        if not limit_result:
            return jsonify({"error": "Daily limit niet gevonden!"}), 404

        daily_limit = limit_result[0]

        # Query de huidige daggegevens
        cursor.execute("""
            SELECT cigarettes_taken, remaining_limit 
            FROM cigarette_usage_logs 
            WHERE date = %s AND user_id = 1
        """, (current_date,))
        usage_result = cursor.fetchone()

        if usage_result:
            # Als er al een record voor vandaag bestaat, voeg alleen 1 toe
            cigarettes_taken = usage_result[0] + 1  # +1 bij elke druk op de knop
            remaining_limit = daily_limit - cigarettes_taken
        else:
            # Maak een nieuwe record aan als dit de eerste druk op de knop van de dag is
            cigarettes_taken = 1
            remaining_limit = daily_limit - cigarettes_taken

        # Zorg ervoor dat de remaining limit niet onder 0 gaat
        if remaining_limit < 0:
            remaining_limit = 0

        # Werk het log bij of voeg een nieuwe rij toe als het de eerste is voor vandaag
        if usage_result:
            cursor.execute("""
                UPDATE cigarette_usage_logs 
                SET cigarettes_taken = %s, remaining_limit = %s 
                WHERE date = %s AND user_id = 1
            """, (cigarettes_taken, remaining_limit, current_date))
        else:
            cursor.execute("""
                INSERT INTO cigarette_usage_logs (device_id, user_id, date, cigarettes_taken, remaining_limit) 
                VALUES (1, 1, %s, %s, %s)
            """, (current_date, cigarettes_taken, remaining_limit))

        db.commit()
        cursor.close()

        return jsonify({"message": "Data succesvol opgeslagen", "cigarettes_taken": cigarettes_taken, "remaining_limit": remaining_limit})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/check_limit", methods=["GET"])
def check_limit():
    try:
        device_id = request.args.get("device_id", type=int)
        if not device_id:
            return jsonify({"error": "Device ID is vereist."}), 400

        # Verkrijg de huidige datum
       current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Query om cigarettes_taken en daily_limit op te halen
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                c.cigarettes_taken,
                l.daily_limit
            FROM 
                cigarette_usage_logs c
            INNER JOIN 
                limits l 
            ON 
                c.user_id = l.user_id
            WHERE 
                c.device_id = %s AND c.date = %s AND l.active = 1
        """, (device_id, current_date))
        result = cursor.fetchone()
        cursor.close()

        if not result:
            return jsonify({"error": "Geen gebruiksgegevens gevonden voor deze dag."}), 404

        cigarettes_taken = result["cigarettes_taken"] or 0
        daily_limit = result["daily_limit"] or 0

        return jsonify({
            "cigarettes_taken": cigarettes_taken,
            "daily_limit": daily_limit
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
