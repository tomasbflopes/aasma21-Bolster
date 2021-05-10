class InvalidDecisionException(BaseException):
    def __init__(self):
        super().__init__("Invalid decision made. Double check the agent code.")


class Decision:
    """DO NOT INSTANTIATE!"""

    def __init__(self, agent):
        self.agent = agent


class UpgradeDecision(Decision):
    """DO NOT INSTANTIATE!"""

    def to_building(self):
        raise NotImplementedError()

    def execute(self):
        raise NotImplementedError()


class UpgradeBarracksDecision(UpgradeDecision):
    def to_building(self):
        return self.agent.get_barracks()

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded the Barracks.")
        print()
        return self.agent.upgrade_barracks()


class UpgradeFarmDecision(UpgradeDecision):
    def to_building(self):
        return self.agent.get_farm()

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded the Farm.")
        print()
        return self.agent.upgrade_farm()


class UpgradeMineDecision(UpgradeDecision):
    def to_building(self):
        return self.agent.get_mine()

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded the Mine.")
        print()
        return self.agent.upgrade_mine()


class UpgradeQuarryDecision(UpgradeDecision):
    def to_building(self):
        return self.agent.get_quarry()

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded the Quarry.")
        print()
        return self.agent.upgrade_quarry()


class UpgradeSawmillDecision(UpgradeDecision):
    def to_building(self):
        return self.agent.get_sawmill()

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded the Sawmill.")
        print()
        return self.agent.upgrade_sawmill()


class UpgradeWallDecision(UpgradeDecision):
    def to_building(self):
        return self.agent.get_wall()

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded the Wall.")
        print()
        return self.agent.upgrade_wall()


class UpgradeWarehouseDecision(UpgradeDecision):
    def to_building(self):
        return self.agent.get_warehouse()

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded the Warehouse.")
        print()
        return self.agent.upgrade_warehouse()


class UpgradeNothingDecision(UpgradeDecision):
    def to_building(self):
        return None

    def execute(self):
        print(f"{self.agent.get_name()} has upgraded nothing.")
        print()
        return self.agent.upgrade_nothing()


class RecruitDecision(Decision):
    """DO NOT INSTANTIATE!"""

    def __init__(self, agent, n="1"):
        super().__init__(agent)

        n = self.check(n)
        self.n = n

    def execute(self, n):
        n = self.check(n)
        if n > self.n:
            raise InvalidDecisionException()

    @staticmethod
    def check(n):
        if not (isinstance(n, int) or n.isdigit()):
            raise InvalidDecisionException()
        n = int(n)
        if n < 1:
            raise InvalidDecisionException()
        return n


class RecruitSpiesDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has recruited {n} Spies.")
        print()
        return self.agent.recruit_spies(n)


class RecruitWarriorsDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has recruited {n} Warriors.")
        print()
        return self.agent.recruit_warriors(n)


class RecruitArchersDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has recruited {n} Archers.")
        print()
        return self.agent.recruit_archers(n)


class RecruitCatapultsDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has recruited {n} Catapults.")
        print()
        return self.agent.recruit_catapults(n)


class RecruitCavalrymenDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has recruited {n} Cavalrymen.")
        print()
        return self.agent.recruit_cavalrymen(n)


class DemoteSpiesDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has demoted {n} Spies.")
        print()
        return self.agent.demote_spies(n)


class DemoteWarriorsDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has demoted {n} Warriors.")
        print()
        return self.agent.demote_warriors(n)


class DemoteArchersDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has demoted {n} Archers.")
        print()
        return self.agent.demote_archers(n)


class DemoteCatapultsDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has demoted {n} Catapults.")
        print()
        return self.agent.demote_catapults(n)


class DemoteCavalrymenDecision(RecruitDecision):
    def execute(self, n):
        super().execute(n)
        print(f"{self.agent.get_name()} has demoted {n} Cavalrymen.")
        print()
        return self.agent.demote_cavalrymen(n)


class RecruitNothingDecision(RecruitDecision):
    def execute(self, n="0"):
        print(f"{self.agent.get_name()} has recruited nothing.")
        print()
        return self.agent.recruit_nothing()


class SpyingDecision(Decision):
    """DO NOT INSTANTIATE!"""

    enemy_village_name = ""

    def execute(self):
        raise NotImplementedError()


class SpyVillageDecision(SpyingDecision):
    def __init__(self, agent, enemy_village_name):
        super().__init__(agent)
        self.enemy_village_name = enemy_village_name

    def execute(self):
        print(f"{self.agent.get_name()} has spied {self.enemy_village_name}.")
        print()
        return self.agent.spy(self.enemy_village_name)


class SpyNothingDecision(SpyingDecision):
    def execute(self):
        print(f"{self.agent.get_name()} has spied nothing.")
        print()
        return self.agent.spy_nothing()


class AttackDecision(Decision):
    """DO NOT INSTANTIATE!"""

    def __init__(self, agent, n_warriors="0", n_archers="0", n_catapults="0", n_cavalrymen="0", enemy_village_name=""):
        super().__init__(agent)

        n_warriors = self.check(n_warriors)
        self.n_warriors = n_warriors

        n_archers = self.check(n_archers)
        self.n_archers = n_archers

        n_catapults = self.check(n_catapults)
        self.n_catapults = n_catapults

        n_cavalrymen = self.check(n_cavalrymen)
        self.n_cavalrymen = n_cavalrymen

        self.enemy_village_name = enemy_village_name

    def execute(self, n_warriors, n_archers, n_catapults, n_cavalrymen):
        n_warriors = self.check(n_warriors)
        n_archers = self.check(n_archers)
        n_catapults = self.check(n_catapults)
        n_cavalrymen = self.check(n_cavalrymen)

        if n_warriors > self.n_warriors or n_archers > self.n_archers or \
           n_catapults > self.n_catapults or n_cavalrymen > self.n_cavalrymen:
            raise InvalidDecisionException()

        if self.n_warriors + self.n_archers + self.n_catapults + self.n_cavalrymen <= 0:
            raise InvalidDecisionException()

    @staticmethod
    def check(n):
        if not (isinstance(n, int) or n.isdigit()):
            raise InvalidDecisionException()
        n = int(n)
        if n < 0:
            raise InvalidDecisionException()
        return n


class AttackVillageDecision(AttackDecision):
    def __init__(self, agent, n_warriors, n_archers, n_catapults, n_cavalrymen, enemy_village_name):
        super().__init__(agent, n_warriors, n_archers, n_catapults, n_cavalrymen, enemy_village_name)
        if self.n_warriors + self.n_archers + self.n_catapults + self.n_cavalrymen <= 0:
            raise InvalidDecisionException()

    def execute(self, n_warriors, n_archers, n_catapults, n_cavalrymen):
        super().execute(n_warriors, n_archers, n_catapults, n_cavalrymen)
        print(f"{self.agent.get_name()} has attacked {self.enemy_village_name} using ", end="")
        print(f"{n_warriors} warriors, {n_archers} archers, {n_catapults} catapults, and {n_cavalrymen} cavalrymen.")
        print()
        return self.agent.send_attack(n_warriors, n_archers, n_catapults, n_cavalrymen, self.enemy_village_name)


class AttackNothingDecision(AttackDecision):
    def execute(self, n_warriors=None, n_archers=None, n_catapults=None, n_cavalrymen=None):
        print(f"{self.agent.get_name()} has attacked nothing.")
        print()
        return self.agent.attack_nothing()