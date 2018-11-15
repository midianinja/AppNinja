import React from 'react';
import { createSwitchNavigator, createStackNavigator } from 'react-navigation';
import MainTabNavigator from './MainTabNavigator';

// Import Screens
import AuthLoadingScreen from '../screens/AuthLoadingScreen';
import SignInScreen from '../screens/SignInScreen';
import HomeScreen from '../screens/HomeScreen';

// Create Navigation
const AuthStack = createStackNavigator({ SignIn: SignInScreen });

export default createSwitchNavigator(
  {
    AuthLoading: AuthLoadingScreen,
    App: MainTabNavigator,
    Auth: AuthStack,
  },
  {
    initialRouteName: 'AuthLoading',
  }
);
