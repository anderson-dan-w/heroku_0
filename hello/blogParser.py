import os

LINE_BREAK = "<br />"

## keywords in blogs that should be stripped and handled differently
KEYWORDS = [
    "title",
    "subtitle",
    "tags",
    "published",
    "lastEdit"
]

## apply arbitrary functions to the value (line) stored by addKeyword()
POST_PROCESS_KEYWORDS = {
    "tags" : lambda x: x.split()
}

def addKeyword(keyword, line, blogDict):
    remove = "#" + keyword + " "
    if line.startswith(remove):
        blogDict[keyword] = line.replace(remove, "")
        return True
    return False

def processKeywords(lines):
    blogDict = {}
    toRemove = {l for l in lines if l.startswith("#")}
    for line in toRemove:
        any(addKeyword(k, line, blogDict) for k in KEYWORDS)
        lines.remove(line)
    for k, fn in POST_PROCESS_KEYWORDS.items():
        if k in blogDict:
            blogDict[k] = fn(blogDict[k])
    return blogDict

def addLineBreaks(lines, blogDict):
    lines = (l if l else LINE_BREAK*2 for l in lines)
    blogDict["text"] = "\n".join(lines)

def parseBlog(fname):
    if not os.path.exists(fname):
        return {}
    with open(fname) as fh:
        lines = fh.read().split("\n")
    d = processKeywords(lines)
    addLineBreaks(lines, d)
    return d

