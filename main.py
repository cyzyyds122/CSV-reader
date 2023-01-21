import time
#首先找到需要读取的文件目录，绝对路径或者相对路径均可
filename = r"tt.csv"

file_data = []
#文件未解码时逐行数据
file_in_data = []
#解码后二维列表
dataname = 'cc'
#csv名
try:
    fp = open(filename,"r")
    print('START')
    #读取成功   
    
    for line in fp.readlines():
        line = line.replace('\n',' ')
        file_data.append(line)
        #去除多余空行
        
    fp.close()
    #关闭文件
except IOError:
    print("ERROR" %filename)
    #错误处理

y = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(y)

#下面是n*n速度的读取模块
for i in range(1,len(file_data)):
    #每一行
    data = []
    datatext = ''
    for j in file_data[i]:
        #每一组
        if j == ',':
            data.append(datatext)
            datatext = ''
        else:
            datatext += j
    file_in_data.append(data)
print(file_in_data)