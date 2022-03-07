class User:     # TODO joku meni vituiks 95% toimii

    """current_rank = -8  # User starts at rank -8 and max rank is 8 --> There is no 0 rank
    current_progress = 0   # Rank progress between 0-100"""

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, completed_activity_level: int):
        progress_gained = 0

        if completed_activity_level < -8 or completed_activity_level == 0 or completed_activity_level > 8:
            raise Exception
        if self.rank == 8:  # If user is max rank, he will not gain more experience
            return

        rank_difference = abs(self.rank - completed_activity_level)     # Calculating the rank difference between the task

        if self.rank < 0 and completed_activity_level > 0:
            rank_difference -= 1

        if rank_difference >= 2 and self.rank > completed_activity_level:
            return
        elif rank_difference >= 1 and self.rank > completed_activity_level:
            self.progress += 1
        elif completed_activity_level == self.rank:
            self.progress += 3
        else:
            progress_gained = 10 * rank_difference * rank_difference    # Progress gained according to the formula

        self.progress += progress_gained    # Updating current progress

        # Checking if progress goes over 100 to reach next rank
        while self.progress >= 100:
            if self.rank == 8:
                self.progress = 0
                break
            if self.progress >= 100:
                if self.rank == -1:     # Rank cannot be 0, skipping it to next available
                    self.rank = 1
                else:
                    self.rank += 1
                self.progress -= 100


jukka = User()
jukka.inc_progress(-1)
print(jukka.progress)
print(jukka.rank)

