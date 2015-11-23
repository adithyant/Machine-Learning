
import numpy as np
import loadDataset as ld

class Metric(object):
    def accuracy(self,actual,predicted,labels):
        count=0
        for i in range(len(actual)):
            
            if labels[np.argmax(list(actual[i]))]==predicted[i]:
               count=count+1
        return float(count)/len(actual)
        
    
    def classAccuracy(self,actual,predicted,labels,dsObj):
        classCount=np.zeros(len(labels))        
        
        self.predictedOneHot=ld.DataSet.oneHot(dsObj,map(int,predicted))        
        for i in range(len(labels)):
            print 'CLASS  ' + str(labels[i]) + ' :'
            for j in range(len(actual)):
                if actual[labels[i]][j] == self.predictedOneHot[labels[i]][j]:
                    classCount[i]=classCount[i]+1
            print str((classCount[i]/float(len(actual)))*100) + '%'
            