import './App.css'

function App() {

  return (
    <>
      <div className='container'>
        <div className='seccion-login'>
          <div className='card card-informative'>
            <div className='container-title'>
              <span className='anton-regular title-1'>CLEAN</span>
              <span className='anton-regular title-2'>STOCK</span>
            </div>
            <p className='presentation'>
              CleanStock es una aplicación innovadora diseñada para optimizar la gestión de inventarios en las organizaciones. Nuestra app facilita el análisis y la administración eficiente de productos, proporcionando a nuestros clientes una visión integral y estratégica de sus inventarios. Inicialmente, CleanStock estará disponible como una aplicación web que require conexión a internet. Sin embargo, nuestro objectivo a largo plazo es desarrollar una version movil que permita a los usuarios gestionar sus inventarios de manera efectiva, incluso sin conexión a internet.
            </p>
          </div>
          <div className='card card-form'>
            <div className='container-phone'>
              <div className='user-logo'></div>
              <div className='form-login'>
                <div>
                  <div className='container-input'>
                    <span className="material-symbols-outlined">person</span>
                    <input type="text" name='userName' placeholder='User name' className='input-login'/>
                  </div>
                  <div className='container-input'>
                    <span className="material-symbols-outlined">lock_open</span>
                    <input type="password" name='password' placeholder='Password' className='input-login'/>
                  </div>
                </div>
                <button className='button-login'>Login</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
