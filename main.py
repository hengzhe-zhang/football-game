import random


class Player:
    def __init__(self, name, position, skill=0):
        self.name = name
        self.position = position
        self.skill = skill if skill else random.randint(60, 90)


class Team:
    def __init__(self, name, goalkeepers, forwards, midfielders, defenders):
        self.name = name
        self.goalkeepers = goalkeepers
        self.forwards = forwards
        self.midfielders = midfielders
        self.defenders = defenders
        self.score = 0

    def getRandomPlayerByPosition(self, position):
        if position == 'goalkeeper':
            return random.choice(self.goalkeepers)
        elif position == 'forward':
            return random.choice(self.forwards)
        elif position == 'midfielder':
            return random.choice(self.midfielders)
        elif position == 'defender':
            return random.choice(self.defenders)
        else:
            return None


def skill_based_chance(player_skill, opponent_skill, base_chance):
    return base_chance + (player_skill - opponent_skill) * 0.1


def battle(team1, team2):
    print(f"\nMatch: {team1.name} vs {team2.name}\n")

    for minute in range(1, 91):
        print(f"Minute {minute}")

        team1_midfielder = team1.getRandomPlayerByPosition('midfielder')
        team2_midfielder = team2.getRandomPlayerByPosition('midfielder')

        team1_defender = team1.getRandomPlayerByPosition('defender')
        team2_defender = team2.getRandomPlayerByPosition('defender')

        team1_shooter = team1.getRandomPlayerByPosition('forward')
        team2_shooter = team2.getRandomPlayerByPosition('forward')

        team1_goalkeeper = team1.getRandomPlayerByPosition('goalkeeper')
        team2_goalkeeper = team2.getRandomPlayerByPosition('goalkeeper')

        # Skill-based pass success chance for midfielders
        pass_success_chance1 = skill_based_chance(team1_midfielder.skill, team2_midfielder.skill, 70)
        pass_success_chance2 = skill_based_chance(team2_midfielder.skill, team1_midfielder.skill, 70)

        # Skill-based tackle success chance for defenders
        tackle_success_chance1 = skill_based_chance(team1_shooter.skill, team2_defender.skill, 60)
        tackle_success_chance2 = skill_based_chance(team2_shooter.skill, team1_defender.skill, 60)

        # Team 1 has a chance to attack if they win the midfield battle
        if random.randint(0, 100) < pass_success_chance1:
            # Team 1 shooter has a chance to shoot if they beat the defender
            if random.randint(0, 100) < tackle_success_chance1:
                # Probability of missing the shot
                shot_success_chance1 = skill_based_chance(team1_shooter.skill, team2_goalkeeper.skill, 20)
                if random.randint(0, 100) < shot_success_chance1:  # 10% chance of missing
                    team1.score += 1
                    print(f"{team1_shooter.name} from {team1.name} scores! Score: {team1.score}-{team2.score}")
                else:
                    print(f"{team1_shooter.name} from {team1.name} misses the shot!")
        else:
            print(f"Passing error by midfielders {team1_midfielder.name}!")

        # Team 2 has a chance to attack if they win the midfield battle
        if random.randint(0, 100) < pass_success_chance2:
            # Team 2 shooter has a chance to shoot if they beat the defender
            if random.randint(0, 100) < tackle_success_chance2:
                print(f"{team2_defender.name} from {team2.name} successfully tackles {team1_shooter.name}!")

                # Probability of missing the shot
                shot_success_chance2 = skill_based_chance(team2_shooter.skill, team1_goalkeeper.skill, 20)
                if random.randint(0, 100) < shot_success_chance2:  # 10% chance of missing
                    team2.score += 1
                    print(f"{team2_shooter.name} from {team2.name} scores! Score: {team1.score}-{team2.score}")
                else:
                    print(f"{team2_shooter.name} from {team2.name} misses the shot!")
        else:
            print(f"Passing error by midfielders {team2_midfielder.name}!")

    print("\nFinal whistle!\n")
    if team1.score > team2.score:
        print(f"{team1.name} wins with a score of {team1.score}-{team2.score}")
    elif team1.score < team2.score:
        print(f"{team2.name} wins with a score of {team1.score}-{team2.score}")
    else:
        print(f"The match ends in a {team1.score}-{team2.score} draw")


if __name__ == "__main__":
    # Create players for Team A (Includes Messi)
    team1_goalkeepers = [Player("Ter Stegen", 'goalkeeper')]
    team1_forwards = [Player("Messi", 'forward'), Player("Griezmann", 'forward'), Player("Suarez", 'forward')]
    team1_midfielders = [Player("Busquets", 'midfielder'), Player("de Jong", 'midfielder'),
                         Player("Pedri", 'midfielder'), Player("Alba", 'midfielder')]
    team1_defenders = [Player("Pique", 'defender'), Player("Lenglet", 'defender'), Player("Roberto", 'defender')]

    # Manually setting Messi's skill to 99
    team1_forwards[0].skill = 99

    # Create players for Team B (Includes Ronaldo)
    team2_goalkeepers = [Player("Buffon", 'goalkeeper')]
    team2_forwards = [Player("Ronaldo", 'forward'), Player("Dybala", 'forward'), Player("Morata", 'forward')]
    team2_midfielders = [Player("Rabiot", 'midfielder'), Player("Bentancur", 'midfielder'),
                         Player("Arthur", 'midfielder'), Player("Cuadrado", 'midfielder')]
    team2_defenders = [Player("Bonucci", 'defender'), Player("Chiellini", 'defender'), Player("Sandro", 'defender')]

    # Manually setting Ronaldo's skill to 99
    team2_forwards[0].skill = 99

    # Create teams
    team1 = Team("Barcelona", team1_goalkeepers, team1_forwards, team1_midfielders, team1_defenders)
    team2 = Team("Juventus", team2_goalkeepers, team2_forwards, team2_midfielders, team2_defenders)

    # Simulate match
    battle(team1, team2)
