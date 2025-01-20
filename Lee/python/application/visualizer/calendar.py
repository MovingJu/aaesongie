import calendar
import matplotlib.pyplot as plt
from datetime import datetime

import data_csv

def create_calendar(year: int, month: int, days: list[int], amounts: list[int]):

    # 오늘 날짜 가져오기
    today = datetime.now()
    current_day = today.day if today.year == year and today.month == month else None

    # 날짜별 금액 데이터를 딕셔너리로 생성
    transactions = dict(zip(days, amounts))

    # 달력을 2D 배열로 생성
    cal = calendar.monthcalendar(year, month)

    # 달력 그리기
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('on')
    ax.set_xticks([])
    ax.set_yticks([])

    # 바탕색을 회색으로 설정
    ax.set_facecolor('gray')

    # 제목 표시
    ax.set_title(f"{year}Y {month}M", fontsize=20, weight='bold', pad=20)

    # 요일 헤더 생성
    week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for col, day in enumerate(week_days):
        ax.text(col, 6, day, ha='center', va='center', fontsize=14, weight='bold')

    # 날짜와 금액 데이터를 매핑하여 표시
    for row, week in enumerate(cal):
        for col, day in enumerate(week):
            if day != 0:  # 날짜가 있는 경우만 처리
                amount = transactions.get(day)  # 수정된 부분: 기본값을 없앰
                if amount is not None and amount != 0:  # 거래 금액이 있을 때만 색상 지정
                    if amount > 0:
                        color = 'blue'
                    elif amount < 0:
                        color = 'red'
                    else:
                        color = 'black'
                    ax.text(col, 5 - row, f"{day}\n{amount:+,}", ha='center', va='center',
                            fontsize=12, color=color)
                else:  # 거래 금액이 없을 경우 날짜만 표시
                    ax.text(col, 5 - row, f"{day}", ha='center', va='center',
                            fontsize=12, color='black')

                # 오늘 날짜 강조: 두꺼운 검은 테두리 박스 추가
                if day == current_day:
                    ax.add_patch(plt.Rectangle((col - 0.5, 5 - row - 0.5), 1, 1, 
                                                facecolor='lightgray',
                                                edgecolor='brown', linewidth=3))
                # 날짜를 둘러싼 기본 박스
                else:
                    ax.add_patch(plt.Rectangle((col - 0.5, 5 - row - 0.5), 1, 1, 
                                                facecolor='lightgray',
                                                edgecolor='gray', linewidth=1))

    # 격자선 스타일 추가 (수평선과 수직선) - 검은색으로 변경
    for x in range(8):
        ax.plot([x - 0.5, x - 0.5], [0.5, 6.5], color='black', linewidth=0.5)
    for y in range(1, 8):
        ax.plot([-0.5, 6.5], [y - 0.5, y - 0.5], color='black', linewidth=0.5)

    # 마진 설정
    plt.tight_layout()

    return fig





def calendar_gen():
    ymd, amount, _ = data_csv.read_set_data('data_csv/data.csv')


    year, month, day = data_csv.day_seper(ymd)

    day = [int(x) for x in day]

    day_idxed, amount_idxed = [], []

    k = 0
    for j in range(len(month) - 1):
        if month[j] != month[j+1]:
            day_idxed.append(day[k:j+1])
            amount_idxed.append(amount[k:j+1])

            k = j+1
        
        if j == len(month) - 2:
            day_idxed.append(day[k:])
            amount_idxed.append(amount[k:])



    month_seted = list(set(month))
    month_seted.sort()
    month_seted = [int(x) for x in month_seted]

    for i in range(len(day_idxed)):

        print(day_idxed[i], amount_idxed[i])

        fig = create_calendar(2025, month_seted[i], day_idxed[i], amount_idxed[i])

        fig.savefig(f'visualizer/graphs/{i + 1}month_calendar.png', dpi = 200, bbox_inches='tight')

if __name__ == "__main__":
    import time
    st = time.time()
    calendar_gen()
    et = time.time()