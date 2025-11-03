import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function Home() {
  return (
    <View style={styles.container}>
      {/* Main content area */}
      <View style={styles.content}>
        <Text style={styles.title}>Welcome to CardWise</Text>
        <Text style={styles.subtitle}>
          Manage your credit cards and get the best recommendations
        </Text>
      </View>

      {/* Bottom bar */}
      <View style={styles.bottomBar}>
        <TouchableOpacity style={styles.barButton}>
          <Text style={styles.barButtonText}>Add Cards</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.barButton}>
          <Text style={styles.barButtonText}>Suggest Cards</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f8fafc",
  },
  content: {
    flex: 1,
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
  bottomBar: {
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    backgroundColor: "#fff",
    paddingVertical: 14,
    borderTopWidth: 1,
    borderTopColor: "#e2e8f0",
    shadowColor: "#000",
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: -1 },
    shadowRadius: 2,
  },
  barButton: {
    backgroundColor: "#3b82f6",
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 20,
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
  },
  barButtonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "600",
  },
});