/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'orange': {
          100: '#FFF5F0',
          200: '#FFE5D9',
          300: '#FFD4B8',
          400: '#FFB088',
          500: '#FF9B5A',
        },
        'green': {
          100: '#E6F5E6',
          200: '#CCF0CC',
        }
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
