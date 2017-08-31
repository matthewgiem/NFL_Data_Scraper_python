class Season(Player):
    def __init__(self, season, **kwargs):
        self.season = season

        for key, value in kwargs.items():
            setattr(self, key, value)
