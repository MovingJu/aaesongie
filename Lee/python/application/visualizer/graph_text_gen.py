import matplotlib.pylab as plt

def graph_text_gen(xlist, ylist, ax, show_level = 3):
    """
    show_level= 0: 전체 표시, 1: 같은 값 제외, 2: 극값만 표시, 3: 전부 제외
    """

    if show_level == 0:

        for idx, txt in enumerate(ylist):

            txt = round(txt/1e6, 3)

            ax.text(xlist[idx], ylist[idx] + 0.4, txt, 
                     ha='center', color='blue', rotation=20)
            


    if show_level == 1:

        b_txt = -1

        for idx, txt in enumerate(ylist):

            txt = round(txt/1e6, 3)

            if b_txt == txt:
                continue

            b_txt = txt

            ax.text(xlist[idx], ylist[idx] + 0.4, txt, 
                     ha='center', color='blue', rotation=20)


    if show_level == 2:

        for idx, txt in enumerate(ylist):

            try: 

                txt = round(txt/1e6, 3)

                if ylist[idx -1] <= ylist[idx] <= ylist[idx + 1]\
                    or ylist[idx -1] >= ylist[idx] >= ylist[idx + 1]:
                    continue


                ax.text(xlist[idx], ylist[idx] + 0.4, txt, 
                            ha='center', color='blue', rotation=20)
                
            except:
                pass

    if show_level == 3:
        pass



    return ax