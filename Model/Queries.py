index = []

# adds a keyword and a URL to the index
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for url_item in entry[1]:
                if url_item[0] == url:
                    return
            entry[1].append([url, 0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url, 0]]])

# adds words from a page to index	
def add_page_to_index(index,url,content):
    list_of_words = content.split()
    for word in list_of_words:
        index.append([word, [url]])

# splits a string of chars using a split-list as a separator
def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        elif atsplit:
            output.append(char)
            atsplit = False
        else:
            output[-1] = output[-1] + char   
    return output 
            