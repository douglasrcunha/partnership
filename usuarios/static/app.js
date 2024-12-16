  import { initializeApp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";
  import { getFirestore, collection, getDocs } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-firestore.js";


  const firebaseConfig = {
    apiKey: "AIzaSyAAuZZUGgfi3Iq_VSbPuR8dxUcfA3LyN1g",
    authDomain: "partnership-b4115.firebaseapp.com",
    projectId: "partnership-b4115",
    storageBucket: "partnership-b4115.firebasestorage.app",
    messagingSenderId: "755300264267",
    appId: "1:755300264267:web:1c5c248769c7343f2f60ce",
    measurementId: "G-9S70HFEGKP"
  };

  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app)

  getDocs (collection(db, 'partnership' ))
    .then(querySnapshot => {
      const partnerslis = querySnapshot.docs.reduce((acc, doc) => { acc += 
        `<li>${doc.data().title}</li>`
        return acc
    }, '')
      console.log(partnerslis)
    }) 
    .catch(console.log)

    formAddUser.addEventListener('submit', e => {
      e.preventDefault()
      console.log(e.target.nome.value, e.target.senha.value)
    })