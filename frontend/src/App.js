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
            This is a landing page with a full screen video background. Feel free to
            use this landing page in your projects. keep adding sections, change the
            video, content , etc
        </p>
    
        <h2>Follow Me On Social Media</h2>
    
        <div class="social">
        </div>
    </section>
    </div>
  );
}

export default App;
