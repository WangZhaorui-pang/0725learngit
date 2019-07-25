'''
# 1. 华氏温度转换为摄氏温度
input_data = float(input("请输入一个华氏温度："))
input_data = float((input_data-32)/1.8)
print (input_data,type(input_data))
'''

'''
# 2. 输入圆的半径计算周长和面积
input_data = float(input("请输入一个圆的半径："))
pi=float("3.1415926")
output1 = float (2*pi*input_data)
output2 = float (pi*input_data*input_data)
print(output1,output2)
print(type(output1),type (output2))
'''

'''
# 3. 输入年份判断是否是闰年 （if else）
# 整百年能被400整除的是闰年 ，非整百年能被4整除的为闰年
year = int(input("请输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))     
else:
   print("{0} 不是闰年".format(year))
'''