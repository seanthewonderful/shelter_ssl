function AnimalCard(props) {
    return (
      <div className="card">
        <p>Species: {props.species} </p>
        <p>Name: {props.name} </p>
        <img src={props.imgUrl} alt="image" />
        <p>Description: {props.description} </p>
      </div>
    );
}

function AddAnimalCard(props) {
  const [name, setName] = React.useState("")
  const [species, setSpecies] = React.useState("")
  const [gender, setGender] = React.useState("")
  const [age, setAge] = React.useState("")
  const [description, setDescription] = React.useState("")
  const [imgUrl, setImgUrl] = React.useState("")

  function addNewCard() {
    fetch("/add-card", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: name, 
                            species: species, 
                            gender: gender, 
                            age: age, 
                            description: description, 
                            imgUrl: imgUrl 
                          }),
    })
      .then((response) => response.json())
      .then((jsonResponse) => {
        const cardAdded = jsonResponse.cardAdded
        props.addCard(cardAdded)
      })
  }

  return (
    <React.Fragment>
      <h2>Add New Animal</h2>
      <label htmlFor="nameInput">Name</label>
      <input 
        value={name}
        onChange={(event) => setName(event.target.value)}
        id="nameInput"
        style={{marginLeft: "5px"}}
      ></input>
      <label
        htmlFor="speciesInput"
        style={{marginLeft: "10px", marginRight: "5px"}}
        >
      Species</label>
      <input 
        value={species}
        onChange={(event) => setSpecies(event.target.value)}
        id="speciesInput">
      </input>
      <label htmlFor="genderInput">Gender</label>
      <input 
        value={gender} 
        onChange={(event) => setGender(event.target.value)} 
        id="genderInput">
      </input>
      <label htmlFor="ageInput">Age</label>
      <input 
        value={age} 
        onChange={(event) => setAge(event.target.value)} 
        id="ageInput">
      </input>
      <label htmlFor="descriptionInput">Description</label>
      <input 
        value={description} 
        onChange={(event) => setDescription(event.target.value)} 
        id="descriptionInput">
      </input>
      <label htmlFor="imgUrlInput">Image URL</label>
      <input 
        value={imgUrl} 
        onChange={(event) => setImgUrl(event.target.value)} 
        id="imgUrlInput">
      </input>
      <button 
        style={{marginLeft: "10px"}}
        onClick={addNewCard}
      >Add</button>
    </React.Fragment>
  )
}

function AnimalCardContainer() {
    const [cards, setCards] = React.useState([])

    function addCard(newCard) {
      const currentCards = [...cards]
      setCards([...currentCards, newCard]);
    }

    React.useEffect(() => {
      fetch("/animals.json")
        .then((response) => response.json())
        // .then((data) => setCards(data.cards))
        .then((data) => {
          const temp_arr = []
          for (const [key, value] of Object.entries(data)) {
            // console.log(`Key: ${key} | Value: ${value}`)
            // temp_arr.push({ key = value })
          }
          console.log(temp_arr)
        })
    }, []);

    const animalCards = [];

    for (const currentCard of cards) {
      console.log(currentCard)
      animalCards.push(
        <AnimalCard
          key={currentCard.name}
          name={currentCard.name}
          species={currentCard.species}
          gender={currentCard.gender}
          age={currentCard.age}
          description={currentCard.description}
          img_url={currentCard.img_url}
          />
      );
    }

    return (
      <React.Fragment>
        <AddAnimalCard addCard={addCard} />
        <h2>Animals for Sale or Trade</h2>
        <div className="grid">{animalCards}</div>
      </React.Fragment>
    )
}

ReactDOM.render(<AnimalCardContainer />, document.getElementById("animal-container"))