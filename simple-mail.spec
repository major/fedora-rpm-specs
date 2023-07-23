%undefine __cmake_in_source_build
%global somajor 0

Name:           simple-mail
Version:        1.4.0
Release:        10%{?dist}
Summary:        SMTP Client Library for Qt

License:        LGPLv2+
URL:            https://github.com/cutelyst/simple-mail
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Add-GNUInstallDirs-to-CMakeLists.patch
Patch1:         0001-Fix-wrong-requirement-in-pkgconfig-file.patch

BuildRequires:  cmake >= 3.5
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  xz
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Network) >= 5.5.0
BuildRequires:  cmake(Qt5Widgets) >= 5.5.0

%description
simple-mail is a small library writen for Qt 5 (C++11 version)
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
%{_libdir}/libSimpleMailQt5.so.%{somajor}
%{_libdir}/libSimpleMailQt5.so.%{version}


%files devel
%{_includedir}/simplemail-qt5/
%{_libdir}/cmake/simplemailqt5/
%{_libdir}/libSimpleMailQt5.so
%{_libdir}/pkgconfig/simplemail-qt5.pc


%changelog
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
