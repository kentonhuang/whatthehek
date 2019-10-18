import React , { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

import Comp from './Comp';

function App() {

  const [score1, setScore] = useState(0)
  const [score2, setScore2] = useState(0)
  const [arr, setArr] = useState([])

  useEffect(() => {
    const interval = setInterval(() => {

      setScore(score => score + Math.round(Math.random() * 3))
      setScore2(score => score + Math.round(Math.random() * 3))

    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const chooseRandom = () => {
    let array = ['Bob scores 2 points', 'Jack scores 3 points', 'Eric dunks for 2']
    const randNum = Math.floor(Math.random() * array.length);
    let temp = arr
    console.log(randNum);
    temp.push(array[randNum]);
    setArr(temp)
  }

  const mapArr = () => {
    let jsx = arr.map((ele, i) => {
      return <li key={i}>{ele}</li>
    }).reverse()
    return jsx;
  }

  const ButtonHandler = () => {
    
  }

  const scoreHandler = () => {
    let temp = score1;
    temp++;
    setScore(temp)
  }

  const scoreHandler2 = () => {
    let temp = score2;
    temp++;
    setScore2(temp)
  }  

  const add1 = (num) => {
    let temp = score1;
    temp = temp + num
    setScore2(temp)
  }

  const add2 = (num) => {
    let temp = score2;
    temp = temp + num
    setScore2(temp)
  }

  console.log(arr);
  return (
    <div className="App">
      <ul className="li">
        {mapArr()}
      </ul>
      <button onClick={chooseRandom}>Hey</button>

      <div className="score">
        <span className="score1">{score1}</span>
        -
        <span className="score2">{score2}</span>
      </div>
      <div>
        <button onClick={scoreHandler}>Score1</button>
        <button onClick={scoreHandler2}>Score2</button>
      </div>


    </div>
  );
}

export default App;
