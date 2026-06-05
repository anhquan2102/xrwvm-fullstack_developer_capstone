import React, { useState } from 'react';
import Header from '../Header/Header';
import './Register.css';

const Register = () => {
  const [userName, setUserName] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [open, setOpen] = useState(true);

  let register_url = window.location.origin + '/djangoapp/registration';

  const register = async (e) => {
    e.preventDefault();
    const res = await fetch(register_url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        userName,
        firstName,
        lastName,
        email,
        password,
      }),
    });
    const json = await res.json();
    if (json.status === 'Authenticated') {
      sessionStorage.setItem('username', json.userName);
      setOpen(false);
    } else {
      alert(json.error || 'Registration failed.');
    }
  };

    window.location.href = '/';
  }

  return (
    <div>
      <Header />
      <div className="modalContainer">
        <form className="login_panel" onSubmit={register}>
          <div>
            <span className="input_field">Username </span>
            <input type="text" placeholder="Username" className="input_field"
              onChange={(e) => setUserName(e.target.value)} required />
          </div>
          <div>
            <span className="input_field">First Name </span>
            <input type="text" placeholder="First Name" className="input_field"
              onChange={(e) => setFirstName(e.target.value)} required />
          </div>
          <div>
            <span className="input_field">Last Name </span>
            <input type="text" placeholder="Last Name" className="input_field"
              onChange={(e) => setLastName(e.target.value)} required />
          </div>
          <div>
            <span className="input_field">Email </span>
            <input type="email" placeholder="Email" className="input_field"
              onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div>
            <span className="input_field">Password </span>
            <input type="password" placeholder="Password" className="input_field"
              onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <div>
            <input className="action_button" type="submit" value="Register" />
            <input className="action_button" type="button" value="Cancel"
              onClick={() => setOpen(false)} />
          </div>
        </form>
      </div>
    </div>
  );
};

export default Register;
