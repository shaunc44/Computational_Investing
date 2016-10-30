##HOW TO INSTALL QSTK ON A MAC
###October 30, 2016
####Coursera - Computational Investing, Part 1 - Dr. Tucker Balch (GaTech)
After perusing many websites I finally discovered a way to install
QSTK on my Macbook Air (SierraOS).  The course's wiki.quantsoftware
instructions advise students to shy away from the mac installation and instead
opt for Ubuntu. Ubuntu did work on my machine, but I felt it was sluggish and
severely slowed my workflow.

-----------------------------------------------------------------
####INSTALLATION INSTRUCTIONS
1. Install the Xcode command line tools (terminal) from the itunes store (its free)
2. Next step is to download fortran for mac from http://gcc.gnu.org/wiki/GFortranBinaries
3. After its done, open the terminal and install this link with your password of your system and enter the subsequent commands in the terminal
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
brew install pkg-config
brew install freetype
brew install libpng
sudo easy_install install pip #after this there will be error message but dont worry, keep going
sudo easy_install pip
sudo pip install numpy #install numpy
curl -O http://pypi.python.org/packages/source/Q/QSTK/QSTK-0.2.5.tar.gz #I suggest you to just copy paste it
tar -zxvf QSTK-0.2.5.tar.gz #untar the packages
sudo pip install -e QSTK-0.2.5/
phyton QSTK-0.2.5/Examples/Validation.py
cd QSTK-0.2.5
cd Examples
cd Basic
python tutorial1.py
ls *.pdf
