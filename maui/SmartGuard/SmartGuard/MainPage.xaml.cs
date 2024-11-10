using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;
using Microsoft.Maui.Controls;
using SmartGuard;

namespace SmokeGuard
{
    public partial class MainPage : ContentPage
    {
        private readonly ApiService _apiService;

        public MainPage()
        {
            InitializeComponent();
            _apiService = new ApiService();
            LoadDataAsync();
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
            string limit = LimitEntry.Text;

            if (int.TryParse(limit, out int weeklyLimit) && weeklyLimit > 0)
            {
                DisplayAlert("Bevestigd", $"Uw wekelijkse limiet is ingesteld op {weeklyLimit} sigaretten.", "OK");
            }
            else
            {
                DisplayAlert("Fout", "Vul een geldig nummer in voor de limiet.", "OK");
            }
        }
    }
}