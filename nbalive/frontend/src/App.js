import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    score1: 0,
    score2: 0,
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
    return (
      <div className="App">
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
