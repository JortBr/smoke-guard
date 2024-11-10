from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
	host="localhost",
	user="student",
	password="Student@123",
	database="smartguard"
)

@app.route("/", methods=["GET"])
def home():
	return "API is running!"

@app.route('/get_records', methods=["GET"]
def get_records():
	try:
		db = mysql.connector.connect(host="localhost", user="student", password="Student@123", database="smartguard")
		cursor = db.cursor(dictionary=True)
		cursor.execute("SELECT * FROM records)
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

	return jsonify({"status": "success", "counter_received": counter })

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
