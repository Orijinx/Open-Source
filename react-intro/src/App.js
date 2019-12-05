import React from 'react';
import logo from './logo.svg';
import './App.css';
import './css_src/style.css'
import './js_src/main.js'

function ActionLink() {

  function append(form) {
    if (form.input.value) {
      var newItem = document.createElement("LI");
      newItem.appendChild(document.createTextNode(form.input.value));
      document.getElementById("myUL").appendChild(newItem);
    }
  }

  function replace(form) {
    if (form.input.value) {
      var newItem = document.createElement("LI");
      var lastChild = document.getElementById("myUL").lastChild;
      newItem.appendChild(document.createTextNode(form.input.value));
      document.getElementById("myUL").replaceChild(newItem, lastChild);
    }
  }

  function restore() {
    var oneChild;
    var mainObj = document.getElementById("myUL");
    while (mainObj.childNodes.length > 2) {
      oneChild = mainObj.lastChild;
      mainObj.removeChild(oneChild);
    }
  }
}

const Greetings = (props) => <div>Hey you! {props.firstName} {props.lastName}!</div>;
const Zal = (props) => <div>Ну кароче это залупа залупная в {props.num} степени!</div>
function App() {
  return (
    <div>
      <div className="logo">
        NEWS
      </div>
      <div className="FlC">
      </div>
      <Greetings firstName="Владос" lastName="Пиздос" />
      <Zal num="4" />
    </div>
  );
}

export default App;
