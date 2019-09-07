import React, { Component } from 'react';
import ReactTable from 'react-table';
import "react-table/react-table.css";
import _ from 'lodash'

class BoxScore extends Component {

  genTable = () => {
    return [{
        Header: 'Name',
        accessor: 'name',
        className: 'heyo',
        width: 200
      },
      {
        Header: 'MIN',
        accessor: 'min',
        minWidth: 50
      },
      {
        Header: 'FGM',
        accessor: 'fgm',
        minWidth: 50
      },
      {
        Header: 'FGA',
        accessor: 'fga',
        minWidth: 50
      },
      {
        id: 'Field Goal Percentage',
        Header: 'FG%',
        accessor: d => ((d.fgm / d.fga) * 100 || 0).toFixed(2),
        minWidth: 50
      },
      {
        Header: '3PM',
        accessor: 'tpm',
        minWidth: 50
      },
      {
        Header: '3PA',
        accessor: 'tpa',
        minWidth: 50
      },
      {
        id: 'Three Field Goal Percentage',
        Header: '3FG%',
        accessor: d => ((d.tpm / d.tpa) * 100 || 0).toFixed(2),
        minWidth: 50
      },
      {
        Header: 'FTM',
        accessor: 'ftm',
        minWidth: 50
      },
      {
        Header: 'FTA',
        accessor: 'fta',
        minWidth: 50
      },
      {
        id: 'FT Percentage',
        Header: 'FT%',
        accessor: d => ((d.ftm / d.fta) * 100 || 0).toFixed(2),
        minWidth: 50
      },
      {
        Header: 'OREB',
        accessor: 'oreb',
        minWidth: 50
      },
      {
        Header: 'DREB',
        accessor: 'dreb',
        minWidth: 50
      },
      {
        Header: 'REB',
        accessor: 'reb',
        minWidth: 50
      },
      {
        Header: 'AST',
        accessor: 'ast',
        minWidth: 50
      },
      {
        Header: 'TOV',
        accessor: 'tov',
        minWidth: 50
      },
      {
        Header: 'STL',
        accessor: 'stl',
        minWidth: 50
      },
      {
        Header: 'BLK',
        accessor: 'blk',
        minWidth: 50
      },
      {
        Header: 'PF',
        accessor: 'pf',
        minWidth: 50
      },
      {
        Header: 'PTS',
        accessor: 'pts',
        minWidth: 50
      },
      {
        Header: '+/-',
        accessor: 'pm',
        minWidth: 50
      },
    ]
  }

  render() {
    const columns = this.genTable()
    return (
      <div>
        <ReactTable 
          data={this.props.gameData}
          columns={columns}
          showPagination={false}
          minRows={0}
        />
      </div>
    );
  }
}

export default BoxScore;