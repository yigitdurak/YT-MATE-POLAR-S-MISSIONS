import datetime

date = datetime.datetime


def input_date():
    while True:
        mt_date = input("enter the midterms date day/month/year hour:minute : ")
        try:
            realdate = date.strptime(mt_date, "%d/%m/%Y %H:%M")
            return realdate
        except ValueError:
            print("enter proper date")


def main():
    mt_date = input_date()
    print(f"Midterm time set: {mt_date}")
    now = datetime.datetime.now()
    remained_time = mt_date - now
    if remained_time.total_seconds() >= 0:
        day = remained_time.days
        hour = remained_time.seconds // 3600
        minute = (remained_time.seconds % 3600) // 60
        print(f"{day} days {hour} hours {minute} minutes left")
    else:
        print("you missed midterm hahahaahaha")


main()
