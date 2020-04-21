
import jieba
import nltk

def cutWord(strs):
    text1=jieba.cut(strs)
    fd=nltk.FreqDist(text1)
    keys=fd.keys()
    item=fd.items()
    dicts=dict(item)
    sort_dict=sorted(dicts.items(),key=lambda d:d[1],reverse=True)

    print(sort_dict)

