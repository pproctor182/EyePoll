# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:03:10 2016

@author: pproctor
"""

import scipy.io
import math

def func_read_SACC_Time_fast(subject_id,sess_id):
    
    """
    subject_id: This is the subject id (in string) of the person who participated in your experiment.
    sess_id: This is the session id (in integer/number value) that the subject participated in. There can be more than one session!

     Data Input Preparation:
         All .ASC files should be in the ./ASC_Data_Folder

     Data Output Preparation:
         All Output files should go to the:
             ./Sacc_Data/Fast/Time/'subject_id'/'sess_id_str'/

     You should create these folders.

     EyeLink Best practices:
         Send a 'Trial X flag' everytime a subject begins a trial. 
         The parser is checking for these flags to make sure it collects the correct information.    
    """
    
    sess_id_str = str(sess_id)
    
    fid = ('./ASC_Data_Full_AAAD_V2/' + subject_id + '_' + sess_id_str + '.asc' )
    
    num_trials = 92 # Assume 100 trials. Change this parameters however you please. You can change this for a function too.
    
    t_line_list = ['ESACC', 'SFIX', 'SSAC', 'EBLINK', 'SBLINK']    

    for n in range(num_trials):
        
        n_str = str(n + 1)
        
        # Show Trial progress:
        print(n_str)        
        
        trial_str = 'Trial ' + n_str
        
        trial_str_sharp = 'Trial' + n_str
                        
        fid_name_start = './Sacc_Data/Fast/Time/' + subject_id + '/' + sess_id_str + '/' + trial_str_sharp + '.csv'
       
        fid_temp_fix = open(fid_name_start, 'r+')
        
        start = True #keeps track of place in the file
        
        while start is True:
            
            with open(fid) as testFile:
                for tline in testFile:
                    
                    if trial_str in tline and start is True:   
                        
                        t_buffer = tline.split()
                        
                        fixation_offset = float(t_buffer[1]) 
                        
                        start = False
                        counter = 0
                        
                        for tline in testFile:               
                            
                             if 'END' in tline:
                                start = False
                                fid_temp_fix.close()
                                break
                            
                             elif tline in t_line_list:                               
                                continue
           
                             elif 'EFIX' in tline:
                                tline_snap = tline.split()
                                
                                if counter == 0:
                                   fixation_time = float(tline_snap[3]) - fixation_offset
                                   fixation_time_str = str(fixation_time)
                                   fid_temp_fix.write('%s\n' % (fixation_time_str))
                                   counter += 1 
                                                  
                                else:
                                   fixation_time = float(tline_snap[3]) - float(tline_snap[2])
                                   fixation_time_str = str(fixation_time)
                                   fid_temp_fix.write('%s\n' % (fixation_time_str))
            
                    
                