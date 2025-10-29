import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import BottomNav from '../components/BottomNav';

function Profile() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/signin');
  };

  return (
    <div className="min-h-screen bg-white pb-20">
      {/* Header */}
      <div className="bg-white border-b border-gray-200 p-4">
        <h1 className="text-xl font-semibold">Profile</h1>
      </div>

      {/* Profile Content */}
      <div className="p-6">
        {/* User Info Card */}
        <div className="bg-gradient-to-br from-orange-200 to-orange-300 rounded-2xl p-6 mb-6">
          <div className="w-20 h-20 bg-white rounded-full mx-auto mb-4 flex items-center justify-center">
            <span className="text-3xl font-bold text-orange-400">
              {user?.name?.[0]?.toUpperCase() || 'U'}
            </span>
          </div>
          <h2 className="text-xl font-bold text-center text-gray-800">{user?.name || 'User'}</h2>
          <p className="text-gray-700 text-center">{user?.email}</p>
        </div>

        {/* Menu Options */}
        <div className="space-y-3 mb-6">
          <button
            onClick={() => navigate('/trips')}
            className="w-full flex items-center justify-between p-4 bg-white border border-gray-200 rounded-xl hover:bg-gray-50 transition"
          >
            <div className="flex items-center gap-3">
              <span className="text-2xl">📊</span>
              <span className="font-medium text-gray-800">Analysis History</span>
            </div>
            <span className="text-gray-400">→</span>
          </button>

          <button
            onClick={() => navigate('/detail')}
            className="w-full flex items-center justify-between p-4 bg-white border border-gray-200 rounded-xl hover:bg-gray-50 transition"
          >
            <div className="flex items-center gap-3">
              <span className="text-2xl">📸</span>
              <span className="font-medium text-gray-800">New Analysis</span>
            </div>
            <span className="text-gray-400">→</span>
          </button>

          <button
            className="w-full flex items-center justify-between p-4 bg-white border border-gray-200 rounded-xl hover:bg-gray-50 transition"
          >
            <div className="flex items-center gap-3">
              <span className="text-2xl">⚙️</span>
              <span className="font-medium text-gray-800">Settings</span>
            </div>
            <span className="text-gray-400">→</span>
          </button>
        </div>

        {/* Logout Button */}
        <button
          onClick={handleLogout}
          className="w-full py-3 bg-red-500 text-white rounded-full font-semibold hover:bg-red-600 transition"
        >
          Logout
        </button>
      </div>

      <BottomNav />
    </div>
  );
}

export default Profile;
