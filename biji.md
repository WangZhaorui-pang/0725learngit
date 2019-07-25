# 学习笔记

## 学习python相关知识

### 已理解进制

* 二进制 、十进制、八进制、十六进制

### 已理解变量
 
* 只有变量 **没有常量**
* 变量命名：区分大小写，字符或下划线开始

### 已基础的变量类型

1. 字符串 “str”
   * 双引号或者单引号里面的内容"abcd" 'abcd' "中文"

``` python
a = "abc"
b = '你好，世界'
print(a,b)
```

2. 整型 “int”

  * **0b**01 :  2进制
  * 10       ： 10进制
  * **0o**07 ： 8进制
  * **0x**ff ： 16进制

  * 浮点数 float

3. 布尔 “bool”
  True
  False

4. 列表 “list”
5. 字典 “dict”
6. 元组 “tuple”
7. 集合 “set”

### 已数据类型转换

1. 进制之间转换
十进制转换二进制 : bin()
十进制转换十六进制 ：hex()
二进制转换成十进制 ： int("1001",2)

2. int() 将 只包含数字的字符串 转换成对应十进制的数字

* 任务：输入一个二进制数字，然后将其转换成十进制，打印出它的值和类型
input：0b1111,1111
output:15

```
input_data = input("请输入二进制：")
input_data = int (input_data,2)
print (input_data,type(input_data))
```

* 任务：输入一个十进制数字，然后将其转换成二进制再加5，再转换成十进制，打印出来它的值和类型

```
#1. 输入一个十进制数字
input_data =int (input ("请输入一个十进制数字："))
#2. 将输入的字符串类型的数字转换成数字
input_data_int=int(input_data,10)
#3. 十进制转成二进制
input_data_bin=bin(input_data_int)
#4. 转换进制进行数学运算
result=int（input_data_bin,2）+5
#5. 打印出来
print(result,type(result))
```

### 已理解输入输出函数

1. print() -输出任意类型
2. input() -输入一段数据

## 已理解运算符

1. 数学运算符
*  (+  -  *  /  //  % ) 加、减、乘、除、地板除（取商）、取余

2. 赋值运算符
*  = 

3. 比较运算符（可以比较数字也可以比较字符串）
* (> >=  <  <=  !=  ==)
* 比较出来的是一个bool型

4. 逻辑运算符
* 与或非   and  or  not  (不需要& || !)

## 学习web相关知识

### 已理解CSS(层叠样式表)

* CSS是用来美化页面用的，可以对页面元素进行更精细的设置，样式主要描述元素的字体颜色、背景颜色、大小、长度、宽度、边框等等。CSS主要有元素内联、页面嵌入和外部引用三种使用方式。

1. 元素内联：
```
直接将样式写入元素的style属性中，<input type=“text” value=“123” style=“background-color:red;border-color:green;”/>适用于样式没有可复用性的场合。(提醒一点：每个元素内联的样式级别高于页面嵌入和外部引用)
```

2. 页面嵌入:
```
在head中加入
           <style type= =“text/css” >
                   input{border-color:yellow;}
           </style>
表示页面中所有input都是采用指定的样式。适合于样式复用，减小页面代码量
```

3. 外部引用:
```
将CSS内容写到具有css后缀的文件中,在head中加入
           <link type=“text/css” rel=“Stylesheet” href=“css1.css”
适合用于多个页面共享css
```

### 已理解样式选择器

* 对于非元素内联的样式需要定义样式选择器，通俗地说及时这个样式适合于哪些元素，三种：标签选择器、class选择器、id选择器

1. 标签选择器：
 ```
 input{border-color:Yellow;color:red;}，对于页面input标签采用统一的样式
```

2. class选择器：
```
 以定义一个命名的样式，然后在用到它的时候设定元素的class属性为样式的名称，还可以同时设定多个class。名称之间加空格
样式名称开头加“.”
.waining{background:Yellow;}
.highlight{font-size:xx-large;cursor:help;}
<table><tr><td class=“highlight”>aaa</td><td class=“waring”>bb</td><td class=“highlight waring”>ccc</td></tr></table>
```

3. 标签+class选择器:
```
 class选择器也可以针对不同的标签，实现同样的样式名对于不同的标签有不同的样式，只要在样式名前加标签名即可
    input.accountno{text-align:right;color:red;}
    label.accountno{font-style:italic;}
    <input class=“accountno” type=“text” value=“haha”/>
    <label class=“accountno”>hahahahaha</label>
```

4. id选择器
```
为指定id的元素设定样式，id前加 #
#username
        {
            font-size:xx-large;
        }

<input id=“username” type=“text” value=“haha”/>


Style、class可以同时使用
<input id=“username” class=“accountno”  type=“text”  style=“font-size:xx-large”  value=“haha”/>
```
