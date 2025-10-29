import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { authService } from '../services/authService';
import Loader from '../components/Loader';

function SignIn() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSignIn = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await authService.signIn(email, password);
      login(response.user, response.token);
      navigate('/home');
    } catch (err) {
      setError(err.response?.data?.error || 'Sign in failed');
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSignIn = () => {
    alert('Google Sign In - Implement OAuth 2.0 flow');
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-orange-300 to-white flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="bg-orange-300 rounded-t-3xl p-8">
          <h1 className="text-3xl font-bold text-gray-800">Sign In</h1>
          <p className="text-sm text-gray-600 mt-2">
            Welcome back! Please sign in to continue
          </p>
        </div>

        <div className="bg-white rounded-b-3xl p-8 shadow-xl">
          <form onSubmit={handleSignIn} className="space-y-4">
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-3 rounded-lg bg-gray-100 border-none focus:ring-2 focus:ring-orange-400"
              required
              disabled={loading}
            />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-lg bg-gray-100 border-none focus:ring-2 focus:ring-orange-400"
              required
              disabled={loading}
            />

            {error && (
              <div className="text-red-500 text-sm text-center">{error}</div>
            )}

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-black text-white py-3 rounded-full font-semibold hover:bg-gray-800 transition disabled:bg-gray-400"
            >
              {loading ? <Loader /> : 'Sign In'}
            </button>
          </form>

          <div className="text-center my-4 text-gray-600">Or make easy</div>

          <button
            onClick={handleGoogleSignIn}
            className="w-full flex items-center justify-between px-6 py-3 bg-gray-100 rounded-full hover:bg-gray-200 transition"
          >
            <span className="text-xl">🔍</span>
            <span className="flex-1 text-center font-semibold">Continue with google</span>
            <span className="text-orange-500">→</span>
          </button>

          <div className="text-center mt-8">
            <Link to="/signup" className="text-gray-800 font-semibold hover:underline">
              SignUp
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SignIn;
