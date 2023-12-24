import pandas as pd

def lambda_hander(event, context):
    # 創建一個示例的DataFrame
    data = {'姓名': ['小明', '小華', '小李', '小張'],
            '年齡': [25, 30, 28, 22],
            '城市': ['台北', '台中', '高雄', '新竹']}

    df = pd.DataFrame(data)

    # 顯示DataFrame的內容
    print(df)
    print('test0000002')