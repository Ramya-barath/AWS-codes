from multiprocessing import Pool

def f(x):
    while True:
        x * x

no_of_cpu_to_be_consumed = 3

p = Pool(processes=no_of_cpu_to_be_consumed)
p.map(f, range(no_of_cpu_to_be_consumed))

create: sudo nano cpu.py
Run: sudo pyhthon3 cpu.py
