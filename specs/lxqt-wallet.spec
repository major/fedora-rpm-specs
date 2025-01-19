%global srcname lxqt_wallet

Name:           %(echo %{srcname} |tr _ - )
Version:        4.0.2
Release:        2%{?dist}
Summary:        Create a kwallet like functionality for LXQt

License:        BSD-2-Clause
URL:            https://github.com/lxqt/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(lxqt)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  libgcrypt-devel
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  qt6-linguist

%description
This project seeks to give a functionality for secure storage
of information that can be presented in key-values pair like
user names-passwords pairs.

Currently the project can store the information in KDE's kwallet,
GNOME's secret service or in an internal system that use libgcrypt
as its cryptographic backend.

The internal secure storage system allows the functionality to
be provided without dependencies on KDE or GNOME libraries.

This project is designed to be used by other projects simply by
adding the source folder in the build system and start using it.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liblxqt-devel%{?_isa}

%description devel
%{summary}.


%prep
%autosetup -n%{srcname}-%{version}
cp -p backend/README README-backend
cp -p frontend/README README-frontend

%build
%cmake_lxqt
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%files -f %{name}.lang
%license LICENSE
%doc README.md changelog
%{_bindir}/lxqt_wallet-cli
%{_libdir}/liblxqt-wallet.so.6.0.0

%files devel
%doc README-*
%{_includedir}/lxqt/lxqt-wallet.h
%{_includedir}/lxqt/lxqt_wallet.h
%{_libdir}/liblxqt-wallet.so
%{_libdir}/pkgconfig/lxqt-wallet.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 09 2024 Steve Cossette <farchord@gmail.com> - 4.0.2-1
- 4.0.2

* Sat Oct 26 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.2-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Ian McInerney <ian.s.mcinerney@ieee.org> - 3.2.2-2
- Revert "update to 1.0.0" because there was actually no new update, and instead it
- made the package go back to version 1.0.0 from 2013. There was no build, so no
- need to bump the release.

* Sat Dec 25 2021 zsun <sztsian@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 11 2021 Raphael Groner <raphgro@fedoraproject.org> - 3.2.2-1
- bump to v3.2.2

* Wed Feb 24 2021 Raphael Groner <raphgro@fedoraproject.org> - 3.2.1-1
- bump to v3.2.1, mind unbundling in zulucrypt, rhbz#1862725 
- use cmake macros properly for out-of-source builds

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Christian Dersch <lupinix@mailbox.org> - 3.1.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.0-2
- rebuilt for latest Qt5

* Wed Aug 03 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.0-1
- new version
- drop hacks for translations and pkgconfig
- readd gcc-c++

* Sat Jul 23 2016 Raphael Groner <projects.rg@smart.ms> - 2.2.1-2
- fix compilation of translations
- add hack for pkgconfig version

* Thu Jul 14 2016 Raphael Groner <projects.rg@smart.ms> - 2.2.1-1
- initial
