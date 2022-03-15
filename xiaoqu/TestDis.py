import requests
import json

def get_distance(origin,destination): #设置函数计算两经纬度间驾车距离
    url = 'https://restapi.amap.com/v3/direction/driving'  # 高德API驾车路径规划服务地址
    params = {'key': '********************************',  # 参数1：个人申请的高德密钥
              'origin': origin, # 参数2：起始点的经纬度坐标
              'destination':destination, # 参数3：目的地的经纬度坐标
              'extensions':'base'} # 参数4：返回结果控制选项，必填项，base:返回基本信息；all：返回全部信息
    try:
        response = requests.get(url, params)  #使用requests模块的get方法请求网址数据
        jd = json.loads(response.text)  #数据json化
        return jd['route']['paths'][0]['distance']  #读取Json需要的distance值
    except:
        return  0  #利用try-except设置防呆机制，这里设置距离0表示未成功获取两地间的距离

import requests
import json
import time

start = time.process_time() #程序开始计时

result=int(get_distance("125.346404,29.034756","236.247568,35.656785"))/1000  #距离单位转换为公里

end = time.process_time() #程序结束计时

duration=end-start #程序运行所需时间

print('两地距离为:'+str(result)+'公里') #显示两地间距离
print('计算耗时:'+str(duration)+'秒') #显示程序运行所需时间
