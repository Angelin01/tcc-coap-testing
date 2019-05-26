# tcc-coap-testing
Project for basic testing of the CoAP protocol for data transmission

---
## Results
Tests were done by monitoring the loopback interface on the Raspberry Pi.
Tests could not be performed on Windows due to a missing implementation regarding IPv6 on Windows.  
Both confirmable and non-confirmable messages were tested. The results show how many bytes were
transmitted between the server and client on a simple POST request.

| Message Size | Size Confirmable | Size Non Confirmable |
|:---:|:---:|:---:|
0| 137| 137
1| 139| 139
10| 148| 148
100| 238| 238
1000| 1138| 1138
10000| 11440‬| 11440

The overhead for empty messages appears to be 137 bytes, including the URI.
Notably, both messages have the same size. This is probably due to the fact that whether the server
responds or not is up to the resource implementation, so even if the message is non confirmable the
server may still answer. This will have a difference on poor network conditions, which are not tested
here.

---
## Conclusion
There is a considerable overhead even using UDP, although there is a good chance it won't grow too
much on poor network conditions. Even then, non confirmable messages should not be used due to the
fire and forget nature.  
CoAP appears to be less supported than MQTT and slightly harder to use, at least for the Python
implementations. The lack of IPv6 support on Windows may present an issue in the future, which
should be taken into account.
