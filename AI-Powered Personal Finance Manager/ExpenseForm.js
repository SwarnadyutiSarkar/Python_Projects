// src/components/ExpenseForm.js
import React, { useState } from 'react';
import axios from 'axios';

const ExpenseForm = () => {
    const [amount, setAmount] = useState('');
    const [category, setCategory] = useState('');
    const [date, setDate] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5000/add_expense', {
            user_id: 1,  // Example user ID
            amount: parseFloat(amount),
            category: category,
            date: date
        })
        .then(response => {
            alert('Expense added successfully');
            setAmount('');
            setCategory('');
            setDate('');
        })
        .catch(error => {
            console.error('There was an error adding the expense!', error);
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Amount:</label>
                <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} required />
            </div>
            <div>
                <label>Category:</label>
                <input type="text" value={category} onChange={(e) => setCategory(e.target.value)} required />
            </div>
            <div>
                <label>Date:</label>
                <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
            </div>
            <button type="submit">Add Expense</button>
        </form>
    );
};

export default ExpenseForm;
