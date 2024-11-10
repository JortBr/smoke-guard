using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http.Json;
using System.Diagnostics;

namespace SmartGuard
{
    public class ApiService
    {
        private readonly HttpClient _httpClient;
        private readonly string _apiUrl = "http://192.168.153.127:5000/get_records";

        public ApiService()
        {
            _httpClient = new HttpClient();
        }

        public async Task<List<Record>> GetRecordsAsync()
        {
            try
            {
                Debug.WriteLine("Verzoek wordt verstuurd naar de API...");

                var records = await _httpClient.GetFromJsonAsync<List<Record>>(_apiUrl);

                if (records != null)
                {
                    Debug.WriteLine($"Aantal records ontvangen: {records.Count}");
                }
                else
                {
                    Debug.WriteLine("Geen records ontvangen.");
                }

                return records ?? new List<Record>();
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Fout bij ophalen van data: {ex.Message}");
                return new List<Record>();
            }
        }
    }

    public class Record
    {
        public int Id { get; set; }
        public int Counter { get; set; }
        public DateTime Date { get; set; }
        public int ProfileId { get; set; }
    }
}
