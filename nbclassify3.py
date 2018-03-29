import sys;
import json;
import string;

def readTestFile(fileName):
    testFile=open(fileName,encoding="utf8");
    return testFile;
def loadProbsFromFile():
    f=open("nbmodel.txt",encoding="utf8");
    lines=f.readlines();
    return json.loads(lines[0]), json.loads(lines[1]),json.loads(lines[2]);

def removePunctuation(line):
    translator = str.maketrans('', '', string.punctuation);
    return line.translate(translator);

def getArgmax(classWordMap,words):
    maxProb = float("-inf");
    argmaxProb = "";
    for classs in classWordMap:
        probOfClass = priorClassProps[classs];
        for word in words:
            word = word.lower();
            probOfClass *= classWordMap[classs].get(word, 1);  # 1 for unknown
        if (maxProb < probOfClass):
            maxProb = probOfClass;
            argmaxProb = classs;
    print(maxProb);
    return argmaxProb;

def labelData(inputFileObj):
    outputFileObj = open('nboutput.txt', 'w', encoding="utf8");
    for line in inputFileObj:
        line = removePunctuation(line);
        doc = line.rstrip().split(" ");
        output=doc[0];
        words = doc[1:];

        derivedClass1=getArgmax(classWordMap1,words);
        derivedClass2 =getArgmax(classWordMap2,words);
        output+=" "+derivedClass1 + " "+derivedClass2;
        print(output,file=outputFileObj);

priorClassProps,classWordMap1,classWordMap2=loadProbsFromFile();
inputFileObj=readTestFile(sys.argv[1]);
labelData(inputFileObj);
inputFileObj.close();