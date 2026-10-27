export default function FormField({ placeholder, label, id, type = "text", className = ""}) {
    return (
        <fieldset className="fieldset">
            <label className="label text-black" htmlFor={id}>{label}</label>
            <input type={type} id={id} className={`input border-primary border-2 outline-none ${className}`} placeholder={placeholder} />
        </fieldset>
    );
}