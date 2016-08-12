# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:03:02 2016

@author: pproctor
"""

import scipy.io
import math
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
    
    trial_num = get_num_trials(subject_id)
    
    if sess_id == 1:
        
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
        
        fid_name_end = './Sacc_Data/Fast/End/' + subject_id + '/' + sess_id_str + '/' + trial_str_sharp + '.csv'
        
        fid_temp_start = open(fid_name_start, 'w')
        fid_temp_end = open(fid_name_end, 'w')
        
        t_line_list = ['EFIX','SFIX','SSAC','EBLINK','SBLINK']
                
        
        with open(fid) as testFile:
            for tline in testFile:
                
                if tline == 'End':
                    fid_temp_start.close()
                    fid_temp_end.close()
                    break
                
                else:
                    continue
                
                while tline != "":
                    if tline in t_line_list:
                        continue
                    
                    elif tline == 'ESACC':
                        tline_snap = tline 
                        t_buffer = tline_snap.split('%s', " ")
                        
                        sac_x_start = t_buffer[4]
                        sac_y_start = t_buffer[5]
                        
                        sac_x_end = t_buffer[6]
                        sac_y_end = t_buffer[7]
                        
                        
                        if t_buffer[4](1) == '.':
                            sac_x_start = 0
                            
                        elif t_buffer[5](1) == '.':
                            sac_y_start = 0
                            
                        elif t_buffer[6](1) == '.':
                            sac_x_end = 0 
                            
                        elif t_buffer[7](1) == '.':
                            sac_y_end = 0
                            
                        else:
                            continue 
                        
                    
                        fid_temp_start.write('%s,%s\n' % (sac_x_start, sac_y_start))                        
                        fid_temp_end.write('%s,%s\n' % (sac_x_end, sac_y_end))
                    
                    
                    else:
                        None
                        
                    
                            
                        
                    
                
                                    
