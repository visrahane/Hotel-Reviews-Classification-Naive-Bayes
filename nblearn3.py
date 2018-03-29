import sys;
import math;
import json;
import string;
from collections import defaultdict;

classCountMap=defaultdict(int);
priorClassProps=defaultdict(float);
vocabMap=defaultdict(int);
classWordMap1=defaultdict(lambda: defaultdict(int));
classWordMap2=defaultdict(lambda: defaultdict(int));


def readFile(fileName):
    inputFileObj=open(fileName,encoding="utf8");
    return inputFileObj;

def saveToFile():
    f = open("nbmodel.txt", "w");
    f.write(json.dumps(priorClassProps));
    f.write("\n");
    f.write(json.dumps(classWordMap1));
    f.write("\n");
    f.write(json.dumps(classWordMap2));
    f.close()

def removePunctuation(line):
    translator = str.maketrans('', '', string.punctuation);
    return line.translate(translator);


def constructTokens(inputFileObj):
    for line in inputFileObj:
        line=removePunctuation(line);
        doc=line.rstrip().split(" ");
        classCountMap[doc[1]]+=1;
        classCountMap[doc[2]] += 1;
        words=doc[3:];
        for word in words:
            word=word.lower();
            if(word in stopList):
                continue;
            vocabMap[word]+=1;
            classWordMap1[doc[1]][word]+=1;
            classWordMap2[doc[2]][word] += 1;

def calculateWordProbs(classWordMap):
    vocab = len(vocabMap);
    for classs,wordCntMap in classWordMap.items():
        wordsinClass=sum(classWordMap[classs].values());
        for word in vocabMap:
            classWordMap[classs][word]= math.log((classWordMap[classs][word] + 1) / (vocab + wordsinClass));

def calculateProbs():
    noOfDocs=sum(classCountMap.values())/2;

    for key in classCountMap:
        priorClassProps[key]=math.log(classCountMap[key]/noOfDocs);

    calculateWordProbs(classWordMap1);
    calculateWordProbs(classWordMap2);

    # for classs,wordCntMap in classWordMap1.items():
    #     wordsinClass=sum(classWordMap1[classs].values());
    #     for word in vocabMap:
    #         classWordMap1[classs][word]=(classWordMap1[classs][word]+1)/(vocab+wordsinClass);
    #
    # for classs,wordCntMap in classWordMap2.items():
    #     wordsinClass=sum(classWordMap2[classs].values());
    #     for word in vocabMap:
    #         classWordMap2[classs][word]=(classWordMap2[classs][word]+1)/(vocab+wordsinClass);

inputFileObj=readFile(sys.argv[1]);
stopList=[line.rstrip() for line in open("input/stop-words.txt",encoding="utf8")];
constructTokens(inputFileObj);
calculateProbs();
saveToFile();
#print("classCountMap:",classCountMap);
#print("priorClassProps:",priorClassProps);
#print("vocab:",vocabMap);
#print("classWordMap:",classWordMap1);
#print("classWordMap:",classWordMap2);