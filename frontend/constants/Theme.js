import { Platform } from 'react-native';
import Layout from './Layout';

export default {
  colors: {
    primary: '#020500',
    secondary: '#a81e1c', 
  },
  Input: {
    autoCorrect: false,
    containerStyle: {
      backgroundColor: '#22241f',
    },
    inputStyle: {
      color: '#ffffff',
    },
    inputContainerStyle: {
      borderBottomWidth: 0,
    },
  },
  Button: {
    buttonStyle: {
      height: 50,
      backgroundColor: '#a81e1c',
    },
    containerStyle: {
      marginTop: 20,
      width: '90%',
    },
  },
  Icon: {
    type: 'font-awesome',
    size: 24,
  },
  Text: {
    style: {
      color: '#ffffff',
      fontSize: 14,
    },
  },
  Overlay: {
    windowBackgroundColor: 'rgba(0, 0, 0, .5)',
    overlayBackgroundColor: 'rgba(0, 0, 0, 0)',
    overlayStyle: {
      justifyContent: 'center',
      alignItems: 'center',
      ...Platform.select({
        android: {
          elevation: 0,
        },
        ios: {
          shadowColor: 'rgba(0, 0, 0, 0)',
        },
      }),
    },
  },
  container: {
    flex: 2,
    alignItems: 'center',
    backgroundColor: '#020500',
  },
  fullContainer: {
    flex: 3,
    alignItems: 'center',
    width: '100%',
    margin: 0,
    padding: 0,
  },
  containerSocialMedia: {
    flex: 3,
    width: '90%',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  logo: {
    flex: 6,
    width: '80%',
  },
  buttonSecondary: {
    buttonStyle: {
      backgroundColor: '#ffffff',
    },
    titleStyle: {
      color: '#020500',
    },
  },
  iconSecondary: {
    color: '#020500',
    containerStyle: {
      width: 40,
      height: 40,
      borderRadius: 2,
      backgroundColor: '#ffffff',
      marginHorizontal: 30,
      alignItems: 'center',
      justifyContent: 'center',
    },
  },
  passwordRecovery: {
    buttonStyle: {
      backgroundColor: 'rgba(0, 0, 0, 0)',
    },
    containerStyle: {
      flex: .1,
      flexDirection: 'row',
      marginTop: -10,
      marginLeft: '118%',
    },
    titleStyle: {
      fontSize: 14,
    },
  },
  accountContainer: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
  accountHeaderContainer: {
    width: '100%',
    height: 300,
    borderTopWidth: 30,
    borderColor: '#000000',
  },
  accountInputsContainer: {
    flex: .6,
  },
  accountHeaderImage: {
    width: '100%',
    height: 200,
  },
  avatarContainer: {
    position: 'absolute',
    left: Layout.window.width / 2 - 50,
    bottom: 10,
    backgroundColor: '#000000',
    borderRadius: 100,
  },
  avatar: {
    width: 100,
    height: 100,
    borderRadius: 50,
    borderWidth: 3,
    borderColor: '#ffffff',
  },
  accountInput: {
    containerStyle: {
      width: '100%',
      paddingHorizontal: 15,
      backgroundColor: null,
      paddingBottom: 20,
    },
    inputStyle: {
      color: null,
      height: 25,
      marginLeft: 0,
    },
    inputContainerStyle: {
      borderBottomWidth: 1,
      borderColor: '#9b9b9b',
    },
    labelStyle: {
      color: '#9b9b9b',
      fontWeight: 'normal',
    },
  },
  accountEditButton: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    width: 50,
    height: 50,
    backgroundColor: '#4084ef',
    borderRadius: 25,
    alignItems: 'center',
    justifyContent: 'center',
  },
  debug: {
    borderWidth: 1,
    borderColor: 'red',
  },
};
