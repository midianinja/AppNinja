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
import Env from '../constants/Environment';

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

    let formData = new FormData();
    formData.append("email", this.state.email);

    let response = await fetch(Env.apiUrl + 'api/account/users/send-recover/', {
      method: 'POST',
      body: formData,
    });

    this.setState({isLoading: false});

    if (!response) {
      showMessage({
        message: 'Erro',
        description: 'Ocorreu um erro de comunicação com o servidor',
        type: 'danger',
      });
    } else if (!response.ok) {
      showMessage({
        message: 'Erro',
        description: 'E-mail não encontrado',
        type: 'danger',
      });
    } else {
      showMessage({
        message: 'Email enviado',
        description: 'Um email foi enviado para a redefinição da sua senha',
        type: 'success',
      });

      this.props.navigation.navigate('App');
    }
  };

  _checkIfEnabled = () => {
    this.setState({ disabled: !this.state.email });
  };
}

