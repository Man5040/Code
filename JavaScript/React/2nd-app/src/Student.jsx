
import PropTypes from "prop-types"

function Student(props){
    return(
        <div className="student">
            <p>Name: {propos.name}</p>
            <p>age: {propos.age}</p>
            <p>Student: {propos.isStudent ? Yes : No}</p>
        </div>
    );
}

Student.PropTypes = {
    name: PropTypes.string,
    age:  PropTypes.age,
    isStudent: PropTypes.bool
}

Student.defaultPropos = {
    name: "Guest",
    age: 0,
    isStudent: false
}






