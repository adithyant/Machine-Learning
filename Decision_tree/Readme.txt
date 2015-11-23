Example:

x = np.loadtxt('Path/to/train file',delimiter=',',dtype=int)
xtest = np.loadtxt('Path/to/test file',delimiter=',',dtype=int)
dtree=buildDecisionTree(x,depth=0,tcol=16)
y_p=predict(dtree,xtest)
print getConsfusionMatrix(xtest[:,16],y_p)