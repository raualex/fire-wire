import React, { Component } from 'react';
import './Information.css';
import fire from './Images/fire-placeholder-pic.jpeg'
import camera from './Images/photo-camera.png'
import cityData from './citydata.js'

class Information extends Component {
  constructor() {
    super();

    this.state = {
      details: '',
      location: '',
      time: '',
      suggestions: cityData.data
    }
  }

  handleChange = (event) => {
    let { name, value } = event.target
    if (!name) {
      this.setState({
        location: value
      })
    } else {
      this.setState({
        [name]: value
      })
    }
  }

  render() {
    return (
      <section className='fire-information-container' >
        <h1 role='banner' className='info-title' >INFORMATION</h1>
        <img 
          src={fire} 
          alt='Forest fire to upload' 
          className='fire-image' 
        />
        <div 
          aria-label='Click here to retake your photo' 
          className='retake-box' 
        >
          <h2 className='retake-txt'>Retake Photo</h2>
          <img 
            src={camera} 
            alt='Camera' 
            className='camera-icon' 
          />
        </div>
        <form>
          <h4 className='sub-titles'>Additonal Details</h4>
          <input 
            type='text' 
            name='details' 
            value={this.state.details}
            onChange={this.handleChange}
            className='details-input'
          />
          <h4 className='sub-titles'>Location</h4>
          <select
            className='location-list' 
            onChange={this.handleChange}
            value={this.state.location}
          >
            { 
              Array.isArray(this.state.suggestions) && 
              this.state.suggestions.map((city, index) => {
                return <option key={Date.now() + index} value={city}>{city}</option>
              })}
          </select>
          <h4 className='sub-titles'>Time (optional)</h4>
          <input 
            className='time-input'
            type='text'
            onChange={this.handleChange}
            name='time'
            value={this.state.time}
          />
          <button className='submit-btn'>
            Submit
          </button>
        </form>
      </section>
    )
  }
}

export default Information;