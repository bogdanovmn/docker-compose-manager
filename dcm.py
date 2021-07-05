#!/usr/bin/env python

import argparse
import subprocess


class ConfigFile:
	def __init__(self, config_file):
		self.config_file = config_file

	def read(self):
		print "Reading config: %s..." % self.config_file
		config = {}		
		with open(self.config_file) as config_file:
			for line in config_file:
				line_parts = line.split()
				config[line_parts[0]] = line_parts[1]

		return Config(config)

class Config:
	def __init__(self, targets):
		self.targets = targets

	def allTargets(self):
		return self.targets.keys()

	def hasTarget(self, target):
		return target in self.targets

	def targetFile(self, target):
		return self.targets[target]

class Command:
	defaults = {
		'up'  : '-d',
		'config'  : '--service',
		'logs': '-f --tail=10'
	}

	def __init__(self, command):
		self.command = command

	def withDefaultArgs(self):
		if self.command in self.defaults:
			return "%s %s" % (self.command, self.defaults[self.command])
		else: 
			return self.command

class DockerComposeShellCommand:
	def __init__(self, config_file_arg, command, extra_options):
		self.config_file_arg = config_file_arg
		self.command = command
		self.extra_options = extra_options

	def execute(self):
		cmd =  "docker-compose -f %s %s %s" % (self.config_file_arg, self.command.withDefaultArgs(), self.extra_options)
		print "\nRUNNING: %s\n" % cmd
		retcode = subprocess.call(cmd.split())

#########################################
# Here we go
#########################################

argsParser = argparse.ArgumentParser()
argsParser.add_argument(
	'-c', '--config', 
	help="config file name. By default is DCMfile (docker compose management file)",
	required=False,
	default='DCMfile'
)
argsParser.add_argument(
	'-s', '--show-config', 
	help='show config details',
	required=False,
	action='store_true'
)
argsParser.add_argument(
	'-t', '--target', 
	help="target of docker-compose command",
	required=False,
	default='all'
)
argsParser.add_argument(
	'-a', '--action', 
	help="a docker-compose command",
	required=False,
	default='ps'
)
argsParser.add_argument(
	'-o', '--extra-options', 
	help="extra options for an action",
	required=False,
	default=''
)
args = argsParser.parse_args()

config = ConfigFile(args.config).read()
if args.target == 'all':
	targets = config.allTargets()
else:
	if config.hasTarget(args.target):
		targets = [args.target]
	else:
		raise Exception(
			"the target is not found: %s (there are only %s)" % (args.target, config.allTargets())
		)

for target in targets:
	DockerComposeShellCommand(
		config.targetFile(target),
		Command(args.action),
		args.extra_options
	).execute()
