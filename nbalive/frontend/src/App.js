import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import _ from 'lodash'

import BoxScoreLoader from './components/BoxScore/BoxScoreLoader';

class App extends Component {
  state = {
    gameData: {},
    score1: 0,
    score2: 0,
    loading: 1,
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/boxscore/1')
      .then(res => {
        const gameData = res.data;
        this.setState({gameData});
        this.setState({loading: 0})
      })
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
    if(this.state.loading) {
      return <div>Loading</div>
    }
    return (
      <div className="App">
        <BoxScoreLoader gameData={this.state.gameData}/>
      </div>
    );
  }
}

export default App;
