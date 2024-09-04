import './App.css'

function App() {

  return (
    <>
      <div className='container'>
        <div className='seccion-login'>
          <div className='card card-informative'>
            <img src="https://www.sitew.com/images/blog/articles/guides_users_es/seo_simple/ejemplos_logos/starbucks_es.png" alt="CleanStock logo" className='logo-clean-stock'/>
            <p>
              CleanStock es una aplicación innovadora diseñada para optimizar la gestión de inventarios en las organizaciones. Nuestra app facilita el análisis y la administración eficiente de productos, proporcionando a nuestros clientes una visión integral y estratégica de sus inventarios. Inicialmente, CleanStock estará disponible como una aplicación web que require conexión a internet. Sin embargo, nuestro objectivo a largo plazo es desarrollar una version movil que permita a los usuarios gestionar sus inventarios de manera efectiva, incluso sin conexión a internet.
            </p>
          </div>
          <div className='card card-form'>
            <h1>Card 1</h1>
            <input type="text" name='userName' placeholder='User name'/>
            <input type="text" name='password' placeholder='Password'/>
            <button>Login</button>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
