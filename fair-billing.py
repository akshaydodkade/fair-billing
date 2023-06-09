# Project: Fair Billing
# Author: Akshay Dodkade

import sys

log_start = ""
log_end = ""
log_report = []

# calculate difference in seconds
def get_time(start_time, end_time):
    start_time_data = start_time.split(':')
    end_time_data = end_time.split(':')
    return ((int(end_time_data[0]) - int(start_time_data[0])) * 60 * 60) + ((int(end_time_data[1]) - int(start_time_data[1])) * 60) + ((int(end_time_data[2]) - int(start_time_data[2])))

def log_validation(log):
    log_data = log.split()

    # data length
    if len(log_data) != 3:
        return False
    # check for log start and end
    if log_data[2] != 'Start' and log_data[2] != 'End':
        return False
    # check for user alphanumeric
    if log_data[1].isalnum() == False:
        return False
    # check for HH:MM:SS format
    time = log_data[0].split(':')
    if len(time) != 3:
        return False
    else:
        if int(time[0]) > 23 or int(time[1]) > 59 or int(time[2]) > 59:
            return False

    return True

try:
    # get file
    if (len(sys.argv[1:]) < 1):
        raise Exception("Please add log file to continue")
    
    log_file = sys.argv[1:][0]
    with open(log_file, 'r+') as file:
        lines = [line.rstrip() for line in file]


    # process file data
    for idx, line in enumerate(lines):
        time_spend = 0
        line_data = line.split()

        # data validation
        if log_validation(line) == False:
            continue

        # get start time
        if (log_start == ""):
            log_start = line_data[0]

        # update end time
        log_end = line_data[0]
        
        if not any(data['user'] == line_data[1] for data in log_report):
            active_sessions = []
            if line_data[2] == 'End':
                time_spend += get_time(log_start, line_data[0])
            else:
                active_sessions = [
                    {
                        'time': line_data[0],
                        'type': line_data[2],
                    }
                ]
            log_report.append({
                'user': line_data[1],
                'sessions': 1,
                'time_spend': time_spend,
                'active_sessions': active_sessions
            })
        else:
            log_idx = log_report.index(next(filter(lambda n: n.get('user') == line_data[1], log_report)))
            if line_data[2] == 'Start':
                log_report[log_idx]['sessions'] += 1
                log_report[log_idx]['active_sessions'].append({
                    'time': line_data[0],
                    'type': line_data[2],
                })
            else:
                if len(log_report[log_idx]['active_sessions']) > 0:
                    # get first session and calculate difference
                    time_spend = get_time(log_report[log_idx]['active_sessions'][0]['time'], line_data[0])
                    log_report[log_idx]['time_spend'] += time_spend
                    log_report[log_idx]['active_sessions'].pop(0)
                else:
                    time_spend = get_time(log_start, line_data[0])
                    log_report[log_idx]['sessions'] += 1
                    log_report[log_idx]['time_spend'] += time_spend


    # log report final cleanup
    for record in log_report:
        if len(record['active_sessions']) > 0:
            time_spend = 0
            for idx, log in enumerate(record['active_sessions']):
                time_spend = get_time(record['active_sessions'][idx]['time'], log_end)
                record['time_spend'] += time_spend
            record['active_sessions'] = []
        
        print(f"{record['user']} {record['sessions']} {record['time_spend']}")

except FileNotFoundError:
    print(f"Error: Please add log file")

except Exception as e:
    print(f"Error: {e}")
