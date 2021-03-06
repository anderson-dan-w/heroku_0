import os

BLOG_DIR = os.path.join(os.path.dirname(__file__), "blogs")

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
    "tags": lambda x: x.split()
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


def addLineBreaks(lines, blogDict, nlines=None):
    new_lines = []
    inside_pre_tag = False
    for line in lines:
        if line.startswith("<pre>"):
            inside_pre_tag = True
        elif line.endswith("</pre>"):
            inside_pre_tag = False
        if not inside_pre_tag and not line:
            line = LINE_BREAK * 2
        new_lines.append(line)
    if nlines is not None:
        new_lines = new_lines[:nlines]
    blogDict["text"] = "\n".join(new_lines)


def parseBlog(fname, nlines=None):
    if not os.path.exists(fname):
        return {}
    with open(fname) as fh:
        lines = fh.read().split("\n")
    d = {"blog_id": os.path.splitext(os.path.basename(fname))[0]}
    d.update(processKeywords(lines))
    addLineBreaks(lines, d, nlines)
    return d


def getSnippet(fname):
    return parseBlog(fname, 1)


def getRecentSnippets():
    nrecent = 5
    snippets = []
    for fname in os.listdir(BLOG_DIR):
        if not fname.endswith(".txt"):
            continue
        snippet = getSnippet(os.path.join(BLOG_DIR, fname))
        snippets.append(snippet)
    snippets.sort(key=lambda d: d['published'], reverse=True)
    return snippets[:nrecent]

