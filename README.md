# Fair Billing

* Calculating user session time in seconds from daily logs file which includes multiple sessions for single user.
* As log data is inconsistent added log data validations like alphanumeric user name acceptance, HH:MM:SS format validation and ignoring non-validated logs.

## Solution
### Approach:

* Looping through logs and calculating sessions and time spend by using a centralized dictionary.


### code flow

* Getting the logs line by line from log file
* Maintaining dictionary name ```log_report``` where calculating sessions and adding active sessions as list of dictionary
* As mentioned taking 1st log time as start time for logs with no start timestamp and last log time as end time for logs with no end timestamp
* If no user added in dictionary then adding new record for the same if log timestamp is of start adding it in active_sessions else calculating seconds session time based on start time of log file
* If record is found then for start timestamp increasing new session and adding record in active_sessions else for end timestamp checking for active_sessions count should be greater than zero
* If active_session are there then taking oldest active_session for calculating time difference and removing it from active_session list else taking log start time and calculating difference
* After looping through all the records, final scanning ```log_report``` for pending active sessions and calculating difference from taking end time of log record and printing out the solution

## Prerequisite
* System Requirement: Python 3.*

### How to Run
```sh
git clone https://github.com/akshaydodkade/fair-billing.git
```
```bash
$ python fair-billing.py <filename.ext>
```
File Name Example: samplelog.txt\
Note: Please add input file in same path and folder of fair-billing.py

### Input Example 
```sh
14:02:03 ALICE99 Start
14:02:05 CHARLIE End
14:02:34 ALICE99 End
14:02:58 ALICE99 Start
14:03:02 CHARLIE Start
14:03:33 ALICE99 Start
14:03:35 ALICE99 End
14:03:37 CHARLIE End
14:04:05 ALICE99 End
14:04:23 ALICE99 End
14:04:41 CHARLIE Start
```

### Output Example(terminal)
```sh
ALICE99 4 240
CHARLIE 3 37
```