
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Login from './Components/Login';
import Dashboard from './Components/Dashboard'
import SignUp from './Components/Signup'
import EmailVerification from './Components/EmailVerification';
import ResetPassword from './Components/ResetPassword';
import OtpVerification from './Components/OtpVerification';
import CourseDetails from './Components/CourseDetails';
import Main from './Components/Main'
import ProtectedRoute from './Components/ProtectedRoute';

const App = () => {
  return (
    // <BrowserRouter>
    //   <Routes>
    //     {/* Public Routes */}
    //     <Route path="/" element={<Login />} />
    //     <Route path="/signup" element={<SignUp />} />
    //     <Route path="/emailverification" element={<EmailVerification />} />
    //     <Route path="/otpverification" element={<OtpVerification />} />
    //     <Route path="/resetpassword" element={<ResetPassword />} />

    //     {/* Protected Routes */}
    //     <Route path="/dashboard" element={<ProtectedRoute component={Dashboard} />}>
    //       <Route index element={<ProtectedRoute component={Main} />} />
    //       <Route path="allcourses" element={<ProtectedRoute component={CourseDetails} />} />
    //     </Route>
    //   </Routes>
    // </BrowserRouter>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Login/>}/>
        {/* <Route path='/dashbord' element={<Dashboard/>}/> */}
        <Route path="/dashbord" element={<Dashboard />}>
          <Route index element={<Main />} />
          <Route path="allcources" element={<CourseDetails />} />
        </Route>
        <Route path='/signup' element={<SignUp/>}/>
        <Route path='/emailverification' element={<EmailVerification/>}/>
        <Route path='/otpverification' element={<OtpVerification/>}/>
        <Route path='/resetpassword' element={<ResetPassword/>}/>
        {/* <Route path='/allcources' element={<CourseDetails/>}/> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
