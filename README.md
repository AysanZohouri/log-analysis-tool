# log-analysis-tool
Python tool for analysing log files and detecting suspicious login attempts
# Log Analysis Tool

This project is a simple Python-based tool that analyses log files to detect suspicious login attempts.

## Features

- Reads log files
- Identifies failed login attempts
- Counts attempts per IP address
- Flags suspicious activity based on repeated failures

## How It Works

The script scans each log entry and tracks failed login attempts. If an IP address exceeds a defined threshold, it is flagged as suspicious.

## Example Output

---- Suspicious Activity ----  
Suspicious IP: 192.168.1.1 | Attempts: 4  
Suspicious IP: 172.16.0.3 | Attempts: 5  

## Key Learning

- Working with file input in Python  
- Basic log analysis techniques  
- Identifying suspicious behaviour patterns  
- Applying security thinking to real data  

## Notes

This project is part of my hands-on learning in cyber security and Python.
