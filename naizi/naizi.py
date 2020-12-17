import json
import os
import shutil
import zipfile
import getpass

print('# by Avalon(moexx)')
print('# 需要使用 gog2.0 同时安装 国服 和 国际服，每次反和谐前，请先验证修复国际服')
print('# 如果不是默认安装目录 请自行修改 data.json 中的 国服(Gwent_CN) 和 国际服(Gwent) 的路径')
print('# 补丁使用说明：https://www.iyingdi.com/web/bbspost/detail/2316619')
print()


# 压缩
def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            datafile = os.path.join(parent, filename)
            rename = datafile[pre_len:].strip(os.path.sep)
            zipf.write(datafile, rename.replace("data_definitions\\", ""))
    zipf.close()


# 反和谐文本
def data_definitions(url):
    print(url)
    print('备份 data_definitions 为 data_definitions1')
    shutil.copy(url, url + '1')

    print('# 解压 data_definitions')
    data_zip = zipfile.ZipFile(url, 'a')
    data_zip.extractall("./data_definitions")
    data_zip.close()
    d = open('data_definitions\\Localization\\zh-cn.csv', encoding='utf-8')
    zh_cn = d.read()
    d.close()

    print('# 开始替换 zh-cn.csv 文字内容')
    for t in text:
        zh_cn = zh_cn.replace(t['River_crab'], t['Against'])
    # 写入文件
    with open('data_definitions\\Localization\\zh-cn.csv', 'w', encoding='utf-8') as f:
        f.write(zh_cn)
        f.close()
    print('# 压缩 data_definitions')
    make_zip('./data_definitions', 'data_definitions.zip')

    print('# 移除临时文件')
    shutil.rmtree('./data_definitions')

    print('# 替换 data_definitions')
    shutil.move('./data_definitions.zip', './data_definitions')
    shutil.move('./data_definitions', url)


if os.path.exists('data.json'):
    f = open('data.json', encoding='utf-8')
    try:
        data = json.load(f)
    except BaseException as e:
        print("# data.json 读取失败，请检查文件是否正确，注意必须为双斜杆")
        print("# 错误原因：", e)
        input('# 按任意键关闭：')

    # 储存数据
    try:
        Gwent_CN = data['path']['Gwent_CN']
        Gwent = data['path']['Gwent']
        file = data['Replace_file']
        folder = data['Replace_folder']
        text = data['text']
        user_definitions = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\LocalLow\\CDProjektRED\\Gwent\\Data\\data_definitions'
    except BaseException as e:
        print("# data.json 中key出错")
        print("# 错误原因：", e)
        input('# 按任意键关闭：')

    print('# 国服安装地址：' + Gwent_CN)
    print('# 国际服安装地址：' + Gwent)
    print()

    if os.path.exists(Gwent_CN + '\\Gwent_Data'):
        if os.path.exists(Gwent + '\\Gwent_Data'):

            is_game = input('# 是否反开始反和谐游戏(y/n)：')
            if is_game == 'y':
                # 反和谐游戏
                print()
                print('开始反和谐游戏')

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
                input('#反和谐游戏成功，按任意键继续：')
            else:
                input('# 反和谐游戏终止，按任意键继续：')
            is_text = input('# 是否反和谐文字(y/n)：')
            if is_text == 'y':
                if os.path.exists(user_definitions):
                    print()
                    print('# 开始反和谐热更后的文本')
                    data_definitions(user_definitions)

                print()
                print('# 开始反和谐本体文本')
                data_definitions(Gwent + '\\Gwent_Data\\StreamingAssets\\data_definitions')

                print()
                input('#反和谐文字成功，按任意键继续：')
            else:
                print()
                input('#反和谐文字终止，按任意键继续：')
        else:
            print('# 国际服安装地址错误')
            input('# 按任意键关闭：')
    else:
        print('# 国服安装地址地址错误')
        input('# 按任意键关闭：')
else:
    print('data.json 缺失，请确保目录下有 data.json 文件')
    input('# 按任意键关闭：')
