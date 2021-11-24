// import React from 'react' {/* Optional */}
import PropTypes from 'prop-types'
import Button from './Button'

function Header({title}) {
    function onClick() {
        console.log('Click')
    }
    
    return (
        <header className='header'>
            {/*
            for CSS in JS
            <h1 style = {headingStyle}>{title}</h1>
            */}

            <h1>{title}</h1>
            <Button onClick={onClick} color='green' text='Add' /> {/* button defined in Button.js */}
        </header>
    )
}

// default Header parameter

Header.defaultProps = {
    title: 'Task Tracker',
}

// throws an error to the console if the argument passed for title isn't a string

Header.propTypes = {
    title: PropTypes.string,
}

// CSS in JS

// const headingStyle = {
//     color: 'red',
//     backgroundColor: 'black'
// }

export default Header
