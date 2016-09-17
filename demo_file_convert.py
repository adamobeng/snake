import snake.python_to_emoji
import snake.emoji_to_python


FILENAME = 'test.py'
EMOJIOUT = "examples/test.emj"


#Converts python into emoji
snake.python_to_emoji.python_to_emoji(FILENAME,EMOJIOUT)

parsed_python = snake.emoji_to_python.emoji_to_python(EMOJIOUT)

print()
print(parsed_python)

