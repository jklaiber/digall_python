# digall_python
Python Script for easier domain lookup

## Getting Started

### Prerequisites

You need to install following prerequisites

```
sudo apt-get install python
```
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install dnspython
```

### Installing

```
git clone https://github.com/jklaiber/digall_python
```
```
chmod +x digall.py
```
```
mv digall.py /bin
```

You get all options by typing -h or --help
```
digall --help

Options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain=DOMAIN
                        the domainname you want to lookup
  -i IPADRESS, --ipadress=IPADRESS
                        the ip adress you want to lookup
  -n NAMESERVER, --nameserver=NAMESERVER
                        take another nameserver default is 8.8.8.8 from google
  -f FILE, --file=FILE  filename
  -p PATH, --path=PATH  path to the reportfile (use only with -f)

```

## Examples
```
digall -d google.com
```
![example_google.com](https://github.com/jklaiber/digall_python/blob/master/examples.png)


## Authors

* **Julian Klaiber** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
