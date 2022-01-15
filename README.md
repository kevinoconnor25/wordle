Kevin's recreation of Wordle

OVERVIEW
This works basically the same way as the original game but the number of letters in the word and number of guesses are configurable. The number of letters can be passed in as a command line argument or just changed in the script itself. For the number of guesses I went with (number of letters - 2) * 2, since it works with the 5-letter/6-guess method that Wordle uses. After playing around with shorter and longer words I might change this because I think guesses might have an inverse correlation to letters but I'd probably want to factor in word count, idk.

DICTIONARY
I hate messing with pip so I decided to use the build in unix "dictionary" in /usr/share/dict/words. I'm discovering that it's missing some common words, and includes a lot of words that I don't think are actually in the dictionary. I'll likely submit to the power of pip but avoiding that for now. The way this program works is that it takes the main words file and creates individual text files containing all words with a certain length and reads from those instead of parsing through the full words file every runtime. It only creates this file one time and names it N-letter-words.txt (in dicts dir) where N is the number of letters. The regex used to add to the new files is ^[a-z]{N}$ since there are some proper nouns and special characters that I want to exclude.

FUTURE WORK
Hmm a lot. I would first like to smooth out the word selection but this will probably be done at the same time as difficulties. Here are my plans for difficulty levels:
- Easy: A subset of all words containing more common words, and the ability to view any possible words remaining. Maybe additional hints too.
- Normal: Standard (Wordle) gameplay, maybe still a subset of all words though. Maybe still have the option to show a few possible answers?
- Hard: Forces user to use given hints, still maybe a subset. Idea here is same as Wordle's hard mode, so same subset of words.
- Expert: Same as hard mode but all words and perhaps fewer guesses.

- Oh I should fix the case where it sets the letter as yellow when it's duplicated and already in the correct position. Here's a case: say the answer is "income" but the user guesses "become". The first 'e' will be marked as yellow because that letter is in the word, but the second 'e' will be green. Yeah this should be priority.

- Need to do the cool output that people share. Should only be like 30 minutes of work cuz I will need to keep track of previous guess results. I'll need that for hard mode anyway.

- Ability to add (or remove) words from the file. Might be tricky once I implement the difficulties and subsets of words since it'll have to take effect in all dictionaries.

- Bots to play against. I'll almost definitely want a separate library for this to help identify more common words.

- A optional timer. Could be time per guess or overall.

- Ooh a dictionary feature (especially for harder difficulties). That way when you inevitably fail to guess correctly (or get lucky) because you don't know the word you can click the button that says "wtf does that word mean".

- Log of everything so you can see all history (exact guesses and all).

- Sharing feature I guess. Save that for the app which will probably never happen. Literally none of this will cuz I have a job and MLB season isn't far away.
