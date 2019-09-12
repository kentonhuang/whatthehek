import React, { Component } from 'react';
import "react-table/react-table.css";
import _ from 'lodash'

import BoxScore from './BoxScore';

import styles from './BoxScore.module.css';

class BoxScoreLoader extends Component {

  state = {
    value: 'end',
    boxViewA: 'away',
    boxViewH: 'home'
  }

  chooseBox = (info) => {
    return this.props.gameData[info].players.player
  }

  handleChange = (event) => {
    this.setState({value: event.target.value})
    if(event.target.value === 'end') {
      this.setState({boxViewA: 'away'})
      this.setState({boxViewH: 'home'})
    }

    else {
      this.setState({boxViewA: 'a_' + event.target.value})
      this.setState({boxViewH: 'h_' + event.target.value})
    }
  }

  render() {
    console.log(this.props);
    const away = this.chooseBox(this.state.boxViewA)
    const home = this.chooseBox(this.state.boxViewH)

    if (_.isEmpty(this.props.gameData)){
      return <div>Loading</div>
    }
    return (
      
      <div className={styles.BoxScore}>
        <BoxScore gameData={away}/>
        <br></br>
        <BoxScore gameData={home}/>
        <select value={this.state.value} onChange={this.handleChange}>
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
}

export default BoxScoreLoader;