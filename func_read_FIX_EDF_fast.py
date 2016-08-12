# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:33:29 2016

@author: pproctor
"""
import scipy.io
import math
from get_num_trials import get_num_trials

def func_read_FIX_EDF_fast(subject_id, sess_id):
    subject_list_1 = ['BT', 'DD', 'TP', 'KN', 'SR', 'AT', 'MZ', 'ANT', 'DJ', 'TPR']
				
    subject_list_2 =['AD', 'NL', 'AK', 'AM', 'NG', 'AO', 'JM', 'CC', 'MAM', 'ET']
    			 		
    if subject_id in subject_list_1:
        AAAD_flag = True
        no_AAAD_flag = False
        
    elif subject_id in subject_list_2:
        AAAD_flag = False
        no_AAAD_flag = True
        
    else:
        None
        
        
    AAAD_start_flag = AAAD_flag
    trial_num = get_num_trials(subject_id)
    
    if sess_id == True:
        
        if AAAD_flag == True:
            num_trials = trial_num(2)
            
        elif AAAD_flag == False:
            num_trials = trial_num(1)
        
        else:
            None
            
    elif sess_id == 2:
        
        if AAAD_flag == True:
            num_trials = trial_num(1)
        
        elif AAAD_flag == False:
            num_trials = trial_num(2)
        
        else:
            None
        
    else:
        None
        
        
    sess_id_str = str(sess_id)
    
    file_name = ('./ASC_Data_Full_AAAD_V2/' + subject_id + '_' + sess_id_str + '.asc')
    
    fid = open(file_name)
    
    
    for i in num_trials:
        
        print(i)
        
        i_str = str(i)
        
        trial_str = 'Trial' + i_str
        
        trial_str_sharp = 'Trial' + i_str
        
        fid_name_start = './Sacc_Data/Fast/Start/' + subject_id + '/' + sess_id_str + '/' + trial_str_sharp + '.csv'
        
        fid_temp_fix = open(fid_name_start, 'w')
        print(fid_temp_fix)
        
        t_line_list = ['ESACC','SFIX','SSAC','EBLINK','SBLINK']        
        
        with open(fid) as testFile:
            for tline in testFile:
                #data = tline
                while tline != "":
                    if tline in trial_str:
                        t_buffer = tline.split('%s', " ") #not sure if this eliminates correct delimiter
                        
                        fixation_offset = int(t_buffer[2])
                        counter_step = 0
                        
                    
                    while True:
                        if tline in t_line_list:
                            continue
                    
                        elif tline == 'EFIX':
                            tline_snap = tline 
                            t_buffer = tline_snap.split('%s', " ")     
                            
                            if counter_step == 0:
                                fixation_time = int(t_buffer[4]) - fixation_offset
                                
                            else:
                                fixation_time = int(t_buffer[4]) - int(t_buffer[3])
                                
                            fixation_time_str = str(fixation_time)
                            
                        else:
                           None
                           
                    break 
                break
            
        #fid_name_end = './Sacc_Data/Fast/End/' + subject_id + '/' + sess_id_str + '/' + trial_str_sharp + '.csv'
        
        
