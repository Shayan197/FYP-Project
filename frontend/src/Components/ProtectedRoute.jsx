
import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ props }) => {
  const token = localStorage.getItem('authToken'); // Check token existence
    const {Component} = props 
  if (!token) {
    return <Navigate to="/" replace />; // Redirect to login if token not found
  }

  return <Component />;
};

export default ProtectedRoute;
