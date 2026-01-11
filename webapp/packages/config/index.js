import localConfig from './environments/local.js';

const env = import.meta.env?.VITE_APP_ENV || process.env.APP_ENV || 'local';
console.log(`Using configuration for environment: ${env}`);

let config;

switch (env) {
  case 'firebase':
    // TODO: Add firebase config when needed
    // import firebaseConfig from './environments/firebase.js';
    throw new Error('Firebase configuration not yet implemented. Create environments/firebase.js');
  case 'amplify':
    // TODO: Add amplify config when needed
    throw new Error('Amplify configuration not yet implemented. Create environments/amplify.js');
  case 'kubernetes':
    // TODO: Add kubernetes config when needed
    throw new Error('Kubernetes configuration not yet implemented. Create environments/kubernetes.js');
  default:
    config = localConfig;
}

config.name = "Gofannon WebApp"
export default config;