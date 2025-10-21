import json

total_lines = 0
error_count = 0
warn_count = 0

with open('sample.log', 'r') as log_file:
    for line in log_file:
        total_lines +=1
        if "ERROR" in line:
            error_count +=1
        
        if "WARN" in line:
            warn_count +=1


print("Total de linhas = ", total_lines)
print("Error count = ", error_count)
print("Warn count = ", warn_count)

with open('report.json', 'w') as report_file:
    report = {
        'total_lines': total_lines,
        'error_count': error_count,
        'warn_count': warn_count
    }
    json.dump(report, report_file, indent=4)