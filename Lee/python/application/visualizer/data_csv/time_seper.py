from .def_li_applyer import li_applyer

def middle_deco(func_str: 'function', func_list: 'function') -> 'function':
    """전체 날짜를 유연하게 일/시및분/초 로 나눠주는 함수
    decorator문법으로 정의됨."""

    def deco(func):

        def wrapper(input_data):
            if isinstance(input_data, str):
                return func_str(input_data)
            elif isinstance(input_data, list):
                return func_list(input_data)
            else:
                raise TypeError("Input must be either a string or a list.")
            
        return wrapper
    
    return deco


def str_time_seper(date: str) -> tuple[str, str, str]:

    
    try:

        day, time = date.split('/')
        hnm, sec = time.split(';')

        return (day, hnm, sec)

    except Exception as e:
        print("an error occured:", e)

        return (None, None, None)
    

    
def li_time_seper(li:list[str]) -> list[tuple[str, str, str]]:

    day, hnm, sec = [], [], []
    
    for i in li_applyer(str_time_seper, li):


        day.append(i[0])
        hnm.append(i[1])
        sec.append(i[2])


    return (day, hnm, sec)


@middle_deco(str_time_seper, li_time_seper)
def time_seper(date):
    pass


if __name__ == "__main__":

    from data_csv import li_applyer

    print(time_seper('2025-01-08/19:21;19:21:24'))

    print(time_seper(['2025-01-08/19:21;19:21:24', '2025-01-08/19:21;19:21:35', None, '2025-01-08/19:21;19:21:58', 
                      '2025-01-08/21:07;21:07:29']))