import React, { Component, useState } from 'react';
import "react-table/react-table.css";
import _ from 'lodash'

import BoxScore from './BoxScore';

import styles from './BoxScore.module.css';

const BoxScoreLoader = ({gameData}) => {

  const [value, setValue] = useState('end')
  const [boxViewA, setBoxViewA] = useState('away')
  const [boxViewH, setBoxViewH] = useState('home')

  const chooseBox = (info) => {
    return gameData[info].players.player
  }

  const handleChange = (event) => {
    setValue(event.target.value)
    if(event.target.value === 'end') {
      setBoxViewA('away')
      setBoxViewH('home')
    }

    else {
      setBoxViewA('a_' + event.target.value)
      setBoxViewH('h_' + event.target.value)
    }
  }

  const away = chooseBox(boxViewA)
  const home = chooseBox(boxViewH)

  if (_.isEmpty(gameData)){
    return <div>Loading</div>
  }
  return (
    
    <div className={styles.BoxScore}>
      <BoxScore gameData={away}/>
      <br></br>
      <BoxScore gameData={home}/>
      <select value={value} onChange={handleChange}>
        <option value="end">End Game</option>
        <option value="q1">Quarter 1</option>
        <option value="q2">Quarter 2</option>
        <option value="q3">Quarter 3</option>
        <option value="q4">Quarter 4</option>
      </select>
      <button>Quarter</button>
    </div>
  );
}

export default BoxScoreLoader;