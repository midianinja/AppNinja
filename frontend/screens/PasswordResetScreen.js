import React from 'react';
import {
  Input,
  Button,
  Icon,
  Text,
  Divider,
  Overlay,
} from 'react-native-elements';
import {
  View,
  StyleSheet,
  Image,
  AsyncStorage,
  ActivityIndicator,
  KeyboardAvoidingView,
} from 'react-native';
import { showMessage } from 'react-native-flash-message';
import theme from '../constants/Theme';

export default class PasswordResetScreen extends React.Component {
  static navigationOptions = {
    header: null,
  };

  constructor(props) {
    super(props);

    this.state = {
      email: '',
      isLoading: false,
      disabled: true,
    };
  }

  render() {
    return (
      <View style={theme.container}>
        <Image style={theme.logo} source={require('../assets/images/logo.png')} />
        <KeyboardAvoidingView behavior='padding' enabled style={[theme.fullContainer, {flex: 6, paddingVertical: 20}]}>
          <Input placeholder='E-mail' leftIcon={
            <Icon name='user' color='white' />
          } onChangeText={(email) => this.setState({email}, this._checkIfEnabled)} value={this.state.email} keyboardType= 'email-address' />
          <Button title='REDEFINIR SENHA' onPress={this._passwordResetAsync} disabled={this.state.disabled} />
        </KeyboardAvoidingView>
        <Overlay isVisible={this.state.isLoading}>
          <ActivityIndicator size='large' color='white'/>
        </Overlay>
      </View>
    );
  }

  _passwordResetAsync = async () => {
    this.setState({ isLoading: true });

    fetch(process.env.API_URL + 'password_reset/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: this.state.email,
      }),
    }).then((response) => {
      let data = response.json();
      showMessage({
        message: 'Email enviado',
        description: 'Um email foi enviado para a redefinição da sua senha',
        type: 'success',
      });
      this.props.navigation.navigate('SignIn');
    }).catch((error) => {
      this.setState({ isLoading: false });
      showMessage({
        message: 'Erro',
        description: 'Ocorreu um erro de comunicação com o servidor',
        type: 'danger',
      });
    });
  };

  _checkIfEnabled = () => {
    this.setState({ disabled: !this.state.email });
  };
}
