git clone https://github.com/cyang-kth/fmm

sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get -q update

sudo apt-get install libboost-dev libboost-serialization-dev \
gdal-bin libgdal-dev make cmake libbz2-dev libexpat1-dev swig

./Anaconda3-2022.10-Linux-x86_64.sh

cd ~ && ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 anaconda3/lib/libstdc++.so.6