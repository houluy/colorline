# colorline
A module for colorful output in command line

Use  
```
pip install colorline
```
or
```
pipenv install colorline
```

to install it.  

An example:

[A colorful calendar](https://github.com/houluy/calendar).


## Background/Foreground color list

'k' -> black
'r' -> red
'g' -> green
'y' -> yellow
'b' -> blue
'p' -> purple
'c' -> cyan
'w' -> white

## Mode list

'default'    -> Normal
'highlight'  -> The text will be highlighted
'underscore' -> As the title
'blink'      -> Blink the text
'inverse'    -> Inverse the bg color with fg color
'invisible'  -> You can't see

## Methods

    cprint(text, color='w', bcolor='b', mode='default', end='\n')


