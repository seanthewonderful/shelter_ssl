
function LoginButton(props) {
  const [showModal, setShowModal] = React.useState(false);
  const [username, setUsername] = React.useState('');
  const [password, setPassword] = React.useState('');

  function handleLogin() {
    setShowModal(true);
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch('/login-admin', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(responseJson => {
        if (responseJson.code === 401) {
            throw new Error(responseJson.message)
        } else {
            setShowModal(false);
        }
      })
  }

  return (
    <React.Fragment>
      <button onClick={handleLogin}>Login</button>
      {showModal && (
        <div className="modal">
          <form onSubmit={handleSubmit}>
            <label>
              Username:
              <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
            </label>
            <label>
              Password:
              <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
            </label>
            <button type="submit">Submit</button>
          </form>
        </div>
      )}
    </React.Fragment>
  );
}

// export default LoginButton;

ReactDOM.render(<LoginButton />, document.getElementById("admin-login"))