import './App.css';
import backgroundVideo from "./assets/background.mp4"
function App() {
  return (
    <div className="App">
      <section class="showcase">
        <div class="video-container">
          <video autostart autoPlay muted loop src={backgroundVideo} type="video/mp4" />
        </div>
        <div class="content">
            <h1>Shoot For The Stars</h1>
            <h3>Welcome to Space Blogs!</h3>
            <a href="#about" class="btn">Go Beyond</a>
        </div>
    </section>
    
    <section id="about">
        <h1>About</h1>
        <p>
            Space blogs is your one stop for the latest news and insightful articles
            about space.
        </p>
    </section>
    </div>
  );
}

export default App;
