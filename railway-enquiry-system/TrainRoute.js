import React, { useState } from 'react';
import axios from 'axios';

const TrainRoute = () => {
    const [trainNumber, setTrainNumber] = useState('');
    const [routeData, setRouteData] = useState(null);

    const handleSearch = async () => {
        const response = await axios.get(`http://127.0.0.1:8000/api/train_route/${trainNumber}/`);
        setRouteData(response.data);
    };

    return (
        <div>
            <h2>Train Route</h2>
            <input
                type="text"
                value={trainNumber}
                onChange={(e) => setTrainNumber(e.target.value)}
                placeholder="Enter Train Number"
            />
            <button onClick={handleSearch}>Search</button>
            {routeData && (
                <div>
                    <h3>Train Route</h3>
                    <pre>{JSON.stringify(routeData, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default TrainRoute;
