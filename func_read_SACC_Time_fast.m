function func_read_SACC_Time_fast(subject_id,sess_id)

%subject_id: This is the subject id (in string) of the person who participated in your experiment.
%sess_id: This is the session id (in integer/number value) that the subject participated in. There can be more than one session!

% Data Input Preparation:
% All .ASC files should be in the ./ASC_Data_Folder

% Data Output Preparation:
% All Output files should go to the:
% ./Sacc_Data/Fast/Time/'subject_id'/'sess_id_str'/

% You should create these folders.

% EyeLink Best practices:
% Send a 'Trial X flag' everytime a subject begins a trial. 
% The parser is checking for these flags to make sure it collects the correct information.

sess_id_str = num2str(sess_id);

file_name = strcat('./ASC_Data_Full_AAAD_V2/',subject_id,'_',sess_id_str,'.asc');

fid = fopen(file_name);

num_trials = 100; %Assume 100 trials. Change this parameters however you please. You can change this for a function too.

for n=1:num_trials

	% Show Trial progress:
	disp(n)

	n_str = num2str(n);
	trial_str = ['Trial ' n_str];

	trial_str_sharp = ['Trial' n_str];

	fid_name_start = ['./Sacc_Data/Fast/Time/' subject_id '/' sess_id_str '/' trial_str_sharp  '.csv'];

	fid_temp_fix = fopen(fid_name_start,'w');

	tline = fgetl(fid);
	while ischar(tline);

		tline = fgetl(fid);

		if ~isempty(strfind(tline,trial_str))

			t_buffer = strread(tline,'%s','delimiter',' \t\n');

			fixation_offset = str2num(t_buffer{2});
			counter_step = 0;

			while(1)
				tline =fgetl(fid);

				if strfind(tline,'END');
					fclose(fid_temp_fix);

					break;
				end

				if ~isempty(strfind(tline,'ESACC')) || ~isempty(strfind(tline,'SFIX')) || ~isempty(strfind(tline,'SSACC')) || ~isempty(strfind(tline,'EBLINK')) || ~isempty(strfind(tline,'SBLINK'))%|| ~isempty(strfind(tline,'ESACC')) %... || ~isempty(strfind(tline,'EBLINK')) || ~isempty(strfind(tline,'SBLINK'))
					continue;
				end

				if ~isempty(strfind(tline,'EFIX'))
					tline_snap = tline;
					t_buffer=strread(tline_snap,'%s','delimiter',' \t\n');

					if counter_step == 0
						fixation_time = str2num(t_buffer{4}) - fixation_offset;

					else
						fixation_time = str2num(t_buffer{4}) - str2num(t_buffer{3});
					end

					fixation_time_str = num2str(fixation_time);

					fprintf(fid_temp_fix,'%s\n',fixation_time_str);
					counter_step = counter_step + 1;

				end

			end

			break;

		end

	end

end

fclose('all');

