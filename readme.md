Create **simplesrorage.sol**

Settings format on save on for both python and solidity


Python 
 *Black* formator for python 
   Pip install black
     Settings python formatting privider select black


New file
   Deploy.py 
    Ist code run
    python deploy.py

Compiler for python

*Py solcx*
Install
 pip install py-solc-x
and
not really need to install solc but just in case 
npm install -g solc

install and open *ganache* ui
quickstart 

*web3.py*
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
  npm install dotenv --save

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
  update :private key 
          address
          http provider / RPC url

*to change from local blockchain to main net or test net all we have to do is change the RPC url/ http provider*
we can also run our own blockchain node similar to running our local blockchain node
but its not easy to do so we can use 3rd party like infura to run a blockchain for us
infura  =>  
          go to infura.io and register for free 
          alchemy.com is another option
          in infura change endpoint to rinkby
          the copy the url
          change the  http provider to url
                      chainId *chainid.network to find out* for rinkby its 4
                      address from metamask
                      privatekey from metamask
                      source.env in command for the env to update in windows and linux




     

