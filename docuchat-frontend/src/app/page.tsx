"use client";

import { useEffect, useState } from "react";
import { apiService } from "@/services/api";

export default function Home() {
  const [status, setStatus] = useState<string>("Loading...");

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const data = await apiService.getHealthStatus();
        setStatus(typeof data === "object" ? JSON.stringify(data, null, 2) : data);
      } catch (error: any) {
        setStatus(`Error: ${error.message}`);
      }
    };

    checkHealth();
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 w-full max-w-2xl items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-8 text-center">DocuChat Frontend</h1>
        <div className="p-8 border border-gray-200 dark:border-gray-800 rounded-lg bg-gray-50 dark:bg-gray-900 shadow-sm text-center">
          <h2 className="text-xl font-semibold mb-4">API Health Status</h2>
          <pre className="text-left bg-gray-100 dark:bg-black p-4 rounded overflow-auto">
            {status}
          </pre>
        </div>
      </div>
    </main>
  );
}
