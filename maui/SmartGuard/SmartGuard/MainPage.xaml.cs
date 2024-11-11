using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;
using Microsoft.Maui.Controls;
using System.IO.Ports;
using SmartGuard;

namespace SmokeGuard
{
    public partial class MainPage : ContentPage
    {
        private SerialPort serialPort;
        private int limit = 0;
        private readonly ApiService _apiService;

        public MainPage()
        {
            InitializeComponent();
            InitializeSerialPort();
            _apiService = new ApiService();
            LoadDataAsync();
        }

        private void InitializeSerialPort()
        {
            try
            {
                serialPort = new SerialPort("COM3", 9600);
                serialPort.Open();
            }
            catch (Exception ex)
            {
                DisplayAlert("Error", $"Kan seriële poort niet openen: {ex.Message}", "OK");
            }
        }

        private async Task LoadDataAsync()
        {
            try
            {
                // Haal records op via de API
                var records = await _apiService.GetRecordsAsync();

                Debug.WriteLine("API call gestart");

                foreach (var record in records)
                {
                    Debug.WriteLine($"ID: {record.Id}, Counter: {record.Counter}, Date: {record.Date}, ProfileId: {record.ProfileId}");
                }

                RecordsListView.ItemsSource = records;
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error loading data: {ex.Message}");
                await DisplayAlert("Fout", $"Er is een fout opgetreden: {ex.Message}", "OK");
            }
        }

        private void OnConfirmLimitButtonClicked(object sender, EventArgs e)
        {
            if (int.TryParse(LimitEntry.Text, out int userLimit))
            {
                limit = userLimit;
                DisplayAlert("Limiet Bevestigd", $"Uw limiet is ingesteld op {limit} sigaretten.", "OK");

                // Stuur het limiet naar de Arduino
                SendLimitToArduino(limit);
            }
            else
            {
                DisplayAlert("Ongeldige invoer", "Voer een geldig nummer in voor het limiet.", "OK");
            }
        }

        // Methode om het limiet naar de Arduino te sturen
        private void SendLimitToArduino(int limit)
        {
            if (serialPort != null && serialPort.IsOpen)
            {
                serialPort.WriteLine(limit.ToString());
            }
            else
            {
                DisplayAlert("Error", "Seriële poort is niet open.", "OK");
            }
        }
    }
}