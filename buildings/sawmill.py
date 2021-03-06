from buildings.building import Building


class Sawmill(Building):
    UPGRADE_COSTS = [None, [90, 90, 50], [200, 200, 125], [500, 500, 300], [1250, 1250, 750]]
    PRODUCTIONS = [None, 20, 40, 80, 160, 320]

    def __init__(self):
        self.level = 1

    def production(self):
        return self.PRODUCTIONS[self.level]

    def next_production(self):
        if self.is_max_level():
            return "(MAXED)"
        else:
            return self.PRODUCTIONS[self.level + 1]
