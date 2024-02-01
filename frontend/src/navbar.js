import {Link, useMatch, useResolvedPath} from "react-router-dom"

export default function Navbar() {
    const path = window.location.pathname
    return (
        <nav className="nav">
            <Link to="/" className="site-title">Site Name</Link>
            <ul>
                <CustomLink to="/pricing">Pricing</CustomLink>
                <CustomLink to="/about">About</CustomLink>
            </ul>
        </nav>
    )
}

function CustomLink({to, children, ...props}){
    const resolvedPath = useResolvedPath(to)
    const is_active = useMatch({
        path: resolvedPath.pathname,
        end: true
    })
    return (
        <li className={is_active ? "active" : ""}>
            <Link to={to} {...props}>
                {children}
            </Link>
        </li>
    )
}