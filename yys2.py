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
    init = 5000
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
  

def att_loop(group, attTimes, yh_type):
    ##att = 17, attPer = 0.02, critPer = 0.02, critAdd = 0.03, critAddinit = 0.5

    attFIX = group[0]
    attPerADD = group[1] + yh_type[1]
    critAdd = group[2] # BS
    critPer = group[3] + yh_type[0] # BJ
    
    att_SUM = 0
    
    Times = 100
    
    for i in range(Times):
        
        for j in attTimes:
            att_1 = att1(i, attFIX, attPerADD, critAdd, critPer)[0]
            att_SUM +=att_1
    
    att_SUM_round = round(att_SUM/1000000,3)
        
    return att_SUM_round, "null"
    
attTimes = get_input()


# 攻击， 攻击加成， 爆伤，暴击
conf_list = {'ONLY_BJ':[304, 0.72, 0, 0.36], 'ONLY_BS': [304, 0.72, 0.54, 0], 'ONLY_GJ': [304, 1.08, 0, 0], \
             'BS+BJ': [304, 0.72, 0.54, 0.12], 'BS+BS': [304, 0.72, 0.72, 0], 'BS+GJ': [304, 0.9, 0.54, 0], \
             'BJ+BJ': [304, 0.72, 0, 0.48], 'BJ+BS': [304, 0.72, 0.12, 0.36], 'BJ+GJ': [304, 0.9, 0, 0.36], \
             'GJ+BJ': [304, 1.08, 0, 0.12], 'GJ+BS': [304, 1.08, 0.12, 0], 'GJ+GJ': [304, 1.2, 0, 0],}

YH_conf = [[0.15,0.15], [0.3,0], [0, 0.3]]

def YH_print():
    for i in YH_conf:
        print ("当前御魂附加暴击 %s，附加攻击%s" % (i[0], i[1]))
        att_group = att_loop(conf_list['ONLY_GJ'], attTimes, i)
        print ("主攻击          - result times - %s, crit times - %s" % (att_group[0], att_group[1]))
        
        critEXT_group = att_loop(conf_list['ONLY_BS'], attTimes, i)
        print ("主爆伤          - result times - %s, crit times - %s" % (critEXT_group[0], critEXT_group[1]))
        
        crit_group = att_loop(conf_list['ONLY_BJ'], attTimes, i)
        print ("主暴击           - result times - %s, crit times - %s" % (crit_group[0], crit_group[1]))
        
        critEXT_crit_group = att_loop(conf_list['BS+BJ'], attTimes, i)
        print ("主爆伤加暴击    - result times - %s, crit times - %s" % (critEXT_crit_group[0], critEXT_crit_group[1]))
        
        critEXT_crit_group = att_loop(conf_list['BS+BS'], attTimes, i)
        print ("主爆伤加爆伤    - result times - %s, crit times - %s" % (critEXT_crit_group[0], critEXT_crit_group[1]))
        
        critEXT_crit_group = att_loop(conf_list['BS+GJ'], attTimes, i)
        print ("主爆伤加攻击    - result times - %s, crit times - %s" % (critEXT_crit_group[0], critEXT_crit_group[1]))
        
        crit_crit_group = att_loop(conf_list['BJ+GJ'], attTimes, i)
        print ("主暴击加攻击   - result times - %s, crit times - %s" % (crit_crit_group[0], crit_crit_group[1]))
        
        crit_crit_group = att_loop(conf_list['BJ+BJ'], attTimes, i)
        print ("主暴击加暴击   - result times - %s, crit times - %s" % (crit_crit_group[0], crit_crit_group[1]))
        
        crit_critEXT_group = att_loop(conf_list['BJ+BS'], attTimes, i)
        print ("主暴击加爆伤   - result times - %s, crit times - %s" % (crit_critEXT_group[0], crit_critEXT_group[1]))
        
        
        att_critplus = att_loop(conf_list['GJ+GJ'], attTimes, i)
        print ("主攻击加攻击    - result times - %s, crit times - %s" % (att_critplus[0], att_critplus[1]))
        
        att_critplus = att_loop(conf_list['GJ+BJ'], attTimes, i)
        print ("主攻击加暴击    - result times - %s, crit times - %s" % (att_critplus[0], att_critplus[1]))
        
        att_critADDplus = att_loop(conf_list['GJ+BS'], attTimes, i)
        print ("主攻击加爆伤   - result times - %s, crit times - %s" % (att_critADDplus[0], att_critADDplus[1]))



YH_print()




















 