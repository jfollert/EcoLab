# EcoLab [vAlpha]
Open plataform for automating computer labs oriented to energy saving.

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
 $ ecolabit.py check [-a] [-i IP]
```

* __-a:__ Return a list of the machines registered with their status.
 
* __-i:__ Return the status (ON/OFF) of a specific machine.

#### ADD
```sh
$ ecolabit.py add [IP:MAC]
```
Adds a machine to the service.


#### REMOVE
```sh
$ ecolabit.py remove [IP/MAC]
```
Removes a machine to the service.
  
#### WAKE
```sh
ecolabit.py wake [-a] [-i IP]
```

* __-a:__ Turn on all the machines registered.

* __-i:__ Turn on a specific machine.

#### DOWN
```sh
ecolabit.py down [-a] [-i IP]
```

* __-a:__ Turn off all the machines registered.

* __-i:__ Turn off a specific machine.


#### SETHOUR
```sh
ecolabit.py sethour [-w] [-d] hh:mm
```

* __-w:__ Sets the power on time.

* __-d:__ Sets the power off time.


###### IN PROCESS

----
### Features:

----
### Structure:
