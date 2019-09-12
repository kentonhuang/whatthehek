import React, { Component } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, BarChart, Bar, Tooltip, Label, LabelList } from 'recharts';

import styles from './Graph.module.css';

class Graph extends Component {

  state = {
    type: 'line',
    team: 'a_',
    combine_team: false,
    stat: ['pts'],
    component: Bar
  }

  transformDataTeam = (subject='team', team='a_') => {
    let data = [];
    let keys = Object.keys(this.props.gameData).filter(obj => {
      return obj.indexOf(team) == 0;
    })

    keys.forEach(ele => {
      data.push(this.props.gameData[ele].players.player)
    })

    let index = data[0].findIndex(o => o.name === "Total")
    let data2 = data.map((obj, i) => {
      let modObj = obj[index]
      let quarter = 'Q' + (i + 1)
      modObj['Quarter'] = quarter
      return modObj
    })

    return data2;
  }

  statRender = (event) => {
    const GraphType = this.state.component;

    let render = this.state.stat.map((stat, index) => {
      console.log(stat);
      return (
        <GraphType type="monotone" dataKey={stat} fill="#8884d8">
          <LabelList dataKey={stat} position="top" />
        </GraphType>
        )
    })
    console.log(render);
    return render;
  }

  toggleTeam = (e) => {
    if(this.state.team === 'a_') {
      this.setState({team: 'h_'})
    }
    else {
      this.setState({team: 'a_'})
    } 
  }

  statSelect = (event) => {
    let stat = []
    stat.push(event.target.value);
    this.setState({stat})
  }

  render() {
    const map = new Map();
    map.set('pts', 'Points')
    map.set('reb', 'Rebounds')
    map.set('ast', 'Assists')
    map.set('stl', 'Steals')
    map.set('blk', 'Blocks')
    const data = this.transformDataTeam('team', this.state.team);
    const data2 = this.transformDataTeam('team', this.state.team);
    console.log(data);
    return (
      <div className={styles.graph}>
        <button onClick={this.toggleTeam}>Team</button>
          <select value={this.state.value} onChange={this.statSelect}>
            <option value="pts">Points</option>
            <option value="reb">Rebounds</option>
            <option value="ast">Assists</option>
            <option value="stl">Steals</option>
            <option value="blk">Blocks</option>
          </select>
        <BarChart width={300} height={200} data={data}>
          {this.statRender()}
          <XAxis dataKey="Quarter" >
            <Label value={map.get(this.state.stat[0]) +' '+ 'Per Quarter'} offset={0} position="insideBottom" />
          </XAxis>
          <YAxis />
          <Tooltip />
        </BarChart>
      </div>
    );
  }
}

export default Graph;