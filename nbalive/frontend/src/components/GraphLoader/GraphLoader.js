import React, { Component } from 'react';

import Graph from './Graph';

class GraphLoader extends Component {

  state = {
    graphs: ['graph']
  }

  mapGraphs = () => {
    return this.state.graphs.map((graph, index) => {
      return <Graph key={index} type={graph} gameData={this.props.gameData}/>
    })
  }

  addGraphButton = (event) => {
    let graphs = this.state.graphs;
    graphs.push('graph');
    this.setState({graphs})
  }

  render() {
    return (
      <div>
        <div>
          {this.mapGraphs()}
        </div>
        <div>
          <button onClick={this.addGraphButton}>Add Graph</button>
        </div>
      </div>
    );
  }
}

export default GraphLoader;