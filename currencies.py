import requests
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def get_dir(cur, prev):
    if prev is None:
        return "same"
    # To avoid floating point noise flagging as up/down, add a tiny epsilon or just use round
    cur_r = round(cur, 4)
    prev_r = round(prev, 4)
    if cur_r > prev_r:
        return "up"
    elif cur_r < prev_r:
        return "down"
    return "same"

def fetch_data(days=30):
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=days)
    url = f"https://api.frankfurter.app/{start_date}..{today}?from=TRY"
    
    try:
        data = requests.get(url).json()
    except:
        return {}

    rates_by_date = data.get("rates", {})
    sorted_dates = sorted(rates_by_date.keys())
    
    if not sorted_dates:
        return {}
        
    result = {}
    last_day = sorted_dates[-1]
    available_currencies = rates_by_date[last_day].keys()
    
    for currency in available_currencies:
        times = []
        alis_list = []
        
        for date_str in sorted_dates:
            day_rates = rates_by_date[date_str]
            if currency in day_rates:
                try:
                    # from=TRY -> 1 TRY = X Currency.
                    # So 1 Currency = 1 / X TRY
                    rate_in_try = 1.0 / day_rates[currency]
                    alis_list.append(rate_in_try)
                    # Format date to match UI nicely (e.g. DD.MM)
                    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                    times.append(dt.strftime("%d.%m"))
                except ZeroDivisionError:
                    continue
                    
        if len(alis_list) > 0:
            current_alis = alis_list[-1]
            prev_alis = alis_list[-2] if len(alis_list) > 1 else current_alis
            
            result[currency] = {
                "tur": "Döviz",
                "alis": current_alis,
                "satis": current_alis, # Frankfurter provides mid-market rates
                "alis_dir": get_dir(current_alis, prev_alis),
                "satis_dir": get_dir(current_alis, prev_alis),
                "history": {
                    "times": times,
                    "alis": alis_list,
                    "satis": alis_list
                }
            }
            
    return result

@app.route("/")
def home():
    result = fetch_data()
    return render_template("currencies.html", data=result)

@app.route("/api/data")
def api_data():
    days_param = request.args.get('days', '30')
    try:
        days = int(days_param)
        if days > 1825: days = 1825 # limit 5 years
        if days < 2: days = 2
    except:
        days = 30
    return fetch_data(days)

if __name__ == "__main__":
    app.run(debug=True)