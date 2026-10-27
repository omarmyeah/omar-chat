export default function FormSubmissionButton({className = "", name, type = "submit"}) {
    return (
        <button type={type} className={`btn bg-base-200 text-white border-2 border-transparent hover:text-primary hover:border hover:border-primary focus-visible:border-2 focus-visible:border-primary ${className}`}>{name}</button>
    );
}