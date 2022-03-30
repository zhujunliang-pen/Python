import datetime
import time
from datetime import timedelta

today = datetime.date.today()
print("today=", today, end="\n")

today = datetime.datetime(2003, 4, 2, 5, 9, 3, 200)
print(today)

'''
%m		month
%d		day
%y		year=yy
%b		month abbreviation
%B		month whole word
%Y		year=YYYY
%A		week day
%H		24 hour
%I 		12 hour
%M		minute
%S		second
%Z		ms
%p		PM/AM


Directive	Meaning							Example																	Notes
%a	Weekday as locale’s abbreviated name.	Sun, Mon, …, Sat (en_US);So, Mo, …, Sa (de_DE)							(1)
%A	Weekday as locale’s full name.			Sunday, Monday, …, Saturday (en_US);Sonntag, Montag, …, Samstag (de_DE)	(1)
%w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.	0, 1, …, 6	 
%d	Day of the month as a zero-padded decimal number.	01, 02, …, 31	 
%b	Month as locale’s abbreviated name.	Jan, Feb, …, Dec (en_US);Jan, Feb, …, Dez (de_DE)							(1)
%B	Month as locale’s full name.	January, February, …, December (en_US);Januar, Februar, …, Dezember (de_DE)		(1)
%m	Month as a zero-padded decimal number.	01, 02, …, 12	 
%y	Year without century as a zero-padded decimal number.	00, 01, …, 99	 
%Y	Year with century as a decimal number.	0001, 0002, …, 2013, 2014, …, 9998, 9999								(2)
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, …, 23	 
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, …, 12	 
%p	Locale’s equivalent of either AM or PM.	AM, PM (en_US);am, pm (de_DE)											(1), (3)
%M	Minute as a zero-padded decimal number.	00, 01, …, 59	 
%S	Second as a zero-padded decimal number.	00, 01, …, 59															(4)
%f	Microsecond as a decimal number, zero-padded on the left.	000000, 000001, …, 999999							(5)
%z	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).	(empty), +0000, -0400, +1030, +063415, -030712.345216	(6)
%Z	Time zone name (empty string if the object is naive).	(empty), UTC, EST, CST	 
%j	Day of the year as a zero-padded decimal number.	001, 002, …, 366	 
%U	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, …, 53	(7)
%W	Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, …, 53	(7)
%c	Locale’s appropriate date and time representation.	Tue Aug 16 21:30:00 1988 (en_US);Di 16 Aug 21:30:00 1988 (de_DE)	(1)
%x	Locale’s appropriate date representation.	08/16/88 (None);08/16/1988 (en_US);16.08.1988 (de_DE)				(1)
%X	Locale’s appropriate time representation.	21:30:00 (en_US);	21:30:00 (de_DE)								(1)
%%	A literal '%' character.	%	 

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))
s = today.strftime("%m-%d-%y %I %H:%M:%S %p.  %d %b %Y is a %A on the %d day of %B.")
#12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.
print(s)
td = today - timedelta(days=1)
print(td)

birthday = datetime.date(1977, 4, 24)
today = datetime.date.today()
td = today - birthday
print(td.days)


ticks = time.time()
print ("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

"""
时间元组: 很多Python函数用一个元组装起来的9组数字处理时间:
序号	字段	值
0	4位数年	2008
1	月	1 到 12
2	日	1到31
3	小时	0到23
4	分钟	0到59
5	秒	0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜

上述也就是struct_time元组。这种结构具有如下属性：

序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	一年中的第几天，1 到 366
8	tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1

"""
