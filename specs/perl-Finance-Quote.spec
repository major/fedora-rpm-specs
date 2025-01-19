%bcond author_tests 0

Name:           perl-Finance-Quote
%global cpan_version 1.64
# RPM version needs 4 digits after the decimal to preserve upgrade path
Version:        %(LANG=C printf "%.4f" %{cpan_version})
Release:        2%{?dist}
Summary:        A Perl module that retrieves stock and mutual fund quotes
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Finance-Quote
Source0:        https://www.cpan.org/modules/by-module/Finance/Finance-Quote-%{cpan_version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(HTTP::CookieJar::LWP) >= 0.014
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent) >= 6.48
BuildRequires:  perl(Module::Load) >= 0.36
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spreadsheet::XLSX)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Util)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Time::Seconds)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Web::Scraper)
BuildRequires:  perl(XML::LibXML)
# Test Suite
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Date::Range)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Author Tests
%if %{with author_tests}
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
# Dependencies
Requires:       perl(LWP::Protocol::https)

%description
This module retrieves stock and mutual fund quotes from various exchanges
using various source.

%prep
%setup -q -n Finance-Quote-%{cpan_version}

# Remove redundant exec permissions
find lib/ -type f -name '*.pm' -exec chmod -c -x {} \;

# Avoid documentation name clash
cp -p README README.dist

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
unset DEBUG
%if %{with author_tests}
make test TEST_AUTHOR=1 AUTHOR_TESTING=1
%else
make test
%endif

%files
%license LICENSE
%doc Change* Documentation/* README.dist
%{perl_vendorlib}/Finance/
%{_mandir}/man3/Finance::Quote.3*
%{_mandir}/man3/Finance::Quote::AEX.3*
%{_mandir}/man3/Finance::Quote::AlphaVantage.3*
%{_mandir}/man3/Finance::Quote::ASEGR.3*
%{_mandir}/man3/Finance::Quote::ASX.3*
%{_mandir}/man3/Finance::Quote::Bloomberg.3*
%{_mandir}/man3/Finance::Quote::BorsaItaliana.3*
%{_mandir}/man3/Finance::Quote::Bourso.3*
%{_mandir}/man3/Finance::Quote::BSEIndia.3*
%{_mandir}/man3/Finance::Quote::BVB.3*
%{_mandir}/man3/Finance::Quote::Comdirect.3*
%{_mandir}/man3/Finance::Quote::Consorsbank.3*
%{_mandir}/man3/Finance::Quote::CSE.3*
%{_mandir}/man3/Finance::Quote::Currencies.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::AlphaVantage.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::CurrencyFreaks.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::ECB.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::FinanceAPI.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::Fixer.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::OpenExchange.3*
%{_mandir}/man3/Finance::Quote::CurrencyRates::YahooJSON.3*
%{_mandir}/man3/Finance::Quote::Deka.3*
%{_mandir}/man3/Finance::Quote::DWS.3*
%{_mandir}/man3/Finance::Quote::FinanceAPI.3*
%{_mandir}/man3/Finance::Quote::Finanzpartner.3*
%{_mandir}/man3/Finance::Quote::Fondsweb.3*
%{_mandir}/man3/Finance::Quote::Fool.3*
%{_mandir}/man3/Finance::Quote::FTfunds.3*
%{_mandir}/man3/Finance::Quote::GoldMoney.3*
%{_mandir}/man3/Finance::Quote::GoogleWeb.3*
%{_mandir}/man3/Finance::Quote::HU.3*
%{_mandir}/man3/Finance::Quote::IndiaMutual.3*
%{_mandir}/man3/Finance::Quote::MarketWatch.3*
%{_mandir}/man3/Finance::Quote::MorningstarAU.3*
%{_mandir}/man3/Finance::Quote::MorningstarCH.3*
%{_mandir}/man3/Finance::Quote::MorningstarJP.3*
%{_mandir}/man3/Finance::Quote::MorningstarUK.3*
%{_mandir}/man3/Finance::Quote::NSEIndia.3*
%{_mandir}/man3/Finance::Quote::NZX.3*
%{_mandir}/man3/Finance::Quote::OnVista.3*
%{_mandir}/man3/Finance::Quote::Oslobors.3*
%{_mandir}/man3/Finance::Quote::SEB.3*
%{_mandir}/man3/Finance::Quote::Sinvestor.3*
%{_mandir}/man3/Finance::Quote::SIX.3*
%{_mandir}/man3/Finance::Quote::StockData.3*
%{_mandir}/man3/Finance::Quote::Stooq.3*
%{_mandir}/man3/Finance::Quote::TesouroDireto.3*
%{_mandir}/man3/Finance::Quote::Tiaacref.3*
%{_mandir}/man3/Finance::Quote::TMX.3*
%{_mandir}/man3/Finance::Quote::Tradegate.3*
%{_mandir}/man3/Finance::Quote::TSP.3*
%{_mandir}/man3/Finance::Quote::TreasuryDirect.3*
%{_mandir}/man3/Finance::Quote::Troweprice.3*
%{_mandir}/man3/Finance::Quote::TwelveData.3*
%{_mandir}/man3/Finance::Quote::Union.3*
%{_mandir}/man3/Finance::Quote::XETRA.3*
%{_mandir}/man3/Finance::Quote::YahooJSON.3*
%{_mandir}/man3/Finance::Quote::YahooWeb.3*
%{_mandir}/man3/Finance::Quote::ZA.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Paul Howarth <paul@city-fan.org> - 1.6400-1
- Update to 1.64
  - Update AlphaVantage.pm (GH#447)
  - Fix to Stooq.pm (GH#445)
  - Updated ASX.pm (GH#404)
  - Added more fields to CSE.pm and exposed all labels
  - Changed parsing in Comdirect.pm (GH#413)
  - Complete rewrite of OnVista.pm (GH#414)
  - Minor fix to FinanceAPI decoding JSON (GH#434)
  - Modified YahooJSON to deal with "nan" as dividend yield in JSON
  - New CurrencyRates module, CurrencyRates/FinanceAPI (GH#427)
  - Fixed Bourso.pm (GH#417)
  - Allowed Currency Rates modules Fixer.pm and OpenExchange.pm to read their
    API keys from environment variables (GH#426)
  - Removed references to IEXCloud (IEX ended support for all products at the
    end of August 2024)
- Switch source URL from cpan.metacpan.org to www.cpan.org
- Add build conditional for author tests, disabled by default

* Sun Sep 22 2024 Paul Howarth <paul@city-fan.org> - 1.6300-1
- Update to 1.63
  - Fixed TesouroDireto.pm - using different source URL (GH#424)
  - Added FinanceAPI.pm - requires API key from https://financeapi.net/
    - US and other exchange data available
  - Fixed BVB.pm (GH#409)
  - Fixed BSEIndia.pm (GH#410); removed Unzip as quotes file is now a CSV file
  - Fixed NSEIndia.pm (GH#410)
  - Fixed NZX.pm (GH#401)

* Thu Aug 22 2024 Michal Josef Špaček <mspacek@redhat.com> - 1.6200-3
- Fix version handling for build with different locales set
  `printf "%.4f" 1.62` has different results e.g. for cs_CZ.UTF-8 vs C
- Rename variable to cpan_version which is common in Fedora

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 17 2024 Paul Howarth <paul@city-fan.org> - 1.6200-1
- Update to 1.62
  - Fixed AEX.pm
  - Removed throttling from AlphaVantage.pm (GH#363)
  - Added CurrencyFreaks.pm - new currency module
  - YahooJSON.pm - added more error handling (GH#390)
  - Fixed MarketWatch.pm module (GH#389)
  - Rewrote Fool.pm and added back to F::Q (GH#379)
  - Added StockData.pm - methods stockdata, nyse, nasdaq
  - Modified YahooJSON.pm module in order handle EU consent redirects better
  - TwelveData.pm - Added "last" to data being returned
  - Added BorsaItaliana.pm - module for Borsa Italiana, Italian traded bonds
    using ISIN
  - YahooWeb.pm - modified YahooWeb to account for changes from Yahoo (GH#377)
- Upstream dropped CONTRIBUTING.pod

* Fri Apr 19 2024 Paul Howarth <paul@city-fan.org> - 1.6100-1
- Update to 1.61
  - SIX.pm - Changed lookup for currency, added lookups for symbol and last
    (GH#380)
  - YahooJSON.pm - URLs to retrieve required cookies and crumbs were changed to
    allow EU-based users to use the module (GH#373)

* Wed Apr 17 2024 Paul Howarth <paul@city-fan.org> - 1.6000-1
- Update to 1.60
  - Removed not working modules Fidelity.pm, Cdbfundlibrary.pm, Fundata.pm and
    Fool.pm (GH#346, GH#366, GH#368)
  - YahooJSON.pm - Added code to retrieve cookies and a "crumb" required to
    continue to utilize the v11 API (GH#369)
  - The YahooJSON.pm currency module was changed to use the v8 chart API
  - Added initial version of CONTRIBUTING.pod that metacpan.org utilizes; it
    will completely replace the Hacker's Guide in the future
  - Bloomberg.pm - Changed module to extract data from JSON structure embedded
    within the HTML (GH#360)
  - NSEIndia.pm - Eliminated need to use temp folders by storing file data from
    URL into a variable
- Exclude Finance::CONTRIBUTING manpage, CONTRIBUTING.pod added as %%doc

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5900-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5900-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan  1 2024 Paul Howarth <paul@city-fan.org> - 1.5900-1
- Update to 1.59
  - Fixed XETRA, Tradegate and SInvestor after webpage was restructured (GH#350)
  - Fidelity.pm temporarily disabled (GH#346)
  - Finanzpartner.pm - Fix scraper, did not work if quote was higher than the
    previous day's quote
  - GoogleWeb.pm - Updated to retrieve mutual fund and BATS prices (GH#355)
  - BSEIndia.pm:
    - Updated to use standardized data file at URL
      https://www.bseindia.com/download/BhavCopy/Equity/BSE_EQ_BHAVCOPY_{DDMMYYYY}.ZIP
    - Eliminated need to use temp folders by storing standardized file data
      from URL into a variable
    - Updated names of source fields to conform to those in the standardized
      data file
    - Removed print when symbol not found (GH#335)
  - IndiaMutual.pm - Eliminated need to use temp folders by storing NAV file
    data from URL into a variable
  - TMX.pm - Correct a self-reference in documentation (GH#345)
  - Stooq.pm - Added new currencies and a fix for commodities' prices
  - YahooWeb.pm - Skip rows in the price table where the prices are "-"; this
    seems to happen sometimes with TIAA (and perhaps other) securities
    including TILIX and QCILIX
  - TSP.pm - Was not returning hash when the HTTP GET failed completely or the
    content did not contain the expected CSV file (GH#338)

* Sun Aug 13 2023 Paul Howarth <paul@city-fan.org> - 1.5800-1
- Update to 1.58
  - New module Consorsbank.pm (GH#329)
  - New module Stooq.pm (GH#203)
  - Bloomberg.pm - Changed modules to utilize cookie jar (GH#324, GH#331)
  - AlphaVantage.pm:
    - Apply currency scaling (GBp -> GBP) when symbol had additional ".X"
      suffix (GH#281)
    - Fixed check for "Information" JSON usually returned when daily API limit
      has been reached
  - YahooWeb.pm - Fixed incorrect pricing for single character symbols and
    changed URL to get trade date (GH#314, GH#319)
  - Another fix to the URL in YahooJSON and CurrencyRates/YahooJSON (GH#318)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5700-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul  2 2023 Paul Howarth <paul@city-fan.org> - 1.5700-1
- Update to 1.57
  - Correct set exchange in YahooJSON.pm (GH#306)
  - Added close, change and p_change to Tradegate, XETRA and Sinvestor; added
    optional parameter INST_ID to specify the institute id; fixed bug in
    Tradegate, XETRA and Sinvestor for numbers equal or higher than 1.000
    (GH#304)
  - Added GoogleWeb module
  - YahooWeb module added (GH#296)
  - Added MarketWatch module
  - Replaced cached file with IO::String object in IndiaMutual.pm
  - Fixed missing date in AEX.pm (GH#298)
  - Fixed Examples in POD Documentation in a few modules (GH#295)
  - Move 'use strict' to be the first statement in TreasuryDirect.pm and
    TwelveData.pm (GH#290)
  - Remove old perl version requirement statements from TreasuryDirect.pm and
    TwelveData.pm (GH#290)
  - Removed Data::Dumper, which caused another test to fail from
    TreasuryDirect.pm (GH#290)
  - Fixed Fool.pm and fool.t (GH#289)

* Mon Jun 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5600-4
- Reverse prior change

* Mon Jun 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5600-3
- Require perl-JSON-Parse

* Tue May 30 2023 Paul Howarth <paul@city-fan.org> - 1.5600-2
- Rebuild

* Tue May 30 2023 Paul Howarth <paul@city-fan.org> - 1.5600-1
- Update to 1.56
  - Replaced Tradeville.pm with BVB.pm (GH#269)
  - Added new TwelveData module
  - Updated YahooJSON.pm and CurrencyRates/YahooJSON.pm to use
    https://query2.finance.yahoo.com/v11 (GH#284)
  - Bourso.pm - Squash anything but numbers and period in quote values
  - Renamed MStarUK.pm to MorningstarUK.pm
  - Added get_features method (GH#260)

* Sun May 14 2023 Paul Howarth <paul@city-fan.org> - 1.5500-1
- Update to 1.55
  - Added YahooJSON currency rate module (GH#270)
  - Added TRV => CAD in AlphaVantage.pm (GH#265, GH#267)
  - Quick fix for YahooJSON.pm API
  - URL Change for MorningstarJP (GH#261)

* Sun May  7 2023 Paul Howarth <paul@city-fan.org> - 1.5402-1
- Update to 1.5402
  - URL Change for MorningstarJP (GH#261)
  - Regex fix in FTfunds.pm and changed test cases ftfunds.t (GH#262)

* Sat Apr  8 2023 Paul Howarth <paul@city-fan.org> - 1.5400-3
- Tweak regex to fix FTfunds.pm
  https://github.com/finance-quote/finance-quote/pull/262

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Paul Howarth <paul@city-fan.org> - 1.5400-1
- Update to 1.54
  - Fix to AEX.pm (GH#235, GH#244)
  - New modules Sinvestor.pm, Tradegate.pm and XETRA.pm (GH#243)
  - Updates to TMX.pm (Toronto Stock Exchange) (GH#248 and GH#253)
  - Reverted API change (GH#230) in CurrencyRates/AlphaVantage.pm (GH#249)
  - Fix to Fondsweb.pm (GH#250)

* Wed Oct 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.5301-1
- 1.5301

* Sun Oct  9 2022 Paul Howarth <paul@city-fan.org> - 1.53-1
- Update to 1.53 (rhbz#2133215)
  - Changed bug tracker to
    https://github.com/finance-quote/finance-quote/issues
  - DWS.pm - Set $info{$symbol, 'symbol'} to $symbol
  - Union.pm - Reworked for a different CSV file (GH#231)
  - CurrencyRates/AlphaVantage.pm - API CURRENCY_EXCHANGE_RATE no longer
    accepts free API keys: changed to use FX_DAILY API (GH#229, GH#230)
  - Set minimum version for LWP::UserAgent to honor redirects
  - CurrencyRates/AlphaVantage.pm - Added logic to account for empty JSON
    returned from currency exchange fetch
  - Bourso.pm - Added Europe and France back as failover methods
  - Tradeville.pm - Changed hostname in URL to tradeville.ro, and added logic
    to better account for the symbol not being found
  - YahooJSON.pm - Account for symbols with '&' (GH#202)
  - Minor change to isoTime function in Quote.pm
  - TSP.pm - Update URL and handling of dates (GH#227)
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul  4 2022 Paul Howarth <paul@city-fan.org> - 1.52-1
- Update to 1.52
  - Quote.pm: Fixed logic for FQ_LOAD_QUOTELET starting with "-defaults"
    (GH#197, GH#199)
  - AlphaVantage currency module: Don't recurse infinitely when exchange rate
    is less than .001 (GH#193)
  - Bourso.pm: Fixed data bug (GH#174, GH#194)
  - TSP.pm: Minor fix for URL used to retrieve data (GH#195); note: URL was
    changed after the PR was merged and the module remains in a non-working
    status
  - TesouroDireto.pm: New module for Brazilian's National Treasury public
    bonds (GH#198)
  - Bloomberg.pm: Update Bloomberg class names (GH#205), correct html parsing
    errors
  - MorningstarCH.pm: Re-enabled and fixed (GH#207)
  - ZA.pm: Change to return price from sharenet in major denomination (GH#208)
  - Changes to SourceForge project website HTML files
  - Add [Prereqs] to dist.ini (GH#215)

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Paul Howarth <paul@city-fan.org> - 1.51-2
- Add explicit dependency on perl(LWP::Protocol::https) (#2021755)

* Thu Jul 22 2021 Paul Howarth <paul@city-fan.org> - 1.51-1
- Update to 1.51
  - Fix bugs in t/fq-object-methods.t
  - Add code to hide warning in t/currency_lookup.t

* Thu Jul 22 2021 Paul Howarth <paul@city-fan.org> - 1.50-1
- Update to 1.50
  - New modules: CurrencyRates
  - Updated modules: ASX, TIAA-CREF, Fool, Currencies
  - Corrected some POD issues (thanks to the Debian Perl Group)
- Add patch to fix FTBFS due to online test (GH#177)
- Use %%license unconditionally

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Paul Howarth <paul@city-fan.org> - 1.49-1
- Update to 1.49
  - Alphavantage: Removed Time::HiRes dependency due to mswin32 not supporting
    clock_gettime calls

* Sun Jun 30 2019 Paul Howarth <paul@city-fan.org> - 1.48-1
- Update to 1.48
  - Alphavantage: Add a waiting mechanism to comply with alphavantage use terms
  - Alphavantage: Added support for several stock exchanges and currencies
  - Updated modules: Union, Deka, Indiamutual, ASX, Yahoojson, TSP, AEX, Fool
  - New modules: IEXTrading, MorningstarAU, MorningstarCH, IEXCloud
  - Yahoo: removed modules referring to yahoo API, which yahoo stopped
  - BUGFIX: 'use of uninitialized value' returned by perl could make gnucash
    fail when more than 15 quotes were requested
  - BUGFIX: MS Windows does not support %%T in strftime call
  - Added new documentation files: Release.txt, Hackers-Guide,
    Modules-README.yml
  - We started moving known failing tests into TODO blocks
- Fix FTfunds (CPAN RT#129586)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.47-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.47-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Paul Howarth <paul@city-fan.org> - 1.47-1
- Update to 1.47
  - Drop long-obsolete debian directory
  - AlphaVantage:
    - Added support for .IL ⇒ USD currency and division
    - Graceful error catchup
  - Yahoojson:
    - Module adapted to new URL and returned json
  - Use AlphaVantage for currency quotes instead of Yahoo

* Fri Nov 10 2017 Paul Howarth <paul@city-fan.org> - 1.45-1
- Update to 1.45
  - AlphaVantage:
    - More suffix - currency pairs added
    - GBP and GBX divided by 100

* Wed Nov  8 2017 Paul Howarth <paul@city-fan.org> - 1.44-1
- Update to 1.44
  - Added currencies for .SA (Brazil) and .TO (Canada/Toronto) markets
  - Set up a pause of .7s between queries in AlphaVantage.pm to limit queries

* Tue Nov  7 2017 Paul Howarth <paul@city-fan.org> - 1.43-1
- Update to 1.43
  - More tests in alphavantage.t
  - Bug resolved: removed time from $last_refresh when markets are open
  - Added currency for .DE market
  - Bugfix in currency determination regex

* Mon Nov  6 2017 Paul Howarth <paul@city-fan.org> - 1.41-1
- Update to 1.41
  - Added AlphaVantage module
  - Some other module changes: yahoojson, Morningstar, Bourso, ASX, TSX
    (not working)
- Simplify find command using -delete

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Paul Howarth <paul@city-fan.org> - 1.38-1
- Update to 1.38
  - Module updates: tiaacref, yahooJSON, FTfunds, MStaruk, USFedBonds, GoldMoney
  - New modules: fidelityfixed, yahooYQL
  - Removed modules: MTGox
  - More tests: yahoo_speed.t, tiaacref.t
- Avoid documentation name clash between two README files

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-3
- Perl 5.22 rebuild

* Tue Feb 24 2015 Paul Howarth <paul@city-fan.org> - 1.37-2
- Fix GBX pricing in FTfunds (CPAN RT#99783)
- Fix MStaruk quote retrieval (CPAN RT#99784)

* Mon Feb  2 2015 Paul Howarth <paul@city-fan.org> - 1.37-1
- Update to 1.37
  - MorningstarJP: changed dependency from Date::Calc to DateTime
  - Modified 00-use.t to show more info
  - Remove Crypt::SSLeay dependency in favour of LWP::Protocol::https
  - Updated HU.pm and test file to current website

* Fri Nov 14 2014 Paul Howarth <paul@city-fan.org> - 1.35-1
- Update to 1.35
- Clean up and modernize spec somewhat (can't build for EL < 7 as the module
  requires Mozilla::CA)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Bill Nottingham <notting@redhat.com> - 1.20-2
- add missing https requires (#859607)

* Mon Feb 17 2014 Bill Nottingham <notting@redhat.com> - 1.20-1
- update to 1.20

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.17-13
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 1.17-9
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.17-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Bill Nottingham <notting@redhat.com> - 1.17-5
- fix TIAA-CREF (#668935, <amessina@messinet.com>)

* Mon Dec 06 2010 Bill Nottingham <notting@redhat.com> - 1.17-4
- fix buildrequires for F-15

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.17-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.17-2
- rebuild against perl 5.10.1

* Mon Nov 23 2009 Bradley Baetz <bbaetz@gmail.com> - 1.17-1
- Update to 1.17
- Add extra BuildRequires needed for tests to pass

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.13-2
Rebuild for new perl

* Wed Sep 26 2007 Bill Nottingham <notting@redhat.com>
- add perl(ExtUtils::MakeMaker) buildreq

* Tue Sep 18 2007 Bill Nottingham <notting@redhat.com>
- fix source download URL

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Mon Jan  8 2007 Bill Nottingham <notting@redhat.com> - 1.13-1
- update to 1.13

* Thu Sep 14 2006 Bill Nottingham <notting@redhat.com> - 1.11-4
- bump for rebuild

* Mon Apr 10 2006 Bill Nottingham <notting@redhat.com> - 1.11-3
- add buildreq for perl-HTML-TableExtract
- clean up sed

* Mon Apr 10 2006 Bill Nottingham <notting@redhat.com> - 1.11-2
- clean up spec file

* Fri Apr  7 2006 Bill Nottingham <notting@redhat.com> - 1.11-1
- initial packaging
