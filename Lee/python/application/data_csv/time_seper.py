def time_seper(li: list[str]) -> tuple[list[str], list[str], list[str]]:

    date, time, hnm, sec = [0 for i in range(len(li))], [0 for i in range(len(li))], [0 for i in range(len(li))], [0 for i in range(len(li))]

    for i in range(len(li)):


        if li[i] != None:

            date[i], time[i] = li[i].split('/')
            hnm[i], sec[i] = time[i].split(';')

        else: 
            (date[i], hnm[i], sec[i]) = (None, None, None)


    return date, hnm, sec


if __name__ == "__main__":
    print(time_seper(['2025-01-08/19:21;19:21:24', '2025-01-08/19:21;19:21:35', None, '2025-01-08/19:21;19:21:58', 
                      '2025-01-08/21:07;21:07:29']))