/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./main/templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        blue: {
            400:'#002e6d',
        },
        red: '#cc0000',
        gray: {
            200:'d1d1d1',
            400:'#969696',
            800:'#686868'
        },
        white: '#ffffff',
      },
      fontFamily: {
        sans: ['Source Sans Pro', 'sans-serif'],
      }
    },
  },
  plugins: [],
}