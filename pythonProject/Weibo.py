# author:cycsir  time:2021/1/22
import spider

baseurl = "https://m.weibo.cn/api/container/getIndex?containerid={}&page={}"
renminwang = "1076032286908003"
yangshixinwen = "1076032656274875"
zgqingnianbao = "1076031726918143"
banyuetan = "1076032318265821"

urls = (
    renminwang,
    yangshixinwen,
    banyuetan
)

startpages = (
    2525,
    2100,
    2550
)

lastpages = (
    2320,
    1005,
    1258,
)

savepave = (
    ".\\01人民网\\",
    ".\\02央视新闻\\",
    ".\\03半月谈\\"
)

header1 = {
    "cookie": "SUB=_2A25NA5ziDeThGeNN61IZ9i_EwzqIHXVuDySqrDV6PUJbktAKLU74kW1NScdmAZozUPCe0F7eylt2zMy9qhd-OTFE; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWozF7q_JZ7Mvh.HDJerxx-5NHD95Qfe0571hqp1hncWs4Dqcjni--fi-2XiKLWi--fi-2XiKLWi--ci-zXiKLFS0nESKBt; SSOLoginState=1611132083; _T_WM=78352212005; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032286908003%26fid%3D1076032286908003%26uicode%3D10000011; XSRF-TOKEN=b2e19b",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}  # page
header2 = {
    "cookie": "WEIBOCN_FROM=1110006030; loginScene=102003; SUB=_2A25ND7h1DeRhGeBO41sT-SvOyjiIHXVu89g9rDV6PUJbkdAKLVfDkW1NRYkdIYNPoipQ2nZMSRxspyX4bDQ8-fcO; _T_WM=78353051297; XSRF-TOKEN=e08b09; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}  # page
header3 = {
    "cookie": "_T_WM=96389282857; WEIBOCN_FROM=1110006030; XSRF-TOKEN=526321; loginScene=102003; SUB=_2A25ND70cDeRhGeFL7lYZ8ynKyTyIHXVu88NUrDV6PUJbktANLVHakW1NfeCpB2THRSjIiXmMEwOZemcERCIBgH1S; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFVzXU6ciuTrqpsinSDlxAg5JpX5KzhUgL.FoMfSKBRe0Mceo52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSK-X1heNSoz7; SSOLoginState=1611386188; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E4%25BA%25BA%25E6%25B0%2591%25E7%25BD%2591%26fid%3D1005052286908003%26uicode%3D10000011",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}  # page
header4 = {
"authority": "m.weibo.cn",
"method": "GET",
"path": "/api/container/getIndex?uid=2286908003&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%BA%BA%E6%B0%91%E7%BD%91&type=uid&value=2286908003&containerid=1005052286908003",
"scheme": "https",
"accept": "application/json, text/plain, */*",
"accept-language": "zh-CN,zh;q=0.9",
"cookie": "_T_WM=96389282857; WEIBOCN_FROM=1110006030; XSRF-TOKEN=526321; loginScene=102003; SUB=_2A25ND70cDeRhGeFL7lYZ8ynKyTyIHXVu88NUrDV6PUJbktANLVHakW1NfeCpB2THRSjIiXmMEwOZemcERCIBgH1S; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFVzXU6ciuTrqpsinSDlxAg5JpX5KzhUgL.FoMfSKBRe0Mceo52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNSK-X1heNSoz7; SSOLoginState=1611386188; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E4%25BA%25BA%25E6%25B0%2591%25E7%25BD%2591%26fid%3D1005052286908003%26uicode%3D10000011mweibo-pwa: 1",
"referer": "https://m.weibo.cn/u/2286908003?uid=2286908003&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%BA%BA%E6%B0%91%E7%BD%91",
 #"sec-ch-ua": "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
"sec-ch-ua-mobile": "?0",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
"x-requested-with": "XMLHttpRequest",
"x-xsrf-token": "526321",
}
header5 = {
    "cookie": "WEIBOCN_FROM=1110006030; SUB=_2A25ND5UmDeRhGeFN7lYU8yrFyjiIHXVu8zturDV6PUJbkdAKLWzekW1NQBhQaT8D2SkSSuKMfC7yMdtxnXPH7XkA; _T_WM=55837080155; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174%26uicode%3D20000174; XSRF-TOKEN=b535fe",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}  # page

headers = (
    header1,
    header2,
    header3,
    header4,
    header5
)

mindKeywords = (
    ['加油03\n', '希望02\n', '致敬00\n', '感谢00\n', '好消息01\n', '挺住03\n', '相信02\n', '支持03\n', '可爱04\n', '喜欢04\n', '必胜02\n', '战胜02\n', '稳住03\n', '胜利02\n', '没事02\n', '自豪01\n', '棒棒04\n', '好看04\n', '开心01\n', '好吃04\n', '好听04\n', '欣赏04\n', '坚强03\n', '真棒04\n', '了不起04\n', '撑住03\n', '庆祝05\n', '顶上去04\n', '满意05\n', '好帅04\n', '太帅04\n', '盼望着03\n', '点赞04\n', '帅气04\n', '冲冲04\n', '热烈祝贺05\n', '敬意04\n', '鼓掌04\n', '最帅04\n', '伟大祖国05\n', '笑容03\n', '胜利在望02\n', '微笑03\n'],
    ['期待13\n', '平平安安13\n', '感动14\n', '祝愿13\n', '保佑13\n', '祈祷13\n', '羡慕13\n', '不信10\n', '前程似锦13\n', '泪目14\n', '佩服13\n', '预祝13\n', '反思15\n', '考必过13\n', '质疑10\n', '缅怀13\n', '期盼13\n', '冷漠11\n', '看哭14\n', '震撼15\n', '祝願13\n', '震惊15\n', '走好15\n', '感人14\n', '牢记15\n', '无忧13\n', '抱歉15\n', '疑问15\n', '同情15\n', '丢脸15\n', '感激14\n', '落泪14\n', '恭祝13\n', '泪点14\n', '淡定15\n', '恳求15\n', '反省15\n', '后悔15\n'],
    ['难过20\n', '眼泪20\n', '可怜20\n', '发抖22\n', '抱怨23\n', '咋办22\n', '活该21\n', '迷惑22\n', '吓人23\n', '失望23\n', '心酸20\n', '绝望23\n', '崩溃22\n', '可恶23\n', '无情23\n', '讨厌23\n', '该死23\n', '心寒23\n', '痛心20\n', '委屈20\n', '无助23\n', '嘲笑23\n', '不服23\n', '累垮23\n', '寒心20\n', '嫌弃23\n', '伤心20\n', '自作孽23\n', '消极23\n', '耻辱23\n', '嫉妒23\n', '可笑23\n', '担忧22\n', '心碎20\n', '顶不住22\n', '气愤23\n', '生怕22\n', '报应23\n', '吓死23\n', '哭泣20\n', '煎熬22\n', '愤怒21\n', '心理压力22\n', '恫吓23\n', '嘲讽23\n']
)

keywords = ['疫情', '病例', '新冠', '肺炎', '确诊', '防控', '武汉', '新增', '输入', '检测', '病毒', '湖北', '医院', '死亡', '医疗队', '患者', '隔离', '专家', '医疗', '抗疫', '感染', '恢复', '世卫', '核酸', '物资', '口罩', '措施', '研究', '复工', '应对', '重症', '出院', '社区', '防疫', '救治', '治疗', '治愈', '疾控中心', '武汉市', '医生', '疑似病例', '支援', '风险', '本土', '入境', '通报', '救援', '复产', '专家组', '生命', '医护人员', '抗击', '保障', '感染者', '症状', '医学观察', '超过', '疫苗', '防护', '测量', '人数', '湖北省', '解除', '试验', '阳性', '聚集', '复课', '观察', '联防', '传播', '蔓延', '管控', '钟南山', '控制', '动物', '护士', '战疫', '公共卫生', '援助', '工作者', '暴发', '扩大', '实验室', '病人', '流行病学', '发热', '检查', '消杀', '疾病', '扩散', '统计数据', '病毒检测', '研究所', '逝世', '收治', '复苏', '传染病', '临床', '防范', '医护', '严防', '驰援', '诊疗', '危重症', '受伤', '医学', '医务人员', '消毒剂', '抗体', '流行', '病区', '病房', '承担', '解封', '注射', '疑似', '采样', '筛查', '封闭', '门诊', '返京', '样本', '医疗机构', '体温', '佩戴', '野生动物', '消毒', '流感', '就诊', '咳嗽', '阴性', '医用', '复学', '高风险', '预防', '首例', '病情', '严控', '免疫', '定点医院', '白衣战士']
