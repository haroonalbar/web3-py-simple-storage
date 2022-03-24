Create simplesrorage.sol

Settings format on save on for both python and solidity


Python 
 Black formator for pyrhon 
   Pip install black
     Settings python formatting privider select black


New file
   Deploy.py 
    Ist code run
    python deploy.py

Compiler for python

Py solcx
Install
 pip install py-solc-x
and
not really need to install solc but just in case 
npm install -g solc

install and open ganache
quickstart 

web3.py
pip install web3
had problem installing web3 
pip install web3 --user
this will install as administrator an fixed it
 deploy it
<class 'web3._utils.datatypes.Contract'>  is shown

setting envirement variable so we dont have to hard code our private key into our code directly " this is also not the best way"

environment variable > new > private_key > ok
comtline >echo %private_key%
to print the private in the command line

.env can be accessed directly with python dotenv package 

**developers merged ganache-core and ganache-cli to just ganache**
*so use ganache insted of ganache-cli*
close ganache ui and install ganache cli => brown is going to use in the background
this will install ganache-cli as a global command in terminal
to install ganache cli download node.js
node --version

install yarn => is a packagemanager like pip
  npm install --global yarn
  yarn --version

install ganachecli
  yarn global add ganache
  ganache --version
  *if facing error*
  npm install -g ganache --user
  ganache --version

*to run a local blockchain from command line*
  ganache *it will create random accounts everytime*
  gancache -d *determinstic/same account*
  it will be listening to 127.0.0.1 *this is called loopback address or local address*
  update private key and address as in the command line




     

