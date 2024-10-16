#include <iostream>
#include <cpr/cpr.h>

using namespace std;

int main() {
    // Define the URL of your website
    string url = "http://127.0.0.1:8000/";

    cpr::Payload payload{{"key1", "value1"}, {"key2", "value2"}};

    cpr::Response response = cpr::Post(cpr::Url{url}, payload);

    cout << "Status Code: " << response.status_code << endl; 
    cout << "Response: " << response.text << endl;

    return 0;
}
