# Fake_TRUMPS
Trump railing against fake news in his first press conference as president. 

CODE OVERVIEW
This is a simple program written as part of an assignment for Allison Parish's class Reading and Writing Electronic Text, 
taught at New York University's Interactive Telecommunications Program (ITP). It is used to focus on instances of a specific 
word referenced in a source text of any size. It is written in Python 2.7.10 and takes source text input by a user via the 
command line. The script converts lines of the source text into a list based on a word (or words) present in that line and 
then prints all of the lines containing the word in a random order.

SOURCE TEXT
I am using a New York Times transcript of Donald Trumps first press conference as my source material. It's a gold mine of one
liners and Trumpisms ("Trumps" as I call them), but I am specifically interested in his obsession with "fake news", 
particularly as a distraction from himself and his team. For this project, I loop over the source text and pull only lines
containing the word "fake", allowing me to isolate these statements from the full 412 line text. 

CONSIDERATIONS
I wanted to clean up the text that campe form the script as much as possible, to focus on what was said, some from Trump
and some form the reporters at the press conference. I stripped out instances of "TRUMP:" and "QUESTION:" from the transcript
and tried to remove other unwanted words such as (inaudible) and (ph). For some reason that I haven't yet figured out,
stripping them didn't work. I'll have to keep playing with that. 


