def reverseParentheses(s):
    if '(' not in s:
        return s
    else:
        indexLeft = s.rfind('(')
        tmp_s = s[indexLeft:]
        indexRight = tmp_s.find(')')
        new_s = tmp_s[:indexRight+1]
        new_s = new_s[1:]
        new_s = new_s[:-1]
        new_s = new_s[::-1]
        new_change_string = s[:indexLeft] + new_s + s[indexLeft+indexRight+1:]
        return reverseParentheses(new_change_string)

