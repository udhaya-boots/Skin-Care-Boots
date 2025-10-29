import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { authService } from '../services/authService';
import Loader from '../components/Loader';

function SignUp() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSignUp = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await authService.signUp(email, password, name);
      login(response.user, response.token);
      navigate('/home');
    } catch (err) {
      setError(err.response?.data?.error || 'Sign up failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-orange-300 to-white flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="bg-orange-300 rounded-t-3xl p-8">
          <h1 className="text-3xl font-bold text-gray-800">Sign Up</h1>
          <p className="text-sm text-gray-600 mt-2">
            Create your account to get started
          </p>
        </div>

        <div className="bg-white rounded-b-3xl p-8 shadow-xl">
          <form onSubmit={handleSignUp} className="space-y-4">
            <input
              type="text"
              placeholder="Full Name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full px-4 py-3 rounded-lg bg-gray-100 border-none focus:ring-2 focus:ring-orange-400"
              required
            />

            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-3 rounded-lg bg-gray-100 border-none focus:ring-2 focus:ring-orange-400"
              required
            />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-lg bg-gray-100 border-none focus:ring-2 focus:ring-orange-400"
              required
            />

            {error && (
              <div className="text-red-500 text-sm text-center">{error}</div>
            )}

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-black text-white py-3 rounded-full font-semibold hover:bg-gray-800 transition disabled:bg-gray-400"
            >
              {loading ? <Loader /> : 'Sign Up'}
            </button>
          </form>

          <div className="text-center mt-8">
            <span className="text-gray-600">Already have an account? </span>
            <Link to="/signin" className="text-gray-800 font-semibold hover:underline">
              Sign In
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SignUp;
