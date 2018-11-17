import { Platform } from 'react-native';

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
    flex: 1,
    alignItems: 'center',
    backgroundColor: '#020500',
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
};
