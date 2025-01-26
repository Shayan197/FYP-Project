import React from 'react'
import Sidebar from './Sidebar'
import Main from './Main'
import { Outlet } from 'react-router-dom'

const Dashboard = () => {
  return (
    <div className='flex'>
      <Sidebar/>
      {/* <Main/> */}
      <div className="flex-1">
        <Outlet />
      </div>
    </div>
  )
}

export default Dashboard
