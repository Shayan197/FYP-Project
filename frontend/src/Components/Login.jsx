
import React, { useState } from 'react'
import { assets } from '../Assets/assets'
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const Login = () => {
  const [regNo, setRegNo] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false); // For button state
  const navigate = useNavigate();

  const handleLogin = async () => {
    // Frontend validation
    if (!regNo || !password) {
      setError('Registration number and password are required.');
      return;
    }
    const loginData = {
      reg_no: regNo,
      password: password,
    };
    setLoading(true); // Disable button during request
    setError(''); // Clear previous errors
    try {
      const response = await axios.post('http://127.0.0.1:5000/login', loginData);
      if (response.status === 200) {
        localStorage.setItem('authToken', response.data.token);
        navigate('/dashbord');
      }
    } catch (error) {
      if (error.response) {
        // Handle backend errors
        setError(error.response.data.message || 'Something went wrong. Please try again.');
      } else {
        setError('Unable to connect to the server. Please try again later.');
      }
    } finally {
      setLoading(false); // Re-enable button
    }
  };

  return (
    <div className='h-screen bg-opacity-90 bg-cover bg-center' style={{ backgroundImage: `url(${assets.background_image})` }}>
      <div className='h-full bg-gradient-to-b from-customBlue/80 via-[#1062BB]/80 to-[#000000]/80'>
        <div className='h-full mx-auto flex justify-around items-center'>

          <div className='flex-col justify-center'>
            <div className='flex justify-center mb-5'>
              <img src={assets.hero_icon} alt="hero_img" className='size-36' />
            </div>
            <div className='flex flex-col items-center'>
              <p className='text-white text-5xl tracking-wider mb-2 font-medium'>CourseAdvisor</p>
              <p className='text-white text-5xl tracking-wider font-medium'>Chatbot</p>
            </div>
          </div>

          <div className='w-[370px] h-[420px] bg-white rounded-xl flex flex-col items-center justify-center'>
            <div className='w-72'>
              <p className='font-medium text-2xl mb-6'>Login</p>
            </div>
            <input
              type="text" required
              placeholder='0000-ARID-0000'
              className='w-72 border-b-2 border-black/50 p-1 outline-none mb-2'
              value={regNo}
              onChange={(e) => setRegNo(e.target.value)} 
              />
            <input type="password" required
              placeholder='Password'
              className='w-72 border-b-2 border-black/50 p-1 outline-none mb-6'
              value={password}
              onChange={(e) => setPassword(e.target.value)} 
              />
            <button className='btn-primary mb-8' onClick={handleLogin} disabled={loading} >{loading ? 'Logging in...' : 'Login Now'}</button>
            {
            error && <div style={{ color: 'red' }}>{error}</div>
            }
            <div className='w-72 flex mb-6'>
              <input type="checkbox" /><p className='text-xs text-black/50 ml-2'>Agree to the terms of use & privacy policy</p>
            </div>
            <p className='w-72 text-xs text-black/50 mb-2'>Forget password <Link to='/emailverification' className='text-customBlue text-[15px]'>Click here</Link></p>
            <p className='w-72 text-xs text-black/50'>Create an accouont <Link to='/signup' className='text-customBlue text-[15px]'>Click here</Link></p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Login
