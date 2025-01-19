import matplotlib
import matplotlib.pyplot as plt
import data_csv
import time
from matplotlib import font_manager

font_path = "NanumGothicBold.ttf"
font_prop = font_manager.FontProperties(fname=font_path)

matplotlib.rcParams['font.family'] = font_prop.get_name()
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


def preprocess_data(file_path):
    """
    데이터 전처리 함수: 날짜, 메모, 금액 등 데이터를 처리.
    """
    date, note, amount, total_amount = data_csv.read_data(file_path)
    ymd, hnm, sec = data_csv.time_seper(date)
    year, month, day = data_csv.day_seper(ymd)

    # 날짜와 월/일 조합 리스트 생성
    mnd = [f"{month[i]}-{day[i]}" for i in range(len(month))]

    return mnd, total_amount


def graph_gen(xlist, ylist, xlable='date', ylable='total_amount', xticks=2,
              figsize=(12, 9), title='그래프 제목', x_rotation=45,
              show_y = 1):
    """
    그래프 생성 함수
    """
    _, _, _, total_amount = data_csv.read_data('data_csv/data.csv')

    fig, ax = plt.subplots(figsize=figsize, facecolor='lightgray')  # 그래프 크기 조정 및 배경색 설정
    ax.plot(xlist, ylist, color='black', marker='o', linestyle='-.', label='데이터')

    # 기준선 추가 (ylist 첫 번째 값 사용)
    if show_y == 1:
        ax.axhline(y=total_amount[0], color='red', linestyle=':', linewidth=1.5, alpha=1, label='기준선')

    # 그래프 제목 및 라벨
    ax.set_title(title, color='black')
    ax.set_xlabel(xlable, loc='left', color='black')
    ax.set_ylabel(ylable, loc='center', color='black')

    # X축 눈금 조정
    ax.set_xticks(range(0, len(xlist), xticks))
    ax.set_xticklabels(xlist[::xticks], rotation=x_rotation, ha='center')

    # 격자선 설정
    ax.grid(color='black', alpha=0.5, linestyle='--', linewidth=1)

    # 배경색 설정
    ax.set_facecolor('lightgray')


    return fig, ax


if __name__ == "__main__":
    # 데이터 전처리
    file_path = 'data_csv/data.csv'
    xlist, ylist = preprocess_data(file_path)

    # 그래프 생성
    fig, ax = graph_gen(xlist, ylist, title='총 소비량', xticks=7)

    for idx, txt in enumerate(ylist):

        try: 

            txt = round(txt/1e6, 3)

            # print(b_txt, txt)

            if ylist[idx -1] <= ylist[idx] <= ylist[idx + 1]\
                or ylist[idx -1] >= ylist[idx] >= ylist[idx + 1]:
                continue

            # print(idx)

            b_txt = txt

            # print('b_txt=', b_txt)

            ax.text(xlist[idx], ylist[idx] + 0.4, txt, 
                        ha='center', color='blue', rotation=20)
            
        except:
            pass

    # 그래프 저장
    fig.savefig('graphs/total.png', dpi=300, bbox_inches='tight')  # 그래프를 PNG로 저장
    print("그래프가 'graphs/total.png'로 저장되었습니다.")
