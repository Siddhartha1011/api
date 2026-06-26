import { useEffect, useState } from "react";
import { getRanking } from "../api";

export default function Leaderboard({ refresh }) {
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const res = await getRanking();
    setData(res.data);
  };

  useEffect(() => {
    fetchData();
  }, [refresh]);

  // 🔥 auto refresh every 5 sec
  useEffect(() => {
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="leaderboard">
      <h2>Leaderboard</h2>

      <table>
        <thead>
          <tr>
            <th>Rank</th>
            <th>User</th>
            <th>Score</th>
            <th>Total</th>
            <th>Txns</th>
          </tr>
        </thead>

        <tbody>
          {data.map((u, i) => (
            <tr key={u.userId}>
              <td>{i + 1}</td>
              <td>{u.userId}</td>
              <td>{u.score}</td>
              <td>{u.totalAmount}</td>
              <td>{u.transactions}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}