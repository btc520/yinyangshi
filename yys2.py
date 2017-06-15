#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random



level = int(raw_input("yuhuan level: (4)") or "4")

def get_input():
    
    attTimes = int(raw_input("attTimes: (5)") or "5")
    AVGcheck = raw_input("average each time? (yes)") or "yes"
    
    attEach =[]
        
    if AVGcheck == "yes":
        AVGper = float(raw_input("average attak per?: (0.5)") or "0.5")
    
        for i in range(attTimes):
            attEach.append(AVGper)
    else:
        for i in range(attTimes):
            
            eachAtt = float(raw_input("enter every time ATT per: (0.5)") or "0.5")
            attEach.append(eachAtt)
    return attEach
    



# attck percentage, 
def att1(attStep, attFix, attPerADD, critAdd, critPer):
    init = 1000
    critInit = 0.1
    critSUM = False
    
    critSum = critInit+critPer
    critAddinit = 1.5 + critAdd
    attADD = 1+attPerADD

    #print ("crit percentage sum is %s" % critSum)
    #print ("crit add sum is %s" % critAddinit)
    #print ("att add sum is %s" % attADD)
    
    randnum = random.randint(1, 100)

    if randnum <= critSum *100:
        #print "crit attack!"
        att1Sum = (init * attStep * attADD + attFix) * critAddinit
        critSUM = True
    else:
        att1Sum = init * attStep * attADD + attFix
        critSUM = False
    #print ("total average attack result is %s " % AVGsum)

    return att1Sum, critSUM
  

def att_loop(group, attStepList):
    ##att = 17, attPer = 0.02, critPer = 0.02, critAdd = 0.03, critAddinit = 0.5

    attFIX = group[0]
    attPerADD = group[1]
    critAdd = group[2]
    critPer = group[3]
    
    att_SUM = 0
    
    Times = 1000
    
    for i in range(Times):
        
        for j in attStepList:
            att_1 = att1(i, attFIX, attPerADD, critAdd, critPer)[0]
            att_SUM +=att_1
    
    att_SUM_round = round(att_SUM/1000000000,1)
        
    return att_SUM_round, "null"
    
attEACH = get_input()


##仅暴击
group_crit = [304, 0.72, 0, 0.36]
crit_group = att_loop(group_crit, attEACH)
print ("仅暴击           - result times - %s, crit times - %s" % (crit_group[0], crit_group[1]))
##爆伤
group_critEXT = [304, 0.72, 0.54, 0]
critEXT_group = att_loop(group_critEXT, attEACH)
print ("仅爆伤          - result times - %s, crit times - %s" % (critEXT_group[0], critEXT_group[1]))

##仅攻击
group_att = [304, 1.08, 0, 0]
att_group = att_loop(group_att, attEACH)
print ("仅攻击          - result times - %s, crit times - %s" % (att_group[0], att_group[1]))


##主爆伤加暴击
group_critEXT_crit = [304, 0.72, 0.54, 0.12]
critEXT_crit_group = att_loop(group_critEXT_crit, attEACH)
print ("主爆伤加暴击    - result times - %s, crit times - %s" % (critEXT_crit_group[0], critEXT_crit_group[1]))


##主暴击加暴击
group_crit_plus = [304, 0.72, 0, 0.48]
crit_plus_crit = att_loop(group_crit_plus, attEACH)
print ("主暴击加暴击   - result times - %s, crit times - %s" % (crit_plus_crit[0], crit_plus_crit[1]))


##主攻击加暴击
group_att_pluscrit = [304, 1.08, 0, 0.12]
att_critplus = att_loop(group_att_pluscrit, attEACH)
print ("主攻击加暴击    - result times - %s, crit times - %s" % (att_critplus[0], att_critplus[1]))


#主攻击加爆伤
group_att_pluscritADD = [304, 1.08, 0.12, 0]
att_critADDplus = att_loop(group_att_pluscritADD, attEACH)

print ("主攻击加爆伤   - result times - %s, crit times - %s" % (att_critADDplus[0], att_critADDplus[1]))
























 