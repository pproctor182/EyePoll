import scipy.io
import math
import numpy as np

def get_num_trials(subject_id):
    subject_list_1 = ['BT','DD','TP','KN','SR','AT','MZ','ANT','DJ','TPR']
    subject_list_2 = ['AD','NL','AK','AM','NG','AO','JM','CC','MAM','ET']
    
    if subject_id in subject_list_1:
        AAAD_flag = True
        no_AAAD_flag = False
        subj_id = subject_id
        
    elif subject_id in subject_list_2:
        AAAD_flag = False
        no_AAAD_flag = True
        subj_id = subject_id
        
    else:
        None
        
    cb_data_dict = {}
    cb_data = scipy.io.loadmat('./cb_data/' + subj_id + '_cb_AAAD_V2.mat', cb_data_dict)
    
    subject_data1 = scipy.io.loadmat('./MAT_Data_Full_AAAD_V2/' + subj_id + '_1.mat' )
    subject_data2 = scipy.io.loadmat('./MAT_Data_Full_AAAD_V2/' + subj_id + '_2.mat')
      
    
    numtrials1 = np.count_nonzero(~np.isnan(subject_data1['response1'])) #sum(not np.isnan(subject_data1['response1']))
    numtrials2 = np.count_nonzero(~np.isnan(subject_data2['response1'][1])) #sum(not np.isnan(subject_data2['response2']))
        
    
    
    if AAAD_flag is True:
        trial_num1 = numtrials2   #trialnum is value to be returned
        trial_num2 = numtrials1
    else:
        trial_num1 = numtrials1   #trialnum is value to be returned
        trial_num2 = numtrials2
    
    return trial_num1, trial_num2
