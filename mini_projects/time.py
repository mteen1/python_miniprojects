import time
time = time.time()
mins = time//60
seconds = time%60
hours = mins//60
mins = mins%60
days = hours//24
hours = hours%24

print(f'{days} days, {hours} hours, {mins} minutes and {seconds} seconds has passed from the greenewich mean time')
