# coding: utf-8

"""
    SEOmonitor API Documentation

    `Introduction`  The SEOmonitor API allows you to programmatically access keyword ranking, traffic, and other SEO data from the SEOmonitor platform. You can use the API to build custom reports, automate workflows, and integrate SEOmonitor data into your own applications. The API enables free and unrestricted access to all your data in the platform, for all Tracked Campaigns. Additionally, it provides access to SEOmonitor's curated UK and US keyword database.   `Main Capabilities`  These are the main data sets you can retrieve with the API 3.0 endpoints:  `Campaign-level data`: Campaign details and campaign-wide keyword data, landing page data, groups data, traffic data, content opportunities data, forecast data, or campaign website research data.  `Keyword-level data`: Data for any and all keywords in the campaign, including ranking data, search data, SERP data, competitor data, SEO Opportunity, keyword-level traffic data, content optimization opportunities' data by keyword and keyword-level forecast projections data.  `Keyword group-level data`: Data for any keyword group in the campaign, including aggregated search and SERP data, website Visibility on specific groups, group SEO Opportunity data.  `Landing page-level data`: Data for specific landing pages that are ranking with the keywords in the campaign, including aggregated search and SERP data, SEO Opportunity, and landing page Visibility.  `Organic traffic data`: Data for the website's organic sessions, conversions, and revenue, including traffic data by segments (brand, non-brand, all traffic, and custom user-created traffic segments), by specific keywords and by specific landing pages.  `Keyword & website research data`: Data for any keyword in SEOmonitor's Research database – any domain-level aggregated search, SERP, and ranking data, and keyword-level and keyword list-level metrics, for the tracked website and for any competitor in top 100.  `Forecast data`: Overview data and details for specific Forecast Scenarios and Objectives, and keyword-level forecast data.  `Website content data`: Data related to content optimization opportunities of the tracked website, including landing page and keyword data for each of the content opportunities categories in SEOmonitor's Content Audit platform (Positive and negative correlations with Visibility, Cannibalization issues, Pages serving too many keywords, Keywords with missing pages, Suboptimal keyword inclusion in the title or H1 or page content, Pages with missing title or H1).   `Getting Started`  Log into your SEOmonitor account and retrieve your unique API Token (Account Settings > Edit Profile).  Check out the `quick start guide` to make your first API call.  Read through the `authentication guide` to learn how to properly authenticate your API requests.   `Libraries and SDKs`  SEOmonitor API uses HTTP protocol, which allows the application of our API to almost all programming languages. All the responses are returned in JSON format by default.  For convenience, we offer client libraries for popular programming languages:  JavaScript PHP Python Java   `Support`  Need help using the API, or have general inquiries? Please contact our support team.  For more information about the SEOmonitor platform, you can visit www.seomonitor.com.   `Changelog`      This is the first version of API 3.0. The Changelog page will be updated as we continue to develop new features and improvements.     `Quick Start Guide`  This guide will walk you through making your first API call.  `Get your API key`  First, you'll need to get an API key:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Edit Profile     3. Copy the API Token to use in your API requests  Note: Clicking `Regenerate API Token` will overwrite the current key and you will lose access if you or other users are currently using it.   `Make a request`  Next, we'll use cURL to make a request to get Tracked Campaigns details:      curl --request GET \\     --url https://apix.seomonitor.com/dashboard/v3.0/campaigns/tracked \\     --header 'Accept: application/json' \\     --header 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'  This will retrieve the Tracked Campaigns data for an SEOmonitor account having the following API Token:      'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA'   Let's break down the parts of the request:      - `--request GET` - Make a GET request     - `--url` - The API endpoint URL     - `--header` - Adds the Authorization header with your API key   Handle the response  The API will return a JSON response like this:      {       \"campaign_info\": {         \"id\": \"74516\",         \"name\": \"Asos.com\",          \"company\": \"Asos\",         \"company_id\": \"51256\",         \"domain\": \"www.asos.com\",         \"keyword_count\": 588,          \"date_created\": \"2023-04-25\",         \"location\": \"United Kingdom\",         \"currency\": \"EUR\",         \"mrr\": 3000       },       \"visibility\": {         \"desktop\": {           \"latest\": 0.28,           \"trend_7days\": 0.2,           \"trend_30days\": 0.2         },         \"mobile\": {           \"latest\": 0.27,            \"trend_7days\": 0.2,           \"trend_30days\": 0.2         }       },       \"multiple_locations\": [         {           \"campaign_id\": 12746,           \"location\": \"London, United Kingdom\",           \"visibility\": {             \"desktop\": {               \"latest\": 0.32,               \"trend_7days\": 0.02               \"trend_30days: 0.1               },             \"mobile\": {               \"latest\": 0.33,               \"trend\": 0.03               \"trend_30days\": 0.1                 }             }           }         }       ],       \"health_status\": \"healthy\",       \"objective_status\": {         \"actual_sessions\": 78400,         \"estimated_sessions\": 78400,           \"performance\": 1,         \"status\": \"on_track\",         \"start_month\": \"Jun, 2023\",          \"end_month\": \"Jul, 2024\"       },       \"reporting_status\": \"submitted\",       \"account_manager\": \"Jo Hart\"     }  And that's it! You just made your first API call. Check out the rest of the API reference documentation to see what else you can build.  `Best practices`      - Keep your API key private – do not share your key publicly.     - Do not include your key directly in code that you distribute – use environment variables instead.     - Regenerate your key periodically for improved security.     - Limit API key access to only required endpoints if possible.  `Revoking API keys`  If your API key is compromised, you can revoke it by regenerating the API Token in your SEOmonitor Account Settings. This will immediately invalidate the current key so further requests can't be made.  For any other issues with authentication, contact our support team.   `Retrieve the IDs of the company, campaigns, keywords and keyword groups`  The unique IDs of your company, campaigns, keywords, or keyword groups can be retrieved either from the specific URLs of the platform, or from specific API endpoint responses. Further below you'll find details on these alternatives.   `Company ID`  The company ID can only be retrieved from the platform. Follow these steps:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings > Billing     3. In the Billing section, the platform URL contains the company ID.     E.g.: \"app.seomonitor.com/v2/account/company/51244/billing\" – in this example, the company ID is \"51244\"   `Campaign ID`  To retrieve the campaign ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign by clicking on its name in the Agency Dashboard.     3. By default, the campaign opens in the Rank Tracker view. The platform URL contains the company ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the campaign ID is \"72416\".  To retrieve the campaign ID through the API, make a call through the `Get Tracked Campaigns Details endpoint`. The response will contain the details of the requested Tracked Campaigns, including their IDs, which you can further use in other endpoint requests.   `Keyword ID`  To retrieve the keyword ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword.     3. The platform URL for the keyword view (Keyword Sidebar) contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe=2023-09-04%3A2023-10-04&ksid=7063139\" – in this example, the keyword ID is \"7063139\"   To retrieve the keyword ID through the API, make a call through the `Get Keyword Data endpoint`. The response will contain the details of the requested keywords, including their IDs, which you can further use in other endpoint requests.   `Keyword Group ID`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword group (Groups side-menu).     3. The platform URL for the keyword group view contains the keyword ID.     E.g.: \"https://app.seomonitor.com/v2/72416/manage/strategy/69976/desktop/keywords?timeframe=2023-09-04%3A2023-10-04\" – in this example, the keyword group ID is \"69976\"  To retrieve the keyword group ID through the API, make a call through the `Get Groups List endpoint`. The response will contain the details of the requested keyword groups, including their IDs, which you can further use in other endpoint requests.   `Forecast ID for Scenarios or Objectives`      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and go to Forecast from the main menu (top).     3. Select a Scenario or the Objective (if set). The platform URL for the specific scenario contains the forecast ID.     E.g.: \"https://app.seomonitor.com/v2/forecast/118794/3788\" – in this example, the forecast ID is \"3788\"   To retrieve the forecast ID through the API, make a call through the`Get Forecast Scenarios endpoint`. The response will contain the details of the requested Scenario or Objective, including their IDs, which you can further use in other endpoint requests.   `SERP Feature Abbreviations`  The returned data for some endpoints will contain SERP feature names in abbreviated form.  The returned values for SERP features are abbreviated as follows:      - \"adt\": Ads Pack Top     - \"def\": Definitions      - \"dir\": Directions      - \"fsn\": Featured Snippet      - \"flt\": Flights      - \"htl\": Hotels      - \"img\": Images Pack      - \"job\": Jobs      - \"kng\": Knowledge Graph      - \"geo\": Local Pack      - \"shp\": Product listing      - \"rcp\": Recipes      - \"qns\": Questions      - \"new\": Top Stories      - \"vid\": Video Carousel      - \"app\": Apps    `Rate Limits`  There are request limits in place to prevent abuse and ensure fair usage.   Exceeding the request limits will lead to HTTP 429 responses. If you need higher limits, contact our support team.   `Limits & Quotas`      -------------------------------------------------------------------------     |Limit                                    |  Number of requests              -------------------------------------------------------------------------     |Maximum requests per second              |  10                              -------------------------------------------------------------------------     |Maximum rows per request (Request Quota) |  1000                            -------------------------------------------------------------------------     |Daily Quota                              |  10 000                          -------------------------------------------------------------------------   `Exceeding Limits`  If you exceed the rate limits, you will receive a 429 Too Many Requests response.  Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.  Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   `Increasing Limits`  The default limits allow most normal API usage patterns. However, if you need higher limits, please contact our support team.    Provide details on:      - Your specific use case      - The endpoints you are using     - The increased limits you are looking for  We will review your request and adjust limits where appropriate   `Need Higher Limits?`  For most use cases, the default limits are sufficient. But if you require higher limits, please contact our support team. We will review your use case and adjust limits where appropriate.   `Errors`  SEOmonitor API uses standard HTTP response codes to indicate the success or failure of API requests.   HTTP Status Codes      ----------------------------------------------------------------------------------     | Code  | Description                                                                 ----------------------------------------------------------------------------------     | 200   | Success                                                                     ----------------------------------------------------------------------------------     | 400   | Bad request - the request was malformed or missing required parameters      ----------------------------------------------------------------------------------      | 401   | Unauthorized - invalid or missing API key                                   ----------------------------------------------------------------------------------     | 403   | Forbidden - API key does not have access to the requested resource          ----------------------------------------------------------------------------------     | 404   | Not found - the requested resource does not exist                           ----------------------------------------------------------------------------------     | 429   | Too many requests - rate or quota limit exceeded                            ----------------------------------------------------------------------------------     | 500   | Internal server error - an unexpected error on the API server               ----------------------------------------------------------------------------------     | 50x   | Errors specific to various endpoints                                        ----------------------------------------------------------------------------------   `Error Response Format`  Error responses will be returned in JSON format:      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   The error object contains:  - `message` - A general error message   - `details` - More specific details about the error   `Common Errors`  401 Unauthorized      {       \"error\": {         \"message\": \"Invalid authentication\",         \"details\": [           \"The API key provided is invalid\"          ]       }     }   Details:   This error message indicates there is a problem with the API key:  - The API key is missing from the request  - The key is invalid or incorrect  - The key is expired or revoked   Check that you are sending the correct API key in the Authorization header.  403 Forbidden      {       \"error\": {         \"message\": \"Forbidden access\",         \"details\": [           \"Your API key does not have access to the requested data\"          ]       }     }  Details:  This error message indicates that the API key being used does not have access to perform the requested operation. Ensure the key has the required scopes enabled.   404 Not Found      {       \"error\": {         \"message\": \"Data not found\",         \"details\": [           \"The requested data does not exist.\"          ]       }     }   Details:  This error message indicates that the object specified by the request does not exist. For example, requesting a keyword that is not in your SEOmonitor account.   429 Too Many Requests   Daily Quota Exceeded      {       \"error\": {         \"message\": \"Daily quota exceeded\",         \"details\": [           \"You have exceeded the allowed daily requests\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.   Rate Limit Exceeded      {       \"error\": {         \"message\": \"Rate limit exceeded\",         \"details\": [           \"You have exceeded the allowed requests per second\"          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   500 Internal Server Error       {       \"error\": {         \"message\": \"Internal server error\",         \"details\": [           \"The server encountered an error while processing your requests\"          ]       }     }   Details:  This error message indicates that an unexpected error occurred on the API server. Try the request again later. If the issue persists, contact support.   50X Endpoint-specific errors  You may encounter errors on specific endpoint requests – these are listed and explained under each endpoint page.   Support  If you have any questions about API errors, please contact our support team.   `Changelog`  Version 3.0 (current)   Release Date: ?  This is the first version of the API 3.0.    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: customer.success@seomonitor.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="SEOmonitor API Documentation",
    author_email="customer.success@seomonitor.com",
    url="",
    keywords=["Swagger", "SEOmonitor API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &#x60;Introduction&#x60;  The SEOmonitor API allows you to programmatically access keyword ranking, traffic, and other SEO data from the SEOmonitor platform. You can use the API to build custom reports, automate workflows, and integrate SEOmonitor data into your own applications. The API enables free and unrestricted access to all your data in the platform, for all Tracked Campaigns. Additionally, it provides access to SEOmonitor&#x27;s curated UK and US keyword database.   &#x60;Main Capabilities&#x60;  These are the main data sets you can retrieve with the API 3.0 endpoints:  &#x60;Campaign-level data&#x60;: Campaign details and campaign-wide keyword data, landing page data, groups data, traffic data, content opportunities data, forecast data, or campaign website research data.  &#x60;Keyword-level data&#x60;: Data for any and all keywords in the campaign, including ranking data, search data, SERP data, competitor data, SEO Opportunity, keyword-level traffic data, content optimization opportunities&#x27; data by keyword and keyword-level forecast projections data.  &#x60;Keyword group-level data&#x60;: Data for any keyword group in the campaign, including aggregated search and SERP data, website Visibility on specific groups, group SEO Opportunity data.  &#x60;Landing page-level data&#x60;: Data for specific landing pages that are ranking with the keywords in the campaign, including aggregated search and SERP data, SEO Opportunity, and landing page Visibility.  &#x60;Organic traffic data&#x60;: Data for the website&#x27;s organic sessions, conversions, and revenue, including traffic data by segments (brand, non-brand, all traffic, and custom user-created traffic segments), by specific keywords and by specific landing pages.  &#x60;Keyword &amp; website research data&#x60;: Data for any keyword in SEOmonitor&#x27;s Research database – any domain-level aggregated search, SERP, and ranking data, and keyword-level and keyword list-level metrics, for the tracked website and for any competitor in top 100.  &#x60;Forecast data&#x60;: Overview data and details for specific Forecast Scenarios and Objectives, and keyword-level forecast data.  &#x60;Website content data&#x60;: Data related to content optimization opportunities of the tracked website, including landing page and keyword data for each of the content opportunities categories in SEOmonitor&#x27;s Content Audit platform (Positive and negative correlations with Visibility, Cannibalization issues, Pages serving too many keywords, Keywords with missing pages, Suboptimal keyword inclusion in the title or H1 or page content, Pages with missing title or H1).   &#x60;Getting Started&#x60;  Log into your SEOmonitor account and retrieve your unique API Token (Account Settings &gt; Edit Profile).  Check out the &#x60;quick start guide&#x60; to make your first API call.  Read through the &#x60;authentication guide&#x60; to learn how to properly authenticate your API requests.   &#x60;Libraries and SDKs&#x60;  SEOmonitor API uses HTTP protocol, which allows the application of our API to almost all programming languages. All the responses are returned in JSON format by default.  For convenience, we offer client libraries for popular programming languages:  JavaScript PHP Python Java   &#x60;Support&#x60;  Need help using the API, or have general inquiries? Please contact our support team.  For more information about the SEOmonitor platform, you can visit www.seomonitor.com.   &#x60;Changelog&#x60;      This is the first version of API 3.0. The Changelog page will be updated as we continue to develop new features and improvements.     &#x60;Quick Start Guide&#x60;  This guide will walk you through making your first API call.  &#x60;Get your API key&#x60;  First, you&#x27;ll need to get an API key:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings &gt; Edit Profile     3. Copy the API Token to use in your API requests  Note: Clicking &#x60;Regenerate API Token&#x60; will overwrite the current key and you will lose access if you or other users are currently using it.   &#x60;Make a request&#x60;  Next, we&#x27;ll use cURL to make a request to get Tracked Campaigns details:      curl --request GET \\     --url https://apix.seomonitor.com/dashboard/v3.0/campaigns/tracked \\     --header &#x27;Accept: application/json&#x27; \\     --header &#x27;Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA&#x27;  This will retrieve the Tracked Campaigns data for an SEOmonitor account having the following API Token:      &#x27;eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZW9tb25pdG9yLmNvbSIsImlhdCI6MTY1Mjc4NTcwNCwidXNlcl9pZCI6IjY2NTI5In0.2_l9e7ohs9QHbwmr48mIoEF-QxZHNPFiAzJbMk00jcA&#x27;   Let&#x27;s break down the parts of the request:      - &#x60;--request GET&#x60; - Make a GET request     - &#x60;--url&#x60; - The API endpoint URL     - &#x60;--header&#x60; - Adds the Authorization header with your API key   Handle the response  The API will return a JSON response like this:      {       \&quot;campaign_info\&quot;: {         \&quot;id\&quot;: \&quot;74516\&quot;,         \&quot;name\&quot;: \&quot;Asos.com\&quot;,          \&quot;company\&quot;: \&quot;Asos\&quot;,         \&quot;company_id\&quot;: \&quot;51256\&quot;,         \&quot;domain\&quot;: \&quot;www.asos.com\&quot;,         \&quot;keyword_count\&quot;: 588,          \&quot;date_created\&quot;: \&quot;2023-04-25\&quot;,         \&quot;location\&quot;: \&quot;United Kingdom\&quot;,         \&quot;currency\&quot;: \&quot;EUR\&quot;,         \&quot;mrr\&quot;: 3000       },       \&quot;visibility\&quot;: {         \&quot;desktop\&quot;: {           \&quot;latest\&quot;: 0.28,           \&quot;trend_7days\&quot;: 0.2,           \&quot;trend_30days\&quot;: 0.2         },         \&quot;mobile\&quot;: {           \&quot;latest\&quot;: 0.27,            \&quot;trend_7days\&quot;: 0.2,           \&quot;trend_30days\&quot;: 0.2         }       },       \&quot;multiple_locations\&quot;: [         {           \&quot;campaign_id\&quot;: 12746,           \&quot;location\&quot;: \&quot;London, United Kingdom\&quot;,           \&quot;visibility\&quot;: {             \&quot;desktop\&quot;: {               \&quot;latest\&quot;: 0.32,               \&quot;trend_7days\&quot;: 0.02               \&quot;trend_30days: 0.1               },             \&quot;mobile\&quot;: {               \&quot;latest\&quot;: 0.33,               \&quot;trend\&quot;: 0.03               \&quot;trend_30days\&quot;: 0.1                 }             }           }         }       ],       \&quot;health_status\&quot;: \&quot;healthy\&quot;,       \&quot;objective_status\&quot;: {         \&quot;actual_sessions\&quot;: 78400,         \&quot;estimated_sessions\&quot;: 78400,           \&quot;performance\&quot;: 1,         \&quot;status\&quot;: \&quot;on_track\&quot;,         \&quot;start_month\&quot;: \&quot;Jun, 2023\&quot;,          \&quot;end_month\&quot;: \&quot;Jul, 2024\&quot;       },       \&quot;reporting_status\&quot;: \&quot;submitted\&quot;,       \&quot;account_manager\&quot;: \&quot;Jo Hart\&quot;     }  And that&#x27;s it! You just made your first API call. Check out the rest of the API reference documentation to see what else you can build.  &#x60;Best practices&#x60;      - Keep your API key private – do not share your key publicly.     - Do not include your key directly in code that you distribute – use environment variables instead.     - Regenerate your key periodically for improved security.     - Limit API key access to only required endpoints if possible.  &#x60;Revoking API keys&#x60;  If your API key is compromised, you can revoke it by regenerating the API Token in your SEOmonitor Account Settings. This will immediately invalidate the current key so further requests can&#x27;t be made.  For any other issues with authentication, contact our support team.   &#x60;Retrieve the IDs of the company, campaigns, keywords and keyword groups&#x60;  The unique IDs of your company, campaigns, keywords, or keyword groups can be retrieved either from the specific URLs of the platform, or from specific API endpoint responses. Further below you&#x27;ll find details on these alternatives.   &#x60;Company ID&#x60;  The company ID can only be retrieved from the platform. Follow these steps:      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Go to Account Settings &gt; Billing     3. In the Billing section, the platform URL contains the company ID.     E.g.: \&quot;app.seomonitor.com/v2/account/company/51244/billing\&quot; – in this example, the company ID is \&quot;51244\&quot;   &#x60;Campaign ID&#x60;  To retrieve the campaign ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign by clicking on its name in the Agency Dashboard.     3. By default, the campaign opens in the Rank Tracker view. The platform URL contains the company ID.     E.g.: \&quot;https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe&#x3D;2023-09-04%3A2023-10-04\&quot; – in this example, the campaign ID is \&quot;72416\&quot;.  To retrieve the campaign ID through the API, make a call through the &#x60;Get Tracked Campaigns Details endpoint&#x60;. The response will contain the details of the requested Tracked Campaigns, including their IDs, which you can further use in other endpoint requests.   &#x60;Keyword ID&#x60;  To retrieve the keyword ID from the platform, follow these steps:       1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword.     3. The platform URL for the keyword view (Keyword Sidebar) contains the keyword ID.     E.g.: \&quot;https://app.seomonitor.com/v2/72416/manage/strategy/0/desktop/keywords?timeframe&#x3D;2023-09-04%3A2023-10-04&amp;ksid&#x3D;7063139\&quot; – in this example, the keyword ID is \&quot;7063139\&quot;   To retrieve the keyword ID through the API, make a call through the &#x60;Get Keyword Data endpoint&#x60;. The response will contain the details of the requested keywords, including their IDs, which you can further use in other endpoint requests.   &#x60;Keyword Group ID&#x60;      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and click on the required keyword group (Groups side-menu).     3. The platform URL for the keyword group view contains the keyword ID.     E.g.: \&quot;https://app.seomonitor.com/v2/72416/manage/strategy/69976/desktop/keywords?timeframe&#x3D;2023-09-04%3A2023-10-04\&quot; – in this example, the keyword group ID is \&quot;69976\&quot;  To retrieve the keyword group ID through the API, make a call through the &#x60;Get Groups List endpoint&#x60;. The response will contain the details of the requested keyword groups, including their IDs, which you can further use in other endpoint requests.   &#x60;Forecast ID for Scenarios or Objectives&#x60;      1. Log in to your SEOmonitor account (https://app.seomonitor.com)     2. Open the required campaign and go to Forecast from the main menu (top).     3. Select a Scenario or the Objective (if set). The platform URL for the specific scenario contains the forecast ID.     E.g.: \&quot;https://app.seomonitor.com/v2/forecast/118794/3788\&quot; – in this example, the forecast ID is \&quot;3788\&quot;   To retrieve the forecast ID through the API, make a call through the&#x60;Get Forecast Scenarios endpoint&#x60;. The response will contain the details of the requested Scenario or Objective, including their IDs, which you can further use in other endpoint requests.   &#x60;SERP Feature Abbreviations&#x60;  The returned data for some endpoints will contain SERP feature names in abbreviated form.  The returned values for SERP features are abbreviated as follows:      - \&quot;adt\&quot;: Ads Pack Top     - \&quot;def\&quot;: Definitions      - \&quot;dir\&quot;: Directions      - \&quot;fsn\&quot;: Featured Snippet      - \&quot;flt\&quot;: Flights      - \&quot;htl\&quot;: Hotels      - \&quot;img\&quot;: Images Pack      - \&quot;job\&quot;: Jobs      - \&quot;kng\&quot;: Knowledge Graph      - \&quot;geo\&quot;: Local Pack      - \&quot;shp\&quot;: Product listing      - \&quot;rcp\&quot;: Recipes      - \&quot;qns\&quot;: Questions      - \&quot;new\&quot;: Top Stories      - \&quot;vid\&quot;: Video Carousel      - \&quot;app\&quot;: Apps    &#x60;Rate Limits&#x60;  There are request limits in place to prevent abuse and ensure fair usage.   Exceeding the request limits will lead to HTTP 429 responses. If you need higher limits, contact our support team.   &#x60;Limits &amp; Quotas&#x60;      -------------------------------------------------------------------------     |Limit                                    |  Number of requests              -------------------------------------------------------------------------     |Maximum requests per second              |  10                              -------------------------------------------------------------------------     |Maximum rows per request (Request Quota) |  1000                            -------------------------------------------------------------------------     |Daily Quota                              |  10 000                          -------------------------------------------------------------------------   &#x60;Exceeding Limits&#x60;  If you exceed the rate limits, you will receive a 429 Too Many Requests response.  Daily Quota Exceeded      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Daily quota exceeded\&quot;,         \&quot;details\&quot;: [           \&quot;You have exceeded the allowed daily requests\&quot;          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.  Rate Limit Exceeded      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Rate limit exceeded\&quot;,         \&quot;details\&quot;: [           \&quot;You have exceeded the allowed requests per second\&quot;          ]       }     }  Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   &#x60;Increasing Limits&#x60;  The default limits allow most normal API usage patterns. However, if you need higher limits, please contact our support team.    Provide details on:      - Your specific use case      - The endpoints you are using     - The increased limits you are looking for  We will review your request and adjust limits where appropriate   &#x60;Need Higher Limits?&#x60;  For most use cases, the default limits are sufficient. But if you require higher limits, please contact our support team. We will review your use case and adjust limits where appropriate.   &#x60;Errors&#x60;  SEOmonitor API uses standard HTTP response codes to indicate the success or failure of API requests.   HTTP Status Codes      ----------------------------------------------------------------------------------     | Code  | Description                                                                 ----------------------------------------------------------------------------------     | 200   | Success                                                                     ----------------------------------------------------------------------------------     | 400   | Bad request - the request was malformed or missing required parameters      ----------------------------------------------------------------------------------      | 401   | Unauthorized - invalid or missing API key                                   ----------------------------------------------------------------------------------     | 403   | Forbidden - API key does not have access to the requested resource          ----------------------------------------------------------------------------------     | 404   | Not found - the requested resource does not exist                           ----------------------------------------------------------------------------------     | 429   | Too many requests - rate or quota limit exceeded                            ----------------------------------------------------------------------------------     | 500   | Internal server error - an unexpected error on the API server               ----------------------------------------------------------------------------------     | 50x   | Errors specific to various endpoints                                        ----------------------------------------------------------------------------------   &#x60;Error Response Format&#x60;  Error responses will be returned in JSON format:      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Rate limit exceeded\&quot;,         \&quot;details\&quot;: [           \&quot;You have exceeded the allowed requests per second\&quot;          ]       }     }   The error object contains:  - &#x60;message&#x60; - A general error message   - &#x60;details&#x60; - More specific details about the error   &#x60;Common Errors&#x60;  401 Unauthorized      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Invalid authentication\&quot;,         \&quot;details\&quot;: [           \&quot;The API key provided is invalid\&quot;          ]       }     }   Details:   This error message indicates there is a problem with the API key:  - The API key is missing from the request  - The key is invalid or incorrect  - The key is expired or revoked   Check that you are sending the correct API key in the Authorization header.  403 Forbidden      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Forbidden access\&quot;,         \&quot;details\&quot;: [           \&quot;Your API key does not have access to the requested data\&quot;          ]       }     }  Details:  This error message indicates that the API key being used does not have access to perform the requested operation. Ensure the key has the required scopes enabled.   404 Not Found      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Data not found\&quot;,         \&quot;details\&quot;: [           \&quot;The requested data does not exist.\&quot;          ]       }     }   Details:  This error message indicates that the object specified by the request does not exist. For example, requesting a keyword that is not in your SEOmonitor account.   429 Too Many Requests   Daily Quota Exceeded      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Daily quota exceeded\&quot;,         \&quot;details\&quot;: [           \&quot;You have exceeded the allowed daily requests\&quot;          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for daily requests. Retry the request after some delay.   Rate Limit Exceeded      {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Rate limit exceeded\&quot;,         \&quot;details\&quot;: [           \&quot;You have exceeded the allowed requests per second\&quot;          ]       }     }   Details:  This error message indicates that the request exceeds the rate limits for requests per second. Retry the request after some delay.   500 Internal Server Error       {       \&quot;error\&quot;: {         \&quot;message\&quot;: \&quot;Internal server error\&quot;,         \&quot;details\&quot;: [           \&quot;The server encountered an error while processing your requests\&quot;          ]       }     }   Details:  This error message indicates that an unexpected error occurred on the API server. Try the request again later. If the issue persists, contact support.   50X Endpoint-specific errors  You may encounter errors on specific endpoint requests – these are listed and explained under each endpoint page.   Support  If you have any questions about API errors, please contact our support team.   &#x60;Changelog&#x60;  Version 3.0 (current)   Release Date: ?  This is the first version of the API 3.0.    # noqa: E501
    """
)
