# About

The program for analyze text

## Apply
To apply, open the Terminal and type the following:
```terminal
 python main_nl.py --file (necessarily) --a(if need) --b(if need) --c(if need) --d(if need)
```
'--file' - for choosing file (.txt only) - is a mandatory function

The following functions can be selected as needed:

'--a' - conducts tokenize, lemmatize and stemming of text

'--b' - delete stop word of text

'--c' - counts all duplicate words in the text

'--d' - displays the specified number of frequent words


For example:
```terminal
 python main_nl.py --file name.txt --d 10 (the right amount) 
```
The result will be displayed in the terminal

