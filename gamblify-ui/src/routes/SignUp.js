import InputBox from "../components/InputBox"

function SignUp() {
    return (
        <div>
            <InputBox placeholder={"Email"} />
            <InputBox placeholder={"Username"} />
            <InputBox placeholder={"Password"} />
            <InputBox placeholder={"Password"} />
            <button>Submit</button>
        </div>
    )
}

export default SignUp