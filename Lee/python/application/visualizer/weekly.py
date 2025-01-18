from datetime import datetime


import data_csv
import visualizer


def preprocessor():
    ymd, amount, total_amount = data_csv.read_set_data('data_csv/data.csv')


    year, month, day = data_csv.day_seper(ymd)
    week_day = []

    for i in ymd:
        imsi_date = datetime.strptime(i, "%Y-%m-%d")
        week_day.append(imsi_date.weekday())  # 월요일이 0, 일요일이 6

    # 주 단위 데이터 분리
    week_data = []
    temp_week = {"days": [], "amounts": [], "month": [], "week_start": "", "week_end": ""}

    for i, wd in enumerate(week_day):
        if wd == 0 and temp_week["days"]:  # 새로운 주 시작
            temp_week["week_end"] = ymd[i - 1]  # 이전 주의 끝 날짜
            week_data.append(temp_week)
            temp_week = {"days": [], "amounts": [], "month": [], "week_start": "", "week_end": ""}

        if not temp_week["week_start"]:  # 새로운 주의 시작 날짜 설정
            temp_week["week_start"] = ymd[i]

        # 주 데이터 추가
        temp_week["days"].append(day[i])
        temp_week["amounts"].append(total_amount[i])
        temp_week["month"].append(month[i])

    # 마지막 주 추가
    if temp_week["days"]:
        temp_week["week_end"] = ymd[-1]
        week_data.append(temp_week)


    return week_data




def weekly_gen():

    week_data = preprocessor()

    # 마지막 4개의 주만 선택
    recent_weeks = week_data[-4:]

    for i, week in enumerate(recent_weeks):
        # 마지막 주 확인
        is_last_week = (i == len(recent_weeks) - 1)

        # x축 라벨 처리
        if is_last_week:
            # 마지막 주의 요일 범위 계산
            start_weekday = datetime.strptime(f'2025-{week["month"][0]}-{week["days"][0]}', "%Y-%m-%d").weekday()
            week_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][start_weekday:start_weekday + len(week["days"])]
        else:
            # 완전한 주의 경우 고정된 라벨
            week_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        # y축 데이터 정렬: 월요일부터 마지막 요일까지
        y_values = week["amounts"][:len(week_labels)]



        # 그래프 생성
        fig, ax = visualizer.graph_gen(week_labels, y_values, figsize=(12, 8), 
                                        title=f'{week["month"][0]}M\'s {week["days"][0]} ~ {week["days"][-1]} Spent Amount',
                                        x_rotation=20, xticks=1,
                                        show_y=1)

        # 텍스트 라벨 추가
        ax = visualizer.graph_text_gen(week_labels, y_values, ax, show_level=0, show_text_level=4)

        # 그래프 저장
        fig.savefig(f'visualizer/graphs/{i}week.png', dpi=200)










if __name__ == "__main__":
    import time

    st = time.time()
    weekly_gen()
    et = time.time()
    print(et - st)
