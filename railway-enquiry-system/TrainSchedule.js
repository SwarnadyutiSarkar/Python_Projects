import React, { useState } from 'react';
import axios from 'axios';

const TrainSchedule = () => {
    const [trainNumber, setTrainNumber] = useState('');
    const [scheduleData, setScheduleData] = useState(null);

    const handleSearch = async () => {
        const response = await axios.get(`http://127.0.0.1:8000/api/train_schedule/${trainNumber}/`);
        setScheduleData(response.data);
    };

    return (
        <div>
            <h2>Train Schedule</h2>
            <input
                type="text"
                value={trainNumber}
                onChange={(e) => setTrainNumber(e.target.value)}
                placeholder="Enter Train Number"
            />
            <button onClick={handleSearch}>Search</button>
            {scheduleData && (
                <div>
                    <h3>Train Schedule</h3>
                    <pre>{JSON.stringify(scheduleData, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default TrainSchedule;
