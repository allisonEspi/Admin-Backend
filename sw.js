var CACHE_NAME = 'turistview-v1';
var urlsToCache = [
    '/',
    '/staticfiles/css/styles.css',
    '/staticfiles/images/logo_negro.png',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});


//solo para cachear todo reemplazar por esta versión del Fetch


self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
     
    );
});
//codigo para notificaciones push
importScripts('https://www.gstatic.com/firebasejs/7.20.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.20.0/firebase-messaging.js');
var firebaseConfig = {
    apiKey: "AIzaSyDrgbMlUhQtWO00ksVYJfL8mQj2pOs6eSE",
    authDomain: "loginturistview.firebaseapp.com",
    databaseURL: "https://loginturistview.firebaseio.com",
    projectId: "loginturistview",
    storageBucket: "loginturistview.appspot.com",
    messagingSenderId: "963572973633",
    appId: "1:963572973633:web:6699aa8f0b6632f8e206c0",
    measurementId: "G-4LWMSYFGLK"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
let messaging=firebase.messaging();
messaging.setBackgroundMessageHandler(function(payload){
    let title='titulo de la notificacion '
    let options={
        body:"este es el mensaje"
    }
    self.registration.showNotification(title,options)
});