function LoginAdmin(props) {
    const [username, setUsername] = React.useState("")
    const [password, setPassword] = React.useState("")

    function Login() {
        fetch("/login-admin", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.getElementById("csrf-token").getAttribute("content")
            },
            body: JSON.stringify({ username, password }),
        })
        .then((response) => response.json())
        .then((jsonResponse) => {
            console.log(jsonResponse.code)
            if (jsonResponse.code == "200") {
                AdminLogin(jsonResponse.username)
            } 
        })
    }

    function AdminLogin(administrator) {
        document.querySelector(".login-container").innerHTML = `<h4>Welcome, ${administrator}`
    }

    return (
        <React.Fragment>
            <div className="login-container">
                <h4>Administrator Login</h4>
                <label htmlFor="usernameInput">Admin Username</label>
                <input 
                    value={username}
                    onChange={(event) => setUsername(event.target.value)}
                    id="usernameInput"
                ></input>
                <label htmlFor="passwordInput">Password</label>
                <input 
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                    id="passwordInput"
                ></input>
                <button 
                    onClick={Login}
                >Login</button>
            </div>
        </React.Fragment>
    )
}

// function LoginFormContainer() {

//     function AdminLogin(administrator) {
//         document.querySelector("login-container").innerHTML = `<h4>Welcome, ${administrator}`
//     }

//     return (
//         <React.Fragment>
//             <LoginAdmin adminLogin={AdminLogin} />
//         </React.Fragment>
//     )
// }

ReactDOM.render(<LoginAdmin />, document.getElementById("admin-login"))