import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import axios from 'axios';

const App = () => {
    const [threats, setThreats] = useState([]);
    const [description, setDescription] = useState('');
    const [threatType, setThreatType] = useState('');
    const [reporter, setReporter] = useState('');

    useEffect(() => {
        loadThreats();
    }, []);

    const loadThreats = async () => {
        const result = await axios.get('/get_threats');
        setThreats(result.data);
    };

    const addThreat = async () => {
        const data = {
            threatType,
            description,
            reporter
        };
        await axios.post('/add_threat', data);
        loadThreats();
    };

    return (
        <div>
            <h1>Decentralized Threat Intelligence Platform</h1>
            <div>
                <input
                    type="text"
                    placeholder="Threat Type"
                    value={threatType}
                    onChange={(e) => setThreatType(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Reporter"
                    value={reporter}
                    onChange={(e) => setReporter(e.target.value)}
                />
                <button onClick={addThreat}>Add Threat</button>
            </div>
            <div>
                <h2>Threats</h2>
                <ul>
                    {threats.map((threat, index) => (
                        <li key={index}>
                            {threat.threatType} - {threat.description} - {threat.reporter} - {new Date(threat.timestamp * 1000).toLocaleString()}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default App;
