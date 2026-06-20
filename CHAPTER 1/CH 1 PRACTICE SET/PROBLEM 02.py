# Install an external module and use it to perform an operation of your interest?import pyttsx3
import pyttsx3
engine = pyttsx3.init()

engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')
engine.runAndWait()

# In this code use module Module is a file containing code written by somebody else. We can use that code by importing the module. Here we have used pyttsx3 module to convert text to speech. We have initialized the engine and then used the say() method to pass the text we want to convert to speech. Finally, we called runAndWait() method to execute the speech.   