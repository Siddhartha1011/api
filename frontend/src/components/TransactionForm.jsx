import { useState } from "react";
import { createTransaction } from "../api";

export default function TransactionForm({ onSuccess }) {
  const [form, setForm] = useState({
    userId: "",
    transactionId: "",
    amount: ""
  });

  const handleSubmit = async () => {
    const payload = {
      userId: form.userId.trim(),
      transactionId: form.transactionId.trim(),
      amount: Number(form.amount)
    };
  
    if (!payload.userId || !payload.transactionId) {
      alert("User ID and Transaction ID cannot be empty.");
      return;
    }
  
    try {
      const res = await createTransaction(payload);
  
      // 🔥 IMPORTANT FIX
      if (res.data.status === "success") {
        alert("Transaction Success");
  
        setForm({
          userId: "",
          transactionId: "",
          amount: ""
        });
  
        onSuccess();
      } 
      else {
        alert(res.data.error || "Transaction Failed");
      }
  
    } catch (err) {
      alert(err.response?.data?.error || "Server Error");
    }
  };

  return (
    <div className="card">
      <h2>Transaction Form</h2>

      <input
          value={form.userId}
          placeholder="User ID"
          onChange={(e) =>
              setForm({
                  ...form,
                  userId: e.target.value
              })
          }
      />

      <input
        value={form.transactionId}
        placeholder="Transaction ID"
        onChange={(e) =>
          setForm({ ...form, transactionId: e.target.value })
        }
      />

      <input
        value={form.amount}
        placeholder="Amount"
        type="number"
        onChange={(e) =>
          setForm({ ...form, amount: e.target.value })
        }
      />

      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}