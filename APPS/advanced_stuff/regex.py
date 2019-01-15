'''
\d{3}-\d{3}-\d{4}

    \d  - looking for integers [0-9]
    {3} - giving repetition. How many chars to look for
    -   - string literal. Character '-' in this case

Special chars in RE

.   - matches any char (except newline)
[]  - matches anything in a given set.           Ex: [a-zA-Z] matches any letter ; [a-z] matches any lowercase letter
^   - negation. matches anything NOT in a given set.    Ex:  ^[a1] matches any char EXCEPT 'a' and '1'
*   - matches 0 or more of a given character or set
+   - matches 1 or more of a given character or set
?   - matches 0 or 1 of a given character or set
a|b - matches either 'a' or 'b'


re.compile  - turns the pattern into something that regex engine can understand
re.search   - scans a string for the pattern and returns a MatchObject for the first match
re.match    - only checks the beginning of the string for the pattern
re.findall  - returns every match, rather then only the first
re.finditer - returns an iterator over all matches
re.sub      - replaces the first instance of a match with a given string
'''

import re


data = '1dpsdajsc[ij1=09u=20cjkcoicw[oeihcw[oevihefwpieuwepiu555-555-5555qpwdoqkq[fiojif[ofiqevq-v-qv349ovhu'

compiled_re = re.compile('\d{3}-\d{3}-\d{4}')
matched_obj = re.search(compiled_re, data)

print(matched_obj.group)    # returns every group that is found
print(matched_obj.group(0))
print(matched_obj.re)       # returns the regex used in the search
print(matched_obj.start())  # returns the start index of the matched group
print(matched_obj.end())    # returns the end index of the matched group


def regex_html_data(data):
    html_match   = re.compile("<.*>")
    # html_results = re.search(html_match, data)
    html_results = re.findall(html_match, data)
    print(html_results)
    # print(html_results.group())
    # print(html_results.group(0))
    return


regex_html_data("asdasdasd<HTML CODE>12313cwecwec<HTML CODE 2>1owncowecn")