from pyexpat import model
import jieba
from gensim.models.word2vec import LineSentence
import logging
from gensim.models import Word2Vec
import gensim.models
from gensim.models import KeyedVectors
from sklearn import model_selection

# str2="今天天气很不错"
# str2=str2.replace("不错","糟糕")
# print(str2)
f=open('秦始皇帝陵博物院(兵马俑).txt',mode="r",encoding='utf-8')
strh=f.read()
strh.strip(',')
list=jieba.lcut(strh,cut_all=False)
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# def tarin_function():
#      new_data = open('fenxi.txt', "r",encoding='UTF-8') #r 只读
#      model = Word2Vec(LineSentence(new_data),vector_size=100,window=5,workers=1000)
#      model.save('new_data.word2vec')
# # tarin_function()
# model = gensim.models.Word2Vec.load("new_data.word2vec")
# print(model.wv.similarity("历史",""))

file=r"Data\wordVector_trainSet\tencent-ailab-embedding-zh-d200-v0.2.0-s.txt"
model = KeyedVectors.load_word2vec_format(file, binary=False)
# print(model.word_vec("华山"))
# print(model.most_similar('历史',topn=30))
# print(model.most_similar('美食',topn=30))
# print(model.most_similar('动物',topn=30))
# print(model.most_similar('娱乐',topn=30))
# print(model.most_similar('运动',topn=30))
# print(model.most_similar('景色',topn=30))
listHistory=['历史']
listFood=['美食']
listAnimal=['动物']
listEntertainment=['娱乐']
listSport=['运动']
listScenic=['景色']
similarHistory=model.n_similarity(list,listHistory)
similarFood=model.n_similarity(list,listFood)
similarAnimal=model.n_similarity(list,listAnimal)
similarEntertainment=model.n_similarity(list,listEntertainment)
similarSport=model.n_similarity(list,listSport)
similarScenic=model.n_similarity(list,listScenic)
print("与文化相关度为"+str(similarHistory))
print("与美食相关度为"+str(similarFood))
print("与动物相关度为"+str(similarAnimal))
print("与娱乐相关度为"+str(similarEntertainment))
print("与运动相关度为"+str(similarSport))
print("与景色相关度为"+str(similarScenic))

