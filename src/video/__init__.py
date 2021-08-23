import src.video.crop as cmd_crop
import src.video.small as cmd_small


class SubCommands:
    def small(self):
        return cmd_small.run()

    def crop(self):
        return cmd_crop.run()