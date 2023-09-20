import json
from flask import Flask, jsonify, request
from flask_cors import CORS  # 导入CORS模块


app = Flask(__name__)
CORS(app)

select_data = {}
with open("data.json") as f:
    all_data = json.load(f)

all_data = [
    {
        "area": "北京",
        "content": [
            {"name": "奥林匹克森林公园站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "北京万柳中路站", "value": "90 nGy/h", "time": "2023-09-19"},
            {"name": "北京门头沟西苑路站", "value": "64 nGy/h", "time": "2023-09-19"},
            {"name": "北京昌平昌赤路站", "value": "69 nGy/h", "time": "2023-09-19"},
            {"name": "亦庄博大公园站", "value": "74 nGy/h", "time": "2023-09-19"},
            {"name": "平谷区赵赵路站", "value": "55 nGy/h", "time": "2023-09-19"},
            {"name": "北京延庆夏都公园站", "value": "68 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "天津",
        "content": [
            {"name": "南开复康路站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "天津津南咸水沽小学站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "天津北辰西平道站", "value": "60 nGy/h", "time": "2023-09-19"},
            {"name": "天津武清安监局站", "value": "68 nGy/h", "time": "2023-09-19"},
            {"name": "宝坻建设路站", "value": "62 nGy/h", "time": "2023-09-19"},
            {"name": "滨海新区世纪大道站", "value": "74 nGy/h", "time": "2023-09-19"},
            {"name": "天津滨海新区监测中心站", "value": "73 nGy/h", "time": "2023-09-19"},
            {"name": "天津宁河环保局站", "value": "66 nGy/h", "time": "2023-09-19"},
            {"name": "天津市静海区西钓台站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "天津蓟州北六里屯站", "value": "63 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "河北",
        "content": [
            {"name": "石家庄市省辐射站", "value": "93 nGy/h", "time": "2023-09-19"},
            {"name": "石家庄槐岭路站", "value": "62 nGy/h", "time": "2023-09-19"},
            {"name": "唐山路北区站", "value": "76 nGy/h", "time": "2023-09-19"},
            {"name": "秦皇岛秦皇东大街站", "value": "74 nGy/h", "time": "2023-09-19"},
            {"name": "邯郸丛台区站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "邢台桥东区站", "value": "76 nGy/h", "time": "2023-09-19"},
            {"name": "保定竞秀区站", "value": "84 nGy/h", "time": "2023-09-19"},
            {"name": "雄安新区容城站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "张家口纬一路站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "承德开发区站", "value": "76 nGy/h", "time": "2023-09-19"},
            {"name": "沧州运河区站", "value": "64 nGy/h", "time": "2023-09-19"},
            {"name": "廊坊安次区站", "value": "77 nGy/h", "time": "2023-09-19"},
            {"name": "衡水桃城区站", "value": "72 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "山西",
        "content": [
            {"name": "太原市省环保局站", "value": "91 nGy/h", "time": "2023-09-19"},
            {"name": "太原长治路站", "value": "89 nGy/h", "time": "2023-09-19"},
            {"name": "大同市文兴路站", "value": "74 nGy/h", "time": "2023-09-19"},
            {"name": "临汾市开发区西大街站", "value": "87 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "内蒙古",
        "content": [
            {"name": "内蒙古环境监测中心站", "value": "105 nGy/h", "time": "2023-09-19"},
            {"name": "呼和浩特市环境监测站", "value": "96 nGy/h", "time": "2023-09-19"},
            {"name": "包头市乌兰计站", "value": "109 nGy/h", "time": "2023-09-19"},
            {"name": "包头市标准站", "value": "111 nGy/h", "time": "2023-09-19"},
            {"name": "通辽市环境监测站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "呼伦贝尔市扎兰屯路站", "value": "82 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "辽宁",
        "content": [
            {"name": "沈阳市东陵站", "value": "67 nGy/h", "time": "2023-09-19"},
            {"name": "大连市旅顺口区站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "大连市庄河站", "value": "109 nGy/h", "time": "2023-09-19"},
            {"name": "鞍山铁西区站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "抚顺市新宾站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "本溪市桓仁站", "value": "92 nGy/h", "time": "2023-09-19"},
            {"name": "丹东市振兴区站", "value": "88 nGy/h", "time": "2023-09-19"},
            {"name": "丹东市东港站", "value": "98 nGy/h", "time": "2023-09-19"},
            {"name": "丹东市凤城站", "value": "112 nGy/h", "time": "2023-09-19"},
            {"name": "锦州松山新区站", "value": "68 nGy/h", "time": "2023-09-19"},
            {"name": "营口市鲅鱼圈站", "value": "80 nGy/h", "time": "2023-09-19"},
            {"name": "阜新细河区站", "value": "74 nGy/h", "time": "2023-09-19"},
            {"name": "盘锦双台子区站", "value": "66 nGy/h", "time": "2023-09-19"},
            {"name": "铁岭凡河新区站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "朝阳双塔区站", "value": "69 nGy/h", "time": "2023-09-19"},
            {"name": "葫芦岛市龙港站", "value": "75 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "吉林",
        "content": [
            {"name": "长春卫星路站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "长春青年路站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "吉林丰满区站", "value": "76 nGy/h", "time": "2023-09-19"},
            {"name": "四平铁西区站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "集安市活龙村站", "value": "87 nGy/h", "time": "2023-09-19"},
            {"name": "长白山北山门站", "value": "94 nGy/h", "time": "2023-09-14"},
            {"name": "临江市鸭绿江大街站", "value": "64 nGy/h", "time": "2023-09-19"},
            {"name": "白山市三道沟镇站", "value": "97 nGy/h", "time": "2023-09-19"},
            {"name": "松原市临江西路站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "白城工业园区站", "value": "83 nGy/h", "time": "2023-09-19"},
            {"name": "延边珲春龙源公园站", "value": "64 nGy/h", "time": "2023-09-19"},
            {"name": "图们市环保局站", "value": "88 nGy/h", "time": "2023-09-19"},
            {"name": "龙井市海蓝公园站", "value": "83 nGy/h", "time": "2023-09-19"},
            {"name": "和龙市气象局站", "value": "97 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "黑龙江",
        "content": [
            {"name": "哈尔滨南直路站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "齐齐哈尔龙沙区站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "鸡西市虎林站", "value": "80 nGy/h", "time": "2023-09-19"},
            {"name": "鹤岗兴安区站", "value": "91 nGy/h", "time": "2023-09-19"},
            {"name": "双鸭山尖山区站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "大庆黑鱼湖水厂站", "value": "77 nGy/h", "time": "2023-09-19"},
            {"name": "伊春伊春区站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "佳木斯江心岛站", "value": "88 nGy/h", "time": "2023-09-19"},
            {"name": "佳木斯市抚远站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "七台河桃山区站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "牡丹江十二条站", "value": "87 nGy/h", "time": "2023-09-19"},
            {"name": "黑河卡伦山村站", "value": "76 nGy/h", "time": "2023-09-18"},
            {"name": "绥化北林区站", "value": "78 nGy/h", "time": "2023-09-19"},
            {"name": "大兴安岭地区漠河站", "value": "93 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "上海",
        "content": [
            {"name": "普陀沪太路站", "value": "65 nGy/h", "time": "2023-09-19"},
            {"name": "浦东新区临港站", "value": "68 nGy/h", "time": "2023-08-27"},
            {"name": "金山临桂路站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "崇明汲浜路站", "value": "80 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "江苏",
        "content": [
            {"name": "南京新城科技园站", "value": "59 nGy/h", "time": "2023-09-19"},
            {"name": "无锡周新东路站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "徐州市自来水厂站", "value": "53 nGy/h", "time": "2023-09-19"},
            {"name": "常州新北区站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "苏州独墅湖站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "南通崇川区站", "value": "81 nGy/h", "time": "2023-09-19"},
            {"name": "连云港新浦站", "value": "104 nGy/h", "time": "2023-09-19"},
            {"name": "淮安清河站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "盐城市文港北路站", "value": "93 nGy/h", "time": "2023-09-19"},
            {"name": "扬州扬子江北路站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "镇江丹徒区站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "泰州海陵区站", "value": "90 nGy/h", "time": "2023-09-19"},
            {"name": "宿迁市自来水厂站", "value": "63 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "浙江",
        "content": [
            {"name": "杭州省辐射站", "value": "99 nGy/h", "time": "2023-09-19"},
            {"name": "杭州三义村站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "宁波宝善路站", "value": "86 nGy/h", "time": "2023-09-19"},
            {"name": "温州三垟湿地公园站", "value": "77 nGy/h", "time": "2023-09-19"},
            {"name": "嘉兴凌公塘路站", "value": "68 nGy/h", "time": "2023-09-19"},
            {"name": "湖州市沿圩湾站", "value": "105 nGy/h", "time": "2023-09-19"},
            {"name": "绍兴市环保局站", "value": "88 nGy/h", "time": "2023-09-19"},
            {"name": "金华金东区站", "value": "92 nGy/h", "time": "2023-09-19"},
            {"name": "衢州西区站", "value": "97 nGy/h", "time": "2023-09-19"},
            {"name": "舟山市体育路站", "value": "91 nGy/h", "time": "2023-09-19"},
            {"name": "台州椒江区站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "丽水经济开发区站", "value": "92 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "安徽",
        "content": [
            {"name": "合肥怀宁路站", "value": "78 nGy/h", "time": "2023-09-19"},
            {"name": "芜湖赭山路站", "value": "70 nGy/h", "time": "2023-09-19"},
            {"name": "蚌埠胜利东路站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "滁州清流西路站", "value": "67 nGy/h", "time": "2023-09-19"},
            {"name": "宿州市人民路站", "value": "88 nGy/h", "time": "2023-09-19"},
            {"name": "宣城宣州区站", "value": "70 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "福建",
        "content": [
            {"name": "福州市福飞北路站", "value": "104 nGy/h", "time": "2023-09-19"},
            {"name": "福州连江站", "value": "93 nGy/h", "time": "2023-09-19"},
            {"name": "厦门杏林南路站", "value": "95 nGy/h", "time": "2023-09-19"},
            {"name": "三明麒麟公园站", "value": "93 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "江西",
        "content": [
            {"name": "南昌洪都北大道站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "景德镇市景东大道站", "value": "92 nGy/h", "time": "2023-09-19"},
            {"name": "九江浔阳路站", "value": "76 nGy/h", "time": "2023-09-19"},
            {"name": "鹰潭月湖区站", "value": "76 nGy/h", "time": "2023-09-19"},
            {"name": "赣州贺兰山路站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "上饶滨江路站", "value": "105 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "山东",
        "content": [
            {"name": "济南市省辐射站", "value": "90 nGy/h", "time": "2023-09-19"},
            {"name": "济南经十路站", "value": "74 nGy/h", "time": "2023-09-19"},
            {"name": "济南市花园北路站", "value": "86 nGy/h", "time": "2023-09-19"},
            {"name": "青岛市环保局站", "value": "92 nGy/h", "time": "2023-09-19"},
            {"name": "青岛崂山区南窑站", "value": "105 nGy/h", "time": "2023-09-19"},
            {"name": "青岛崂山区登瀛站", "value": "96 nGy/h", "time": "2023-09-19"},
            {"name": "淄博柳泉路站", "value": "63 nGy/h", "time": "2023-09-19"},
            {"name": "枣庄薛城区站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "东营东营区站", "value": "79 nGy/h", "time": "2023-09-19"},
            {"name": "烟台青年南路站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "潍坊新华路站", "value": "79 nGy/h", "time": "2023-09-19"},
            {"name": "济宁汶上县站", "value": "78 nGy/h", "time": "2023-09-19"},
            {"name": "荣成市观海东路站", "value": "92 nGy/h", "time": "2023-09-19"},
            {"name": "威海市环保局站", "value": "93 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "河南",
        "content": [
            {"name": "郑州大王庄站", "value": "86 nGy/h", "time": "2023-09-19"},
            {"name": "洛阳中州东路站", "value": "78 nGy/h", "time": "2023-09-19"},
            {"name": "漯河龙江路站", "value": "83 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "湖北",
        "content": [
            {"name": "武汉市公正路站", "value": "78 nGy/h", "time": "2023-09-19"},
            {"name": "黄石市苏州路站", "value": "59 nGy/h", "time": "2023-09-19"},
            {"name": "宜昌胜利四路站", "value": "69 nGy/h", "time": "2023-09-19"},
            {"name": "襄阳新华路站", "value": "81 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "湖南",
        "content": [
            {"name": "望城区环保局站", "value": "91 nGy/h", "time": "2023-09-19"},
            {"name": "长沙万家丽中路站", "value": "65 nGy/h", "time": "2023-09-19"},
            {"name": "张家界大庸路站", "value": "86 nGy/h", "time": "2023-09-19"},
            {"name": "怀化怀黔路站", "value": "67 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "广东",
        "content": [
            {"name": "广州大道站", "value": "91 nGy/h", "time": "2023-09-19"},
            {"name": "韶关武江区站", "value": "79 nGy/h", "time": "2023-09-19"},
            {"name": "珠海市中山大学站", "value": "135 nGy/h", "time": "2023-09-19"},
            {"name": "汕头龙湖区站", "value": "92 nGy/h", "time": "2023-09-19"},
            {"name": "佛山禅城区站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "江门蓬江区站", "value": "89 nGy/h", "time": "2023-09-19"},
            {"name": "湛江开发区站", "value": "62 nGy/h", "time": "2023-09-19"},
            {"name": "茂名乙烯生活区站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "肇庆端州区站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "惠州市红花湖站", "value": "79 nGy/h", "time": "2023-09-19"},
            {"name": "梅州梅江区站", "value": "79 nGy/h", "time": "2023-09-19"},
            {"name": "汕尾海滨大道站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "河源市紫金县站", "value": "119 nGy/h", "time": "2023-09-19"},
            {"name": "清远佛冈县站", "value": "107 nGy/h", "time": "2023-09-19"},
            {"name": "东莞市植物园站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "中山市横栏镇站", "value": "87 nGy/h", "time": "2023-09-19"},
            {"name": "潮州凤新东路站", "value": "90 nGy/h", "time": "2023-09-19"},
            {"name": "揭阳榕城区站", "value": "112 nGy/h", "time": "2023-09-19"},
            {"name": "云浮市云安区站", "value": "75 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "广西",
        "content": [
            {"name": "广西辐射站", "value": "68 nGy/h", "time": "2023-09-19"},
            {"name": "柳州城中区站", "value": "54 nGy/h", "time": "2023-09-19"},
            {"name": "桂林市市民广场", "value": "76 nGy/h", "time": "2023-09-19"},
            {"name": "梧州长洲区站", "value": "73 nGy/h", "time": "2023-09-19"},
            {"name": "北海海城区站", "value": "60 nGy/h", "time": "2023-09-19"},
            {"name": "防城港万鹤路站", "value": "63 nGy/h", "time": "2023-09-19"},
            {"name": "钦州钦州学院站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "贵港港北区站", "value": "62 nGy/h", "time": "2023-09-19"},
            {"name": "玉林人民东路站", "value": "65 nGy/h", "time": "2023-09-19"},
            {"name": "百色辐射站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "贺州南环路站", "value": "77 nGy/h", "time": "2023-09-19"},
            {"name": "河池金城江区站", "value": "65 nGy/h", "time": "2023-09-19"},
            {"name": "来宾新桥路站", "value": "57 nGy/h", "time": "2023-09-19"},
            {"name": "崇左江州区站", "value": "75 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "海南",
        "content": [
            {"name": "海口市白驹大道站", "value": "59 nGy/h", "time": "2023-09-19"},
            {"name": "海口红旗镇站", "value": "60 nGy/h", "time": "2023-09-19"},
            {"name": "三亚榆亚路站", "value": "86 nGy/h", "time": "2023-09-19"},
            {"name": "三亚海棠湾青田水厂站", "value": "91 nGy/h", "time": "2023-09-19"},
            {"name": "三亚海棠湾301医院站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "三亚亚龙湾站", "value": "92 nGy/h", "time": "2023-09-19"},
            {"name": "三沙市永兴岛站", "value": "81 nGy/h", "time": "2023-09-19"},
            {"name": "儋州第一中学站", "value": "67 nGy/h", "time": "2023-09-19"},
            {"name": "五指山阿驼岭站", "value": "84 nGy/h", "time": "2023-09-18"},
            {"name": "琼海金海北路站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "白沙邦溪镇站", "value": "89 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "重庆",
        "content": [
            {"name": "天城大道站", "value": "66 nGy/h", "time": "2023-09-19"},
            {"name": "李渡站", "value": "86 nGy/h", "time": "2023-09-19"},
            {"name": "大礼堂站", "value": "77 nGy/h", "time": "2023-09-19"},
            {"name": "白市驿站", "value": "83 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "四川",
        "content": [
            {"name": "成都市温江区花土路站", "value": "78 nGy/h", "time": "2023-09-19"},
            {"name": "成都熊猫基地站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "成都锦江区站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "攀枝花机场路站", "value": "86 nGy/h", "time": "2023-09-19"},
            {"name": "泸州纳溪区站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "德阳泰山南路站", "value": "72 nGy/h", "time": "2023-09-19"},
            {"name": "绵阳三水厂站", "value": "71 nGy/h", "time": "2023-09-19"},
            {"name": "眉山眉州大道站", "value": "78 nGy/h", "time": "2023-09-19"},
            {"name": "宜宾敬业路站", "value": "73 nGy/h", "time": "2023-09-19"},
            {"name": "达州通川区站", "value": "89 nGy/h", "time": "2023-09-19"},
            {"name": "雅安雨城区站", "value": "79 nGy/h", "time": "2023-09-19"},
            {"name": "资阳雁江区站", "value": "67 nGy/h", "time": "2023-09-19"},
            {"name": "甘孜康定榆林路站", "value": "117 nGy/h", "time": "2023-09-19"},
            {"name": "西昌海南乡站", "value": "97 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "贵州",
        "content": [
            {"name": "贵州省辐射环境监理站", "value": "66 nGy/h", "time": "2023-09-19"},
            {"name": "贵阳青云路站", "value": "63 nGy/h", "time": "2023-09-19"},
            {"name": "六盘水明湖路站", "value": "73 nGy/h", "time": "2023-09-19"},
            {"name": "遵义市三贤路站", "value": "85 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "云南",
        "content": [
            {"name": "昆明环城西路站", "value": "84 nGy/h", "time": "2023-09-19"},
            {"name": "保山九龙路站", "value": "69 nGy/h", "time": "2023-09-19"},
            {"name": "西双版纳州景洪市民航路站", "value": "99 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "西藏",
        "content": [
            {"name": "拉萨东嘎镇站", "value": "191 nGy/h", "time": "2023-09-19"},
            {"name": "日喀则市青岛路站", "value": "172 nGy/h", "time": "2022-04-15"},
            {"name": "林芝迎宾路站", "value": "149 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "陕西",
        "content": [
            {"name": "陕西省环保大厦站", "value": "89 nGy/h", "time": "2023-09-19"},
            {"name": "西安北郊污水处理厂站", "value": "90 nGy/h", "time": "2023-09-19"},
            {"name": "宝鸡眉县站", "value": "102 nGy/h", "time": "2023-09-19"},
            {"name": "延安市双拥大道站", "value": "85 nGy/h", "time": "2023-09-19"},
            {"name": "汉中民主街站", "value": "95 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "甘肃",
        "content": [
            {"name": "兰州市金昌路站", "value": "103 nGy/h", "time": "2023-09-19"},
            {"name": "兰州市东岗站", "value": "101 nGy/h", "time": "2023-09-19"},
            {"name": "嘉峪关嘉北工业园站", "value": "115 nGy/h", "time": "2023-09-19"},
            {"name": "金昌市公园路站", "value": "96 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "宁夏",
        "content": [
            {"name": "西宁市共和路站", "value": "89 nGy/h", "time": "2023-09-19"},
            {"name": "西宁纳家山站", "value": "118 nGy/h", "time": "2023-09-19"},
            {"name": "瓦里关站", "value": "175 nGy/h", "time": "2023-09-19"},
            {"name": "玉树通天河站", "value": "150 nGy/h", "time": "2023-09-19"},
            {"name": "格尔木昆仑路站", "value": "134 nGy/h", "time": "2023-09-19"},
        ],
    },
    {
        "area": "新疆",
        "content": [
            {"name": "乌鲁木齐长春北路站", "value": "82 nGy/h", "time": "2023-09-19"},
            {"name": "乌鲁木齐北京中路站", "value": "74 nGy/h", "time": "2023-09-19"},
            {"name": "克拉玛依准噶尔路站", "value": "75 nGy/h", "time": "2023-09-19"},
            {"name": "哈密翰林路站", "value": "116 nGy/h", "time": "2023-09-19"},
            {"name": "喀什人民东路站", "value": "91 nGy/h", "time": "2023-09-19"},
            {"name": "伊犁新华西路站", "value": "106 nGy/h", "time": "2023-09-19"},
        ],
    },
]


@app.route("/api/endpoint", methods=["POST"])
def receive_data():
    global select_data
    data = request.json
    if data:
        key1_value = data.get("key1")
        select_data = next(item for item in all_data if item["area"] == key1_value)
        return {"message": "Data received successfully", "key1": key1_value}
    else:
        return {"message": "No data received"}, 400  # 返回400状态码表示请求无效


@app.route("/api/endpoint")
def data():
    print("API is Running")
    return jsonify(select_data)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
