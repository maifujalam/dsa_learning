1. Dot (.) matches any character
2. Backslash (\) is used to escape special characters
3. Caret (^) matches the start of a string
4. Dollar sign ($) matches the end of a string.
5. Asterisk (*) matches zero or more occurrences of the preceding character.Example:- 0,1,2,3
6. Plus sign (+) matches one or more occurrences of the preceding character.Example:- 1,2,3
7. Question mark (?) matches zero or one occurrence of the preceding character. Example:- 0,1
8. Square brackets ([]) match any one of the characters inside the brackets.Example:- [abc] matches a, b, or c
9. Hyphen (-) inside square brackets indicates a range of characters.Example:- [a-z] matches any lowercase letter
10. Parentheses (()) are used for grouping and capturing.
11. Pipe (|) is used for alternation (OR)
12. Curly braces ({}) are used to specify a specific number of occurrences
13. \d matches any **digit** (0-9).Example of digit character:- 0,1,2,3,4,5,6,7,8,9.Regex: [0-9]
14. \D matches any **non-digit** character.Regex of it: [^0-9]
15. \w matches any **word character** (alphanumeric + underscore).Its regex is [a-zA-Z0-9_]. Here \w matches any character that is a letter, digit, or underscore.
16. \W matches any **non-word character**.Its regex is [^a-zA-Z0-9_]. Here \W matches any character that is not a letter, digit, or underscore.
17. \s matches any **whitespace character** (space, tab, newline).[ \r\n\t\f ].Here \r is carriage return, \n is newline, \t is tab, and \f is form feed.
18. \S matches any **non-whitespace character**.Example of non whitespace character:- a,b,1,2,3,!,@,#,$,%,^,&,*,(,),_,+,=,{,[,],},|,:,;,",',<,>,?,/,\,.,~,`,-
19. \b is zero-width—it doesn't consume any characters.It only checks if the current position is between a word character
    (\w: letters, numbers, underscores) and a non-word character (\W: spaces, punctuation, symbols, or the start/end of the string).
20. More 