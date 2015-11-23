Usage:

obj=logistic()
obj.loadData('path to train.csv',16,False,True)
obj.loadData('path to test.csv',16,False,False)

aa=obj.train(40,0.3,False)  
pp=obj.testPredict(False)
pp1=obj.trainPredict(False)
acc1=obj.performance(False,'classAccuracy')
acc2=obj.performance(False,'Accuracy')
