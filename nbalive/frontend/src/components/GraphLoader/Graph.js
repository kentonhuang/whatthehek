import React, { useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, BarChart, Bar, Tooltip, Label, LabelList } from 'recharts';

import styles from './Graph.module.css';

const map = new Map();
  map.set('pts', 'Points')
  map.set('reb', 'Rebounds')
  map.set('ast', 'Assists')
  map.set('stl', 'Steals')
  map.set('blk', 'Blocks')

function Graph({index, type, gameData, removeGraph}){

  const [graphType, setGraphType] = useState('line')
  const [team, setTeam] = useState('a_')
  const [combine_team, setCombine] = useState(false)
  const [stat, setStat] = useState(['pts'])
  const [component, setComponent] = useState([Bar])
  const [addStat, setAddStat] = useState([])
  const [selected, setSelected] = useState('pts')

  const transformDataTeam = (subject='team', team='a_') => {
    let data = [];
    let keys = Object.keys(gameData).filter(obj => {
      return obj.indexOf(team) === 0;
    })

    keys.forEach(ele => {
      data.push(gameData[ele].players.player)
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

  const statRender = () => {
    const GraphType = component[0];

    let render = stat.map((stat, index) => {
      return (
        <GraphType key={index} type="monotone" dataKey={stat} fill="#8884d8">
          <LabelList dataKey={stat} position="top" />
        </GraphType>
        )
    })
    return render;
  }

  const toggleTeam = (e) => {
    if(team === 'a_') {
      setTeam('h_')
    }
    else {
      setTeam('a_')
    } 
  }

  const statSelect = () => {
    let stats = [...stat]
    stats.push(selected);
    console.log(stats);
    setStat(stats)
    console.log(stats);
  }

  const removeStat = (event) => {
    let stats = [...stat];
    stats.splice(event.target.getAttribute('index'), 1);
    setStat(stats)
  }

  const mapGraphType = () => {
    return stat.map((ele, index) => {
      let mapStat = map.get(ele);
      return <span index={index} type={ele} key={index} className={styles.typeDisplay} onClick={removeStat}>{mapStat}</span>
    })
  }

  console.log(index);
  const data = transformDataTeam('team', team);
  return (
    <div className={styles.graph}>
      <div className={styles.topBar}>
        <button onClick={toggleTeam}>Team</button>
        <select value={selected} onChange={(e) => setSelected(e.target.value)}>
          <option value="pts">Points</option>
          <option value="reb">Rebounds</option>
          <option value="ast">Assists</option>
          <option value="stl">Steals</option>
          <option value="blk">Blocks</option>
        </select>
        <button onClick={statSelect}>Add Stat</button>
        <button onClick={() => removeGraph(index)}>Remove Graph</button>
      </div>
      <div className={styles.graphBar}>
        {mapGraphType()}
      </div>
      <BarChart width={400} height={250} data={data}>
        {statRender()}
        <XAxis dataKey="Quarter" >
          <Label value={map.get(stat[0]) +'Per Quarter'} offset={0} position="insideBottom" />
        </XAxis>
        <YAxis width={20}/>
        <Tooltip />
      </BarChart>
    </div>
  );
}

export default Graph;