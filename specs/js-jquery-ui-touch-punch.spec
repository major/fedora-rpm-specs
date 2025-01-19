%global commit 4bc009145202d9c7483ba85f3a236a8f3470354d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global jsname jquery-ui-touch-punch

Name:		js-%{jsname}
Version:	0.2.3
Release:	0.20.20141219git%{shortcommit}%{?dist}
Summary:	Touch Event Support for jQuery UI

# Automatically converted from old format: MIT or GPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-MIT OR GPL-2.0-only
URL:		http://touchpunch.furf.com/
Source0:	https://github.com/furf/%{jsname}/archive/%{commit}/%{jsname}-%{version}-%{shortcommit}.tar.gz

BuildArch:	noarch
BuildRequires:	uglify-js
BuildRequires:	web-assets-devel
Requires:	js-jquery >= 1.6
Requires:	js-jquery-ui >= 1.8
Requires:	web-assets-filesystem

%description
jQuery UI Touch Punch is a small hack that enables the use of touch
events on sites using the jQuery UI user interface library.

%prep
%setup -q -n %{jsname}-%{commit}

# Remove pre-minified script
rm *.min.js

%build
# Minify script
uglifyjs jquery.ui.touch-punch.js -c -m --comments '/^!/' \
      -o jquery.ui.touch-punch.min.js

%install
mkdir -p %{buildroot}/%{_jsdir}/%{jsname}
install -m 644 -p *.js %{buildroot}/%{_jsdir}/%{jsname}

%files
%{_jsdir}/%{jsname}
%doc README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.20.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.3-0.19.20141219git4bc0091
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.18.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.17.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.16.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.15.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.14.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.13.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.12.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.11.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 11 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.3-0.10.20141219git4bc0091
- Change Requires to new js-jquery-ui package (also for EPEL 8)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.9.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.8.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.3-0.7.20141219git4bc0091
- Drop jquery-ui dependency for EPEL 8, package not available.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.6.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.5.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.4.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.3.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.2.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.3-0.1.20141219git4bc0091
- First packaging for Fedora
