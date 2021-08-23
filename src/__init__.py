import fire

import src.hdd as hdd
import src.video as video


# ===================================================================================================================================

r"""サブコマンドを辞書型で作成する方法

'zd hdd format /dev/sda -- --trace' を実行した結果、以下の順で実行されることが確認できる
    Fire trace:
    1. Initial component
    2. Accessed property "hdd"
    3. Instantiated class "SubCommands" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\hdd\__init__.py:6)
    4. Accessed property "format" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\hdd\__init__.py:7)
    5. Called routine "format" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\hdd\__init__.py:7)
"""

# def run():
#     """辞書でサブコマンドを作ると、ここの docstring はヘルプに使えない:("""

#     # Make Python Fire not use a pager when it prints a help text
#     # (https://github.com/google/python-fire/issues/188#issuecomment-791972163)
#     fire.core.Display = lambda lines, out: print(*lines, file=out)
#     fire.Fire({
#         'hdd' : hdd.SubCommands,
#         'video': video.SubCommands,
#         # 'help': help(),
#     })


# def help():
#     """--helpをオーバーライドできない"""
#     print('~~ help message ~~')

# -- or -----------------------------------------------------------------------------------------------------------------------------

r"""サブコマンドをクラスの実体で作成する方法

'zd hdd format /dev/sda -- --trace' を実行した結果、以下の順で実行されることが確認できる
    Fire trace:
    1. Initial component
    2. Instantiated class "Commands" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\__init__.py:23)
    3. Accessed property "hdd" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\hdd\__init__.py:6)
    4. Instantiated class "SubCommands" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\hdd\__init__.py:6)
    5. Accessed property "format" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\hdd\__init__.py:7)
    6. Called routine "format" (c:\users\yosei\documents\fairyworkspace\cli_example\fire_example\src\hdd\__init__.py:7)
"""

def run():
    # Make Python Fire not use a pager when it prints a help text
    # (https://github.com/google/python-fire/issues/188#issuecomment-791972163)
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(Commands)


class Commands:
    """コマンドでサブコマンドを指定すると help にここの docstring が使えるようになる"""

    # def __init__(self, help=False):
    #     """
    #     helpフラグをコンストラクタで設定したらhelp表示が綺麗になるかと思ったけど、
    #     オーバーライドできずに両方表示される羽目になった。
    #     stderr や stdout を /dev/null に捨てる記述も入れてみたけど無意味だった。
    #     help は __doc__ を呼んでるっぽいのでそれを止めるとかなら可能...?

    #     ただ、ヘルプ表示が
        
    #     SYNOPSIS
    #         zd --help COMMAND
        
    #     COMMANDS
    #         COMMAND is one of the following:
        
    #          hdd
        
    #          help
        
    #     みたいになって気持ち悪くなったのでコンストラクタを導入するのは却下。
    #     """
    #     if(help):
    #         from contextlib import redirect_stderr
    #         import os

    #         with redirect_stderr(open(os.devnull, 'w')):
    #             self.help()
    
    # def help(self):
    #     print('~~ this is help message ~~')
    
    hdd = hdd.SubCommands   # コマンド名 = 呼び出す関数, クラス
    video = video.SubCommands

# ===================================================================================================================================


if __name__ == '__main__':
    run()