import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

function BottomNav() {
  const navigate = useNavigate();
  const location = useLocation();

  const isActive = (path) => location.pathname === path;

  return (
    <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 px-6 py-4 z-50">
      <div className="flex justify-around items-center max-w-md mx-auto">
        <button
          onClick={() => navigate('/home')}
          className={`flex flex-col items-center transition-colors ${
            isActive('/home') ? 'text-gray-800' : 'text-gray-400'
          }`}
        >
          <span className="text-2xl mb-1">🏠</span>
          <span className="text-xs font-medium">Home</span>
        </button>
        
        <button
          onClick={() => navigate('/trips')}
          className={`flex flex-col items-center transition-colors ${
            isActive('/trips') ? 'text-gray-800' : 'text-gray-400'
          }`}
        >
          <span className="text-2xl mb-1">📋</span>
          <span className="text-xs font-medium">Trips</span>
        </button>
        
        <button
          onClick={() => navigate('/profile')}
          className={`flex flex-col items-center transition-colors ${
            isActive('/profile') ? 'text-gray-800' : 'text-gray-400'
          }`}
        >
          <span className="text-2xl mb-1">👤</span>
          <span className="text-xs font-medium">Profile</span>
        </button>
      </div>
    </nav>
  );
}

export default BottomNav;
