import './App.css';
import Login from './components/Login';
import SignUp from './components/SignUp';

function App() {
  return (
    <div className="App">
      <h1>Welcome To Gamblify</h1>
      <Login></Login>
      <SignUp></SignUp>
    </div>
  );
}

export default App;