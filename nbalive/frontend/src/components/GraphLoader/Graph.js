import React, { Component } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, BarChart, Bar, Tooltip } from 'recharts';

import styles from './Graph.module.css';

class Graph extends Component {

  state = {
    type: 'line'
  }

  transformDataTeam = (subject='team', team='a_') => {
    let data = [];
    let keys = Object.keys(this.props.gameData).filter(obj => {
      return obj.indexOf(team) == 0;
    })

    keys.forEach(ele => {
      data.push(this.props.gameData[ele].players.player)
    })

    console.log(data);
    let index = data[0].findIndex(o => o.name === "Total")
    let data2 = data.map((obj, i) => {
      let modObj = obj[index]
      let quarter = 'Q' + (i + 1)
      modObj['Quarter'] = quarter
      return modObj
    })
    console.log(data2);

    return data2;
  }

  render() {
    console.log(this.props);
    const data = this.transformDataTeam();
    console.log(data);
    return (
      <div className={styles.graph}>
        <BarChart width={300} height={200} data={data}>
          <Bar type="monotone" dataKey={"pts"} fill="#8884d8" />
          <XAxis dataKey="Quarter" />
          <YAxis />
          <Tooltip />
        </BarChart>
      </div>
    );
  }
}

export default Graph;