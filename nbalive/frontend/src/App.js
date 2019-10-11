import React, { Component,  useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

import BoxScoreLoader from './components/BoxScore/BoxScoreLoader';
import GraphLoader from './components/GraphLoader/GraphLoader';
import GameScoreBox from './components/GameScore/GameScoreBox';

function App() {

  const [gameData, setData] = useState({})
  const [scoreData, setScore] = useState({})
  const [loading, setLoading] = useState(1)

  const getData = async () => {
    const res = await axios.get('http://localhost:8000/api/boxscore/1')
      const gameData = res.data;
      setData(gameData);
      setLoading(0)
  }

  const getScore = async () => {
    const res = await axios.get('http://localhost:8000/api/game/1')
    const scoreData = res.data;
    setScore(scoreData);
  }

  useEffect( () => {
    getData()
    getScore()
  }, [])

  if(loading) {
    return <div>Loading</div>
  }
  return (
    <div className="App">
      <GameScoreBox gameData={gameData} scoreData={scoreData}/>
      <BoxScoreLoader gameData={gameData}/>
      <GraphLoader gameData={gameData}/>
    </div>
  );
}

export default App;
