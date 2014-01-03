import Numeric
from EnzymeKinetics import *

##a=LookFor('galactose')
##b=[]
##for k in a: b.append(EquationParser(k))
##d=b
##c=CollectCompounds(d)
##InitialCondition=Numeric.ones(106,Numeric.Float)
##InitialCondition[4]=3
##InitialCondition[16]=4
##InitialCondition[14]=3
##InitialCondition[7]=10
##InitialCondition[8]=10
##InitialCondition[46]=4
##InitialCondition[49]=3
##InitialCondition[105]=4

##K=Numeric.zeros((len(d),2),Numeric.Float)
##for k in range(len(d)):
##    for j in range(2):
##        K[k,j]=-random.random()*0.125
        
##y=SolveNetwork(d,InitialCondition,K,0,1,100)
##print K

a=['2.7.1.2','5.3.1.9','2.7.1.11','4.1.2.13','1.2.1.12','2.7.2.3','5.4.2.1','4.2.1.11','2.7.1.40','5.3.1.1']
b=[]
for k in a: b.append(EquationParser(k))
c=CollectCompounds(b)
InitialCondition=Numeric.array((4,0.03,0.12,5,0.14,1.85,0.031,0.014,5,0.083,0.019,0,5,0,0.14,1,0.023,0.051),Numeric.Float)
##InitialCondition=Numeric.array((4,0.01,0.01,0.01,0.01,4,0.01,0.01,4,0.01,0.01,0.01,4,0.01,0.01,4,0.01,0.01),Numeric.Float)
K=Numeric.zeros((10,2),Numeric.Float)
##for k in range(10):
##    for j in range(2):
##        K[k,j]=random.random()
##K[6,0]=-K[6,0]
##K[6,1]=-K[6,1]
##K[8,0]=-K[8,0]
##K[8,1]=-K[8,1]
##K[5,0]=-K[5,0]
##K[5,1]=-K[5,1]
##K[9,0]=-K[9,0]
##K[9,1]=-K[9,1]
K[0,0]=0.05896235
K[0,1]=0.94289084
K[1,0]=0.46270551
K[1,1]=0.18425005
K[2,0]=0.99509258
K[2,1]=0.77118606
K[3,0]=0.73096511
K[3,1]=0.71323266
K[4,0]=0.30008683
K[4,1]=0.53397941
K[5,0]=-0.53042004
K[5,1]=-0.5017144
K[6,0]=-0.27204919
K[6,1]=-0.59356926
K[7,0]=0.85654551
K[7,1]=0.16472936
K[8,0]=-0.65080809
K[8,1]=-0.28294028
K[9,0]=-0.36994987
K[9,1]=-0.1655352
y=SolveNetwork(b,InitialCondition,K,0,3,300)
