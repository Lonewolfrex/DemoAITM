 
import React, { useEffect, useState } from 'react';

function ThreatList() {
   const [threats, setThreats] = useState([]);

   useEffect(() => {
       fetch('/api/threats')
           .then(response => response.json())
           .then(data => setThreats(data));
   }, []);

   return (
       <ul>
           {threats.map(threat => (
               <li key={threat.id}>{threat.description}</li>
           ))}
       </ul>
   );
}

export default ThreatList;