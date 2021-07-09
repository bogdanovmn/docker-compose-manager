# About

A simple tool for managing multiple docker-compose configuration

# Configuration

All you need is just specify docker-compose configs and their aliases 
You can find an example in the example dir. The default config name is DCMfile. Also, you can specify it using command line argument

## Adding the script in your PATH
```bash
export PATH="/path/to/dcm/bin:$PATH"
```

# Examples

## Config
```
backend    /root/path/to/backend/docker-compose.yaml
frontend   /root/path/to/front/docker-compose.yaml
monitoring /root/path/to/monitoring/docker-compose.yaml
```

## Up everything
```bash
$ dcm -a up
```

## Figuring out all service names
```
$ dcm -a config
```

## Execute a command inside a service container
```
$ dcm -t backend -a exec -o "service-from-backend sh"
```

## Show logs for all services in the "frontend" configuration
```
$ dcm -t frontend -a logs
```
