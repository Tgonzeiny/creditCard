import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';
import React, { useState } from 'react';
import { useRouter } from 'expo-router';

export default function RegisterScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleRegistration = async () => {
    try{
      const res = await fetch('http://192.168.40.15:5000/api/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ email: email, password: password }),
      });

    if (res.ok) {
      const data = await res.json();
      alert("Account created successfully!");
      router.navigate("/login"); // Redirect to login after successful registration
    } else {
      alert("Error creating account. Please try again.");
    }
    } catch (e) {
      console.error(e);
      alert("An error occurred while trying to create your account");
  };
}

// Styles for the registration screen
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f8fafc",
    alignItems: "center",
    justifyContent: "center",
    padding: 24,
  },
  title: {
    fontSize: 32,
    fontWeight: "700",
    color: "#1e293b",
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: "#64748b",
    marginBottom: 32,
    textAlign: "center",
  },
  input: {
    width: "100%",
    backgroundColor: "#fff",
    paddingVertical: 14,
    paddingHorizontal: 16,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: "#e2e8f0",
    marginBottom: 16,
    fontSize: 16,
    color: "#1e293b",
    shadowColor: "#000",
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: 1 },
    shadowRadius: 2,
  },
  button: {
    backgroundColor: "#3b82f6",
    paddingVertical: 14,
    paddingHorizontal: 30,
    borderRadius: 30,
    marginBottom: 20,
    width: "100%",
    alignItems: "center",
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "600",
  },
  linkText: {
    color: "#3b82f6",
    fontSize: 14,
    marginTop: 8,
  },
});

// Render the registration screen
return (
  <View style={styles.container}>
    <Text style={styles.title}>Create an Account</Text>
    <Text style={styles.subtitle}>Sign up to start earning rewards</Text>

    {/* Email input */}
    <TextInput
      placeholder="Email"
      placeholderTextColor="#94a3b8"
      onChangeText={setEmail}
      value={email}
      autoCapitalize="none"
      style={styles.input}
    />

    {/* Password input */}
    <TextInput
      placeholder="Password"
      placeholderTextColor="#94a3b8"
      secureTextEntry
      onChangeText={setPassword}
      value={password}
      style={styles.input}
    />

    {/* Submit button */}
    <TouchableOpacity style={styles.button} onPress={handleRegistration}>
      <Text style={styles.buttonText}>Sign Up</Text>
    </TouchableOpacity>

    {/* Back to login */}
    <TouchableOpacity onPress={() => router.navigate('/login')}>
      <Text style={styles.linkText}>Already have an account? Log in</Text>
    </TouchableOpacity>
  </View>
);

}