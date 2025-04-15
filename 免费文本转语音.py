import requests
import re
import time

data = [
    "ruler尺子", "pencil铅笔", "eraser橡皮", "crayon蜡笔", "bag书包", "pen钢笔", "book书", "sharpener卷笔刀", "school学校", "head头", "face脸", "nose鼻子", "mouth嘴", "eye眼睛", "ear耳朵", "arm手臂", "leg腿", "foot脚", "red红色", "yellow黄色", "green绿色", "blue蓝色", "black黑色", "white白色", "orange橙色", "cat猫", "dog狗", "panda熊猫", "bird鸟", "tiger老虎", "zoo动物园", "cake蛋糕", "bread面包", "milk牛奶", "water水", "fish鱼", "rice米饭", "one一", "two二", "three三", "four四", "five五", "six六", "seven七", "eight八", "nine九", "ten十", "girl女孩", "family家庭", "father爸爸", "mother妈妈", "brother兄弟", "sister姐妹", "grandpa爷爷", "grandma奶奶", "apple苹果", "banana香蕉", "orange橙子", "grape葡萄", "like喜欢", "monkey猴子", "elephant大象", "lion狮子", "giraffe长颈鹿", "tall高的", "short矮的", "car小汽车", "boat小船", "map地图", "cap帽子", "pear梨", "strawberry草莓", "watermelon西瓜", "eleven十一", "twelve十二", "thirteen十三", "fifteen十五", "twenty二十", "classroom教室", "window窗户", "blackboard黑板", "light电灯", "picture图画", "door门", "teacher's desk讲台", "computer计算机", "fan风扇", "wall墙壁", "floor地板", "TV电视", "clean打扫", "help帮助", "schoolbag书包", "maths book数学书", "English book英语书", "Chinese book语文书", "storybook故事书", "notebook笔记本", "toy玩具", "key钥匙", "strong强壮的", "friendly友好的", "quiet安静的", "glasses眼镜", "hat帽子", "classroom教室", "really真的", "near靠近", "schoolbag书包", "lost丢失", "friendly友好的", "quiet安静的", "hair头发", "shoe鞋子", "bedroom卧室", "sofa沙发", "fridge冰箱", "phone电话", "first floor一楼", "second floor二楼", "teachers' office教师办公室", "library图书馆", "playground操场", "computer room计算机房", "art room美术教室", "music room音乐教室", "breakfast早餐", "English class英语课", "lunch午餐", "PE class体育课", "dinner晚餐", "get up起床", "go to school上学", "cold寒冷的", "warm温暖的", "hot炎热的", "sunny晴朗的", "rainy多雨的", "windy多风的", "cloudy多云的", "tomato西红柿", "potato土豆", "carrot胡萝卜", "green beans豆角", "horse马", "cow奶牛", "sheep绵羊", "clothes衣服", "dress连衣裙", "skirt短裙", "coat外套", "shirt衬衫", "shoes鞋子", "gloves手套", "scarf围巾", "umbrella雨伞", "sunglasses太阳镜", "expensive昂贵的", "cheap便宜的", "size尺码", "price价格", "sale促销", "cashier收银员", "spring春天", "summer夏天", "autumn秋天", "winter冬天", "rainy多雨的", "sunny晴朗的", "windy多风的", "cloudy多云的", "bedroom卧室", "living room客厅", "kitchen厨房", "bathroom浴室", "fridge冰箱", "sofa沙发", "table桌子", "January一月", "February二月", "March三月", "April四月", "May五月", "June六月", "July七月", "August八月", "September九月", "October十月", "November十一月", "December十二月", "Monday星期一", "Tuesday星期二", "Wednesday星期三", "Thursday星期四", "Friday星期五", "Saturday星期六", "Sunday星期日", "beef牛肉", "chicken鸡肉", "noodles面条", "soup汤", "chopsticks筷子", "fork餐叉", "do morning exercises晨练", "eat breakfast吃早餐", "have English class上英语课", "play sports运动", "go shopping购物", "spring春天", "summer夏天", "autumn秋天", "winter冬天", "season季节", "January一月", "February二月", "March三月", "April四月", "May五月", "June六月", "climb mountains爬山", "visit grandparents看望祖父母", "go hiking远足", "weekend周末", "kangaroo袋鼠", "jump跳", "swim游泳", "fly飞", "July七月", "August八月", "September九月", "October十月", "November十一月", "December十二月", "do homework做作业", "watch TV看电视", "read books读书", "climb trees爬树", "catch mice捉老鼠", "go camping露营", "take photos拍照", "science科学", "history历史", "geography地理", "biology生物", "chemistry化学", "physics物理", "mathematics数学", "language语言", "doctor医生", "engineer工程师", "artist艺术家", "nurse护士", "farmer农民", "driver司机", "scientist科学家", "astronaut宇航员", "pilot飞行员", "coach教练", "robot机器人", "rocket火箭", "spaceship宇宙飞船", "satellite卫星", "recycle回收", "pollution污染", "protect保护", "energy能源", "traditional传统的", "festival节日", "custom习俗", "passport护照", "visa签证", "sightseeing观光", "luggage行李", "architect建筑师", "journalist记者", "artificial intelligence人工智能", "programming编程", "sustainable可持续的", "carbon footprint碳足迹", "Mid-Autumn Festival中秋节", "Dragon Boat Festival端午节", "boarding pass登机牌", "currency货币", "souvenir纪念品"
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