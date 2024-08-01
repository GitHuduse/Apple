from os import *
from os.path import abspath, dirname
configfile = {
"config": {
    "title": "Apple",
    "color": {
        "tips": '''
            COLOR [attr]

            attr        指定控制台输出的颜色属性。

            颜色属性由两个十六进制数字指定 -- 第一个
            对应于背景，第二个对应于前景。每个数字
            可以为以下任何值:

                0 = 黑色       8 = 灰色
                1 = 蓝色       9 = 淡蓝色
                2 = 绿色       A = 淡绿色
                3 = 浅绿色     B = 淡浅绿色
                4 = 红色       C = 淡红色
                5 = 紫色       D = 淡紫色
                6 = 黄色       E = 淡黄色
                7 = 白色       F = 亮白色

            如果没有给定任何参数，此命令会将颜色还原到 CMD.EXE 启动时
            的颜色。这个值来自当前控制台
            窗口、/T 命令行开关或 DefaultColor 注册表
            值。

            如果尝试使用相同的
            前景和背景颜色来执行
            COLOR 命令，COLOR 命令会将 ERRORLEVEL 设置为 1。

            示例: "COLOR fc" 在亮白色上产生淡红色
            ''',
        "background": "A",
        "font": "0",
    },
    },
}
system(f"color {configfile['config']['color']['background']}{configfile['config']['color']['font']}")
app = {
    'name':'Apple',
    'version':1.0,
    'source-page':'https://github.com/GitHuduse/Apple',
    'applications': {
        'python': 'python',
        'wsl': 'wsl',
        'cmd': 'cmd',
        'powershell': 'powershell',
    },
    'config': {
        'applications': False,
    },
    'data': {
        'applications': {
            'help': '''语法:
                      applications [application]
                      application: 可用的应用程序

                      如：
                      applications python:
                        打开名为Python的应用程序
''', 
        }, 
    }, 
}
print(f'''
{app['name']} Version:{str(app['version'])}\n
View-Source:{app['source-page']}
''')
while True:
    try:
        put = input(f"{dirname(abspath(__file__))}>")
        code = str(put).split()
        if code[0] == 'exit':
            break
        elif code[0] == 'echo':
            text = code[1]
            print(text)
        elif code[0] == 'applications':
            if app['config']['applications'] == True:
                print(f"Cmd已关闭\n{app['data']['applications']['help']}")
                app['config']['applications'] = False
            else:
                app['config']['applications'] = True
                print(f"Cmd已打开\n{app['data']['applications']['help']}")
            if code[1] == '/?':
                print("可用的App:")
                for key in list(app['applications'].keys()):
                    print(key)

                print(app['data']['applications']['help'])
            else:
                system(code[1])
        else:
            if app['config']['applications'] == True:
                system(put)
            else:
                print(f"{put}: Command not found")
    except:
        pass


exit()
print()