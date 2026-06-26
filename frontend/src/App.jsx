import { useState } from "react";
import Header from "./components/Header";
import UserSummary from "./components/UserSummary";
import TransactionForm from "./components/TransactionForm";
import Leaderboard from "./components/Leaderboard";
import "./styles.css";

export default function App() {
  const [refresh, setRefresh] = useState(false);

  const triggerRefresh = () => {
    setRefresh(prev => !prev);
  };

  return (
    <div className="page">
  
      <Header />
  
      <div className="container">
        <div className="top-section">
          <UserSummary />
          <TransactionForm />
        </div>
  
        <Leaderboard />
      </div>
  
    </div>
  );
}
