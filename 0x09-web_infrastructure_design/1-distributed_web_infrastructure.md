# Distributed Web Infrastructure

## Description

This is a distributed web infrastructure that attempts to break up the internet so that no single entity has control over all the data on it.

## Specifics About This Infrastructure

+ The load balancer distributes network traffic across multiple servers.<br/> It uses an algorithm that works by using each server behind the load balancer in turns, according to their weights. The load balancer is configured with the *Round Robin* distribution algorithm. A client request is forwarded to each server in turn. The algorithm instructs the load balancer to go back to the top of the list and repeats again.
  
+ The setup enabled by the load-balancer.<br/>The HAProxy load-balancer is enabling an *Active-Passive* setup rather than an *Active-Active* setup. In an *Active-Active* setup, the load balancer distributes workloads across all nodes in order to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an *Active-Passive* setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.
  
+ How a database *Primary-Replica* (*Master-Slave*) cluster works.<br/>A *Primary-Replica* setup configures one server to act as the *Primary* server and the other server to act as a *Replica* of the *Primary* server. However, the *Primary* server is capable of performing read/write requests whilst the *Replica* server is only capable of performing read requests. Data is synchronized between the *Primary* and *Replica* servers whenever the *Primary* server executes a write operation.
  
+ The difference between the *Primary* node and the *Replica* node in regard to the application.<br/>The *Primary* node is responsible for all the write operations the site needs whilst the *Replica* node is capable of processing read operations, which decreases the read traffic to the *Primary* node.

## Issues With This Infrastructure

+ There are SPOFs (Single Point Of Failure) in this infrastructure.
For example, if the Application Server or the MySQL database is down, the entire connection would be down.
  
+ There is little to no security.<br/>The information that travels in the network isn't encrypted through an SSL certificate. There are no firewalls so there is no of blocking unauthorized IPs since there's no firewall installed on any server. We also have no monitoring have therefore there is no way of knowing the status of each server.
