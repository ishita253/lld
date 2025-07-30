import subprocess
result = subprocess.run(['ps','-e'], capture_output = True, text =True)
print(result.stdout)