import string,Numeric,random,Gnuplot,time
from Enzyme import Enzyme

def EquationParser(EnzNumber):
    # It takes a chemical reaction in format ENZYME, and offers a tuple:
    #  ec-number ,    substrate   ,  reactants
    # ('0.0.0.0' ,['water',sugar'],['coke','gas'])
    #    If two or more molecules of a compound are present in the
    #    reaction, it outputs something like this:
    # 0.0.0.0: H(2)O + 2 sugar = coke + 3 gas
    # ('0.0.0.0',['H(2)O','sugar','sugar'],['coke','gas','gas','gas'])
    reaction          = Enzyme[EnzNumber]
    substrate,reactant=[],[]
    
    dummy     = reaction[0:reaction.index(' = ')]
    elements  = dummy.count(' + ')+1
    if elements==1: substrate=dummy
    else:
        for k in range(elements-1):
            step=dummy[0:dummy.index(' + ')]
            space=step.find(' ')
            if space==-1:
                substrate.append(step)
            else:
                number=step[0:space]
                if number.isdigit():
                    number=string.atoi(number)
                    step=step[space+1:]
                    for j in range(number):
                        substrate.append(step)
                else: substrate.append(step.replace(' ',''))
                    
            dummy=dummy[dummy.index(' + ')+3:]

        space=dummy.find(' ')
        if space==-1: substrate.append(dummy)
        else:
            number=dummy[0:space]
            if number.isdigit():
                number=string.atoi(number)
                dummy=dummy[space+1:]
                for j in range(number):
                    substrate.append(dummy)
            else: substrate.append(dummy.replace(' ',''))

    dummy     = reaction[reaction.index(' = ')+3:]
    elements  = dummy.count(' + ')+1
    if elements==1: reactant=dummy
    else:
        for k in range(elements-1):
            step=dummy[0:dummy.index(' + ')]
            space=step.find(' ')
            if space==-1:
                reactant.append(step)
            else:
                number=step[0:space]
                if number.isdigit():
                    number=string.atoi(number)
                    step=step[space+1:]
                    for j in range(number):
                        reactant.append(step)
                else: reactant.append(step.replace(' ',''))
                        
            dummy=dummy[dummy.index(' + ')+3:]

        space=dummy.find(' ')
        if space==-1: reactant.append(dummy)
        else:
            number=dummy[0:space]
            if number.isdigit():
                number=string.atoi(number)
                dummy=dummy[space+1:]
                for j in range(number):
                    reactant.append(dummy)
            else: reactant.append(dummy.replace(' ',''))
        
    if type(substrate)!=type([]): substrate=[substrate]
    if type(reactant)!=type([]): reactant=[reactant]
    return EnzNumber,substrate,reactant

def LookFor(name):
    output=[]
    for reaction in Enzyme.items():
        if reaction[1].find(name)>-1: output.append(reaction[0])
    return output

def CollectCompounds(network):
    # A network is simply a list of parsed reactions
    # ('0.0.0.0',['water','sugar'],['coke'])
    cmp=[]
    for reaction in network:
        bulk=reaction[1]+reaction[2]
        for k in range(len(bulk)):
            cmp.append(bulk[k].replace(' ',''))
    cmp.sort()
    k1,k2=0,len(cmp)-1
    while k1<k2:
        if cmp[k1]==cmp[k1+1]:
            del cmp[k1+1]
            k2=k2-1
        else:
            k1=k1+1
    return cmp

def DifferentialEquation(network,compounds):
    dictionary={}
    for k in range(len(compounds)): dictionary[compounds[k]]=k
    
    substrate,reactant='',''
    counter=-1
    eqns=[]
    for reaction in network:
        counter=counter+1
        substrate='(-k['+str(counter)+',0]*x['+str(dictionary[reaction[1][0].replace(' ','')])+']'
        SubstrateIndicator=')*Numeric.sign(x['+str(dictionary[reaction[1][0].replace(' ','')])+']'
        reactant='+k['+str(counter)+',1]*x['+str(dictionary[reaction[2][0].replace(' ','')])+']'
        if len(reaction[1])>1:
            for k in range(len(reaction[1])-1):
                substrate=substrate+'*x['+str(dictionary[reaction[1][k+1].replace(' ','')])+']'
                SubstrateIndicator=SubstrateIndicator+'*x['+str(dictionary[reaction[1][k+1].replace(' ','')])+']'
        if len(reaction[2])>1:
            for k in range(len(reaction[2])-1):
                reactant=reactant+'*x['+str(dictionary[reaction[2][k+1].replace(' ','')])+']'
        eqns.append(substrate+reactant+SubstrateIndicator+')')

    y=[]
    for k in range(len(compounds)):
        ystep='0'
        for j in range(len(network)):
            if (network[j][1]).count(compounds[k])>0: ystep=ystep+'+'+eqns[j]
            if (network[j][2]).count(compounds[k])>0: ystep=ystep+'-'+eqns[j]
        y.append(ystep)

    f=open('diffeq.py','w')
    f.write('import Numeric\n')
    f.write('\n')
    f.write('def function(x,k):\n')
    f.write('  y=Numeric.zeros('+str(len(compounds))+',Numeric.Float)\n')
    for k in range(len(compounds)):
        f.write('  y['+str(k)+']='+y[k]+'\n')
    f.write('  return y\n')
    f.close()
    return y

def SolveNetwork(network,InitialConditions,K,t0,tf,steps):
    h=abs(tf-t0)/float(steps)
    cmp=CollectCompounds(network)
    if len(InitialConditions)!=len(cmp):
        print "# Initial Conditions ("+str(len(InitialConditions))+") doesn't match # components ("+str(len(cmp))+")"
        y=InitialConditions
    else:
        starting1=time.time()
        top=0
        for k in InitialConditions:
            top=top+k
        DifferentialEquation(network,cmp)
        print "Computed differential system in",time.time()-starting1,"seconds."
        starting2=time.time()
        from diffeq import function
        y=Numeric.zeros((len(cmp),steps),Numeric.Float)
        for k in range(len(cmp)): y[k,0]=InitialConditions[k]
        ##print y[:,0]
        for k in range(steps-1):
            coeffs1=h*function(y[:,k],K)
            coeffs2=h*function(y[:,k]+0.5*coeffs1,K)
            coeffs3=h*function(y[:,k]+0.5*coeffs2,K)
            coeffs4=h*function(y[:,k]+coeffs3,K)
            values=y[:,k] + coeffs1/float(6) + coeffs2/float(3) + coeffs3/float(3) + coeffs4/float(6)
            for j in range(len(cmp)):
                y[j,k+1]=max(values[j],0)
            ##print y[:,k+1]
        print "Computed solution to system in",time.time()-starting2,"seconds."

    for k in range(len(y)):
        f=open('cmp.'+str(k),'w')
        f.write('# Compound '+cmp[k]+'\n\n')
        for j in range(steps):
            f.write(str(t0+j*(tf-t0)/float(steps))+' '+str(y[k,j])+'\n')
        f.close()
    print "Finished writing concentrations to disk. Overall:",time.time()-starting1,"seconds."
    return y

def PlotConcentration(y,cmp,key):
    if key=='all':
        set=cmp
        modifyier=0
        plots=len(set)
    else:
        if str(key).isdigit():
            modifyier=key
            set=[cmp[modifyier]]
            plots=1
        else:
            modifyier=cmp.index(key)
            set=[cmp[modifyier]]
            plots=1
            
    for k in range(plots):
        var=str(k+modifyier)
        var=Gnuplot.Gnuplot(debug=1)
        name="'cmp."+str(k+modifyier)+"' smooth csplines"
        var.title('Concentration of '+set[k])
        var.plot(name)
        raw_input('Press ENTER')

    return
