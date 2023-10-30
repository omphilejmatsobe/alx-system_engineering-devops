# Scaled Up Web Infrastructure

## Description

This web infrastructure is a scaled-up version of the simple web infrastructure. In this version, the SPOFs have been removed, the SSL protection isn't terminated at the load-balancer and each server's network is protected with a firewall and they're also monitored.

## Specifics About This Infrastructure

+ The addition of a firewall between each server.<br/>This protects each server from unauthorized users accessing the network rather than protecting a single server. This is the same with the addition of SSL.

+ Each server is monitored and this is to make sure there is no server in the network that is ignored and unmonitored. 

## Issues With This Infrastructure

+ High maintenance costs.<br/>Moving each of the major components to its own server means that more servers would be in operation and the company's electricity bill would rise along with the maintenance of the servers and other components in the network.
