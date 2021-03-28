import axios from 'axios';
import {API_HOST, API_PORT} from "@/api.config";


export function filterBadWords(rawPhrase, locale = 'en_US') {
    return new Promise(function (resolve) {
        axios.get(`${API_HOST}:${API_PORT}/api/filter-bad-words/${locale}/`, {
            params: {
                raw_phrase: rawPhrase,
            }
        })
            .then(response => {
                resolve({
                    filteredText: response.data.filtered_phrase,
                })
            })
            .catch(error => {
                resolve({
                    filteredText: error.response?.data.filtered_phrase || '',
                    errorText: error.response?.data.error_message || '',
                })
            })
    })
}
