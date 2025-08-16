import { View, Text, TextInput, Button, Alert } from 'react-native';
import React, { useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useRouter } from 'expo-router';

export default function RegisterScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleRegistration = async () => {
    try{
      const res = await fetch('http://192.168.40.14:5000/api/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ email: email, password: password }),
      });

    if (res.ok) {
      const data = await res.json();
      alert("Account created successfully!");
      router.push("/login"); // Redirect to login after successful registration
    } else {
      alert("Error creating account. Please try again.");
    }
    } catch (e) {
      console.error(e);
      alert("An error occurred while trying to create your account");
  };

return (
  <View style={{ padding: 20, backgroundColor: '#84ca8eff', flex: 1 }}>
    <Text style={{ fontSize: 24, marginBottom: 20 }}>Create an Account</Text>

      {/* Input for email */}
      <TextInput 
        placeholder="Email" 
        onChangeText={setEmail} 
        value={email} 
        autoCapitalize="none" 
        style={{ marginVertical: 10, padding: 8, backgroundColor: '#fff' }}
      />

      {/* Input for password */}
      <TextInput 
        placeholder="Password" 
        secureTextEntry 
        onChangeText={setPassword} 
        value={password} 
        style={{ marginVertical: 10, padding: 8, backgroundColor: '#fff' }}
      />

      {/* Create an account button */}
      <Button title="Create an Account" onPress={handleRegistration} />
    </View>
  );
}
}