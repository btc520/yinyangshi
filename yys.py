#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

level = int(raw_input("yuhuan level: (4)") or "4")




def attLoop(AVGAttTimes, AVGAttPer, EXTAttTimes, EXTAttPer, initAdd, attPer, critAdd, critPer):
    AVGsum = 0
    AVGcritsum = 0
    EXTsum = 0
    EXTcritsum = 0  
    init = 1000
    
    
    critInit = 0.1
    
    critSum = critInit+critPer
    critAddinit = 1.5 + critAdd
    attPerSum = 1+attPer

    #print ("crit percentage sum is %s" % critSum)
    #print ("crit add sum is %s" % critAddinit)
    #print ("att add sum is %s" % attPerSum)
    
    for i in range(AVGAttTimes):
        randnum = random.randint(1, 100)

        if randnum<= critSum *100:
            #print "crit attack!"
            attOnce = init * AVGAttPer * 1.5 * attPerSum + initAdd
            AVGsum += attOnce
            AVGcritsum = AVGcritsum+1
        else:
            attOnce = init * AVGAttPer * attPerSum + initAdd
            AVGsum += attOnce
    #print ("total average attack result is %s " % AVGsum)

    for i in range(EXTAttTimes):
        randnum = random.randint(1, 100)

        if randnum<= critSum *100:
            #print "crit attack!"
            attOnce = init * EXTAttPer * 1.5 * attPerSum + initAdd
            EXTsum += attOnce
            EXTcritsum = EXTcritsum + 1
        else:
            attOnce = init * EXTAttPer * attPerSum + initAdd
            EXTsum += attOnce
    #print ("final attack result is %s " % EXTsum)        

    return AVGsum, AVGcritsum, EXTsum, EXTcritsum

def addpara_1():
    ##att = 17, attPer = 0.02, critPer = 0.02, critAdd = 0.03, critAddinit = 0.5
    
    AVGAttTimes = int(raw_input("AVGAttTimes: (3)") or "3")
    EXTAttTimes = int(raw_input("EXTAttTimes: (1)") or "1")

    AVGAttPer = float(raw_input("AVGAtt: (0.33)") or "0.33")
    EXTAttPer = float(raw_input("AVGAtt: (0.88)") or "0.88")

    critAdd_4 = [0, 0.03, 0.06, 0.09, 0.12, 0.15, 0.18,  0.21, 0.24, 0.27, 0.3, 0.33, 0.36, 0.39, 0.42, 0.45, 0.48, 0.52, 0.55, 0.58, 0.61]
    critPer_4 = [0, 0.02, 0.04, 0.06, 0.08, 0.10]
    
    att_4 = [0, 18, 37, 36, 76, 94, 112,  126, 140, 154, 172, 190, 208, 216, 234, 252, 270, 288, 306, 324, 342]
    attPer_4 = [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12,  0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4,  0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68]

    times = 3    
    tester = 0
    
    critAdd_count = 0
    critPer_count = 0
    att_count = 0
    attPer_count = 0
    recTimes = 0
    
    for x in range(1,times):
        for i in critAdd_4:
            for j in critPer_4:
                for k in att_4:
                    for h in attPer_4:
                        att_result = attLoop(AVGAttTimes, AVGAttPer, EXTAttTimes, EXTAttPer, k,h, i, j)
                        result_sum = att_result[0] + att_result[2]
                        crit_sum = att_result[1] + att_result[3]
                        if result_sum >= 4800:
                            tester = result_sum
                            print ("new result %s (times %s) .. critAdd - %s .. critPer - %s .. att - %s .. attPer - %s" % (result_sum, crit_sum, critAdd_4.index(i), critPer_4.index(j), att_4.index(k), attPer_4.index(h) ) )
                            critAdd_count += i
                            critPer_count += j
                            att_count += k
                            attPer_count += h
                            recTimes += 1
                        
    return tester, critAdd_count, critPer_count, att_count, attPer_count, recTimes

def addpara_2():
    ##att = 17, attPer = 0.02, critPer = 0.02, critAdd = 0.03, critAddinit = 0.5
    
    AVGAttTimes = int(raw_input("AVGAttTimes: (3)") or "3")
    EXTAttTimes = int(raw_input("EXTAttTimes: (1)") or "1")

    AVGAttPer = float(raw_input("AVGAtt: (0.33)") or "0.33")
    EXTAttPer = float(raw_input("AVGAtt: (0.88)") or "0.88")
    
    group1 = [304, 0.36, 0, 0.36, 0, 0.54]
    group1 = [304, 0.36, 0, 0.36, 0, 0.35]

    critAdd_4 = [0, 0.03, 0.06, 0.09, 0.12, 0.15]
    critPer_4 = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12,  0.14, 0.16, 0.18, 0.2, 0.22, 0.25, 0.27, 0.29, 0.31, 0.32, 0.34, 0.36, 0.38, 0.4]
    
    att_4 = [0, 18, 37, 36, 76, 94, 112,  126, 140, 154, 172, 190, 208, 216, 234, 252, 270, 288, 306, 324, 342]
    attPer_4 = [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12,  0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4,  0.42, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68]

    times = 3    
    tester = 0
    
    critAdd_count = 0
    critPer_count = 0
    att_count = 0
    attPer_count = 0
    recTimes = 0
    
    for x in range(1,times):
        for i in critAdd_4:
            for j in critPer_4:
                for k in att_4:
                    for h in attPer_4:
                        att_result = attLoop(AVGAttTimes, AVGAttPer, EXTAttTimes, EXTAttPer, k,h, i, j)
                        result_sum = att_result[0] + att_result[2]
                        crit_sum = att_result[1] + att_result[3]
                        if result_sum >= 4500:
                            tester = result_sum
                            print ("new result %s (times %s) .. critAdd - %s .. critPer - %s .. att - %s .. attPer - %s" % (result_sum, crit_sum, critAdd_4.index(i), critPer_4.index(j), att_4.index(k), attPer_4.index(h) ) )
                            critAdd_count += i
                            critPer_count += j
                            att_count += k
                            attPer_count += h
                            recTimes += 1
                        
    return tester, critAdd_count, critPer_count, att_count, attPer_count, recTimes



def addparaPrint():    
    testerA = addpara_1()
    testerA_0 = testerA[0]
    testerA_1 = testerA[1]/0.61
    testerA_2 = testerA[2]/0.4
    testerA_3 = testerA[3]/342
    testerA_4 = testerA[4]/0.68
    testerA_5 = testerA[5]
    
    testerB = addpara_2()
    testerB_0 = testerB[0]
    testerB_1 = testerB[1]/0.61
    testerB_2 = testerB[2]/0.4
    testerB_3 = testerB[3]/342
    testerB_4 = testerB[4]/0.68
    testerB_5 = testerB[5]
    print (".............................................." )
    print ("A highest record is %s" % testerA_0)
    print ("A critAdd_count is %s" % testerA_1)
    print ("A critPer_count is %s" % testerA_2)
    print ("A att_count is %s" % testerA_3)
    print ("A attPer_count is %s" % testerA_4)
    print ("A record time is %s" % testerA_5)
    print ("................B. increase crit percentage..........................." )
    print ("B highest record is %s" % testerB_0)
    print ("B critAdd_count is %s" % testerB_1)
    print ("B critPer_count is %s" % testerB_2)
    print ("B att_count is %s" % testerB_3)
    print ("B attPer_count is %s" % testerB_4)
    print ("B record time is %s" % testerB_5)
    print (".............................................." )
    ##print ("attack result is %s" % (critatt))

    #print ("attack result is %s, total crit times is %s" % (data[0], data[1]))
    

group_critADD = [304, 0.72, 0.54, 0]
group_critADD_pluscrit = [304, 0.72, 0.54, 0.12]
group_crit = [304, 0.72, 0, 0.36]
group_crit_plus = [304, 0.72, 0, 0.48]
group_att = [304, 1.08, 0, 0]
group_att_pluscrit = [304, 1.08, 0, 0.12]
group_att_pluscritADD = [304, 1.08, 0.12, 0]

AVGAttTimes = int(raw_input("AVGAttTimes: (3)") or "3")
EXTAttTimes = int(raw_input("EXTAttTimes: (1)") or "1")

AVGAttPer = float(raw_input("AVGAtt: (0.33)") or "0.33")
EXTAttPer = float(raw_input("AVGAtt: (0.88)") or "0.88")



def addpara_x(group):
    ##att = 17, attPer = 0.02, critPer = 0.02, critAdd = 0.03, critAddinit = 0.5
    


    attBASE = group[0]
    attPER = group[1]
    critADD = group[2]
    critPER = group[3]
    
    times = 10000 
    
    tester = 0
    
    result_times =0
    crit_times =0
    
    for x in range(1,times):
        result_sum = 0
        crit_sum = 0

        att_result = attLoop(AVGAttTimes, AVGAttPer, EXTAttTimes, EXTAttPer, attBASE, attPER, critADD, critPER)
        
        result_sum = att_result[0] + att_result[2]
        crit_sum = att_result[1] + att_result[3]
        
        if result_sum >= 5500:
            #print ("att total - %s, crit times - %s" % (result_sum, crit_sum))
            #print ("Result sum - %s .. crit sum - %s" % (result_sum, crit_sum) )
            result_times +=1
            crit_times += crit_sum
                        
    return result_times, crit_times
    
critADD = addpara_x(group_critADD)
crit_r = addpara_x(group_crit)
crit_plus_ADD = addpara_x(group_critADD_pluscrit)
crit_plus_crit = addpara_x(group_crit_plus)

att_r = addpara_x(group_att)
att_critplus = addpara_x(group_att_pluscrit)
att_critADDplus = addpara_x(group_att_pluscritADD)

print ("crit ADD         - result times - %s, crit times - %s" % (critADD[0], critADD[1]))
print ("crit             - result times - %s, crit times - %s" % (crit_r[0], crit_r[1]))
print ("att              - result times - %s, crit times - %s" % (att_r[0], att_r[1]))
print ("crit plus ADD    - result times - %s, crit times - %s" % (crit_plus_ADD[0], crit_plus_ADD[1]))
print ("att crit plus    - result times - %s, crit times - %s" % (att_critplus[0], att_critplus[1]))

print ("att critADD plus - result times - %s, crit times - %s" % (att_critADDplus[0], att_critADDplus[1]))

print ("crit plus crit   - result times - %s, crit times - %s" % (crit_plus_crit[0], crit_plus_crit[1]))