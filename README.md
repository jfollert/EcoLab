# EcoLab [vAlpha]
An open platform made to optimize resources in computer science labs.

![Status](https://img.shields.io/badge/version-alpha-red.svg)
![Python](https://img.shields.io/badge/python-2.7-blue.svg)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://raw.githubusercontent.com/basfom/EcoLab/master/LICENSE)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/EcoLabMSG/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

----
### Objectives:

----
### Commands:
#### CHECK
```sh
 $ python ecolab.py check [-a] [-i IP]
```

* __-a:__ Returns a list of all registered machines and their status.
 
* __-i:__ Returns the status (ON/OFF) of a specific machine.

#### ADD
```sh
$ python ecolab.py add [IP:MAC]
```
* Adds a machine to the network.


#### REMOVE
```sh
$ python ecolab.py remove [IP/MAC]
```
* Removes a machine from the network.
  
#### WAKE
```sh
$ python ecolab.py wake [-a] [-i IP]
```

* __-a:__ Turns on all registered machines.

* __-i:__ Turns on a specific machine.

#### DOWN
```sh
$ python ecolab.py down [-a] [-i IP]
```

* __-a:__ Turns off all registered machines.

* __-i:__ Turns off a specific machine.


#### SETHOUR
```sh
$ python ecolab.py sethour [-w] [-d] hh:mm
```

* __-w:__ Sets a time at which a machine turns on.

* __-d:__ Sets a time at which a machine turns off.
