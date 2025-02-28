import React, { useState } from 'react';
import axiosInstance from '../api/axios';

function CreateBlog() {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        axiosInstance.post('blogs/create/', { title, content })
            .then(response => {
                console.log('Blog created:', response.data);
                setTitle('');
                setContent('');
            })
            .catch(error => {
                console.error('Error creating blog:', error);
            });
    };

    return (
        <div>
            <h1>Create Blog</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                />
                <textarea
                    placeholder="Content"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    required
                />
                <button type="submit">Post</button>
            </form>
        </div>
    );
}

export default CreateBlog;
