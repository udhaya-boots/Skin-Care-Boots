import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Home from './pages/Home';
import SignIn from './pages/SignIn';
import SignUp from './pages/SignUp';
import DetailSkin from './pages/DetailSkin';
import Trips from './pages/Trips';
import Profile from './pages/Profile';
import ProtectedRoute from './router/ProtectedRoute';

function App() {
    return (
        <BrowserRouter>
            <AuthProvider>
                <Routes>
                    <Route path="/signin" element={<SignIn />} />
                    <Route path="/signup" element={<SignUp />} />
                    <Route
                        path="/home"
                        element={
                            <ProtectedRoute>
                                <Home />
                            </ProtectedRoute>
                        }
                    />
                    <Route
                        path="/detail"
                        element={
                            <ProtectedRoute>
                                <DetailSkin />
                            </ProtectedRoute>
                        }
                    />
                    <Route
                        path="/trips"
                        element={
                            <ProtectedRoute>
                                <Trips />
                            </ProtectedRoute>
                        }
                    />
                    <Route
                        path="/profile"
                        element={
                            <ProtectedRoute>
                                <Profile />
                            </ProtectedRoute>
                        }
                    />
                    <Route path="/" element={<Navigate to="/home" />} />
                </Routes>
            </AuthProvider>
        </BrowserRouter>
    );
}

export default App;
