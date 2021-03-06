class Report:
    def __init__(self, attacking_village, defending_village, attacking_luck, defending_luck,
                 starting_attacking_warriors, starting_attacking_archers,
                 starting_attacking_catapults, starting_attacking_cavalrymen,
                 starting_defending_warriors, starting_defending_archers,
                 starting_defending_catapults, starting_defending_cavalrymen,
                 winner, loser, casualty_luck, attacking_power, defending_power):
        self.new = True

        self.attacking_village = attacking_village
        self.defending_village = defending_village

        # Converts [0.8, 1.2) luck values to [0, 100)% interval
        self.attacking_luck = ((attacking_luck - 0.8) / 0.4) * 100
        self.defending_luck = ((defending_luck - 0.8) / 0.4) * 100

        self.starting_attacking_warriors = starting_attacking_warriors
        self.starting_attacking_archers = starting_attacking_archers
        self.starting_attacking_catapults = starting_attacking_catapults
        self.starting_attacking_cavalrymen = starting_attacking_cavalrymen
        self.starting_defending_warriors = starting_defending_warriors
        self.starting_defending_archers = starting_defending_archers
        self.starting_defending_catapults = starting_defending_catapults
        self.starting_defending_cavalrymen = starting_defending_cavalrymen

        self.winner = winner
        self.loser = loser

        # Converts [2, 6) luck value to [0, 100)% interval
        self.casualty_luck = ((casualty_luck - 2) / 4) * 100

        self.attacking_power = attacking_power
        self.defending_power = defending_power

        self.ending_attacking_warriors = None
        self.ending_attacking_archers = None
        self.ending_attacking_catapults = None
        self.ending_attacking_cavalrymen = None
        self.ending_defending_warriors = None
        self.ending_defending_archers = None
        self.ending_defending_catapults = None
        self.ending_defending_cavalrymen = None

        self.resources_to_plunder = None
        self.plundered_resources = None
        self.defending_village_health_before = None
        self.damage_dealt = None

        self.turn = -1

    def is_new(self):
        return self.new

    def get_winner(self):
        return self.winner

    def get_loser(self):
        return self.loser

    def get_attacking_village(self):
        return self.attacking_village

    def get_defending_village(self):
        return self.defending_village

    def get_resources_to_plunder(self):
        return self.resources_to_plunder

    def get_plundered_resources(self):
        return self.plundered_resources

    def get_damage_dealt(self):
        return self.damage_dealt

    def set_new(self, new):
        self.new = new

    def get_turn(self):
        return self.turn

    def set_turn(self, turn):
        self.turn = turn

    def set_ending_troops(self, ending_attacking_warriors, ending_attacking_archers,
                          ending_attacking_catapults, ending_attacking_cavalrymen,
                          ending_defending_warriors, ending_defending_archers,
                          ending_defending_catapults, ending_defending_cavalrymen):
        self.ending_attacking_warriors = ending_attacking_warriors
        self.ending_attacking_archers = ending_attacking_archers
        self.ending_attacking_catapults = ending_attacking_catapults
        self.ending_attacking_cavalrymen = ending_attacking_cavalrymen
        self.ending_defending_warriors = ending_defending_warriors
        self.ending_defending_archers = ending_defending_archers
        self.ending_defending_catapults = ending_defending_catapults
        self.ending_defending_cavalrymen = ending_defending_cavalrymen

    def set_resources_to_plunder(self, resources_to_plunder):
        self.resources_to_plunder = resources_to_plunder

    def set_plundered_resources(self, plundered_resources):
        self.plundered_resources = plundered_resources

    def set_damage_dealt(self, damage_dealt):
        self.damage_dealt = damage_dealt

    def set_defending_village_health_before(self, hp):
        self.defending_village_health_before = hp

    def truncate_losing_report(self):
        self.defending_power = None
        self.starting_defending_warriors = None
        self.starting_defending_archers = None
        self.starting_defending_catapults = None
        self.starting_defending_cavalrymen = None
        self.ending_defending_warriors = None
        self.ending_defending_archers = None
        self.ending_defending_catapults = None
        self.ending_defending_cavalrymen = None

    def get_attacking_casualties(self):
        return {"warriors": self.starting_attacking_warriors - self.ending_attacking_warriors,
                "archers": self.starting_attacking_archers - self.ending_attacking_archers,
                "catapults": self.starting_attacking_catapults - self.ending_attacking_catapults,
                "cavalrymen": self.starting_attacking_cavalrymen - self.ending_attacking_cavalrymen}

    def get_defending_casualties(self):
        if self.defending_power is None:
            raise Exception("Should not get here! Check get_defending_casualties() code")
        else:
            return {"warriors": self.starting_defending_warriors - self.ending_defending_warriors,
                    "archers": self.starting_defending_archers - self.ending_defending_archers,
                    "catapults": self.starting_defending_catapults - self.ending_defending_catapults,
                    "cavalrymen": self.starting_defending_cavalrymen - self.ending_defending_cavalrymen}

    def __repr__(self):
        string = "\n\n~~~~~~~~~~ NEW REPORT ~~~~~~~~~~\n"
        string += f"(on turn {self.turn})\n"
        string += f"Attacking village: {self.attacking_village} "
        string += f"({'winner' if self.attacking_village == self.winner else 'loser'})\n"
        string += f"Defending village: {self.defending_village} "
        string += f"({'winner' if self.defending_village == self.winner else 'loser'})\n"
        string += f"Attacking luck: {round(self.attacking_luck, 1)}%\n"
        string += f"Defending luck: {round(self.defending_luck, 1)}%\n"
        string += f"Casualty luck: {round(self.casualty_luck, 1)}%\n"
        string += f"Attacking army at the start (total power: {round(self.attacking_power, 1)}): "
        string += f"{self.starting_attacking_warriors} warriors, "
        string += f"{self.starting_attacking_archers} archers, "
        string += f"{self.starting_attacking_catapults} catapults, "
        string += f"{self.starting_attacking_cavalrymen} cavalrymen\n"
        if self.defending_power is None:
            string += f"Defending army at the start: [no info gathered]\n"
        else:
            string += f"Defending army at the start (total power: {round(self.defending_power, 1)}): "
            string += f"{self.starting_defending_warriors} warriors, "
            string += f"{self.starting_defending_archers} archers, "
            string += f"{self.starting_defending_catapults} catapults, "
            string += f"{self.starting_defending_cavalrymen} cavalrymen\n"
        string += f"Attacking army in the end: "
        string += f"{self.ending_attacking_warriors} warriors, "
        string += f"{self.ending_attacking_archers} archers, "
        string += f"{self.ending_attacking_catapults} catapults, "
        string += f"{self.ending_attacking_cavalrymen} cavalrymen\n"
        if self.defending_power is None:
            string += f"Defending army in the end: [no info gathered]\n"
        else:
            string += f"Defending army in the end: "
            string += f"{self.ending_defending_warriors} warriors, "
            string += f"{self.ending_defending_archers} archers, "
            string += f"{self.ending_defending_catapults} catapults, "
            string += f"{self.ending_defending_cavalrymen} cavalrymen\n"
        string += f"Plundered resources: {self.plundered_resources}\n"
        string += f"Initial health of defending village: {self.defending_village_health_before}\n"
        string += f"Damage dealt: {self.damage_dealt}\n"
        string += f"Current health of defending village: "
        string += f"{self.defending_village_health_before - self.damage_dealt}\n\n"
        return string
