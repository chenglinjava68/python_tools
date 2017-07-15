import random

'''
随机整数

fromInt <= res <= to
'''
def getRandomBetweenNumbers(fromInt , to) :
    return random.randint(int(fromInt), int(to));


'''
返回字符串
'''
def getRandomBetweenNumbersStr(fromInt , to) :
    return str(random.randint(int(fromInt), int(to)));


'''
随机浮点数
'''
def getRandomFloatBetweenNumbers(fromInt , to) :
    return random.uniform(fromInt, to);



'''
获取随机数组
'''
def getRamdonByArr(arr):
    if arr and len(arr) > 0:
        idx = random.randint(0, len(arr) - 1);
        return arr[idx];
    return None;

'''
获取随机时间
'''
def getLimitRandomTime():
    startYear = '2017';
    endYear = '2017';

    startMonth = '5';
    endMonth = '7';

    startDate = '1';
    endDate = '28';

    time = '';
    time += getRandomBetweenNumbersStr(startYear, endYear);
    time += '-';

    month = getRandomBetweenNumbersStr(startMonth, endMonth);
    if int(month) < 10 :
        time += '0';
    time += month;
    time += '-';

    date = getRandomBetweenNumbersStr(startDate, endDate);
    if int(date) < 10 :
        time += '0';
    time += date;
    time += ' ';

    hour = getRandomBetweenNumbersStr(0, 23);
    if (int(hour) < 10) :
        time += '0';


    time += hour;
    time += ':';

    minute = getRandomBetweenNumbersStr(0, 59);
    if (int(minute) < 10) :
        time += '0';

    time += minute;
    time += ':';

    second = getRandomBetweenNumbersStr(0, 59);
    if (int(second) < 10) :
        time += '0';
    time += second;
    return time;


def getRandomTime():
    startYear = 2015;
    endYear = 2017;

    startMonth = 1;
    endMonth = 12;

    startDate = 1;
    endDate = 28;

    time = '';

    time += getRandomBetweenNumbersStr(startYear, endYear);
    time += '-';

    month = getRandomBetweenNumbersStr(startMonth, endMonth);
    if int(month) < 10 :
        time += '0';
    time += month;
    time += '-';

    date = getRandomBetweenNumbersStr(startDate, endDate);
    if int(date) < 10 :
        time += '0';
        time += date;
    time += ' ';

    hour = getRandomBetweenNumbersStr(0, 23);
    if (int(hour) < 10) :
        time += '0';


    time += hour;
    time += ':';

    minute = getRandomBetweenNumbersStr(0, 59);
    if (int(minute) < 10) :
        time += '0';

    time += minute;
    time += ':';

    second = getRandomBetweenNumbersStr(0, 59);
    if (int(second) < 10) :
        time += '0';
    time += second;
    return time;