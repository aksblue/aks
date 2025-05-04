// Variables used by Scriptable.
// These must be at the very top of the file. Do not edit.
// icon-color: pink; icon-glyph: magic;
/*
Header
Version: 11.0
Author: Aks
Date: 2025 (before March 20)
Description: This script is designed to find the best matching anime based on the search term provided. It compares the search term with a list of anime titles and calculates a match score. If no sufficient match is found, a fallback algorithm is invoked to attempt finding the best match.

New Features:
- Calls an additional fallback algorithm when the primary matching algorithm struggles to find a match.
- Allows toggling between text and JSON format for match data output.

Improvements:
- Refined matching logic with better handling of partial matches in titles.
- Added support for special symbols in titles using a dictionary for substitution.

Known Issues:
- none so far.
- [Any known issues if applicable]

Dependencies:
- External module: anime_algorithm/animeAlgorithmBitBitMatch@2 (for fallback algorithm).

Usage:
1. Provide a search term as input (via shortcutParameter).
2. The script processes the input data, compares it to titles from API data, and calculates a match score.
3. If no match is found, a fallback algorithm is triggered to enhance the match-finding process.
4. The match data is returned in either text or JSON format, based on the matchDataAsText flag.

What’s new:
- The fallback algorithm has been integrated to improve match accuracy when the initial algorithm doesn't provide a strong match.

*/


// Import the fallback algorithm
const secondFindBestMatch = importModule('./anime_algorithm/animeAlgorithmBitBitMatch@2');




// Flag to toggle match data output format
const matchDataAsText = false; // Set to true for current text format, false for JSON format

// Helper: Compare words by parts (with tolerance for partial matches)
function compareParts(word1, word2) {
    // Check if words are an exact match
    if (word1 === word2) {
        return 10; // Exact match
    }

    // Check partial match (e.g., "me" vs "mess")
    let commonLength = 0;
    let minLength = Math.min(word1.length, word2.length);
    
    for (let i = 0; i < minLength; i++) {
        if (word1[i] === word2[i]) {
            commonLength++;
        } else {
            break;
        }
    }

    // If there's a common prefix, give partial score
    if (commonLength > 0) {
        return commonLength; // Partial match score based on common characters
    }

    return 0; // No match
}

// Function to calculate match score
function calculateScore(searchTerm, title) {
    if (!searchTerm || !title) {
        console.error("Missing data: searchTerm or title is undefined or empty.");
        return 0;
    }

    // Normalize the input (trim, lowercase, remove extra spaces)
    searchTerm = searchTerm.trim().replace(/\s+/g, ' ').toLowerCase();
    title = title.trim().replace(/\s+/g, ' ').toLowerCase();
    
    // Check for exact match
    if (searchTerm === title) {
        return 100; // Perfect match
    }

    const searchWords = searchTerm.split(' ');
    let titleWords = title.split(' ');

    let score = 0;

    // Compare each search word with title words
    searchWords.forEach((searchWord) => {
        let matched = false;

        // Look for partial matches in the title words
        for (let i = 0; i < titleWords.length; i++) {
            const matchScore = compareParts(searchWord, titleWords[i]);

            if (matchScore > 0) {
                score += matchScore;
                titleWords.splice(i, 1); // Remove matched word
                matched = true;
                break;
            }
        }

        // If no match is found, adjust the subtraction dynamically
        if (!matched) {
            // Subtract a smaller or larger value depending on the word length
            let penalty = 1;
            if (searchWord.length > 5) { // Larger penalty for longer words
                penalty = 3;
            }
            score -= penalty; // Subtract based on the length of the unmatched word
        }
    });

    // Calculate penalty for extra unmatched words in title
    const extraWordsPenalty = Math.max(0, (titleWords.length / title.split(' ').length) * 10);
    score -= extraWordsPenalty;

    // Ensure score is between 0 and 100
    score = Math.max(0, Math.min(score, 100));

    return score;
}

// Symbol dictionary
const symbolDictionary = {
    "Ω": "omega",
    // You can add more symbols as you find them
};

// Main Logic for handling input and output
if (args.shortcutParameter) {
    let receivedData = args.shortcutParameter;
    let search = receivedData.search;
    let apiData = JSON.parse(receivedData.sent_data);
    let debug = receivedData.debug;
    let send_data_debug = receivedData.send_data_debug;

    let bestMatch = null;
    let highestScore = 0;
    let comparisonLogs = [];

    if (apiData.data) {
        for (let item of apiData.data) {
            if (item.titles && Array.isArray(item.titles)) {
                for (let titleObj of item.titles) {
                    if (titleObj.title) {
                        let title = titleObj.title;

                        // Replace symbols in title with their name equivalents from the dictionary
                        Object.keys(symbolDictionary).forEach((symbol) => {
                            title = title.replace(symbol, symbolDictionary[symbol]);
                        });

                        let matchScore = calculateScore(search, title);

                        let comparisonLog = {
                            title: title,
                            searchTerm: search,
                            matchScore: matchScore
                        };

                        comparisonLogs.push(comparisonLog);

                        // Only consider scores >= 20
                        if (matchScore >= 20 && matchScore > highestScore) {
                            highestScore = matchScore;
                            bestMatch = item;
                        }
                    }
                }
            }
        }
    }
    
    // Fallback: if no match was found in the initial search
    if (!bestMatch) {
        // Create an array of JSON-stringified title objects for the fallback algorithm
        const apiResults = [];
        if (apiData.data) {
            apiData.data.forEach(item => {
                if (item.titles && Array.isArray(item.titles)) {
                    item.titles.forEach(titleObj => {
                        apiResults.push(JSON.stringify(titleObj));
                    });
                }
            });
        }
        
        // Call the fallback algorithm
        let fallbackResult = secondFindBestMatch.find_best_anime_match(search, apiResults);
        
        // If fallback returns a result, use its best_matching_title to redo the search
        if (fallbackResult) {
            let correctedTitle = fallbackResult.best_matching_title;
            for (let item of apiData.data) {
                if (item.titles && Array.isArray(item.titles)) {
                    if (item.titles.some(titleObj => titleObj.title === correctedTitle)) {
                        bestMatch = item;
                        break;
                    }
                }
            }
        }
    }
    
    
    
    

    // Match data output logic
    let matchedData;
    if (matchDataAsText) {
        matchedData = bestMatch
            ? `Title: ${bestMatch.title}\n\nData:\n${JSON.stringify(bestMatch, null, 2)}`
            : "No data found";
    } else {
        matchedData = bestMatch
            ? JSON.stringify(bestMatch, null, 2)
            : JSON.stringify({ message: "No close match found" }, null, 2);
    }

    // Debug and received dictionary control # do not erase this comment is for me to see where the controls are###
// Debug and received dictionary control # do not erase this comment is for me to see where the controls are###
// Debug and received dictionary control # do not erase this comment is for me to see where the controls are###
// Debug and received dictionary control # do not erase this comment is for me to see where the controls are###
    
        //true or false to send debug
    const includeDebugLogs = debug;
    const includeReceivedDictionary = send_data_debug;

    let debugOutput = "";

    if (includeDebugLogs) {
        debugOutput += `
// Comparison Logs:
${JSON.stringify(comparisonLogs, null, 2)}
`;
    }

    if (includeReceivedDictionary) {
        debugOutput += `
// Received Dictionary:
${JSON.stringify({
            search: search,
            sent_data: receivedData.sent_data
        }, null, 2)}
`;
    }

    let output = `
${matchedData}








${debugOutput}
`;

    Script.setShortcutOutput(output);
} else {
    let output = "No input received.";
    Script.setShortcutOutput(output);
}