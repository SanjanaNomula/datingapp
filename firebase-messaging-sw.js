importScripts('https://www.gstatic.com/firebasejs/10.11.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.11.0/firebase-messaging-compat.js');

firebase.initializeApp({
    apiKey: "AIzaSyDNiJROEM1-oa2kidoUorjFPS4FvP_et0M",
    authDomain: "datingapp-636fa.firebaseapp.com",
    projectId: "datingapp-636fa",
    storageBucket: "datingapp-636fa.firebasestorage.app",
    messagingSenderId: "848138254029",
    appId: "1:848138254029:web:db606ec479cc1220805b84",
    measurementId: "G-VVG7199H45"
});

const messaging = firebase.messaging();
