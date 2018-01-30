# \usr\bin\python
# -*coding:UTF-8-*-
# 原文连接： http://blog.csdn.net/qq_18301257/article/details/79078191
# 从 天气后报 获取指定城市指定日期的天气信息，存储为txt格式
def ModSearchWeather(City, Date):  # 定义一个对象:获取天气历史信息
    import re, requests, sys  # 引用re,requests,sys等相应库
    # 获取网页数据
    FilePath = sys.path[0] + '/' + City + '(' + Date + ').txt'  # 定义FilePath为输出txt文件路径
    url = 'http://www.tianqihoubao.com/lishi/' + City + '/month/' + Date + '.html'  # 定义url为获取天气历史数据的网址
    xml = requests.get(url).text  # 定义xml为获取网页数据
    xml = xml.replace('  ', '').replace('   ', '').replace('\n', '')  # 用replace方法初步处理不必要的空格和换行符
    reObj = re.compile(u'<td>(.*?)</td>')  # 运用正则表达式获取<td></td>中的表格内容
    textlist = reObj.findall(xml)  # 将获取到的表格内容赋值给textlist
    # 进一步处理所获得的数据内容
    if len(textlist) > 1:  # 判断是否获得了数据
        # 如是:获得数据
        FileName = open(FilePath, 'w')  # 新建一个txt文件,如当前文件夹中存在,则直接覆盖
        FileName.write('')  # 清空txt文件中内容,主要针对已存在的txt文件
        for i in range(len(textlist)):  # 设置循环,直到所获数据的最后一位
            if (i + 1) % 4 == 0:  # 设置规则:隔4个内容获取输出一次,这里是为了配合网站表格中的每一行
                text = textlist[i - 3:i + 1]  # 输出列表内容到text
                textinfo = ''  # 定义textinfo来存放临时处理好的数据
                textOut = ''  # 定义textOut来存放处理好的数据,并用于输出
                for j in range(4):  # 设置循环,4位
                    textinfo = text[j].replace('\r', '').replace(' ', '') \
                        .replace('<b>', '').replace('</b>', '')  # 将所获取的数据一一处理，去除\r,<b>,<\b>和空格等无关的内容
                    if len(textinfo) > 30:  # 判断处理完的数据字符串是否大于30,因为大于30位的字符串为包含链接的日期,输出时仅保留日期即可
                        # 如是:字符串大于30
                        textinfo = textinfo[textinfo.find('>') + 1:len(textinfo) - 4]  # 用find方法来截取字符串,输出日期
                    else:
                        # 如不是:字符串小于30
                        textinfo = textinfo  # 直接输出内容
                    textOut = textOut + ',' + textinfo  # 将处理好的数据按照',A,B,C,D'等方式输出
                ##      print textOut.replace(',','',1)
                FileName = open(FilePath, 'a')  # 在追加模式(a)模式下将内容输入到txt文件中
                FileName.write(textOut.replace(',', '', 1).encode(
                    'utf-8') + '\n')  # 删除多余的',',按照'A,B,C,D'的格式输入到txt文件中,行与行之间进行换行处理
                FileName.close()  # 关闭txt文件
        return '\n' + City + '(' + Date + ')' + 'Search Successful\n' + \
               '----------------------------------------------\n'  # 执行完毕后显示输出成功提示
    else:
        # 如不是:没有获得数据
        return '\n' + City + '(' + Date + ')' + 'Search Fails\n' + \
               '----------------------------------------------\n'  # 执行完毕后显示输出失败提示


def InputInfo():  # 定义一个对象:用于输入信息
    City = raw_input('Please Enter Chinese City English Name: ')  # 定义City为输入的城市名称
    Date = raw_input('Please Enter Search Date(YYYYMM) Or Year(YYYY): ')  # 定义Date为输入的获取日期
    if len(Date) == 6:  # 判断输入日期的字符串长度
        # 如等于6,则为按月获取天气历史信息
        print ModSearchWeather(City, Date)  # 执行获取天气历史信息函数
    elif len(Date) == 4:
        # 如等于4,则为按年获取天气历史信息
        for i in range(1, 13):  # 设置循环,从1到12月获取每月天气信息,并输出到txt文件中
            print ModSearchWeather(City, Date + str(i).zfill(2))  # 执行获取天气历史信息函数
    print InputInfo()  # 执行完毕后再次进入输入信息界面


print InputInfo()  # 进入输入信息界面
