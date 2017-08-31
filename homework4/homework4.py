import re


def max_relative_frequency(content):
    content = re.sub('[^A-Za-z]+', '', content.lower())
    if len(content) == 0:
        return 0
    count = dict()
    for chearcter in content:
        if chearcter in count:
            count[chearcter] = count[chearcter] + 1
        else:
            count[chearcter] = 1

    return count[(max(count, key=count.get)[0])] / len(content)
