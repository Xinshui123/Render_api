import json
from flask import Flask, jsonify, request
from flask_cors import CORS  # 导入CORS模块
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

# test

area_dict = {
    86: "北京",
    87: "天津",
    88: "河北",
    89: "山西",
    85: "内蒙古",
    84: "辽宁",
    83: "吉林",
    62: "黑龙江",
    94: "上海",
    92: "江苏",
    93: "浙江",
    95: "安徽",
    97: "福建",
    96: "江西",
    91: "山东",
    90: "河南",
    99: "湖北",
    98: "湖南",
    100: "广东",
    101: "广西",
    102: "海南",
    104: "重庆",
    103: "四川",
    105: "贵州",
    106: "云南",
    107: "西藏",
    108: "陕西",
    109: "甘肃",
    110: "青海",
    110: "宁夏",
    111: "新疆",
}


all_data = {}

base_url = "https://data.rmtc.org.cn/gis/listsation0_{}M.html"


def find_key_by_value(dictionary, target_value):
    reversed_dict = {value: key for key, value in dictionary.items()}
    return reversed_dict.get(target_value)


def new(area_name):
    all_data = {}
    # 通过传入地区名称来找到对应的地区值
    num = find_key_by_value(area_dict, area_name)
    # 生成对应的url
    url = base_url.format(num)
    # 生成对应的的地区名称
    # area_name = area_dict[num]

    # 解析html
    response = requests.get(url)
    html = response.text
    if not isinstance(html, str):
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    else:
        soup = BeautifulSoup(html, "html.parser")

    # 提取需要的数据
    content = []
    for item in soup.select("li.datali"):
        name = item.select_one("div.divname").get_text(strip=True)
        value = item.select_one("span.label").text
        time = item.select_one("span.showtime").text

        content.append({"name": name, "value": value, "time": time})

    all_data = {"area": area_name, "content": content}

    return all_data


@app.route("/api/endpoint", methods=["POST"])
def receive_data():
    global all_data
    data = request.json  # 获取前端发送的JSON数据
    # 在这里处理数据
    if data:
        key1_value = data.get("key1")
        all_data = {}  # 重置之前的内容
        all_data = new(key1_value)  # 直接覆盖之前的数据
        return {"message": "Data received successfully", "key1": key1_value}
    else:
        return {"message": "No data received"}, 400  # 返回400状态码表示请求无效


@app.route("/api/endpoint")
def data():
    print("API is Running")
    return jsonify(all_data)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
