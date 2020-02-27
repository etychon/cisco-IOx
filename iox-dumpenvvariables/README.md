## IOx Dump Environment Variables

This Cisco IOx application purpose is to:

a) Read the package_config.ini file from its location within the IOx
docker environment. This file can contain additional parameters for
users to configure during application deployment. Typical examples
are passwords, or IP address of an MQTT broker.

b) List all the configured environment variables on the given
platform. This will allow to see and list all the variables, some
of which might not be documented.

This container is made for Cisco IOx on ARM platforms and
more specifically for IE3400 and IR1101. It is being delivered
here for education purpose only.
