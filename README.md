# Fair Billing

Calculating billing hours from system daily logs.


```bash
pip install foobar
```
## Installation
System Requirement: Python 3.*

## Execution:
```bash
$ python fair-billing.py
```

```bash
$ Enter file name to take logs:
```
Log File Name (Example: samplelog.txt)


## Example
Log File Data: 
```txt
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

Output: 
```txt
ALICE99 4 240
CHARLIE 3 37
```
