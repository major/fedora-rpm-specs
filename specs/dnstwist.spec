Name: dnstwist
Summary: Domain name permutation engine
License: Apache-2.0

Version: 20250130
Release: 1%{?dist}

URL:     https://github.com/elceef/%{name}/
Source0: %{url}archive/%{version}/%{name}-%{version}.tar.gz

# Remove all "are we on MS Windows?" checks
Patch0: 0000--no-win32-check.patch
# Remove all "is this Python import present?" checks
Patch1: 0001--modules-always-present.patch

%global geolite_version 2016.09

BuildRequires: GeoIP-GeoLite-data >= %{geolite_version}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildArch: noarch

Requires: GeoIP-GeoLite-data >= %{geolite_version}
Requires: python3dist(dnspython) >= 1.16.0
Requires: python3dist(geoip) >= 1.3.2
Requires: python3dist(geoip2) >= 4.0.0
Requires: python3dist(idna) >= 2.8
Requires: python3dist(ssdeep) >= 3.1
Requires: python3dist(tld) >= 0.9.1
Requires: python3dist(tlsh) >= 4.5

Requires: ((python3dist(pillow) >= 7.0.0-0) if chromedriver)
Requires: ((python3dist(selenium) >= 4.0.0-0) if chromedriver)

%{?python_enable_dependency_generator}


%description
See what sort of trouble users can get in trying to type your domain name.
Find similar-looking domains that adversaries can use to attack you.
Detect typosquatters, phishing attacks, fraud and corporate espionage.
Useful as an additional source of targeted threat intelligence.


%prep
%autosetup -p1
GEOIP_PATH="$(find %{_datadir}/GeoIP -name GeoLite2-Country.mmdb)"
sed -e "s|__GEOIP__COUNTRY__PATH__|'${GEOIP_PATH}'|g" -i dnstwist.py


%build
# Nothing to do here


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -p %{name}.py  %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a dictionaries/ %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 -p docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc docs/README.md docs/THANKS.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 30 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20250130-1
- Update to v20250130

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20240812-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 12 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20240812-1
- Update to v20240812

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20240116-1
- Update to v20240116

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230918-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230918-1
- Update to v20230918

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230509-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230509-1
- Update to v20230509

* Mon Apr 17 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230413-2
- Add dependency on legacy GeoIP (for fallback purposes)
- Fix unsatisfiable dependency on tlsh

* Thu Apr 13 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230413-1
- Update to v20230413

* Sun Apr 02 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230402-1
- Update to v20230402
- Migrate license tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20221213-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20221213-1
- Update to v20221213

* Sat Oct 22 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20221022-1
- Update to v20221022

* Tue Oct 11 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20221011-1
- Update to v20221011

* Sun Oct 09 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20221008-1
- Update to v20221008

* Mon Aug 15 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20220815-1
- Update to v20220815

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220131-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20220131-1
- Update to v20220131

* Mon Jan 24 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20220120-1
- Update to v20220120

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20211204-2
- Fix dependency list (replace python-GeoIP with python-geoip2)

* Sat Dec 04 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20211204-1
- Update to v20211204

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201228-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201228-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 02 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20201228-2
- Fix package being uninstallable due to unsatisfiable dependencies
  (some python3-XYZ packages don't provide python3dist(XYZ), but something
  slightly different)

* Wed Dec 30 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20201228-1
- Update to latest upstream release
- Use "python3dist(XYZ)" instead of python3-XYZ for specifying dependencies

* Thu Oct 22 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20201022-1
- Update to latest upstream release

* Fri Sep 18 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20200916-1
- Update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200707-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Artur Iwicki <fedora@svgames.pl> - 20200707-1
- Update to latest upstream release

* Thu Jun 25 2020 Artur Iwicki <fedora@svgames.pl> - 20200521-2
- Add an explicit BuildRequires on python3-setuptools

* Fri May 22 2020 Artur Iwicki <fedora@svgames.pl> - 20200521-1
- Update to latest upstream release

* Wed Apr 29 2020 Artur Iwicki <fedora@svgames.pl> - 20200429-1
- Update to latest upstream release
- Drop Source101 (man page - merged upstream)

* Sun Mar 22 2020 Artur Iwicki <fedora@svgames.pl> - 20190706-3
- Remove the bundled GeoIP database,
  require the GeoIP-GeoLite-data package instead

* Thu Mar 05 2020 Artur Iwicki <fedora@svgames.pl> - 20190706-2
- Add a man page
- Preserve timestamps during %%install

* Sun Dec 22 2019 Artur Iwicki <fedora@svgames.pl> - 20190706-1
- Initial packaging
