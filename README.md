# port_supervisor

Port supervisor checks if a port is active and restarts the service associated with the port if it is down. Currently,
the following services are supported on their default ports:

* apache2
* redis
* cups
* mysql
* exim4

## Install
The recommend method to install this script is using pip. A virtualenv is also recommended. Use the following command:

```
pip install -e git+https://github.com/jmetzmeier/port_supervisor.git@master#egg=port_supervisor
```

## Usage
This script can read options from stdin, command line args, or prompt if nothing is provided. To check apache2 and exim4 on localhost:

`port_supervisor -i 127.0.0.1 -p 80,631`

Using stdin:

`printf '127.0.0.1\n80,631' | port_supervisor -i 127.0.0.1 -p 80,631`

## Logging output
By default port_supervisor will log data to ./port_supervisor.log. Use `--help` to see a full list of options



