import api from './api';

export const authService = {
  async signUp(email, password, name) {
    const response = await api.post('/auth/signup', { email, password, name });
    return response.data;
  },

  async signIn(email, password) {
    const response = await api.post('/auth/signin', { email, password });
    return response.data;
  },

  async googleSignIn(email, name) {
    const response = await api.post('/auth/google', { email, name });
    return response.data;
  },

  async verifyToken() {
    const response = await api.get('/auth/verify');
    return response.data;
  },

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  }
};
