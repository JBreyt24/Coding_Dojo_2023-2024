import './App.css'
import PersonCard from './components/PersonCard';

function App() {

  return (
    <>
      <div className = "App">
        <PersonCard firstName={"Jane"} lastName={"Doe"} age={45} hairColor={"Black"} />
        <PersonCard firstName={"John"} lastName={"Smith"} age={88} hairColor={"Brown"} />
        <PersonCard firstName={"Millard"} lastName={"Fillmore"} age={45} hairColor={"Red"} />
        <PersonCard firstName={"Maria"} lastName={"Smith"} age={45} hairColor={"Blonde"} />
      </div>
    </>
  );
}

export default App;
