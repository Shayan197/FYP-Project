import React, { useState } from 'react'
import { assets } from '../Assets/assets'

const Sidebar = () => {

    const [extended, setExtended] = useState(false)

    return (
        <div className='min-h-screen inline-flex flex-col justify-between bg-[#f0f4f9] px-4 py-6'>
            <div className="top">
                <img className="menu w-6 block ml-3 cursor-pointer" src={assets.menu_icon} alt=""  onClick={() => setExtended(prev => !prev)}/>
                <div className="new-chat mt-10 inline-flex items-center gap-3 px-4 py-3 bg-[#e6eaf1] rounded-full text-xs text-gray-600 cursor-pointer">
                    <img className='w-5' src={assets.plus_icon} alt="" />
                    {
                        extended ? <p>New Chat</p> : null
                    }
                </div>
                {
                    extended ?
                        <div className="flex flex-col">
                            <p className="mt-8 mb-4">Recent</p>
                            <div className="sidebar_icon_design pr-10">
                                <img className='w-5' src={assets.message_icon} alt="" />
                                <p>What is React...</p>
                            </div>
                        </div> : null
                }
            </div>
            <div className="bottom flex flex-col">
                <div className='sidebar_icon_design'>
                    <img className='w-5' src={assets.question_icon} alt="" />
                    {
                        extended ? <p>Help</p> : null
                    }
                </div>
                <div className='sidebar_icon_design'>
                    <img className='w-5' src={assets.history_icon} alt="" />
                    {
                        extended ? <p>Activuty</p> : null
                    }
                </div>
                <div className='sidebar_icon_design'>
                    <img className='w-5' src={assets.setting_icon} alt="" />
                    {
                        extended ? <p>Settings</p> : null
                    }
                </div>
            </div>
        </div>
    )
}

export default Sidebar
