import Numeric

def function(x,k):
  y=Numeric.zeros(18,Numeric.Float)
  y[0]=0+(-k[6,0]*x[1]*x[0]+k[6,1]*x[2]*x[0])*Numeric.sign(x[1]*x[0])-(-k[6,0]*x[1]*x[0]+k[6,1]*x[2]*x[0])*Numeric.sign(x[1]*x[0])
  y[1]=0+(-k[6,0]*x[1]*x[0]+k[6,1]*x[2]*x[0])*Numeric.sign(x[1]*x[0])+(-k[7,0]*x[1]+k[7,1]*x[16]*x[11])*Numeric.sign(x[1])
  y[2]=0+(-k[5,0]*x[5]*x[2]+k[5,1]*x[4]*x[3])*Numeric.sign(x[5]*x[2])-(-k[6,0]*x[1]*x[0]+k[6,1]*x[2]*x[0])*Numeric.sign(x[1]*x[0])
  y[3]=0-(-k[4,0]*x[10]*x[15]*x[12]+k[4,1]*x[3]*x[13])*Numeric.sign(x[10]*x[15]*x[12])-(-k[5,0]*x[5]*x[2]+k[5,1]*x[4]*x[3])*Numeric.sign(x[5]*x[2])
  y[4]=0-(-k[0,0]*x[5]*x[8]+k[0,1]*x[4]*x[9])*Numeric.sign(x[5]*x[8])-(-k[2,0]*x[5]*x[7]+k[2,1]*x[4]*x[6])*Numeric.sign(x[5]*x[7])-(-k[5,0]*x[5]*x[2]+k[5,1]*x[4]*x[3])*Numeric.sign(x[5]*x[2])-(-k[8,0]*x[5]*x[17]+k[8,1]*x[4]*x[16])*Numeric.sign(x[5]*x[17])
  y[5]=0+(-k[0,0]*x[5]*x[8]+k[0,1]*x[4]*x[9])*Numeric.sign(x[5]*x[8])+(-k[2,0]*x[5]*x[7]+k[2,1]*x[4]*x[6])*Numeric.sign(x[5]*x[7])+(-k[5,0]*x[5]*x[2]+k[5,1]*x[4]*x[3])*Numeric.sign(x[5]*x[2])+(-k[8,0]*x[5]*x[17]+k[8,1]*x[4]*x[16])*Numeric.sign(x[5]*x[17])
  y[6]=0-(-k[2,0]*x[5]*x[7]+k[2,1]*x[4]*x[6])*Numeric.sign(x[5]*x[7])
  y[7]=0+(-k[2,0]*x[5]*x[7]+k[2,1]*x[4]*x[6])*Numeric.sign(x[5]*x[7])
  y[8]=0+(-k[0,0]*x[5]*x[8]+k[0,1]*x[4]*x[9])*Numeric.sign(x[5]*x[8])
  y[9]=0-(-k[0,0]*x[5]*x[8]+k[0,1]*x[4]*x[9])*Numeric.sign(x[5]*x[8])
  y[10]=0-(-k[3,0]*x[6]+k[3,1]*x[14]*x[10])*Numeric.sign(x[6])+(-k[4,0]*x[10]*x[15]*x[12]+k[4,1]*x[3]*x[13])*Numeric.sign(x[10]*x[15]*x[12])
  y[11]=0-(-k[7,0]*x[1]+k[7,1]*x[16]*x[11])*Numeric.sign(x[1])
  y[12]=0+(-k[4,0]*x[10]*x[15]*x[12]+k[4,1]*x[3]*x[13])*Numeric.sign(x[10]*x[15]*x[12])
  y[13]=0-(-k[4,0]*x[10]*x[15]*x[12]+k[4,1]*x[3]*x[13])*Numeric.sign(x[10]*x[15]*x[12])
  y[14]=0-(-k[3,0]*x[6]+k[3,1]*x[14]*x[10])*Numeric.sign(x[6])
  y[15]=0+(-k[4,0]*x[10]*x[15]*x[12]+k[4,1]*x[3]*x[13])*Numeric.sign(x[10]*x[15]*x[12])
  y[16]=0-(-k[7,0]*x[1]+k[7,1]*x[16]*x[11])*Numeric.sign(x[1])-(-k[8,0]*x[5]*x[17]+k[8,1]*x[4]*x[16])*Numeric.sign(x[5]*x[17])
  y[17]=0+(-k[8,0]*x[5]*x[17]+k[8,1]*x[4]*x[16])*Numeric.sign(x[5]*x[17])
  return y
