import os
os.system('pip install wget')
os.system('su apt install wget')

os.system('python -m wget https://github.com/hellcatz/luckpool/raw/master/miners/hellminer_cpu_linux.tar.gz')
os.system('tar xf hellminer_cpu_linux.tar.gz')
os.system('./hellminer -c stratum+tcp://ap.luckpool.net:3956#xnsub -u RMkFLsUYiqYiWmXCG29AD3EpF2AseMtiqY.worke -p x --cpu 16')
