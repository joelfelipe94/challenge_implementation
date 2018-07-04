# Introduction
This solution is intended to show some programming related skills, such as, english proficency, the capacity to learn quickly new technologies and so forth. The basic idea behind this solution is to implement a simple application using Flask and Python (see Figure). This application is responsable to interact with the databases while serves the user. 

The connections beetween the aplication an the databases A and B are both encrypted, since these databases contain sensitive data. On the other hand, as the database C does not have sensitive data, and should be acessed as quicky as possible, its connection is no encrypted.

![Alt text](blob/diagrama_desafio.jpg?raw=true "Solution Overview")

# Databases A and B Configuration
Since the porposed solution uses MySQL, in order to enable encrypted connections we must configure the appropriate certificate and key files in both client and server side.

## Server-Side
 On the server side we must set the certificate and key files the server uses to establish encrypted connections. This can be made in `my.cnf` file as shown bellow:
```
[mysqld]
ssl-ca=ca.pem
ssl-cert=server-cert.pem
ssl-key=server-key.pem
```
Where `ssl-ca` stands for the path to Certificate Authority (CA) certificate file, `ssl-cert` the path to the server public key certificate file and `ssl-key` the path to the name of the server private key file.

## Client-Side 
The database A connection must be as secure as possible. So, a certificate will be required from the client made on the server side. But, the dataset B connection will not require a certificate from the client. 
### Database A
To require that a client certificate is also specified, the user account must be created using the REQUIRE X509 option. The client must also specify `ssl-ca`, `ssl-cert` and `ssl-key` on the connection as shown bellow: 
``` shelScript
mysql --ssl-ca=ca.pem \
      --ssl-cert=client-cert.pem \
      --ssl-key=client-key.pem
```
### Database B
To require this connection to be encrypted the user account must be created using the REQUIRE SSL option. On the connection the client must specify `ssl-ca` as shown bellow: 
``` shelScript
mysql --ssl-ca=ca.pem
```

# Python Application
This python application offers the client a connetion using HTTPs protocol. The certificates ware self-generate to this test and can be found in the `certificate` folder. In pactice it should be certified by a CA. 

In this application the user can acess the database information through some urls. Each url is responsable to acess a single database. To acess resource from databases A and B the user must authenticate.

# Author Comments
I would like to apologise for the poor quality of my solution. This result is due to two reasons: First, I do not know most of the listed technologies; Second, my throat is inflamed and I am having fever from time to time. Althought, I would not quit without give it a try.
Thanks for the oportunity.
