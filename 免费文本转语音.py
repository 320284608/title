import requests
import re
import time

data = [
    "apple苹果", "banana香蕉", "cat猫", "dog狗", "egg鸡蛋", "fish鱼",
    "green绿色", "hello你好", "ice cream冰淇淋", "jump跳", "kite风筝", "lion狮子",
    "milk牛奶", "nose鼻子", "orange橙色", "pig猪", "queen女王", "rabbit兔子",
    "sun太阳", "tiger老虎", "umbrella雨伞", "van货车", "water水", "box盒子",
    "yellow黄色", "zoo动物园", "classroom教室", "blackboard黑板", "computer电脑",
    "teacher老师", "student学生", "math数学", "English英语", "music音乐", "sport运动",
    "friend朋友", "family家庭", "father父亲", "mother母亲", "brother兄弟", "sister姐妹",
    "grandpa爷爷", "grandma奶奶", "Monday星期一", "Friday星期五", "January一月", "December十二月",
    "spring春天", "summer夏天", "weather天气", "rainy下雨的", "hospital医院", "library图书馆",
    "supermarket超市", "station车站", "museum博物馆", "direction方向", "left左边", "right右边",
    "straight直行", "travel旅行", "country国家", "China中国", "America美国", "Japan日本",
    "language语言", "Chinese中文", "festival节日", "Christmas圣诞节", "dragon龙", "traditional传统的",
    "invite邀请", "prepare准备", "celebrate庆祝", "special特别的", "environment环境", "pollution污染",
    "recycle回收", "energy能源", "planet行星", "future未来", "technology科技", "robot机器人",
    "internet互联网", "space太空", "universe宇宙", "experiment实验", "scientist科学家", "discover发现",
    "invention发明", "important重要的", "dangerous危险的", "healthy健康的", "exercise锻炼", "vegetable蔬菜",
    "vitamin维生素", "decision决定", "organization组织", "community社区", "volunteer志愿者"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2_1 like Mac OS X) AppleWebKit/537.36  (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/537.36',
    'accept': '*/*',
   'sec-fetch-site':'same-origin',
   'sec-fetch-mode': 'cors',
   'sec-fetch-dest': 'empty',
   'referer': 'https://t.leftsite.cn/',  # 修改为 https 协议
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i'
}

base_url = 'https://t.leftsite.cn/tts'  # 修改为 https 协议

for item in data:
    # 提取英文部分（包含空格）
    match = re.match(r'^([a-zA-Z\s]+)', item)
    if not match:
        print(f"无法处理条目：{item}，跳过")
        continue

    en_part = match.group(1).strip()
    en = en_part.replace(' ', '_')  # 替换空格为下划线

    params = {
        't': item,
        'v': 'zh-CN-XiaoxiaoNeural',
        'r': 0,
        'p': -3
    }

    try:
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code == 200:
            with open(f'{en}.mp3', 'wb') as f:
                f.write(response.content)
            print(f"成功保存：{en}.mp3")
        else:
            print(f"请求失败，状态码：{response.status_code}，条目：{item}")
    except Exception as e:
        import traceback
        print(f"请求异常，条目：{item}，错误：{e}，堆栈跟踪：{traceback.format_exc()}")

    time.sleep(3)  # 添加时间间隔
