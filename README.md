# EcoLab [vAlpha]
Open platform made to optimize resources on Computer Science labs.

![Status](https://img.shields.io/badge/version-alpha-yellow.svg)
![Python](https://img.shields.io/badge/python-2.7-blue.svg)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://raw.githubusercontent.com/basfom/EcoLab/master/LICENSE)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/EcoLabMSG/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

----
### Objetives:

----
### Commands:
#### CHECK
```sh
 $ ecolab.py check [-a] [-i IP]
```

* __-a:__ Return a list of the machines registered with their status.
 
* __-i:__ Return the status (ON/OFF) of a specific machine.

#### ADD
```sh
$ ecolab.py add [IP:MAC]
```
Adds a machine to the service.


#### REMOVE
```sh
$ ecolab.py remove [IP/MAC]
```
Removes a machine to the service.
  
#### WAKE
```sh
$ ecolab.py wake [-a] [-i IP]
```

* __-a:__ Turn on all the machines registered.

* __-i:__ Turn on a specific machine.

#### DOWN
```sh
$ ecolab.py down [-a] [-i IP]
```

* __-a:__ Turn off all the machines registered.

* __-i:__ Turn off a specific machine.


#### SETHOUR
```sh
$ ecolab.py sethour [-w] [-d] hh:mm
```

* __-w:__ Sets the power on time.

* __-d:__ Sets the power off time.


###### IN PROCESS

----
### Features:

----
### Structure:
