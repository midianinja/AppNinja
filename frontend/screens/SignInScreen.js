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
      isLoading: false,
    };
  }

  render() {
    return (
      <View style={[theme.container, {flex: 18, paddingVertical: 20}]}>
        <Image style={theme.logo} source={require('../assets/images/logo.png')} />
        <View style={[theme.fullContainer, {flex: 6, paddingVertical: 20}]}>
          <Input placeholder='Usuário' leftIcon={
            <Icon name='user' color='white' />
          } onChangeText={(email) => this.setState({email})} />
          <Input containerStyle={{marginTop: 5}} secureTextEntry placeholder='Senha' leftIcon={
            <Icon name='lock' color='white' />
          } onChangeText={(password) => this.setState({password})} />
          <Button title='LOGIN' onPress={this._signInAsync} />
          <Button {...theme.passwordRecovery} title='Esqueci a senha' onPress={this._passwordResetScreen} />
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
        <Overlay isVisible={this.state.isLoading}>
          <ActivityIndicator size='large' color='white'/>
        </Overlay>
      </View>
    );
  }

  _signInAsync = async () => {
    this.setState({isLoading: true});

    fetch(process.env.API_URL + 'api/auth/login/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: this.state.email,
        password: this.state.password,
      }),
    }).then((response) => {
      this.setState({isLoading: false});
      let data = response.json();
      await AsyncStorage.setItem('userToken', data.data.token);
      console.log('token:', data.data.token);
      this.props.navigation.navigate('App');
    }).catch((error) => {
      this.setState({isLoading: false});
      let data = error.json();
      this.setState({ isLoading: false });
      showMessage({
        message: 'Erro',
        description: data.message,
        type: 'danger',
      });
    });
  };

  _passwordResetScreen = () => {
    this.props.navigation.navigate('PasswordReset');
  };

  _signUpScreen = () => {
    this.props.navigation.navigate('SignUp');
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

