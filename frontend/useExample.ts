import { useState } from 'react';

const API_URL = import.meta.env.VITE_EXAMPLE_API_URL || '/api/example';

interface RequestData {
  message: string;
}

interface ResponseData {
  message: string;
  received: RequestData;
}

export function useExample() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const sendRequest = async (data: RequestData): Promise<ResponseData> => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });

      if (!response.ok) {
        throw new Error('Request failed');
      }

      return await response.json();
    } catch (err) {
      setError(err as Error);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { sendRequest, loading, error };
}
