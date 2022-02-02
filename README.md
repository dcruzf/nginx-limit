# NGNIX _rate-limiting_

This repository includes some NGINX configuration of rate limiting for fastapi endpoints.

## Discursion

If anyone can use your API as much as they want, then you can have overloaded servers by
abusive rapid requests, or even suffer a brute-force attack.

There are many reasons to limit the rate of request, one being security.
Maybe you need to protect your APIs from inadvertent overuse, too. Without rate
limiting, each user may make a request as often as they like,
leading to “spikes” of requests that starve other consumers.

**Rate limit** allows you to limit the number of requests that a user can make in a
given period of time. It protects your API from inadvertent or malicious
overuse by limiting how often each user can call the API.

One of the most useful features of NGINX is rate-limiting.

## Basic configuration
