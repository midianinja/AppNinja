import React from 'react';
import {
  ActivityIndicator,
  AsyncStorage,
  StatusBar,
  StyleSheet,
  View,
  Text,
  Image,
} from 'react-native';

export default class AuthLoadingScreen extends React.Component {
  constructor(props) {
    super(props);
    this._bootstrapAsync();
  }

  // Fetch the token from storage then navigate to our appropriate place
  _bootstrapAsync = async () => {
    const splashScreenDelay = 2000;
    const userToken = await AsyncStorage.getItem('userToken');

    // This will switch to the App screen or Auth screen and this loading
    // screen will be unmounted and thrown away.
    setTimeout(() => this.props.navigation.navigate(userToken ? 'App' : 'Auth'), splashScreenDelay);
  };

  // Render any loading content that you like here
  render() {
    return (
      <View style={styles.container}>
        <Image style={styles.splashScreen} source={require('../assets/images/splash.jpg')} />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  splashScreen: {
    height: '100%',
    width: '100%',
  },
});
