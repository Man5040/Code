import { useState, useEffect } from "react"

const App = () => {
    const[ message, setMessage] = useState(null)
    const[ value, setValue] = useState(null)
    const[ previousChats, setPreviousChats] = useState([])
    const[currentTitle, setcurrentTitle] = useState(null)

    const createNewChat = () => {
      setMessage(null)
      setValue("")
      setcurrentTitle(null)
    }

    const hancleClick = (uniqueTitle) => {
      setcurrentTitle(uniqueTitle)
      setMessage(null)
      setValue("")
    }

  const getMessages = async () => {
    const options = {
      method: "POST",
      body: JSON.stringify({ 
        message: value
    }),
    headers: {
      "Content-Type": "application/json"
    }
  }
    try {
        const response = await fetch("https://api.openai.com/v1/completions", options)
        const data = await response.json()
        setMessage(data.choices[0].message)
    } catch (error) {
      console.error(error)
    }
  }

  useEffect( () => {
    if (!currentTitle && value && message){
      setcurrentTitle(value)
    }
    if (currentTitle && value && message){
      setPreviousChats(prevChats => ([...prevChats, 
        {
          title: currentTitle,
          role: "user",
          content: value
        },
      {
        title: currentTitle,
        role: message.role,
        content: message.content
      }]))
    }
  }, [message, currentTitle])

  const currentChat = previousChats.filter(previousChats => previousChats.title === currentTitle)
  const uniqueTitles = Array.from(new Set(previousChats.map(previousChat => previousChat.title)))


  return (
    <div className="app">
      <section className="sidebar">
        <button onClick={createNewChat}>+ New chat</button>
        <ul className = "history">
          {uniqueTitles?.map((uniqueTitle, index) => <li key={index} onClick={ () => hancleClick(uniqueTitle)}>{uniqueTitle}</li>)}
        </ul>
        <nav>
            <p>Mady by Man</p>
        </nav>
      </section>
      <section className="main">
          {!currentTitle && <h1>ProGPT</h1>}
          <ul className="feed">
            {currentChat?.map((chatMessage, index) => <li key={index}>
                <p className="role" >{chatMessage.role}</p>
                <p>{chatMessage.content}</p>
              </li>)}
          </ul>
          <div className="bottom-section">
            <div className="input-container">
              <input value={value} onChange={(e) => setValue(e.target.value)}/>
              <div id="submit" onClick={getMessages}> =&gt; </div>
            </div>
            <p className="info">
              Chat GPT New Version
            </p>
          </div>
      </section>
    </div>
  );
}

export default App;
