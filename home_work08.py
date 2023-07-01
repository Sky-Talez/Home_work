from datetime import datetime, timedelta
from collections import defaultdict
import faker


def get_period() -> tuple[datetime.date, datetime.date]:
    today = datetime.now().date()
    start_period = today + timedelta(days=(5 - today.weekday()))
    return start_period, start_period + timedelta(6)
    

def get_birthdays_per_week(users : list[dict]) -> dict:
    week = defaultdict(list)
    curent_year = datetime.now().year
    start_week, end_week = get_period()
    for i in users:
        b_day = i["birthday"].replace(year= curent_year).date()
        if start_week <= b_day <= end_week:
            if b_day.weekday() in (5, 6):
                week["Monday"].append(i["name"]) 
            else:
                week[b_day.strftime("%A")].append(i["name"])
    return week



if __name__=="__main__":
    gen = faker.Faker()

    test_list = []
    for _ in range(1000):
        x = {"name": gen.first_name(), "birthday":  datetime.strptime(gen.date(), "%Y-%m-%d")}
        test_list.append(x)
    
    for k,v in get_birthdays_per_week(test_list).items():
        print(f"{k}: " + ", ".join(v))



