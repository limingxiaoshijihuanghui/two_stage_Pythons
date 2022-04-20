def days(month):
    if month == 2:
        return 28
    elif month in [1,3,5,7,9,10,12]:
        return 31
    elif month in (4,6,8,11):
        return 30

def month_true(month):
    if 0 < month <= 12 and month == int(month):
        day = days(month)
        return day
    else:
        print('请输入正确的月份数!')

if __name__ == '__main__':
    month = eval(input('请输入当前月份数：'))
    day = month_true(month)
    if day != None:
        print('当前月份共有{}日。'.format(day))
