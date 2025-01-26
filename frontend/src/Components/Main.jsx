import React from 'react'
import { assets } from '../Assets/assets'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const Main = () => {
  const navigate = useNavigate()
  const [dropdown, setDropdown] = useState(false)

  const handleLogout = () => {
    localStorage.removeItem('authToken'); // Remove token
    navigate('/'); // Redirect to login
  };
  return (
    <div className='flex-1 min-h-screen pb-24 relative'>
      <div className='flex justify-between items-center text-2xl p-5 text-customGray/90'>
        <p>Chatbot</p>
        <div>
          <img src={assets.profile_icon} alt="" className='w-10 cursor-pointer' onClick={() => setDropdown(prev => !prev)} />
          {
            dropdown && (
              <div className="absolute right-5 bg-[#f0f4f9] text-base px-4 py-1">
                <p className='hover:bg-[#dfe4ea] cursor-pointer' onClick={() => navigate('allcources')}>Courses Details</p>
                <p className='hover:bg-[#dfe4ea] cursor-pointer text-red-400' onClick={handleLogout}>Logout</p>
              </div>
            )
          }
        </div>
      </div>
      <div className="main-cont max-w-4xl m-auto">
        <div className="greet mx-0 my-12 text-5xl text-[#b2b6b3] font-medium">
          <p className='text-customGray/70 mb-2'>Hello, Dev.</p>
          <p>How can I assist you today?</p>
        </div>
        <div className="cards grid grid-cols-[repeat(auto-fill,minmax(180px,1fr))] gap-4 p-5">
          <div className="card_design">
            <p>Suggest me about the percentage and calculate my grade</p>
            <img src={assets.compass_icon} alt="" className='card_img_design' />
          </div>
          <div className="card_design">
            <p>Suggest me about the percentage and calculate my grade</p>
            <img src={assets.bulb_icon} alt="" className='card_img_design' />
          </div>
          <div className="card_design">
            <p>Suggest me about the percentage and calculate my grade</p>
            <img src={assets.message_icon} alt="" className='card_img_design' />
          </div>
          <div className="card_design">
            <p>Suggest me about the percentage and calculate my grade</p>
            <img src={assets.code_icon} alt="" className='card_img_design' />
          </div>
        </div>
        <div className="main-botom absolute bottom-0 w-full max-w-4xl py-0 px-5 m-auto">
          <div className="searchBox flex items-center justify-between bg-[#f0f4f9] px-5 py-2 rounded-full">
            <input type="text" placeholder='Enter a prompt here' className='flex-1 bg-transparent border-none outline-none p-2 text-xl' />
            <img src={assets.send_msg_icon} alt="" className='cursor-pointer' />
          </div>
          <p className='text-xs my-3 mx-auto text-center font-normal text-customGray/60'>Chatbot may apply inaccurate info, including about people so double check its responses. Your question trained it.</p>
        </div>
      </div>
    </div>
  )
}

export default Main
