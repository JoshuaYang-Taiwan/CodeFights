def htmlEndTagByStartTag(startTag):
    return "</{}>".format(startTag[1:startTag.find(" ")])
