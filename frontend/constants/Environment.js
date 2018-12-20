import { Constants } from 'expo';

const ENV = {
  dev: {
    apiUrl: 'http://api.midianinja.org:8000/',
  },
  staging: {
    apiUrl: 'http://api.midianinja.org:8000/',
  },
  prod: {
    apiUrl: 'http://api.midianinja.org/',
  },
};

function getEnvVars(env = '') {
  if (env === null || env === undefined || env === '') return ENV.dev;
  if (env.indexOf('dev') !== -1) return ENV.dev;
  if (env.indexOf('staging') !== -1) return ENV.staging;
  if (env.indexOf('prod') !== -1) return ENV.prod;
}

export default getEnvVars(Constants.manifest.releaseChannel);
