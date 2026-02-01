<!DOCTYPE html>
<html>
<head>
    <title>Alert Button</title>
    <style>
        button {

          padding: 15px 30px;
          font-size: 18px;
          background-color: 18px;
          color: white;
          border: none;
          border-radius: 8px;
          cursor: pointer;
        }   
    </style>
</head>
<body>
    <h1>Click the button!</h1>
    <button id='alertBtn'>Show Alert</button>
    
    <script>
        let button = document.getElementById('alertBtn');
        button.addEventListener('clcik', function() {
            alert('Button clicked!');
        });