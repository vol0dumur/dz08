from datetime import date, datetime, timedelta

DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

def get_birthdays_per_week(users: list) -> dict:
    """Receives a list of dictionaries with employee data 
    and returns a dictionary with employee birthdays for the next week."""

    check_next_year = False

    # Спочатку результат записуємо у list, який потім перетворимо на dict.
    result_list = [[], [], [], [], []]

    today_date = date.today()

    # Якщо сьогодні неділя, то зсуваємо діапазон дат назад на 1 день, 
    #  щоб захопити і суботу.
    if today_date.weekday() == 6:
        today_date = today_date + timedelta(days=-1)

    # Задаємо кінець діапазону дат.
    today_date_plus_week = today_date + timedelta(days=6)

    # Якщо кінцева дата діапазону в наступному році - 
    #  треба приділити увагу до перевірки дат січня.
    if today_date.year < today_date_plus_week.year:
        check_next_year = True

    for item in users:

        # Замінюємо рік у оригінальній даті для зручного порівняння.
        if check_next_year and item["birthday"].month == 1:
            check_date = item["birthday"].replace(year=today_date.year + 1)
        else:
            check_date = item["birthday"].replace(year=today_date.year)

        # Порівнюємо дати.
        if today_date <= check_date <= today_date_plus_week:

            if check_date.weekday() in (5, 6):
                result_list[0].append(item["name"])
            else:
                result_list[check_date.weekday()].append(item["name"])

    result_dict = {}

    # Перетворюємо list у dict. Це потрібно, щоб dict був впорядкований
    #  за днем тижня, інакше буде провалено тест 5.
    for i in range(5):

        if len(result_list[i]):

            result_dict.update({DAYS_OF_WEEK[i]: []})

            for j in result_list[i]:
                result_dict[DAYS_OF_WEEK[i]].append(j)

    return result_dict