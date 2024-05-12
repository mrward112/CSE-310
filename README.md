# Overview



{Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.}
{Description}
I have attached both peer to peer and server-client based programs. the peer to peer scripts allow for the server and client modules to communicate with each other by sending messages. 
Both programs simply need to be running at the same time. The server-client relationship program fetches information from the client after the client has connected to the server ip.

{Describe your purpose for writing this software.}
{Purpose}
To experiment with network server client relationships and create a working model

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}
{Youtube Link}
[Software Demo Video](https://youtu.be/B2Flq5CPyA8)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}
well, I actually ended up doing both.

{Identify if you are using TCP or UDP and what port numbers are used.}
TCP with ports 12345, 5000, 5001

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}

# Development Environment

{Describe the tools that you used to develop the software}
> The Threading module was used in the peer to peer program to allow the server and client files to handle seperate connections and make a more streamlined experience for the user.
> The Socket module allows for the programs to actually communicate over network connections.


{Describe the programming language that you used and any libraries.}
I used python as the main programming language and used the socket, platform, subprocess, and threading librarys


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](https://www.webroot.com/us/en/resources/glossary/what-is-peer-to-peer-networking)
* [Web Site Name](https://www.geeksforgeeks.org/platform-module-in-python/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* I want to keep the peer to peer connection stable without ever disconnecting
* Add the ability to send files over the peer to peer connection
* Allow the Server to control more than just simple commands on the client side