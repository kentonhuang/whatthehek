import React, { useState } from 'react';

import Graph from './Graph';

import styles from './GraphLoader.module.css';

function GraphLoader({gameData}) {
  const [graphs, setGraphs] = useState(['graph'])

  const mapGraphs = () => {
    return graphs.map((graph, index) => {
      return <Graph index={index} key={index} type={graph} gameData={gameData} removeGraph={removeGraph}/>
    })
  }

  const removeGraph = (key) => {
    let graphsTemp = [...graphs];
    console.log(key);
    graphsTemp.splice(key, 1);
    setGraphs(graphsTemp)
  }

  const addGraphButton = () => {
    let graphsTemp = [...graphs];
    graphsTemp.push('graph' + graphsTemp.length);
    setGraphs(graphsTemp)
  }

  return (
    <div className={styles.GraphLoader}>
      <div>
        {mapGraphs()}
      </div>
      <div>
        <button onClick={addGraphButton}>Add Graph</button>
      </div>
    </div>
  );
}

export default GraphLoader;