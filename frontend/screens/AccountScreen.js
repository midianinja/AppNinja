import React from 'react';
import {
  Input,
  Icon,
  Text,
  Divider,
  Overlay,
  Button,
} from 'react-native-elements';
import {
  View,
  ScrollView,
  StyleSheet,
  Image,
  AsyncStorage,
  ActivityIndicator,
  KeyboardAvoidingView,
  TouchableOpacity,
} from 'react-native';
import { showMessage } from 'react-native-flash-message';
import theme from '../constants/Theme';

export default class AccountScreen extends React.Component {
  static navigationOptions = {
    header: null,
  };

  constructor(props) {
    super(props);

    this.state = {
      imageUrl: '',
      nome: '',
      cidade: '',
      estado: '',
      pais: '',
      telefone: '',
      nascimento: '',
      etnia: '',
      genero: '',
      orientacao: '',
      facebook: '',
      instagram: '',
      telegram: '',
      causas: '',
      identidade: '',
      profissao: '',
      bio: '',
      editing: false,
      isLoading: false,
    };

    this._loadInformation();
  }

  render() {
    return (
      <KeyboardAvoidingView behavior='padding' enabled style={{flex: 1, padding: 0}}>
        <ScrollView style={theme.accountContainer}>
          <View style={theme.accountHeaderContainer}>
            <Image style={theme.accountHeaderImage} source={require('../assets/images/icon.png')} />
            <View style={theme.avatarContainer}>
              <Image style={theme.avatar} source={this.state.imageUrl ? {uri: this.state.imageUrl} : require('../assets/images/logo.png')} />
              <Icon size={20} containerStyle={{position: 'absolute', bottom: 4, left: 40}} name='camera' color='white'/>
            </View>
          </View>
          <View style={{alignItems: 'center', justifyContent: 'center', paddingBottom: 40}} >
            <Text style={{color: 'black', fontSize: 22}}>{this.state.nome || '#Ninja#' }</Text>
            <View style={{flexDirection: 'row', alignItems: 'center', justifyContent: 'center'}} >
              <Icon containerStyle={{padding: 5}} size={15} name='map-marker' />
              <Text style={{color: 'black', fontSize: 18}}>{this.state.estado || 'Além'}</Text>
            </View>
          </View>
          <View style={theme.accountInputsContainer}>
            <Input {...theme.accountInput} label='Nome' editable={this.state.editing} onChangeText={(nome) => this.setState({nome})} value={this.state.nome} />
            <Input {...theme.accountInput} label='Cidade' editable={this.state.editing} onChangeText={(cidade) => this.setState({cidade})} value={this.state.cidade} />
            <Input {...theme.accountInput} label='Estado' editable={this.state.editing} onChangeText={(estado) => this.setState({estado})} value={this.state.estado} />
            <Input {...theme.accountInput} label='País' editable={this.state.editing} onChangeText={(pais) => this.setState({pais})} value={this.state.pais} />
            <Input {...theme.accountInput} label='Bio' editable={this.state.editing} onChangeText={(bio) => this.setState({bio})} value={this.state.bio} />
            <Input {...theme.accountInput} label='Telefone' editable={this.state.editing} onChangeText={(telefone) => this.setState({telefone})} value={this.state.telefone} />
            <Input {...theme.accountInput} label='Nascimento' editable={this.state.editing} onChangeText={(nascimento) => this.setState({nascimento})} value={this.state.nascimento} />
            <Input {...theme.accountInput} label='Etnia' editable={this.state.editing} onChangeText={(etnia) => this.setState({etnia})} value={this.state.etnia} />
            <Input {...theme.accountInput} label='Gênero' editable={this.state.editing} onChangeText={(genero) => this.setState({genero})} value={this.state.genero} />
            <Input {...theme.accountInput} label='Orientação' editable={this.state.editing} onChangeText={(orientacao) => this.setState({orientacao})} value={this.state.orientacao} />
            <Input {...theme.accountInput} label='Facebook' editable={this.state.editing} onChangeText={(facebook) => this.setState({facebook})} value={this.state.facebook} />
            <Input {...theme.accountInput} label='Instagram' editable={this.state.editing} onChangeText={(instagram) => this.setState({instagram})} value={this.state.instagram} />
            <Input {...theme.accountInput} label='Telegram' editable={this.state.editing} onChangeText={(telegram) => this.setState({telegram})} value={this.state.telegram} />
            <Input {...theme.accountInput} label='Causas' editable={this.state.editing} onChangeText={(causas) => this.setState({causas})} value={this.state.causas} />
            <Input {...theme.accountInput} label='Identidade' editable={this.state.editing} onChangeText={(identidade) => this.setState({identidade})} value={this.state.identidade} />
            <Input {...theme.accountInput} label='Profissão' editable={this.state.editing} onChangeText={(profissao) => this.setState({profissao})} value={this.state.profissao} />
            {this.state.editing && <View style={{alignItems: 'center', justifyContent: 'center'}}>
              <Button containerStyle={{marginBottom: 20}} title='SALVAR ALTERAÇÕES' onPress={this._saveInformation} />
            </View>}
          </View>
        </ScrollView>
        {!this.state.editing && <TouchableOpacity style={theme.accountEditButton} onPress={() => this.setState({editing: !this.state.editing})}>
          <Icon size={20} name='pencil' color='white' />
        </TouchableOpacity>}
        <Overlay isVisible={this.state.isLoading}>
          <ActivityIndicator size='large' color='white'/>
        </Overlay>
      </KeyboardAvoidingView>
    );
  }

  _saveInformation = async () => {
    this.setState({editing: false, isLoading: true});

    let fields = [
      'nome',
      'cidade',
      'estado',
      'pais',
      'telefone',
      'nascimento',
      'etnia',
      'genero',
      'orientacao',
      'facebook',
      'instagram',
      'telegram',
      'causas',
      'identidade',
      'profissao',
      'bio',
    ];

    let data = fields.reduce((acc, el) => {
      acc[el] = this.state[el];
      return acc;
    }, {});

    console.log(data);

    let dataString = JSON.stringify(data);
    let userToken = await AsyncStorage.getItem('userToken');
    await AsyncStorage.setItem('user', dataString);

    let response = await fetch(process.env.API_URL + 'api/account/cadastro/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        Authorization: 'Token ' + userToken,
      },
      body: dataString,
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
        description: 'Ocorreu um erro ao salvar os seus dados :(',
        type: 'danger',
      });
    } else {
      showMessage({
        message: 'Sucesso!',
        description: 'Seus dados foram salvos :D',
        type: 'success',
      });
    }
  };

  _loadInformation = async () => {
    let userDataString = await AsyncStorage.getItem('user');

    if (userDataString) {
      let userData = JSON.parse(userDataString);
      this.setState(userData);
      return;
    }

    let userToken = await AsyncStorage.getItem('userToken');

    let response = await fetch(process.env.API_URL + 'api/account/', {
      method: 'GET',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        Authorization: 'Token ' + userToken,
      },
    });

    if (!response || !response.ok) {
      console.log(response);

      showMessage({
        message: 'Erro',
        description: 'Ocorreu um erro ao obter os seus dados :(',
        type: 'danger',
      });
    } else {
      let data = await response.json();
      this.setState(data.data);
    }
  };
}

