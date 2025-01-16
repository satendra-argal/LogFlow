import React from 'react';

const LogsTable = ({ logs }) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>User ID</th>
                    <th>Activity</th>
                    <th>Timestamp</th>
                    <th>Metadata</th>
                </tr>
            </thead>
            <tbody>
                {logs.map((log, index) => (
                    <tr key={index}>
                        <td>{log.user_id}</td>
                        <td>{log.activity}</td>
                        <td>{log.timestamp}</td>
                        <td>{JSON.stringify(log.metadata)}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default LogsTable;