

def li_applyer(func: 'function', li: list) -> list:
    """
    apply function to elements in index.
    """
    
    li1 = [func(i) for i in li]
    
    return li1


if __name__ == "__main__":

    from time_seper import str_time_seper

    print(li_applyer(str_time_seper, ['2025-01-08/19:21;19:21:24', '2025-01-08/19:21;19:21:35', None, '2025-01-08/19:21;19:21:58', 
                      '2025-01-08/21:07;21:07:29']))