import RedirectButton from "../components/RedirectButton"

function Landing() {
    return (
        <div>
            <h1>Gamblify</h1>
            <RedirectButton to="/login" text="Login"></RedirectButton>
            <RedirectButton to="/signup" text="Sign Up"></RedirectButton>
        </div>
    )
}

export default Landing