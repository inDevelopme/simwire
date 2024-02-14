import React, {useState} from 'react'
import axios from "axios";
import {useNavigate} from 'react-router-dom'

const LoginForm = () => {
    // flask api url
    const flaskapiUrl = 'http://localhost:9000'

    // use the usehistory hook to get the history object
    const navigate = useNavigate();

    //State to manage form fields
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    // Function to hndle form input changes
    const handleInputChange = (e) => {
        const {name, value} = e.target;
        setFormData((prevData) => ({...prevData, [name]: value }));
    };

    // Function to hndle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();

        // add your authentication logic here
        try {
            console.log('Form submitted with data: ', formData);
            const response = await axios.post(flaskapiUrl + '/login', formData)


            if(response.data === 1){
                //Handle succesful login
                console.log('Login successful', response.data);
                navigate('/desktop')
            }
        } catch(error) {
            // Handle error
            console.error('Error during login:', error.message);
            throw error

        }

        //Reset form fields after submission
        setFormData({
            username: '',
            password: '',
        });
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleInputChange}
                        required
                    />
                </label>
                <br/>
                <label>
                    Password:
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleInputChange}
                        required
                    />
                </label>
                <br/>
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default LoginForm;