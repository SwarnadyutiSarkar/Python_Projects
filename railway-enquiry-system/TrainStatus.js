import React, { useState } from 'react';
import axios from 'axios';

const TrainStatus = () => {
    const [trainNumber, setTrainNumber] = useState('');
    const [trainData, setTrainData] = useState(null);

    const handleSearch = async () => {
        const response = await axios.get(`http://127.0.0.1:8000/api/train_status/${trainNumber}/`);
        setTrainData(response.data);
    };

    return (
        <div>
            <h2>Train Status</h2>
            <input
                type="text"
                value={trainNumber}
                onChange={(e) => setTrainNumber(e.target.value)}
                placeholder="Enter Train Number"
            />
            <button onClick={handleSearch}>Search</button>
            {trainData && (
                <div>
                    <h3>Train Information</h3>
                    <pre>{JSON.stringify(trainData, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default TrainStatus;
