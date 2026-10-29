num_bits = 1000;
Eb_No_dB = 10;

tx_bits = randi([0 1], 1, num_bits);

tx_signal = 2 * tx_bits - 1;

Eb = 1;
No = Eb / (10 ^ (Eb_No_dB / 10));
noise = sqrt(No / 2) * randn(1, num_bits);
rx_signal = tx_signal + noise;

rx_bits = rx_signal > 0;

num_errors = sum(xor(tx_bits, rx_bits));
ber = num_errors / num_bits;
disp([ 'Bit Error Rate (BER): ', num2str(ber) ]);

figure;
subplot(2, 1, 1);
stem(tx_bits(1 : 20), 'filled', 'LineWidth', 2);
title('Transmitted Bits (First 20)');
xlabel('Bit Index');
ylabel('Binary Value');
ylim([-0.5 1.5]);

subplot(2, 1, 2);
plot(rx_signal(1 : 20), 'r-o', 'LineWidth', 2);
title('Received Signal with AWGN (First 20 Samples)');
xlabel('Sample Index');
ylabel('Amplitude');
grid on;