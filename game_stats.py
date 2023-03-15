import json

class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计数据"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应该重置最高得分
        self.get_history()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def get_history(self):
        # 如果以前存储了用户名，就加载它
        # 否则，提示用户输入用户名并存储它

        filename = 'high_score.json'
        try:
            with open(filename) as f_obj:
                highest_score = json.load(f_obj)
        except FileNotFoundError:
            with open(filename, "w") as f_obj:
                json.dump(0, f_obj)
        else:
            self.high_score = highest_score