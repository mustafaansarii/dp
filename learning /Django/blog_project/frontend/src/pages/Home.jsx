import React, { useEffect, useState } from 'react';
import axiosInstance from '../api/axios';
import { Link } from 'react-router-dom';

const Home = () => {
  const [blogs, setBlogs] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    axiosInstance
      .get('blogs/')
      .then((response) => {
        setBlogs(response.data);
      })
      .catch((error) => {
        setError('Error fetching blogs');
      });
  }, []);

  return (
    <div>
      <h2>All Blogs</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {blogs.map((blog) => (
          <li key={blog.id}>
            <h3>{blog.title}</h3>
            <p>{blog.content}</p>
            <small>By {blog.author}</small>
          </li>
        ))}
      </ul>
      <Link to="/create">Create New Blog</Link>
    </div>
  );
};

export default Home;
