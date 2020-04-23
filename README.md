# Cisco IOx Applications

List of Cisco IOx sample applications with source code to be used as a template to build your own applications.
All those examples are provided for educational use only.

For the Cisco IOx documentation please refer to [Cisco DevNet for IOx](https://developer.cisco.com/docs/iox/)

## For Cisco IR829 and IR809 (x86 based):

* [iox-x86-hello-world](https://github.com/etychon/iox-x86-hello-world)
Compact IOx application build on a small rootfs with a C-compiled "hello world" example that generate logs. Pefect to get started or as a sample IOx application to test IOx.

* [ubuntu-IOx-x86](https://github.com/etychon/ubuntu-IOx-x86)
Ubuntu Docker image running as a container. It includes SSH, Python 3 and Microsoft Azure SDK. It builds large IOx applications that are typically not recomended in production.

* [iox-x86-secure-storage-demo](https://github.com/etychon/iox-x86-secure-storage-demo)
IOx application build for IR8x9 and IC3000 to use [Cisco IOx Secure Storage API](https://developer.cisco.com/docs/iox/#!secure-storage-service-and-api) to securely store and retrieve sentitive information.

* [iox-signed-app-ir8x9](https://github.com/etychon/iox-signed-app-ir8x9)
Showcase how to generate third-party signed IOx applications, and how to make your gateway to only accept applications signed by your organisation.

## For Cisco IE1101 and IE3400 (ARM based):

* [iox-aarch64-hello-world](https://github.com/etychon/iox-aarch64-hello-world)
Compact IOx application build on a small rootfs with a C-compiled "hello world" example that generate logs. Pefect to get started or as a sample IOx application to test IOx.

* [iox-dumpenvvariables-aarch64](https://github.com/etychon/iox-dumpenvvariables-aarch64)
Cisco IOx application dealing with bootstapping and environment variables, more specifically to demonstrate the use of package_config.ini to configure additional parameters (such as a key, or a URL) from the IOx Management application. 


* [iox-ir1101-modbustcp-br-py](https://github.com/etychon/iox-ir1101-modbustcp-br-py)
Cisco IOx application example to use Modbus TCP on a Cisco IR1101 with Python, this example uses a B&R PLC but it can serve as a starting point to build anything with Python on the top of a compact Alpine linux image.

* [iox-ir1101-dotnet-sample](https://github.com/etychon/iox-ir1101-dotnet-sample) 
Sample IOx application based on Microsoft .NET Core SDK for ARM

* [iox-ir1101-dio-read](https://github.com/etychon/iox-ir1101-dio-read)
Read digital-IO (Alarm) port status on Cisco IR1101 using Cisco IOx with Python

## Multi-Architecture

* [iox-multiarch-nginx-nyancat-sample](https://github.com/etychon/iox-multiarch-nginx-nyancat-sample)
Show a way to build and package IOx applications for both x86 and ARM from the same Dockerfile. In this case this creates a webserver showing a running Nyan cat. 
