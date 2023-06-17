import { Link } from "react-router-dom"
import RedirectButton from "../components/RedirectButton"

function Home() {
    return (
        <div>
            <ul>
                <li><a href="default.asp">Home</a></li>
                <Link to='/nfl'>NFL</Link>
                <Link to='/nba'>NBA</Link>
                <Link to='/nhl'>NHL</Link>
                <Link to='/mlb'>MLB</Link>
            </ul>
        </div>
    )
}

export default Home