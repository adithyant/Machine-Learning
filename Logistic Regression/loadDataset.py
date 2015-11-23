
import numpy as np

class DataSet(object):
     def loadTrainData(self,filename,targetCol,header):
            if header == True:
                self.X=np.loadtxt(filename,delimiter=',',skiprows=1,dtype=str)
            else:
                self.X=np.loadtxt(filename,delimiter=',',dtype=str)
            
        
            self.y_actual=self.X[:,targetCol]
            self.y_actual=map(int,list(self.y_actual))            
            
            self.class_labels=set()
            for i in range(len(self.y_actual)):
                self.class_labels.add(self.y_actual[i])
            
            self.class_labels=list(self.class_labels)
                        
            self.class_labels=map(int,self.class_labels)
            self.class_labels.sort()
                         
            self.class_labels=map(str,list(self.class_labels))
            self.y_actual=self.oneHot(self.X[:,targetCol])
            
            self.X=np.delete(self.X,targetCol,1)
            
            for i in range(self.X.shape[1]):
                if not str.isdigit(self.X[0,i]):
                    self.X[:,i]=self.preprocessData(self.X[:,i])
                else:
                    self.X[:,i]=map(float,self.X[:,i])
            
            return self.X,self.y_actual,self.class_labels  
    
     def oneHot(self,y):
            self.temp_data_type=[(str(n),'i4') for n in self.class_labels ]
            temp_y=np.zeros(shape=(len(y)),dtype=self.temp_data_type)
            for i in range(len(y)):
                temp_y[str(y[i])][i]=1
            return temp_y
    
     def preprocessData(self,data):
            return data
    