import { Link } from "react-router-dom"

function RedirectButton({ text, to }) {
    return (
        <Link to={to}><button>{text}</button></Link>
    )
}

export default RedirectButton