import { View, Text, TextInput, Button, Alert } from 'react-native';
import React, { useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useRouter } from 'expo-router';

export default function LoginScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleLogin = async () => {
    try{
      const res = await fetch('http://192.168.40.14:5000/api/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ email: email, password: password }),
      });
    

    const data = await res.json();

    if (data.success) {
      await AsyncStorage.setItem('userToken', data.token);
      router.replace('/(tabs)');
    } else {
      Alert.alert('Login Successful', data.message);
    }
    } catch (e){
      Alert.alert('Error', 'Could not authenticate the server. Please try again later.');
    }
  };

return (
    <View style={{ padding: 20,  backgroundColor: '#84ca8eff'}}>
      <Text style={{ fontSize: 24 }}>Log In</Text>

      {/* Input for email */}
      <TextInput 
        placeholder="Email" 
        onChangeText={setEmail} 
        value={email} 
        autoCapitalize="none" 
        style={{ marginVertical: 10 }}
      />

      {/* Input for password */}
      <TextInput 
        placeholder="Password" 
        secureTextEntry 
        onChangeText={setPassword} 
        value={password} 
        style={{ marginVertical: 10 }}
      />

      {/* Log in button */}
      <Button title="Log In" onPress={handleLogin} />
    </View>
  );
}