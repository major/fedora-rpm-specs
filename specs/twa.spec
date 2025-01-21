Name:    twa
Version: 1.11.0
Release: 3%{?dist}
Summary: Tiny web auditor with strong opinions
License: MIT

URL:     https://github.com/trailofbits/twa
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: sed

Requires: bash >= 4.0.0
Requires: curl
Requires: gawk
Requires: jq
Requires: nc
Requires: /usr/bin/dig

Recommends: testssl


%description
%{name} is a website auditing tool that can be used to detect
HTTPS issues, missing security headers, information-leaking headers,
and other potential security headers.


%prep
%setup -q

# Fix shebang
sed -e 's|^#!/usr/bin/env bash$|#!%{_bindir}/bash|' -i twa

# Remove the bash version check
sed -e '/Expected GNU Bash 4.0 or later/d' -i twa

# Remove the "ensure dependency is installed" checks
sed -e '/^ensure installed .*/d' -i twa


%build
# Nothing to do here - this is a shell script


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -p twa    %{buildroot}%{_bindir}/
install -m 755 -p tscore %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p twa.1 %{buildroot}%{_mandir}/man1/


%files
%license LICENSE
%doc README.md
%{_bindir}/twa
%{_bindir}/tscore
%{_mandir}/man1/twa.*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.11.0-1
- Update to v1.11.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.10.0-1
- Update to latest upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Artur Iwicki <fedora@svgames.pl> - 1.9.3-1
- Update to latest upstream release

* Wed Apr 29 2020 Artur Iwicki <fedora@svgames.pl> - 1.9.2-1
- Update to latest upstream release
- Add a weak dependency on testssl

* Fri Apr 24 2020 Artur Iwicki <fedora@svgames.pl> - 1.9.1-1
- Update to latest upstream release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Artur Iwicki <fedora@svgames.pl> - 1.8.0-2
- Add missing dependency on /usr/bin/dig

* Sun Feb 17 2019 Artur Iwicki <fedora@svgames.pl> - 1.8.0-1
- Update to latest upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Artur Iwicki <fedora@svgames.pl> - 1.7.1-1
- Update to latest upstream version

* Tue Nov 06 2018 Artur Iwicki <fedora@svgames.pl> - 1.6.2-1
- Update to latest upstream version

* Sat Oct 20 2018 Artur Iwicki <fedora@svgames.pl> - 1.6.0-1
- Update to latest upstream version
- Update upstream URL (repo owner change)

* Sat Oct 06 2018 Artur Iwicki <fedora@svgames.pl> - 1.5.1-1
- Update to latest upstream version

* Tue Sep 18 2018 Artur Iwicki <fedora@svgames.pl> - 1.3.1-1
- Update to latest upstream version
- Use "install -p" (preserve file timestamps)

* Sun Sep 16 2018 Artur Iwicki <fedora@svgames.pl> - 1.2.0-1
- Initial packaging
