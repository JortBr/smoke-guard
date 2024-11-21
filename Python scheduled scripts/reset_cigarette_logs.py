import mysql.connector
import datetime

def reset_cigarette_logs():
    db = mysql.connector.connect(
        host="localhost",
        user="student",
        password="Student@123",
        database="smartguard"
    )

    cursor = db.cursor()

    # Haal de daily_limit op voor de gebruiker
    cursor.execute("SELECT daily_limit FROM limits WHERE user_id = 1 AND active = 1")
    result = cursor.fetchone()

    if not result:
        print("Fout: daily_limit niet gevonden voor de gebruiker.")
        return

    daily_limit = result[0]

    # Haal de huidige datum op
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Reset cigarettes_taken naar 0 en stel remaining_limit in op daily_limit
    cursor.execute("""
        UPDATE cigarette_usage_logs
        SET cigarettes_taken = 0, remaining_limit = %s
        WHERE date = %s AND user_id = 1
    """, (daily_limit, current_date))

    db.commit()
    cursor.close()
    db.close()

    print("Dagelijkse reset voltooid.")
if __name__ == "__main__":
    reset_cigarette_logs()