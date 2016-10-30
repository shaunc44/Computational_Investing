##HOW TO INSTALL QSTK ON A MAC
####October 30, 2016
###Coursera - Computational Investing, Part 1 - Dr. Tucker Balch (GaTech)
After perusing many websites I finally discovered a way to install
QSTK on my Macbook Air (SierraOS).  The instructions found at wiki.quantsoftware
advise students to shy away from the mac installation and instead
opt for Ubuntu. Ubuntu did work on my machine, but I felt it was sluggish and
severely slowed my workflow, therefore I kept trying all of the solutions on found
online. The instructions below worked for me.

-----------------------------------------------------------------
###INSTALLATION INSTRUCTIONS
1. Go to spotlight search and search for 'terminal'
2. Open the terminal and enter:  
```	xcode-select --install ```  
	*A pop-up window will appear asking you about installing tools, choose install tools, wait for install to finish*
3. Next, download fortran for mac from http://gcc.gnu.org/wiki/GFortranBinaries

4. After fortran is done, open the terminal and paste this link with your sytem password and enter the subsequent commands in the terminal

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
#####*The homebrew download will take a while*
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
#####*There will be error message but dont worry, keep going*
```
sudo easy_install pip
```
```
sudo pip install numpy
```
#####*Install numpy*
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