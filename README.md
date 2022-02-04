# NGNIX _rate-limiting_

This repository includes some NGINX configuration of rate limiting for _FastAPI_ endpoints.

## Discursion

If anyone can use your API as much as they want, then you can have overloaded servers by
abusive rapid requests, or even suffer a brute-force attack.

There are many reasons to limit the rate of request, one being security.
But maybe you need to protect your APIs from inadvertent overuse. Without rate
limiting, each user may make a request as often as they like,
leading to “spikes” of requests that starve other consumers.

**Rate limit** allows you to limit the number of requests that a user can make in a
given period. It protects your API from inadvertent or malicious
overuse by limiting how often each user can call the API.

One of the most useful features of NGINX is rate-limiting.

## Basic configuration

There are two main directives, `limit_req_zone` and `limit_req`.

### `limit_req_zone`

The first directive is `limit_req_zone`, it defines the parameters for rate limiting.

> `Syntax: limit_req_zone key zone=name:size rate=rate;`

The `key` is the request characteristic against which the limit is applied,
`zone` defines the shared memory zone used to store the state of each `key`,
and `rate` is the maximum request rate. In the `zone`, `name` is the identification of the zone and `size` is the storage size.

Example:

> `limit_req_zone $binary_remote_addr zone=ip_1:10m rate=1r/s;`

The key is `$binary_remote_addr`, the binary representation remote ip address,the name of the `zone` is `ip_1` the memory is `10m`, 10 megabytes, and the `rate` is one request per second. This rate will be applied to every request with the same ip address.

### `limit_req`

The second directive is `limit_req`, it sets the parameters for rate limiting and the shared memory zone.

> Syntax: `limit_req zone=name [burst=number] [nodelay | delay=number];`

It can e used in the `htpp`, `server` or `location` contexts.
Example:

```
limit_req_zone $binary_remote_addr zone=ip_1:10m rate=1r/s;

server {
    location /limited/ {
            limit_req zone=ip_1;
    }
}
```
