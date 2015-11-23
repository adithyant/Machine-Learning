import numpy as np
import math
import pandas as pd

def find_factors(x):
 
	dictionary = {}
	for i in range(0,x.shape[1]):
		temp = []
		temp.append(x[0,i])

		for j in range (1,len(x)):
			if x[j,i] not in temp:
				temp.append(x[j,i])

		#temp = temp.sort()
		dictionary[i] = temp 		
	return dictionary

def find_factors1d(x):
      
      
    temp = []
    temp.append(x[0])

    for j in range (1,len(x)):
        if x[j] not in temp:
            temp.append(x[j])

				
    return temp
	
	#print (dictionary)

def entropy(x,d):
	ent=0

	for i in range (0,len(d)):
		#p_i=-1
		#ent=0
		p_i=float(list(x).count(d[i]))/len(x)
		#print p_i
		if p_i > 0:
			ent=ent+(-p_i * math.log(p_i,2))

	return ent


def information_gain(col,y,d_y,d_a):
	entropy_s=entropy(y,d_y)
	#print entropy_s
	entropy_sv=0
	for i in range(len(d_a)):
		
		temp = [j for j, x in enumerate(col) if x == d_a[i]]
	 	temp2=[y[z] for z in temp]
	 	if len(temp2) > 0 :
	 		entropy_sv=entropy_sv+((entropy(temp2,d_y)*len(temp))/float(len(y)))
	 	#print ((entropy(temp2,d_y)*len(temp))/float(len(y)))
	return (entropy_s-entropy_sv)
	#return 0

def max_gain(x,y,d,notvisited):
	max_infogain=0;
	#ret_gain=-1
	#print x.shape
	for i in range(x.shape[1]):
		#if i not in visited:
			#print i
			#print x[:,i]
			if len(x[:,i])>0:
				temp=information_gain(x[:,i],y,d[x.shape[1]],d[i])
			#print temp
				if  temp >= max_infogain:
					max_infogain = temp
					ret_gain=i
	return ret_gain;



def decision_tree(x,y,d,depth,notvisited):

        defa = max_values(y)
        if len(notvisited) <= 0:
            return defa
        if len(x) <= 0:
            return defa
        
        elif np.all(y[1:] == y[:-1]):
        	 return y[0]
        else:
        			
            node = max_gain(x,y,d,notvisited)
            dtree = {node:{}}
            for i in range(len(d[node])):
                temp = [j for j, z in enumerate(x[:,node]) if z == d[node][i]]
                dtreesub=decision_tree(x[temp,:],y[temp],d,depth+1,notvisited)

                dtree[node][d[node][i]]=dtreesub    
                    
            
        return dtree

def max_values(y1):
    counts = np.bincount(y1)
    return np.argmax(counts)

def predict(tree,tst):
    predictions=[]
    for i in range(tst.shape[0]):
        tempans=pr(tree,tst[i,:])
        predictions.append(tempans)
    return predictions
        
        
def pr(tr,itst):
    if bool(tr) and hasattr(tr, '__iter__'):
            for key in tr:
                root=key
            
            ans=pr(tr[root][itst[root]],itst)
            return ans
    else:
            return tr
            
def buildDecisionTree(x,depth,tcol):
    y = x[:,tcol]
    temp_d=find_factors(x)
    x = np.delete(x,tcol,1)
    return decision_tree(x,y,temp_d,depth,[i for i in range(0,x.shape[1])])

def getConsfusionMatrix(y_a,y_p):
    class_dict=find_factors1d(y_a)
    confusion_matrix=pd.DataFrame(np.zeros((len(class_dict),len(class_dict)),dtype=int),columns=class_dict,index=class_dict)
    for i in range(len(class_dict)):
                temp = [j for j, z in enumerate(y_a) if z == class_dict[i]]  
                for j in temp:
                    if class_dict[i]==y_p[j]:
                        confusion_matrix[class_dict[i]][class_dict[i]]=confusion_matrix[class_dict[i]][class_dict[i]]+1
                    else:
                        confusion_matrix[y_p[j]][class_dict[i]]=confusion_matrix[y_p[j]][class_dict[i]]+1
    return confusion_matrix
    
    


x = np.loadtxt('C:\\Users\\adi\\Downloads\\zoo-train.csv',delimiter=',',dtype=int)
x1 = np.loadtxt('C:\\Users\\adi\\Downloads\\zoo-train.csv',delimiter=',',dtype=int)

dtree=buildDecisionTree(x,depth=0,tcol=16)
an=predict(dtree,x)
print an
print getConsfusionMatrix(x[:,16],an)