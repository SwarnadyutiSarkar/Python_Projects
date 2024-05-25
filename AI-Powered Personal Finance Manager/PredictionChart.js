// src/components/PredictionChart.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const PredictionChart = () => {
    const [data, setData] = useState({});

    useEffect(() => {
        axios.get('http://localhost:5000/predict_expenses', { params: { user_id: 1 } })
            .then(response => {
                const predictions = response.data.predictions;
                const labels = Object.keys(predictions);
                const values = Object.values(predictions);

                setData({
                    labels: labels,
                    datasets: [{
                        label: 'Predicted Expenses',
                        data: values,
                        borderColor: 'rgba(75,192,192,1)',
                        borderWidth: 2,
                        fill: false
                    }]
                });
            })
            .catch(error => {
                console.error('There was an error fetching the predictions!', error);
            });
    }, []);

    return (
        <div>
            <h2>Expense Predictions</h2>
            <Line data={data} />
        </div>
    );
};

export default PredictionChart;
