import { useEffect, useState } from "react";
import { getSummary } from "../api";

export default function UserSummary({ refresh }) {
  const [userId, setUserId] = useState("");
  const [data, setData] = useState(null);

  const fetchData = async () => {
    if (!userId.trim()) return;

    const res = await getSummary(userId.trim());
    setData(res.data);
  };

  // 🔥 THIS IS THE FIX
  useEffect(() => {
    if (userId) {
      fetchData();
    }
  }, [refresh]);   // <-- triggers after transaction

  return (
    <div className="card">
      <h2>User Summary</h2>

      <input
        value={userId}
        placeholder="Enter User ID"
        onChange={(e) => setUserId(e.target.value)}
      />

      <button onClick={fetchData}>Get Summary</button>

      {data && (
        <div>
          <p>User: {data.userId}</p>
          <p>Total Amount: {data.totalAmount}</p>
          <p>Transactions: {data.totalTransactions}</p>
          <p>Score: {data.score}</p>
        </div>
      )}
    </div>
  );
}