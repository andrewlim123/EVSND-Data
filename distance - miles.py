distances = {
    'Hongkong': {
        'Shenzhen': 30,
        'Guangzhou': 135,
        'Dongguan': 68,
        'Foshan': 100,
        'Huizhou': 150,
        'Zhuhai': 60,
        'Macao': 70,
        'Jiangmen': 140,
        'Zhongshan': 90,
        'Zhaoqing': 180
    },
    'Shenzhen': {
        'Hongkong': 30,
        'Guangzhou': 110,
        'Dongguan': 50,
        'Foshan': 80,
        'Huizhou': 120,
        'Zhuhai': 100,
        'Macao': 110,
        'Jiangmen': 160,
        'Zhongshan': 80,
        'Zhaoqing': 170
    },
    'Guangzhou': {
        'Hongkong': 135,
        'Shenzhen': 110,
        'Dongguan': 80,
        'Foshan': 45,
        'Huizhou': 150,
        'Zhuhai': 145,
        'Macao': 140,
        'Jiangmen': 100,
        'Zhongshan': 105,
        'Zhaoqing': 180
    },
    'Dongguan': {
        'Hongkong': 68,
        'Shenzhen': 50,
        'Guangzhou': 80,
        'Foshan': 55,
        'Huizhou': 90,
        'Zhuhai': 90,
        'Macao': 100,
        'Jiangmen': 130,
        'Zhongshan': 40,
        'Zhaoqing': 160
    },
    'Foshan': {
        'Hongkong': 100,
        'Shenzhen': 80,
        'Guangzhou': 45,
        'Dongguan': 55,
        'Huizhou': 110,
        'Zhuhai': 70,
        'Macao': 80,
        'Jiangmen': 60,
        'Zhongshan': 60,
        'Zhaoqing': 125
    },
    'Huizhou': {
        'Hongkong': 150,
        'Shenzhen': 120,
        'Guangzhou': 150,
        'Dongguan': 90,
        'Foshan': 110,
        'Zhuhai': 140,
        'Macao': 150,
        'Jiangmen': 130,
        'Zhongshan': 100,
        'Zhaoqing': 170
    },
    'Zhuhai': {
        'Hongkong': 60,
        'Shenzhen': 100,
        'Guangzhou': 145,
        'Dongguan': 90,
        'Foshan': 70,
        'Huizhou': 140,
        'Macao': 10,
        'Jiangmen': 90,
        'Zhongshan': 50,
        'Zhaoqing': 150
    },
    'Macao': {
        'Hongkong': 70,
        'Shenzhen': 110,
        'Guangzhou': 140,
        'Dongguan': 100,
        'Foshan': 80,
        'Huizhou': 150,
        'Zhuhai': 10,
        'Jiangmen': 100,
        'Zhongshan': 60,
        'Zhaoqing': 160
    },
    'Jiangmen': {
        'Hongkong': 140,
        'Shenzhen': 160,
        'Guangzhou': 100,
        'Dongguan': 130,
        'Foshan': 60,
        'Huizhou': 130,
        'Zhuhai': 90,
        'Macao': 100,
        'Zhongshan': 60,
        'Zhaoqing': 90
    },
    'Zhongshan': {
        'Hongkong': 90,
        'Shenzhen': 80,
        'Guangzhou': 105,
        'Dongguan': 40,
        'Foshan': 60,
        'Huizhou': 100,
        'Zhuhai': 50,
        'Macao': 60,
        'Jiangmen': 60,
        'Zhaoqing': 120
    },
    'Zhaoqing': {
        'Hongkong': 180,
        'Shenzhen': 170,
        'Guangzhou': 180,
        'Dongguan': 160,
        'Foshan': 125,
        'Huizhou': 170,
        'Zhuhai': 150,
        'Macao': 160,
        'Jiangmen': 90,
        'Zhongshan': 120
    }
}
dis={}

for city1 in distances:
    for city2 in distances[city1]:
        distances[city1][city2] *= 0.621371
        dis[city1,city2]=distances[city1][city2]

