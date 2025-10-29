import api from './api';

export const productService = {
  async getAllProducts() {
    const response = await api.get('/products/all');
    return response.data;
  },

  async getTopProducts(limit = 3) {
    const response = await api.get(`/products/top?limit=${limit}`);
    return response.data;
  },

  async getProduct(id) {
    const response = await api.get(`/products/${id}`);
    return response.data;
  },

  async getRecommendations(concerns, skinType) {
    const response = await api.post('/products/recommend', { 
      concerns, 
      skin_type: skinType 
    });
    return response.data;
  }
};
