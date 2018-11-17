import React from 'react';
import {
  Input,
  Button,
  Icon,
  Text,
  Divider,
} from 'react-native-elements';
import {
  View,
  StyleSheet,
  Image,
  AsyncStorage,
} from 'react-native';
import theme from '../constants/Theme';

export default class SignInScreen extends React.Component {
  static navigationOptions = {
    header: null,
  };

  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: '',
    };
  }

  render() {
    return (
      <View style={[theme.container, {flex: 18, paddingVertical: 20}]}>
        <Image style={theme.logo} source={require('../assets/images/logo.png')} />
        <View style={[theme.fullContainer, {flex: 6, paddingVertical: 20}]}>
          <Input placeholder='Usuário' leftIcon={
            <Icon name='user' color='white' />
          } />
          <Input containerStyle={{marginTop: 5}} secureTextEntry placeholder='Senha' leftIcon={
            <Icon name='lock' color='white' />
          } />
          <Button title='LOGIN' onPress={this._signInAsync} />
          <Button {...theme.passwordRecovery} title='Esqueci a senha' onPress={this._passwordRecoveryScreen} />
        </View>
        <View style={[theme.fullContainer, {paddingTop: 20}]}>
          <Text>_____________     Ou acesse com     _____________</Text>
          <View style={theme.containerSocialMedia}>
            <Icon name='facebook' {...theme.iconSecondary} onPress={this._signInWithFacebook} />
            <Icon name='twitter' {...theme.iconSecondary} onPress={this._signInWithTwitter} />
            <Icon name='google' {...theme.iconSecondary} onPress={this._signInWithGoogle} />
          </View>
        </View>
        <View style={[theme.fullContainer, {paddingVertical: 20}]}>
          <Text>Não tem uma conta?</Text>
          <Button title='CRIAR UMA CONTA' {...theme.buttonSecondary} onPress={this._signUpScreen} />
        </View>
      </View>
    );
  }

  _signInAsync = async () => {
    await AsyncStorage.setItem('userToken', 'abc');
    this.props.navigation.navigate('App');
  };

  _passwordRecoveryScreen = () => {
    this.props.navigation.navigate();
  };

  _signUpScreen = () => {
    this.props.navigation.navigate();
  };

  _signInWithFacebook = () => {
    console.log('Sign in with Facebook...');
  };

  _signInWithTwitter = () => {
    console.log('Sign in with Twitter...');
  };

  _signInWithGoogle = () => {
    console.log('Sign in with Google...');
  };
}

