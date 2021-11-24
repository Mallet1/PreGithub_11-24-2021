import Header from './components/Header'
import Tasks from './components/Tasks'
import {useState} from 'react'

function App() {
  const [tasks, setTasks] = useState([
    {
      id: 1,
      text: 'Doctors Appointment',
      day: 'Feb 5th at 2:30pm',
      reminder: true,
    }
  ])
  
  return (
    <div className="container">
      <Header title = 'Task Tracker'/>
      <Tasks tasks={tasks}/>
    </div>
  );
}

// Notes

// function App() {
//   const name = 'Brad'
  
//   return (
//     <div className="container">
//       <h1>Hello From React</h1> 
      
//       {/* Every thing returned must be within one element (div in this case) */}

//       <h2>Hello {name}</h2>

//       <Header title = 'Hello'/>
//     </div>
//   );
// }

// Class version

// class App extends React.Component {
//   render() {
//     return <h1>Hello from a class</h1>
//   }
// }

export default App;
