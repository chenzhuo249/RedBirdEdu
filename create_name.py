


str1 = """
赵    钱    孙    李    周    吴    郑    王    冯    陈    褚    卫    蒋    沈    韩    杨    朱    秦    尤   许 

何    吕    施    张    孔    曹    严    华    金    魏    陶    姜    戚    谢    邹    喻    柏    水    窦   章 

云    苏    潘    葛    奚    范    彭    郎    鲁    韦    昌    马    苗    凤    花    方    俞    任    袁   柳 

酆    鲍    史    唐    费    廉    岑    薛    雷    贺    倪    汤    滕    殷    罗    毕    郝    邬    安   常 

乐    于    时    傅    皮    卞    齐    康    伍    余    元    卜    顾    孟    平    黄    和    穆    萧   尹 

姚    邵    湛    汪    祁    毛    禹    狄    米    贝    明    臧    计    伏    成    戴    谈    宋    茅   庞 

熊    纪    舒    屈    项    祝    董    梁    杜    阮    蓝    闵    席    季    麻    强    贾    路    娄   危 
"""

for line in str1.split("\n"):
    print(line.split("    "))

['']
['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤 \xa0 许\xa0']
['']
['何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦 \xa0 章\xa0']
['']
['云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁 \xa0 柳\xa0']
['']
['酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安 \xa0 常\xa0']
['']
['乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧 \xa0 尹\xa0']
['']
['姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅 \xa0 庞\xa0']
['']
['熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄 \xa0 危\xa0']
['']