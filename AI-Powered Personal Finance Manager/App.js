// src/App.js
import React from 'react';
import ExpenseForm from './components/ExpenseForm';
import PredictionChart from './components/PredictionChart';

function App() {
    return (
        <div className="App">
            <h1>AI-Powered Personal Finance Manager</h1>
            <ExpenseForm />
            <PredictionChart />
        </div>
    );
}

export default App;
