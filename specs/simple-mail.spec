%global somajor 0

Name:           simple-mail
Version:        3.1.0
Release:        2%{?dist}
Summary:        SMTP Client Library for Qt

License:        LGPL-2.1-only
URL:            https://github.com/cutelyst/simple-mail
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.5
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  xz
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Network) >= 5.5.0
BuildRequires:  cmake(Qt5Widgets) >= 5.5.0

%description
simple-mail is a small library written for Qt 5 (C++11 version)
that allows application to send complex emails (plain text, html,
attachments, inline files, etc.) using the Simple Mail Transfer
Protocol (SMTP).


%package devel
Summary:        SMTP Client Library for Qt - Development Files
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Header and development files for libsimplemail-qt5.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libSimpleMail3Qt5.so.%{somajor}
%{_libdir}/libSimpleMail3Qt5.so.%{version}


%files devel
%{_includedir}/simplemail3-qt5/
%{_libdir}/cmake/SimpleMail3Qt5/
%{_libdir}/libSimpleMail3Qt5.so
%{_libdir}/pkgconfig/SimpleMail3Qt5.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Jonathan Wright <jonathan@almalinux.org> - 3.1.0-1
- update to 3.1.0 rhbz#2319816

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Jonathan Wright <jonathan@almalinux.org> - 3.0.0-1
- update to 3.0.0 rhbz#2275823

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Jonathan Wright <jonathan@almalinux.org> - 2.3.0-1
- Update to 2.3.0 rhbz#1804007

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Dakota Williams <raineforest@raineforest.me> - 1.4.0-2
- Backport fix from upstream to fix generated pkgconfig() dependencies

* Mon Dec  9 2019 Dakota Williams <raineforest@raineforest.me> - 1.4.0-1
- Initial packaging
