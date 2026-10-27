import { useState } from 'react';
import Navbar from '../components/Navbar';
import Logo from '../components/Logo';
import GradientDiv from '../components/GradientDiv';
import Card from '../components/Card';

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
        <img src="chat-demo.png" alt="A demo of Omar chat" className='border-2 border-black' />
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
      <h1 className="text-5xl text-black mt-10 mb-10 text-center">Frequently Asked Questions</h1>
      {/* FAQ Accordion */}
      <div className='mb-10'>
        {questionsArray.map(element => {
          if (typeof element.answer != 'object') {
            return (
              <AccordionElement title={element.question.replace(placeholder, name)} content={element.answer.replace(placeholder, name)} />
            );
          } else {
            return (
                <AccordionElement title={element.question.replace(placeholder, name)} content={
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

function Footer({ Logo }) {
  return (
    <footer className="footer footer-horizontal footer-center bg-black text-primary-content p-5 mt-10">
      <aside>
        {Logo}
      </aside>
      <nav>
        <div className="grid grid-flow-col gap-4">
          <a 
            href="https://github.com/omarmyeah" 
            target="_blank" 
            rel="noopener noreferrer" 
            aria-label="GitHub Profile"
          >
            <svg 
              role="img" 
              viewBox="0 0 24 24" 
              xmlns="http://www.w3.org/2000/svg"
              className="w-6 h-6 fill-current"
            >
              <title>GitHub</title>
              <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
            </svg>
          </a>
        </div>
      </nav>
    </footer>
  );
}

export default function Index() {
  return (
    <>
    <GradientDiv>
        <Navbar clickableItems={[{'Login':'login'}, {'Register':'register'}]}/>
        <Welcome />
        <Card className='w-3/4 mx-auto'>
            <FrequentlyAskedQuestions questionsArray={faqs} name="Omar Chat" placeholder={"{name}"}/>
        </Card>
        <Footer Logo={<Logo />}/>
    </GradientDiv>
    </>
  );
}