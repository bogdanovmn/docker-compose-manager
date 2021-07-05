# About

A simple tool for managing multiple docker-compose configuration

# Configuration

All you need is just specify docker-compose configs and their aliases 
You can find an example in the example dir. The default config name is DCMfile. Also, you can specify it using command line argument

# Examples

## Config
```
backend    /root/path/to/backend/docker-compose.yaml
frontend   /root/path/to/front/docker-compose.yaml
monitoring /root/path/to/monitoring/docker-compose.yaml
```

## Up everything
```
./dcm.py -a up
```

## Figuring out services names
```
./dcm.py -a config
```

## Execute a command inside a service container
```
./dcm.py -t backend -a exec -o "service-from-backend sh"
```

## Show logs for all services in frontend
```
./dcm.py -t frontend -a logs
```
