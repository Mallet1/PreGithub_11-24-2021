import re, pyperclip

def wordReplace():
    print('What word would you like to replace')
    word=input()
    print('What would you like to replace it with')
    replace=input()

    replaceRegex = re.compile(word+r'+') # checks for the word
    paragraph = pyperclip.paste() # pastes the message you want to check
    extractedWords=replaceRegex.findall(paragraph) # finds every 'word'
    print(replaceRegex.sub(replace,paragraph))
    pyperclip.copy(replaceRegex.sub(replace,paragraph)) # Copies to clipboard
    print('New paragraph copied to clipboard!')

def delExtraSpaces():
    paragraph=pyperclip.paste()
    spacesRegex=re.compile(r' {2,}') # checks for a double or triple space
    print(spacesRegex.sub(' ',paragraph))
    pyperclip.copy(spacesRegex.sub(' ',paragraph))
    print('New paragraph copied to clipboard!')

def capAfterPeriod():
    paragraph=pyperclip.paste()
    punc_filter = re.compile('([.!?;]\s*)')
    split_with_punctuation = punc_filter.split(paragraph)
    for i,j in enumerate(split_with_punctuation):
        if len(j) > 1:
            split_with_punctuation[i] = j[0].upper() + j[1:]
    newText=''.join(split_with_punctuation)
    print(newText)
    pyperclip.copy(newText)
    print('New paragraph copied to clipboard!')


def dateCleanUp():
    text=pyperclip.paste()
    dateRegex=re.compile(r'''
    \d{1,2}
    [/-]
    \d{1,2}
    [/-]
    \d{2,4}
    ''',re.VERBOSE)
    print(dateRegex.findall(text))


dateCleanUp()
