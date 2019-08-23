""" Pattern and template based chatbot dialog engines """
import re


from .template_generators import generate_sentence  # noqa


class Bot:
    def reply(self, statement):
        """ Chatbot "main" function to respond to a user command or statement

        >>> respond('Hi')
        Hi!
        """
        responses = []
        match = re.match(r'\b(hi|hello|hey)\b(.*)', statement.lower())
        if match:
            responses.append((0.1, "Hello"))
            if 'mycroft' in match.groups()[1].lower():
                responses.append((0.2, "Hi!"))
                responses.append((0.2, "Hi! What would you like to talk about?"))
                responses.append((0.2, "Hi! You remembered me! How are you doing?"))
            if 'bot' in match.groups()[1].lower():
                responses.append((0.2, "Hey. That's a good one."))
        return responses
