import React, { useState } from "react";
//import "./Crick.css";
const Cricket = (props) => {
  console.log("props", props);
  console.log("targert = ", props.target);
  //states are created here inside the function
  const [runs, setRuns] = useState(0);
  const [wickets, setWickets] = useState(0);
  const [target, setTarget] = useState(props.target);
  const [balls, setBalls] = useState(0);
  const totalOvers = props.totalOvers;
  const totalBalls = totalOvers * 6;

  const handleSix = () => {
    setRuns(runs + 6);
    setBalls(balls + 1);
  };

  const handleFour = () => {
    setRuns(runs + 4);
    setBalls(balls + 1);
  };
  const handleThree = () => {
    setRuns(runs + 3);
    setBalls(balls + 1);
  };
  const handleTwo = () => {
    setRuns(runs + 2);
    setBalls(balls + 1);
  };
  const handleOne = () => {
    setRuns(runs + 1);
    setBalls(balls + 1);
  };

  // const handleRuns = (run) => {
  //   if (runs + run >= target) alert("Target Chased");
  //   setRuns(runs + run);
  //   setBalls(balls + 1);
  // };

  // overs done => "Failed to Chase Target"

  const handleWicket = () => {
    if (wickets + 1 === 10) alert("All Out");

    setWickets(wickets + 1); // it will take some time to update
    setBalls(balls + 1);
  };

  const oversBowled = Math.floor(balls / 6);
  const ballsThisOver = balls % 6;
  const oversLeft = totalOvers - oversBowled - (ballsThisOver ? 1 : 0);

  const gameOver = wickets >= 10 || runs >= props.target || balls >= totalBalls;

  return (
    <>
      <h1>
        Scrore : {runs} / {wickets}
      </h1>
      <h2>
        Current Over : {oversBowled}.{ballsThisOver}
      </h2>
      <h2>Overs Left: {Math.max(0, (totalBalls - balls) / 6).toFixed(1)}</h2>
      {wickets < 10 && runs < target ? (
        <div>
          <button onClick={handleSix}>Six</button>
          <button onClick={handleFour}>Four</button>
          <button onClick={handleThree}>Three</button>
          <button onClick={handleTwo}>Two</button>

          <button onClick={() => setBalls(balls + 1)}>Dot Ball</button>
          {
            //Add 3 2 dotball also
          }
          <button onClick={handleOne}>One</button>
          <button onClick={handleWicket}>Wicket</button>
        </div>
      ) : (
        <h2>Game Over</h2>
      )}
    </>
  );
};

export default Cricket;
