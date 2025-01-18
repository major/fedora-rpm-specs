Summary:        Facebook protocol plugin for BitlBee
Name:           bitlbee-facebook
Version:        1.2.2
Release:        11%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/bitlbee/bitlbee-facebook
Source0:        https://github.com/bitlbee/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(bitlbee) >= 3.4
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.14.0
# Tests
# script(1) comes from somewhere in the overall util-linux* package mess
BuildRequires:  %{_bindir}/script

%description
The Facebook protocol plugin for BitlBee. This plugin uses the Facebook
Mobile API.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/bitlbee/facebook.la

%check
echo -e "[settings]\nRunMode = Inetd\nPluginDir = $RPM_BUILD_ROOT%{_libdir}/bitlbee/" > bitlbee.conf
script -c 'timeout --preserve-status --signal=TERM 5s bitlbee -c bitlbee.conf' -e -f check.log -q
! grep -q 'Error: ' check.log || { cat check.log; exit 1; }  # Any other BitlBee error during startup?

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/bitlbee/facebook.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 31 2024 Robert Scheck <robert@fedoraproject.org> 1.2.2-9
- Test whether BitlBee can load plugin during startup (#2272092)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 13 2021 Robert Scheck <robert@fedoraproject.org> 1.2.2-1
- Upgrade to 1.2.2 (#1928417)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Robert Scheck <robert@fedoraproject.org> 1.2.1-2
- Added upstream patch to avoid ERROR_QUEUE_UNDERFLOW upon login

* Thu Oct 22 2020 Robert Scheck <robert@fedoraproject.org> 1.2.1-1
- Upgrade to 1.2.1 (#1889850)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 David Cantrell <dcantrell@redhat.com> - 1.2.0-1
- Upgrade to 1.2.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.1.2-2
- Changes to match with Fedora Packaging Guidelines (#1290235)

* Fri Sep 15 2017 Robert Scheck <robert@fedoraproject.org> 1.1.2-1
- Upgrade to 1.1.2

* Mon Apr 03 2017 Robert Scheck <robert@fedoraproject.org> 1.1.1-1
- Upgrade to 1.1.1

* Tue Mar 08 2016 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0

* Wed Dec 09 2015 Robert Scheck <robert@fedoraproject.org> 0-0.1.20151105git
- Upgrade to GIT 20151105
- Initial spec file for Fedora and Red Hat Enterprise Linux
