import React, { useEffect, useState } from 'react';
import axiosInstance from '../api/axios';

function BlogList() {
    const [blogs, setBlogs] = useState([]);

    useEffect(() => {
        axiosInstance.get('blogs/')
            .then(response => {
                setBlogs(response.data);
            })
            .catch(error => {
                console.error('Error fetching blogs:', error);
            });
    }, []);

    return (
        <div>
            <h1>Blogs</h1>
            {blogs.map(blog => (
                <div key={blog.id}>
                    <h2>{blog.title}</h2>
                    <p>{blog.content}</p>
                    <small>By {blog.author}</small>
                </div>
            ))}
        </div>
    );
}

export default BlogList;
