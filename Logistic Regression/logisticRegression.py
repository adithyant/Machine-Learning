
import numpy as np
import math
import loadDataset as ld
import accuracy as acc

class logistic(object):
        def  __init__(self):
            return None
            
        def loadData(self,filename,targetCol,header,train):
            
            self.datasetObj=ld.DataSet()
            if train == True:            
                self.X,self.y_actual,self.class_labels=ld.DataSet.loadTrainData(self.datasetObj,filename,targetCol,header)
            else:
                self.testX,self.test_y_actual,bv=ld.DataSet.loadTrainData(self.datasetObj,filename,targetCol,header)
                  
        
        
        def train(self,iteration,alpha,proba):
            
            
            self.W=np.zeros((self.X.shape[1]+1,len(self.class_labels)),dtype=float)
            self.iter=iteration
            self.alpha=alpha
            for ittr in range(self.iter):
                for j in range(len(self.X)):
                    self.update(self.X[j,:],self.y_actual[j])
            
            return self.predict(self.X,proba)
            
        def testPredict(self,proba):
            self.test_predicted_labels=self.predict(self.testX,proba)
            return self.test_predicted_labels
        
        def trainPredict(self,proba):
            self.train_predicted_labels=self.predict(self.X,proba)
            return self.train_predicted_labels
        
        def predict(self,X,proba):
            test=np.zeros(shape=(len(X),len(self.class_labels)))
            for lenw in range(len(self.class_labels)):
                
                for lenx in range(len(X)):
                    test[lenx][lenw]=self.sigmoid(X[lenx,:],self.W[:,lenw])
            if proba==True:
                return test
            else:
                
                return [self.class_labels[i] for i in np.argmax(test,axis=1)]
            
        
        def update(self,X,y_actual):
            for leny in range(len(y_actual)):
                self.temp_error=(y_actual[leny]-self.sigmoid(X,self.W[:,leny]))            
                self.W[0][leny]=self.W[0][leny]+(self.temp_error*1)
                
                for z in range(1,len(self.W)):            
                    self.W[z][leny]=self.W[z][leny]+(self.alpha*self.temp_error*float(X[z-1]))
                
        def sigmoid(self,X,W):
            z=W[0]*1
            
            for sg in range(1,len(W)):
                z=z+(W[sg]*float(X[sg-1]))
            return 1/(1+math.exp(-z))
        
        def performance(self,Train,metric):
            
            self.metricsObj=acc.Metric()
            if str.lower(metric) == 'accuracy':
            
                if Train == False:
                    return acc.Metric.accuracy(self.metricsObj,self.test_y_actual,self.test_predicted_labels,self.class_labels)
                else:
                    return acc.Metric.accuracy(self.metricsObj,self.y_actual,self.train_predicted_labels,self.class_labels)
            if str.lower(metric) == 'classaccuracy':
            
                if Train == False:
                    return acc.Metric.classAccuracy(self.metricsObj,self.test_y_actual,self.test_predicted_labels,self.class_labels,self.datasetObj)
                else:
                    return acc.Metric.classAccuracy(self.metricsObj,self.y_actual,self.train_predicted_labels,self.class_labels,self.datasetObj)
            
            

             
        



            