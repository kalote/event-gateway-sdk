# Event Gateway Python SDK

Python library for interacting with the [Event Gateway](https://github.com/serverless/event-gateway).

## Contents

- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Constructor](#constructor)
- [Available Functions](#available-functions)
- [Contributing](#contributing)

## Background

This is the Python SDK for interacting with the [Event Gateway](https://github.com/serverless/event-gateway), the hub for connecting events to serverless functions.

## Installation

TBD

## Usage

Use the `emit` command to emit a [CloudEvent](https://github.com/cloudevents/spec) payload to your Event Gateway. The event will be received by any function that is subscribed to your event.

```python
import eventgateway from eventgateway

eg = eventgateway.EventGateway()
cloudEvent = {
    "eventType": "user.created",
    "cloudEventsVersion": "0.1",
    "source": "/services/users",
    "data": {
        "userId": "foo",
        "userName": "bar"
    }
}
eg.emit(cloudEvent=configData, path="/user/send-mail-user")
```

The `emit()` function takes three arguments: 
- an `event` which is a valid CloudEvent,
- a `path` which is the path associated to the function (default: `/`)
- a `headers` object that represents the headers sent to the gateway (default: `{"Content-type": "application/json"}`)

The function returns a request object. If your event has a `sync` subscription attached, the `fetch` response will have the status code and body from the subscription. If not, the response will return a `202 Accepted` status code with an empty body.

## Constructor

In the example above, we created an Event Gateway client using the application URL from the [hosted Event Gateway](https://dashboard.serverless.com/) provided by Serverless, Inc. 

You can also use the Event Gateway SDK with your own, self-hosted Event Gateway. Constructor details are listed below.

**Parameters**

- `url` - `string` - optional, Events API URL, default: `http://localhost`
- `space` - `string` - optional, space name, default: `default`
- `adminPort` - `int` - optional, port for configuration, default: `4001`
- `clientPort` - `int` - optional, port for calling the event gateway, default: `4000`

**Example**

```python
import eventgateway from eventgateway

eg = eventgateway.EventGateway(url="https://mytenant-myapp.slsgateway.com", space="user")
```

## Available Functions

### checkConnection

Used to check the connectivity to the Event Gateway (using the `/v1/status` endpoint).

**Example**

```python
import eventgateway from eventgateway

eg = eventgateway.EventGateway()
if eg.checkConnection():
    print("Connection succesfull")
else:
    print("Issue while connecting")
```

### printConfig

Utility to print the current configuration.

**Example**

```python
import eventgateway from eventgateway

eg = eventgateway.EventGateway()
eg.printConfig()
```

### createEventType

Function to create an event type.

**Example**

```python
import eventgateway from eventgateway

eventtype = {
    "name": "http.request"
}
eg = eventgateway.EventGateway()
eg.createEventType(eventtype)
```

### createFunction

Function to create a function trigger.

**Example**

```python
import eventgateway from eventgateway

function = {
    "functionId": "new-user",
    "type": "http",
    "provider":{
        "url": "http://myapp.com/user/new"
    }
}
eg = eventgateway.EventGateway()
eg.createFunction(function)
```

### createSubscription

Function to subscribe to a function.

**Example**

```python
import eventgateway from eventgateway

subscription = {
    "functionId": "new-user",
    "event": "http",
    "method": "POST",
    "path": "/user/new",
    "eventType": "http.request",
    "type": "async"
}
eg = eventgateway.EventGateway()
eg.createSubscription(subscription)
```

## Contribute

TBD
