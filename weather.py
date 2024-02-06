import requests

# 替换成你的API密钥
key = 'xxxx'
# 设置你想要查询的城市的adcode
city = 'xxxxxx'
# 设置返回数据格式为全部预报信息
extensions = 'all'
# 拼接请求URL
url = f'http://restapi.amap.com/v3/weather/weatherInfo?key={key}&city={city}&extensions={extensions}'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析返回的JSON数据
    data = response.json()
    # 获取天气预报列表
    forecasts = data['forecasts'][0]['casts']
    # 打印城市信息
    print(f"新民市的天气预报：")
    # 遍历并打印每天的天气信息
    for forecast in forecasts:
        date = forecast['date']
        dayweather = forecast['dayweather']
        nightweather = forecast['nightweather']
        daytemp = forecast['daytemp']
        nighttemp = forecast['nighttemp']
        daywind = forecast['daywind']
        nightwind = forecast['nightwind']
        daypower = forecast['daypower']
        nightpower = forecast['nightpower']
        # 格式化输出
        print(f"{date} - 白天：{dayweather} {daytemp}°C, {daywind}风 {daypower}级; 夜晚：{nightweather} {nighttemp}°C, {nightwind}风 {nightpower}级")
else:
    print('请求失败', response.status_code)
