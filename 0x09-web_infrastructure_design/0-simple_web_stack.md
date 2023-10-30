# Simple Web Stack

## Description

This is a simple web infrastructure that hosts a website that is reachable via `www.foobar.com`. There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.

## Specifics About This Infrastructure

+ A server is a piece of computer hardware/software that provides functionality for other programs or devices, called "clients".

+ The DNS(Domain Name Server) is used to translate domain names into a specific IP address so that the clients can load the requested Internet resources from the specific IP address.

+ The type of DNS record www.foobar.com uses is called an A record. This can be checked by running dig www.foobar.com.

+ The web server is a software/hardware that accepts requests via HTTP or the secure version of the HTTP (HTTPS) and responds with the content requested or an error messsage.

+ The application server is a server that is used to install, operate, manage, and host user's business logic while facilitating access to and performance of the business application.
  
+ The role of the database.<br/>To maintain a collection of organized information that can easily be accessed, managed and updated

+ What the server uses to communicate with the client (computer of the user requesting the website).<br/>Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

## Issues With This Infrastructure

+ There are SPOFs (Single Point Of Failure) in this infrastructure.<br/>For example, if the Application Server or the MySQL database is down, the entire connection would be down.

+ Cannot scale if there's too much incoming traffic.<br/>It would be hard to scale this infrastructure becauses one server contains the required components. The server can quickly run out of resources or slow down when it starts receiving a lot of requests.
  
+ The is little to no network security. There is no Firewall, no monitoring and no SSL certificates.  

+ Downtime when maintenance needed.<br/>When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.

