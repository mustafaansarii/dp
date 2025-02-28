import React, { useState } from 'react';
import axiosInstance from '../api/axios';
import { useNavigate } from 'react-router-dom';

const CreateBlog = () => {
  const [formData, setFormData] = useState({ title: '', content: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axiosInstance
      .post('blogs/', formData)
      .then((response) => {
        navigate('/'); // Redirect to home after blog creation
      })
      .catch((error) => {
        setError('Error creating blog. Please try again!');
      });
  };

  return (
    <div>
      <h2>Create New Blog</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          placeholder="Blog Title"
          value={formData.title}
          onChange={handleChange}
        />
        <textarea
          name="content"
          placeholder="Blog Content"
          value={formData.content}
          onChange={handleChange}
        />
        <button type="submit">Create Blog</button>
      </form>
    </div>
  );
};

export default CreateBlog;
