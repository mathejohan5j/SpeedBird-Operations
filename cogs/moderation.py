# moderation.py

class Moderation:
    def ban(self, user_id):
        """Bans a user by user_id."""
        pass

    def kick(self, user_id):
        """Kicks a user by user_id."""
        pass

    def warn(self, user_id, reason):
        """Issues a warning to a user."""
        pass

    def warnings(self, user_id):
        """Retrieves all warnings for a user."""
        pass

    def clearwarnings(self, user_id):
        """Clears all warnings for a user."""
        pass

    def slowmode(self, channel_id, duration):
        """Sets slowmode for a channel."""
        pass

    def automatic_slur_filter(self, message):
        """Filters slurs from a message."""
        pass
