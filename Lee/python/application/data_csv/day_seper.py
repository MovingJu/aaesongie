from .def_li_applyer import li_applyer

def middle_deco(func_str: 'function', func_list: 'function') -> 'function':
    """년-월-일을 각각 튜플로 나눠주는 함수
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


def str_day_seper(date: str) -> tuple[str, str, str]:

    
    try:

        year, day, month = date.split('-')

        return (year, day, month)

    except Exception as e:
        print("an error occured:", e)

        return (None, None, None)
    

    
def li_day_seper(li:list[str]) -> list[tuple[str, str, str]]:

    day, hnm, sec = [], [], []
    
    for i in li_applyer(str_day_seper, li):


        day.append(i[0])
        hnm.append(i[1])
        sec.append(i[2])


    return (day, hnm, sec)


@middle_deco(str_day_seper, li_day_seper)
def day_seper(date):
    pass
