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
            200:'#00a2ff',
            400:'#005fdd',
            600:'#002e6d', //SBA
        },
        red: {
          200:'#ff5959',
          400:'#cc0000', //SBA
          600:'#af0505',
        },
        gray: {
            200:'#d1d1d1', 
            400:'#969696', //SBA
            800:'#686868' //SBA
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