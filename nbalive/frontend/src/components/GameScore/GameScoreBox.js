import React from 'react';

import away from '../../logo/TOR_logo.svg'
import home from '../../logo/GSW_logo.svg'

import styles from './GameScoreBox.module.css';

const GameScoreBox = ({gameData, scoreData}) => {

  console.log(gameData);

  return (
    <div className={styles.GameScoreBox}>
      <div className={styles.GameScoreSummary}>
        <span className={styles.TeamName}>{scoreData.away_team_name}</span>
        <div className={styles.GameScoreLogo}>
          <img src={away} style={{width: '10rem'}}/> <span>{gameData.score_away}</span>
        </div>
        <span styles={styles.Final}>FINAL</span>
        <div className={styles.GameScoreLogo}>
          <img src={home} style={{width: '10rem'}}/> <span>{gameData.score_home}</span>
        </div>
        <span className={styles.TeamName}>{scoreData.home_team_name}</span>
      </div>
    </div>
  );
};

export default GameScoreBox;