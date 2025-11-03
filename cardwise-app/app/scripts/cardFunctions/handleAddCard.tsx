import { Alert } from "react-native";

const handleAddCard = async(cardID) => {
    const username = await AsyncStorage.getItem('username');
    try {
        const response = await fetch('http://192.168.40.15:5000/api/addCard', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ username: username, cardID: cardID }),
        });

    const data = await response.json();
    Alert.alert(data.success ? "Success" : "Error", data.message);
    } catch (e) {
        Alert.alert("Error", "Could not connect to the server");
    }
}