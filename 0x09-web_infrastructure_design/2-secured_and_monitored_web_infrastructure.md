# Secured and Monitored Web Infrastructure

## Description

This is a web infrastructure that is secured, monitored and serves encrypted traffic. It uses the combination of technical and administrative measures that are put in place to ensure the security and reliability of a website or web-based application

## Specifics About This Infrastructure

+ The purpose of the firewalls.<br/>The firewall is used to protect the network (web servers, anyway) from unauthorized computers by acting as an intermediary between the internal network and the external network and blocking incoming traffic. 

+ The purpose of the SSL certificate.<br/>The SSL certificate is for encrypting the traffic between the web servers and the external network to prevent man-in-the-middle attacks (MITM) and network sniffers from sniffing the traffic which could expose valuable information. The SSL certs ensure privacy, integrity, and identification. When a web browser contacts a secured website, the SSL certificate enables an encrypted connection

+ The purpose of the monitoring clients.<br/>The monitoring clients are for monitoring the servers and the external network. This is to make sure websites and web servers are always available. The monitoring tools observe the servers and provide key metrics about the servers' operations to the administrators.

## Issues With This Infrastructure

+ Terminating SSL at the load balancer level decreases security as the traffic between the load balancer and the web servers would be unencrypted.

+ A single MySQL server is not scalable and can act as a single point of failure for the web infrastructure in a network.

+ Having servers with all the same components would make the components contend for resources on the server like CPU, Memory, I/O, etc., which can lead to poor performance and also make it difficult to locate the source of the problem. A setup such as this is not easily scalable. 
