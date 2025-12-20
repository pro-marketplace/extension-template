import { useExample } from './useExample';

interface Props {
  onSuccess?: () => void;
  onError?: (error: Error) => void;
}

export function ExampleComponent({ onSuccess, onError }: Props) {
  const { sendRequest, loading } = useExample();

  const handleClick = async () => {
    try {
      await sendRequest({ message: 'test' });
      onSuccess?.();
    } catch (error) {
      onError?.(error as Error);
    }
  };

  return (
    <button onClick={handleClick} disabled={loading}>
      {loading ? 'Загрузка...' : 'Отправить'}
    </button>
  );
}
