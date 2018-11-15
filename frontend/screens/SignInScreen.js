import React from 'react';
import {
  ActivityIndicator,
  AsyncStorage,
  StatusBar,
  StyleSheet,
  View,
  Text,
  Button,
} from 'react-native';

export default class SignInScreen extends React.Component {
  static navigationOptions = {
    title: 'Please sign in',
  };

  render() {
    return (
      <View style={styles.container}>
        <Button title="Sign in!" onPress={this._signInAsync} />
      </View>
    );
  }

  _signInAsync = async () => {
    await AsyncStorage.setItem('userToken', 'abc');
    this.props.navigation.navigate('App');
  };
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
  },
});
