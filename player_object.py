class Player:

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)
    team = ""
    age = 0
    passing_yrd = 0
    passing_td = 0
    passing_int = 0
    rushing_att = 0
    rushing_yrd = 0
    rushing_td = 0
    receiving_trg = 0
    receiving_rec = 0
    receiving_yrd = 0
    receiving_td = 0
    return_yrd = 0
    return_td = 0
    misc_2pt = 0
    fum_lost = 0
    tack_solo = 0
    tack_ast = 0
    sack = 0
    safety = 0
    pass_deff = 0
    blk_kick = 0
    turnover_int = 0
    fum_force = 0
    fum_recover = 0
    defensive_td = 0
    fgm_0_19 = 0
    fgm_20_29 = 0
    fgm_30_39 = 0
    fgm_40_49 = 0
    fgm_50 = 0
    pat = 0
    bye_week = 0
