from agent.agent import Agent
from agent.decisions import *


class DeliberativeAgent(Agent):

    desires = []
    intention = None
    plan = []

    def upgrade_decision(self):
        self.brf()

        while True:
            if self.plan and not self.succeeded_intention() and not self.impossible_intention():
                action = self.plan.pop(0)
                if self.sound():
                    assert issubclass(action.__class__, UpgradeDecision)
                    return action.execute()
                else:
                    self.plan = self.remake_plan()
                if self.reconsider():
                    self.desires = self.options()
                    self.intention = self.filter()

            else:
                self.desires = self.options()
                self.intention = self.filter()
                self.plan = self.make_plan()
                if not self.plan:
                    action = UpgradeNothingDecision(self)
                    assert issubclass(action.__class__, UpgradeDecision)
                    return action.execute()

    def brf(self):
        pass

    def options(self):
        options = []
        for building in self.village.get_all_buildings():
            if self.can_upgrade(building):
                options.append(self.building_to_upgrade_action(building))
        options.append(UpgradeNothingDecision(self))
        return options

    def filter(self):
        # Priority system as follows (SUBJECT TO LOTS OF CHANGES, namely considering desires from other decision types):
        # - Upgrade farm if farm is full
        # - Upgrade warehouse if production of a resource is > 0.5 * warehouse capacity
        # - Upgrade resource camp, prioritizing resource with lowest amount
        # - Upgrade barracks
        # - Upgrade wall
        # - Upgrade warehouse if full
        # - Upgrade farm if warehouse is full (just as a resource dump)
        # - Upgrade nothing

        # Farm
        if self.village.get_troops() == self.get_farm().capacity():
            for desire in self.desires:
                if isinstance(desire, UpgradeFarmDecision):
                    return desire

        # Warehouse (if producing a lot)
        if self.village.get_mine().production() > 0.5 * self.village.get_warehouse().capacity() or \
           self.village.get_quarry().production() > 0.5 * self.village.get_warehouse().capacity() or \
           self.village.get_sawmill().production() > 0.5 * self.village.get_warehouse().capacity():
            for desire in self.desires:
                if isinstance(desire, UpgradeWarehouseDecision):
                    return desire

        # Barracks
        for desire in self.desires:
            if isinstance(desire, UpgradeBarracksDecision):
                return desire

        # Resource camp
        if self.village.get_iron() >= self.village.get_stone() >= self.village.get_wood():
            priorities = [UpgradeMineDecision(self), UpgradeQuarryDecision(self), UpgradeSawmillDecision(self)]
        elif self.village.get_iron() >= self.village.get_wood() >= self.village.get_stone():
            priorities = [UpgradeMineDecision(self), UpgradeSawmillDecision(self), UpgradeQuarryDecision(self)]
        elif self.village.get_stone() >= self.village.get_iron() >= self.village.get_wood():
            priorities = [UpgradeQuarryDecision(self), UpgradeMineDecision(self), UpgradeSawmillDecision(self)]
        elif self.village.get_stone() >= self.village.get_wood() >= self.village.get_iron():
            priorities = [UpgradeQuarryDecision(self), UpgradeSawmillDecision(self), UpgradeMineDecision(self)]
        elif self.village.get_wood() >= self.village.get_iron() >= self.village.get_stone():
            priorities = [UpgradeSawmillDecision(self), UpgradeMineDecision(self), UpgradeQuarryDecision(self)]
        else:
            priorities = [UpgradeSawmillDecision(self), UpgradeQuarryDecision(self), UpgradeMineDecision(self)]
        for i in range(3):
            for desire in self.desires:
                if isinstance(desire, priorities[i].__class__):
                    return desire

        # Wall
        for desire in self.desires:
            if isinstance(desire, UpgradeWallDecision):
                return desire

        if self.village.get_iron() == self.village.get_warehouse().capacity() or \
           self.village.get_stone() == self.village.get_warehouse().capacity() or \
           self.village.get_wood() == self.village.get_warehouse().capacity():
            # Warehouse (if full of at least one resource)
            for desire in self.desires:
                if isinstance(desire, UpgradeWarehouseDecision):
                    return desire
            # Farm (if warehouse is full of at least one resource, just to dump resources)
            for desire in self.desires:
                if isinstance(desire, UpgradeFarmDecision):
                    return desire

        # Nothing
        for desire in self.desires:
            if isinstance(desire, UpgradeNothingDecision):
                return desire

        raise Exception("Should not get here! Failed in upgrade_filter()")

    def make_plan(self):
        return [self.intention]

    def succeeded_intention(self):
        return False

    def impossible_intention(self):
        return False

    def sound(self):
        for action in self.plan:
            if action.to_building().is_max_level():
                return False
        total_iron = 0
        total_stone = 0
        total_wood = 0
        for action in self.plan:
            total_iron += self.cost_of_upgrade_action(action)[0]
            total_stone += self.cost_of_upgrade_action(action)[1]
            total_wood += self.cost_of_upgrade_action(action)[2]
        if total_iron > self.village.get_wood() or \
           total_stone > self.village.get_stone() or \
           total_wood > self.village.get_wood():
            return False
        return True

    def remake_plan(self):
        return [UpgradeNothingDecision(self)]

    def reconsider(self):
        return True

    def recruit_decision(self):
        action = RecruitNothingDecision(self)

        assert issubclass(action.__class__, RecruitDecision)
        return action.execute()

    def spying_decision(self):
        action = SpyNothingDecision(self)

        assert issubclass(action.__class__, SpyingDecision)
        return action.execute()

    def attack_decision(self):
        action = AttackNothingDecision(self)

        assert issubclass(action.__class__, AttackDecision)
        return action.execute()