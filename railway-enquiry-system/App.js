import React from 'react';
import TrainStatus from './components/TrainStatus';
import TrainSchedule from './components/TrainSchedule';
import TrainRoute from './components/TrainRoute';

const App = () => {
    return (
        <div>
            <h1>Indian Railway Enquiry System</h1>
            <TrainStatus />
            <TrainSchedule />
            <TrainRoute />
        </div>
    );
};

export default App;
