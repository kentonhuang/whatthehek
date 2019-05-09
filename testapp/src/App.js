import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import Comp from './Comp';

class App extends Component {

  state = {
    arr: [],
    score1: 0,
    score2: 0,
  }

  chooseRandom = () => {
    let array = ['Bob scores 2 points', 'Jack scores 3 points', 'Eric dunks for 2']
    const randNum = Math.floor(Math.random() * array.length);
    let temp = this.state.arr
    console.log(randNum);
    temp.push(array[randNum]);
    this.setState({arr: temp})
  }

  mapArr = () => {
    let jsx = this.state.arr.map((ele, i) => {
      return <li key={i}>{ele}</li>
    }).reverse()
    return jsx;
  }

  ButtonHandler = () => {
    
  }

  scoreHandler = () => {
    let score1 = this.state.score1;
    score1++;
    this.setState({score1})
  }

  scoreHandler2 = () => {
    let score2 = this.state.score2;
    score2++;
    this.setState({ score2 })
  }  
  
  scoreHandler = () => {
    let score1 = this.state.score1;
    score1++;
    this.setState({score1})
  }

  scoreHandler2 = () => {
    let score2 = this.state.score2;
    score2++;
    this.setState({ score2 })
  }

  render() {
    console.log(this.state.arr);
    return (
      <div className="App">
        <ul className="li">
          {this.mapArr()}
        </ul>
        <button onClick={this.chooseRandom}>Hey</button>

        <div className="score">
          <span className="score1">{this.state.score1}</span>
          -
          <span className="score2">{this.state.score2}</span>
        </div>
        <div>
          <button onClick={this.scoreHandler}>Score1</button>
          <button onClick={this.scoreHandler2}>Score2</button>
        </div>


      </div>
    );
  }

}

export default App;
