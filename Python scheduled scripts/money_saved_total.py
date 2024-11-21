import mysql.connector

# Verbinding maken met de database
db = mysql.connector.connect(
    host="localhost",
    user="student",
    password="Student@123",
    database="smartguard"
)

cursor = db.cursor()

# Selecteer het meest recente record (hoogste entry_id) voor user_id = 1
cursor.execute("""
    SELECT entry_id, daily_usage, pack_price, COALESCE(money_saved, 0) AS total_savings 
    FROM costs_and_savings 
    WHERE user_id = 1 
    ORDER BY entry_id DESC LIMIT 1
""")
result = cursor.fetchone()

if result:
    entry_id, daily_usage, pack_price, total_savings = result

    # Bereken de prijs per sigaret op basis van daily_usage en pack_price
    price_per_cigarette = pack_price / daily_usage if daily_usage > 0 else 0

    # Haal de huidige waarde van cigarettes_taken op uit cigarette_usage_logs
    cursor.execute("""
        SELECT cigarettes_taken 
        FROM cigarette_usage_logs 
        WHERE user_id = 1 
        ORDER BY log_id DESC LIMIT 1
    """)
    usage_result = cursor.fetchone()

    if usage_result:
        cigarettes_taken = usage_result[0]
                                                                                
        # Bereken het aantal sigaretten dat is bespaard
        cigarettes_saved = daily_usage - cigarettes_taken

        # Bereken de dagelijkse besparing in geld
        daily_money_saved = round(cigarettes_saved * price_per_cigarette, 2)

        # Bereken de nieuwe totale besparing
        updated_total_savings = round(total_savings + daily_money_saved, 2)

        # Werk de totale besparing bij in het juiste record in costs_and_savings
        cursor.execute("""
            UPDATE costs_and_savings 
            SET money_saved = %s 
            WHERE entry_id = %s
        """, (updated_total_savings, entry_id))
        db.commit()

        print(f"Daily money saved: €{daily_money_saved}")
        print(f"Updated total money saved: €{updated_total_savings}")
    else:
        print("Geen gegevens gevonden in cigarette_usage_logs.")
else:
    print("Geen gegevens gevonden in costs_and_savings.")

# Sluit de cursor en de databaseverbinding
cursor.close()
db.close()