import { Slot, useRouter, useSegments, Tabs } from 'expo-router';
import { useEffect, useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function RootLayout() {
  const[isAuthenticated, setIsAuthenticated] = useState<boolean | null>(null);
  const segments = useSegments();
  const router = useRouter();

  useEffect(() => {
    const checkAuthentication = async () => {
      const token = await AsyncStorage.getItem('userToken');
      setIsAuthenticated(!!token);
    };

    checkAuthentication();
  }, []);

  //If not logged in redirect to welcome screen
  useEffect(() => {
    if (isAuthenticated === false) {
      const currentRoute = segments[0];
      const allowedRoutes = ['login', 'register', ''];

      if (!allowedRoutes.includes(currentRoute)) {
        router.replace('/');
      }
    }
  }, [segments, isAuthenticated]);

  // Wait until authentication status is determined
  if (isAuthenticated === null)  return null;

  return <Slot />;
}
