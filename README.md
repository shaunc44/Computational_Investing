## HOW TO INSTALL QSTK ON A MAC
### Coursera - Computational Investing, Part 1
### *Dr. Tucker Balch of Georgia Tech*
#### October 30, 2016

After perusing many websites I finally discovered a way to install
QSTK on my Macbook Air (SierraOS).  The instructions found at wiki.quantsoftware
advise students to shy away from the mac installation and instead
opt for Ubuntu. Ubuntu did work on my machine, but I felt it was sluggish and
severely slowed my workflow, therefore I kept trying all of the solutions on found
online. The instructions below worked for me.

-----------------------------------------------------------------
### INSTALLATION INSTRUCTIONS

1. Open the mac terminal and enter:  
```	xcode-select --install ```  
	* A pop-up window will appear asking you about installing tools, choose install tools, wait for install to finish

2. Next, download fortran for mac from http://gcc.gnu.org/wiki/GFortranBinaries

3. After the fortran download is complete, open the terminal and paste this link with your sytem password and enter the subsequent commands in the terminal. Be sure to update the version numbers as new versions are released..

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
##### *The homebrew download will take a while*

```
brew install pkg-config
```
```
brew install freetype
```
```
brew install libpng
```
```
sudo easy_install install pip
```
##### *There will be an error message but dont worry, keep going*
```
sudo easy_install pip
```
```
sudo pip install numpy
```
##### *Installs numpy*
```
curl -O https://github.com/QuantSoftware/QuantSoftwareToolkit/releases/download/0.2.8/QSTK-0.2.8.tar.gz
```
#####*Copy and paste to save time*
```
tar -zxvf QSTK-0.2.8.tar.gz
```
#####*Un-tar the packages*
```
sudo pip install -e QSTK-0.2.8/
```
```
python QSTK-0.2.8/Examples/Validation.py
```

##### *Your output should look like this:*
![](https://cloud.githubusercontent.com/assets/7787405/19863916/73b63b38-9f6c-11e6-97ff-ab4bba6a19f3.png)

```
cd QSTK-0.2.8
```
```
cd Examples
```
```
cd Basic
```
```
python tutorial1.py
```
```
ls *.pdf
```
##### *Try opening the normalized pdf with:*
```
open normalized.pdf
```
##### *A graph should open with normalized prices*
