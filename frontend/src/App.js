import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div className='header-text'>
          <h1>OPENcave-API</h1>
          <p>Open-source Model Catalog using python-awips, flask, and API data from Unidate.unicar.edu</p>

        </div>
        
        </header>
    </div>
    
  );
}

export default App;
