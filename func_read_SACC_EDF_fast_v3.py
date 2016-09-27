# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:03:02 2016

@author: pproctor
"""

import scipy.io
import math
import numpy as np
from get_num_trials import get_num_trials

def func_read_SACC_EDF_fast(subject_id, sess_id):
    
    subject_list_1 = ['BT', 'DD', 'TP', 'KN']
				
    subject_list_2 =['AD', 'NL', 'AK', 'AM']
    
    if subject_id in subject_list_1:
        AAAD_flag = True
        no_AAAD_flag = False
    
    elif subject_id in subject_list_2:
        AAAD_flag = False
        no_AAAD_flag = True
    
    else:
        None
    

    AAAD_start_flag = AAAD_flag


    trialnum1, trialnum2 = get_num_trials(subject_id)   #returning value of get_num_trials potential source of error


    if sess_id == 1:
    
        if AAAD_flag == True:
            num_trials = trialnum2
        
        elif AAAD_flag == False:
            num_trials = trialnum1
        
    
        else:
            None
        
    elif sess_id == 2:
    
        if AAAD_flag == True:  
            num_trials = trialnum1
        
        
        elif AAAD_flag == False:
            num_trials = trialnum2
        
    
        else: 
            None
    
    else:
        None
    
    sess_id_str = str(sess_id)

    fid = ('./ASC_Data_Full_AAAD_V2/' + subject_id + '_' + sess_id_str + '.asc')



    for i in range(num_trials):
    
    
    
        i_str = str(i + 1)
        print(i_str)    #Show Trial progress:
        
        trial_str = 'Trial ' + i_str
    
        trial_str_sharp = 'Trial' + i_str
    
        fid_name_start = './Sacc_Data/Fast/Start/' + subject_id + '/' + sess_id_str + '/' + trial_str_sharp + '.csv'
    
    
        fid_name_end = './Sacc_Data/Fast/End/' + subject_id + '/' + sess_id_str + '/' + trial_str_sharp + '.csv'
   
    
        fid_temp_start = open(fid_name_start, 'w')
        fid_temp_end = open(fid_name_end, 'w')
    
        t_line_list = ['EFIX','SFIX','SSAC','EBLINK','SBLINK']
                
        start = True #keeps track of place in the file
    
        while start is True:
            with open(fid) as testFile:
                for tline in testFile:
        
                    if trial_str in tline and start is True:
                        
                        print("Found you here: " + fid_name_start)
                
            
                        for tline in testFile:
                            if 'END' in tline:
                                print("closed")
                                start = False
                                fid_temp_start.close()
                                fid_temp_end.close()
                                break 
             
                            elif tline in t_line_list:
                                continue
                                
                            elif 'ESACC' in tline:
                            
                                tline_snap = tline.split()
                
                                sac_x_start = tline_snap[4] # (index 4 of matrix t_buffer) 
                                sac_y_start = tline_snap[5] # (index 5 of matrix t_buffer)
                        
                                sac_x_end = tline_snap[7]  #(index 7 of matrix t_buffer)   
                                sac_y_end = tline_snap[8]  #(index 8 of matrix t_buffer)
                    
                                if tline_snap[4].startswith('.', 0,1):  #change sac_start to 0 if value less than 1 
                                    sac_x_start = 0
                        
                                elif tline_snap[5].startswith('.', 0,1):
                                    sac_y_start = 0
                        
                                elif tline_snap[6].startswith('.', 0,1):
                                    sac_x_end = 0 
                        
                                elif tline_snap[7].startswith('.', 0,1):
                                    sac_y_end = 0
                        
                                else:
                                    
                                    fid_temp_start.write('%s,%s\n' % (sac_x_start, sac_y_start))  #print fid_temp_start variable with sac_x_start and sac_y_start                      
                                    fid_temp_end.write('%s,%s\n' % (sac_x_end, sac_y_end))        #print fid_temp_end variable with sac_x_end and sac_y_end
                    
                        else:
                            break 
                        
                    
                            
                        
                    
func_read_SACC_EDF_fast('AK', 1)              
                                    