 
import React from 'react';
import ReactDOM from 'react-dom';
import ThreatList from './components/ThreatList';

function App() {
   return (
       <div>
           <h1>Threat Intelligence Dashboard</h1>
           <ThreatList />
       </div>
   );
}

ReactDOM.render(<App />, document.getElementById('root'));