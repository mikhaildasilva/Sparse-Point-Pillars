From [this](https://discuss.pytorch.org/t/pytorch-cuda-11-4/137900) discourse, PyTorch supports CUDA10.2 to CUDA11.5

Purge all drivers on the system 
```
$ sudo apt-get purge nvidia*
```
Search for drivers on the system
```
$ ubuntu-drivers devices
```
Driver 470.x.x works well
```
$ sudo apt-get install nvidia-driver-470
```
## Reboot the system
```
$ sudo reboot
```
To verify 
```
$ nvidia-smi
```
## Download cuDNN library
[Download the Runtime, Developer and Code Samples (Deb)](https://developer.nvidia.com/rdp/cudnn-archive))

Should have the following files in ~/Downloads
- [1] libcudnn8_8.2.4.15-1+cuda11.4_amd64.deb
- [2] libcudnn8-dev_8.2.4.15-1+cuda11.4_amd64.deb
- [3] libcudnn8-samples_8.2.4.15-1+cuda11.4_amd64.deb
## Now begin installation process
```
sudo dpkg -i libcudnn8_8.2.4.15-1+cuda11.4_amd64.deb
```
```
sudo dpkg -i libcudnn8-dev_8.2.4.15-1+cuda11.4_amd64.deb
```
```
sudo dpkg -i libcudnn8-samples_8.2.4.15-1+cuda11.4_amd64.deb
```
## Check to see if everything has installed 
```
nvidia-smi
```
## Testing the installation of cuDNN    
```
cp -r /usr/src/cudnn_samples_v8/ $HOME
```
## Troubleshooting
If you get an error that says FreeImage is not setup correctly, the do follow the below steps:
```
sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
```
Then run:
```
cd $HOME/cudnn_samples_v8/mnistCUDNN/
```
```
make
```
```
./mnistCUDNN
```
If error still persists:
```
sudo apt-get install libfreeimage3 libfreeimage-dev
```
Then:
```
cd $HOME/cudnn_samples_v8/mnistCUDNN/
```
```
make
```
```
./mnistCUDNN
```