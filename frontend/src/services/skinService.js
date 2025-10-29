import api from './api';

export const skinService = {
  async analyzeSkin(imageData) {
    const response = await api.post('/skin/analyze', { image: imageData });
    return response.data;
  },

  async getHistory() {
    const response = await api.get('/skin/history');
    return response.data;
  },

  async getTips() {
    const response = await api.get('/skin/tips');
    return response.data;
  }
};
