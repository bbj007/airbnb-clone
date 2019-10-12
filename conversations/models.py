from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):
    """ Conversation Models Defition """

    participants = models.ManyToManyField("users.User",related_name="conversation",blank=True)

    def __str__(self):
        return str(self.created)
    
    def count_messages(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"        

class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User",related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation",related_name="messages", on_delete=models.CASCADE)

    def __Str__(self):
        return f"{self.user} says : {self.message}"

