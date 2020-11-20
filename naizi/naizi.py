import json
import os
import shutil

print('#by Avalon(moexx)')
print('#需要使用 gog2.0 同时安装 国服 和 国际服，每次反和谐前，请先验证修复国际服')
print('#如果不是默认安装目录 请自行修改 data.json 中的 国服(Gwent_CN) 和 国际服(Gwent) 的路径')
print('#补丁使用说明：https://www.iyingdi.com/web/bbspost/detail/2316619')
print()

if os.path.exists('data.json'):
    f = open('data.json', encoding='utf-8')
    try:
        data = json.load(f)
    except BaseException as e:
        print("data.json 读取失败，请检查文件是否正确，注意必须为双斜杆")
        print("错误原因：", e)
        input('#按任意键关闭：')

    # 储存数据
    try:
        Gwent_CN = data['path']['Gwent_CN']
        Gwent = data['path']['Gwent']
        file = data['Replace_file']
        folder = data['Replace_folder']
        text = data['text']
    except BaseException as e:
        print("data.json 中key出错")
        print("错误原因：", e)
        input('#按任意键关闭：')

    print('国服安装地址：' + Gwent_CN)
    print('国际服安装地址：' + Gwent)
    print()

    if os.path.exists(Gwent_CN + '\\Gwent_Data'):
        if os.path.exists(Gwent + '\\Gwent_Data'):
            input('请确认地址正确后 按【回车键】开始反和谐：')
            print()
            print('开始反和谐')

            # 替换文件
            for path in file:
                print('替换文件：' + Gwent + path['Gwent_CN'])
                shutil.copy(Gwent_CN + path['Gwent_CN'], Gwent + path['Gwent'])

            print()

            # 移动文件夹
            for path in folder:
                G = Gwent + path['Gwent']
                # 判断文件夹是否存在
                if os.path.exists(G):
                    # 删除文件夹删除
                    print('删除文件夹：' + G)
                    shutil.rmtree(G)
                # 移动文件夹
                print('移动文件夹：' + G)
                shutil.copytree(Gwent_CN + path['Gwent_CN'], G)

            print()
            input('#反和谐成功，按任意键关闭：')
        else:
            print('国际服安装地址错误')
            input('#按任意键关闭：')
    else:
        print('国服安装地址地址错误')
        input('#按任意键关闭：')
else:
    print('data.json 缺失，请确保目录下有 data.json 文件')
    input('#按任意键关闭：')
