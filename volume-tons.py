vol = {
    'Hongkong': {
        'Shenzhen': 387,
        'Guangzhou': 335,
        'Dongguan': 168,
        'Foshan': 182,
        'Huizhou': 73,
        'Zhuhai': 35,
        'Macao': 180,
        'Jiangmen': 47,
        'Zhongshan': 136,
        'Zhaoqing': 27
    },
    'Shenzhen': {
        'Hongkong': 380,
        'Guangzhou': 300,
        'Dongguan': 350,
        'Foshan': 80,
        'Huizhou': 120,
        'Zhuhai': 100,
        'Macao': 80,
        'Jiangmen': 160,
        'Zhongshan': 180,
        'Zhaoqing': 70
    },
    'Guangzhou': {
        'Hongkong': 335,
        'Shenzhen': 330,
        'Dongguan': 280,
        'Foshan': 145,
        'Huizhou': 150,
        'Zhuhai': 145,
        'Macao': 70,
        'Jiangmen': 120,
        'Zhongshan': 105,
        'Zhaoqing': 80
    },
    'Dongguan': {
        'Hongkong': 368,
        'Shenzhen': 330,
        'Guangzhou': 380,
        'Foshan': 55,
        'Huizhou': 90,
        'Zhuhai': 90,
        'Macao': 850,
        'Jiangmen': 130,
        'Zhongshan': 240,
        'Zhaoqing': 60
    },
    'Foshan': {
        'Hongkong': 100,
        'Shenzhen': 180,
        'Guangzhou': 145,
        'Dongguan': 155,
        'Huizhou': 110,
        'Zhuhai': 70,
        'Macao': 80,
        'Jiangmen': 60,
        'Zhongshan': 90,
        'Zhaoqing': 65
    },
    'Huizhou': {
        'Hongkong': 150,
        'Shenzhen': 190,
        'Guangzhou': 200,
        'Dongguan': 190,
        'Foshan': 110,
        'Zhuhai': 140,
        'Macao': 150,
        'Jiangmen': 130,
        'Zhongshan': 100,
        'Zhaoqing': 70
    },
    'Zhuhai': {
        'Hongkong': 60,
        'Shenzhen': 180,
        'Guangzhou': 145,
        'Dongguan': 90,
        'Foshan': 70,
        'Huizhou': 140,
        'Macao': 200,
        'Jiangmen': 90,
        'Zhongshan': 60,
        'Zhaoqing': 50
    },
    'Macao': {
        'Hongkong': 170,
        'Shenzhen': 100,
        'Guangzhou': 180,
        'Dongguan': 100,
        'Foshan': 80,
        'Huizhou': 50,
        'Zhuhai': 200,
        'Jiangmen': 100,
        'Zhongshan': 60,
        'Zhaoqing': 50
    },
    'Jiangmen': {
        'Hongkong': 140,
        'Shenzhen': 160,
        'Guangzhou': 180,
        'Dongguan': 130,
        'Foshan': 60,
        'Huizhou': 130,
        'Zhuhai': 90,
        'Macao': 100,
        'Zhongshan': 160,
        'Zhaoqing': 50
    },
    'Zhongshan': {
        'Hongkong': 90,
        'Shenzhen': 250,
        'Guangzhou': 205,
        'Dongguan': 240,
        'Foshan': 60,
        'Huizhou': 100,
        'Zhuhai': 150,
        'Macao': 50,
        'Jiangmen': 120,
        'Zhaoqing': 60
    },
    'Zhaoqing': {
        'Hongkong': 80,
        'Shenzhen': 70,
        'Guangzhou': 80,
        'Dongguan': 60,
        'Foshan': 125,
        'Huizhou': 70,
        'Zhuhai': 50,
        'Macao': 60,
        'Jiangmen': 90,
        'Zhongshan': 120
    }
}
vol2={}
node = ["Zhaoqing", "Guangzhou","Shenzhen","Hongkong","Huizhou","Dongguan","Zhuhai","Macao","Foshan","Zhongshan","Jiangmen"]

for city1 in node:
    for city2 in vol[city1]:
        vol2[city1,city2] = vol[city1][city2]