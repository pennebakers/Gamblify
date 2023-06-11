import InputBox from "../components/InputBox"

function Login() {
    return (
        <div>
            <InputBox placeholder={"username"} />
            <InputBox placeholder={"password"} />
            <button>Submit</button>
        </div>
    )
}

export default Login