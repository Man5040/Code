import Button from "./Button.jsx";
import Student from "./Student.jsx";
import List from './List.jsx';
import Counter from "./Counter.jsx";
import MyComponent from "./Onhandle.jsx";
import ColorPicker from "./Colorpocker.jsx";
import MyObjects from "./Objeccts.jsx";
import MyArrays from "./array.jsx";
import UsEffect from "./useEffect.jsx";
import ComponentA from "./Components/ComponentA.jsx";
import UsRef from "./useRef.jsx";

function App() {

  const fruits = [
    { id: 1, name: "apple", calories: "apple" },
    { id: 2, name: "orange", calories: 45 },
    { id: 3, name: "banana", calories: 105 },
    { id: 4, name: "coconut", calories: 159 },
    { id: 5, name: "pineapple", calories: 37 }
  ];

  const vegetables = [
    { id: 6, name: "potatoes", calories: 110 },
    { id: 7, name: "celery", calories: 15 },
    { id: 8, name: "carrots", calories: 25 },
    { id: 9, name: "corn", calories: 63 },
    { id: 10, name: "broccoli", calories: 50 }
  ];


  return (
      <>
      <Button/>

      <Student name="Spongebob" age="30" isStudent={true}/>
      <Student name="Patrick" age="31" isStudent={false}/>

      {fruits.length > 0 && <List items={fruits} category="Fruits" />}
      {vegetables.length > 0 && <List items={vegetables} category="Vegetables" />}

      <Counter/>

      <MyComponent/>

      <ColorPicker/>

      <MyObjects/>

      <MyArrays/>

      <usEffect/>

      <ComponentA/>

      <UsRef/>
      </>
      
  )
}

export default App
