export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

export const APP_NAME = 'Skin Care Analyzer';

export const ROUTES = {
  HOME: '/home',
  SIGNIN: '/signin',
  SIGNUP: '/signup',
  DETAIL: '/detail',
  TRIPS: '/trips',
  PROFILE: '/profile'
};

export const STORAGE_KEYS = {
  TOKEN: 'token',
  USER: 'user'
};

export const SKIN_TYPES = {
  OILY: 'oily',
  DRY: 'dry',
  NORMAL: 'normal',
  COMBINATION: 'combination'
};

export const CONCERNS = {
  PORE: 'pore',
  ACNE: 'acne',
  TEXTURE: 'texture',
  WRINKLES: 'wrinkles',
  DARK_SPOTS: 'dark_spots'
};
