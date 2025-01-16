import React, { useState } from 'react';
import axios from 'axios';
import LogsTable from './components/LogsTable';

function App() {
    const [userId, setUserId] = useState('');
    const [logs, setLogs] = useState([]);

    const fetchLogs = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/logs/${userId}`);
            setLogs(response.data);
        } catch (error) {
            console.error('Error fetching logs:', error);
        }
    };

    return (
        <div>
            <h1>User Activity Logs</h1>
            <input
                type="text"
                placeholder="Enter User ID"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
            />
            <button onClick={fetchLogs}>Fetch Logs</button>
            <LogsTable logs={logs} />
        </div>
    );
}

export default App;