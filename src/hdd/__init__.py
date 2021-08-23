import sys

import src.hdd.format as cmd_format


class SubCommands:

    def format(self, dev_name: str):
        """
        
        HDDにパーティションを作成し、ext4でフォーマットする

        Args:
            dev_name (str): HDDのパス
        """
        if not type(dev_name) == str:
            print('Input str object')
            sys.exit(-1)
        
        return cmd_format.run(dev_name)