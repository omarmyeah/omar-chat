import Logo from '../components/Logo';
import Card from '../components/Card';
import Footer from '../components/Footer';

const faqs = [
  {
    question: "Is {name} free?",
    answer: "Yes, all features of {name} are completely free."
  },
  {
    question: "How do I login / register?",
    answer: 'Both the Login and Register buttons are located on the navigation bar (The topmost bar where "{name}." is written). Just click on them and you\'ll be taken to the Login or Register pages.'
  },
  {
    question: "Does {name} actually work as a chat app?",
    answer: "Yes, you can message other users and they'll actually receive the messages on their {name} account."
  },
  {
    question: "What are the limitations of {name}?",
    answer: {
      intro: "Currently, {name} doesn't support the following:",
      limitations: [
        "Voice and video calling",
        "Group chats",
        "AI chats",
        "Posts and stories",
        "Friend lists"
      ]
    }
  }
];

function Welcome() {
  return (
    <div className="md:grid md:grid-cols-2 py-25">
      {/* first column - cold welcome text and punchline*/}
      <div className="col-span-1 py-20 px-20 text-center">
        <h1 className='sm:text-9xl max-sm:text-3xl'>Welcome.</h1>
        <p className='text-2xl'>The next generation of chatting.</p>
      </div>
      {/* second column - image of usage */}
      <div className="col-span-1 px-10">
        <img src="chat-demo.png" alt="A demo of Omar chat" className='border-2 border-base-content' />
      </div>
    </div>
  );
}

function AccordionElement({ title, content }) {
  return (
    <details className="collapse bg-base-100 border border-base-300 mb-0.5 w-3/4 mx-auto" name="my-accordion-det-1">
      <summary className="collapse-title font-semibold">{title}</summary>
      <div className="collapse-content text-sm">{content}</div>
    </details>
  );
}

function FrequentlyAskedQuestions({ questionsArray, name, placeholder }) {
  return (
    <>
      <h1 className="text-5xl text-base-content mt-10 mb-10 text-center">Frequently Asked Questions</h1>
      {/* FAQ Accordion */}
      <div className='mb-10'>
        {questionsArray.map(element => {
          if (typeof element.answer != 'object') {
            return (
              <AccordionElement key={element.question} title={element.question.replace(placeholder, name)} content={element.answer.replace(placeholder, name)} />
            );
          } else {
            return (
                <AccordionElement key={element.question} title={element.question.replace(placeholder, name)} content={
                    <>
                    <p>{element.answer.intro.replace(placeholder, name)}</p>
                    <ul className='list-disc list-inside py-3'>
                        {element.answer.limitations.map((limitation) => {
                            return (
                            <li key={limitation} className='px-5'>{limitation}</li>
                            );
                        })}
                    </ul>
                    </>
                  }/>
            );
          }
        })}
      </div>
    </>
  );
}

export default function Index() {
  return (
    <>
      <Welcome />
      <Card className='w-3/4 mx-auto mb-5'>
          <FrequentlyAskedQuestions questionsArray={faqs} name="Omar Chat" placeholder={"{name}"}/>
      </Card>
    </>
  );
}