import InputBox from "../components/InputBox"
import RedirectButton from "../components/RedirectButton"

function Login() {
    return (
        <div>
            <InputBox placeholder={"username"} />
            <InputBox placeholder={"password"} />
            <RedirectButton to="/home" text="Login" />
        </div>
    )
}

export default Login