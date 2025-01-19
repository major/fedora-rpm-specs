# Sources use deprecated Qt4 code.
# https://bugreports.qt.io/browse/QTBUG-29333
# https://codereview.qt-project.org/#/c/107725/
# https://codereview.qt-project.org/#/c/105285/
%bcond_without  qt5

%global gitdate 20140202
%global commit0 6ada849baca7918078e53f7dece4d96b2a0e6210

Name:           lxqt-config-randr
Version:        0.1.2
%if 0%{?gitdate}
Release:        24.%{gitdate}git%(c=%{commit0}; echo ${c:0:7} )%{?dist}
%else
Release:        23%{?dist}
%endif
Summary:        GUI interface to RandR extension

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/zballina/%{name}
%if 0%{?gitdate}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
%else
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
# Initial qt5 support
Patch0:         http://bazaar.launchpad.net/~lubuntu-dev/lxde/%{name}/diff/29#/%{name}-qt5.patch

BuildRequires: make
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  desktop-file-utils

%if %with qt5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  qt5-linguist
%endif

# qmake-qt4, even needed to configure qt5
BuildRequires:  qt4-devel

%description
Qt-based tool to configure the X output using the RandR 1.3/1.2 extension,
based in KDE parts, intended to be a viable option for the LXQt desktop.


%prep
%if 0%{?gitdate}
%setup -qn%{name}-%{commit0}
# revert Virtual Modes: Fixing bug in Brightness setting (PR#6)
# commit/3aa7fa26fb61a7a521443ff3ef1d3abc574f609e
# prevents gcc error: 'sleep' was not declared in this scope
sed -i /sleep/d src/randrcrtc.cpp
%else
%setup -q
%endif
%if %with qt5
%patch -P0 -p0
# fixes for Fedora Qt5.6
sed -i -r -e 's,(find_package.lxqt)-qt5,\1,' -e /include/d CMakeLists.txt
# permessive gcc
sed -i s,None,0, src/randroutput.cpp
%endif

%build
%cmake_lxqt -DCMAKE_BUILD_TYPE:STRING=Debug \
%if %with qt5
 -DUSE_QT5:BOOL=ON
%endif
%cmake_build

%install
%cmake_install
# Exclude category as been Service 
desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt \
 --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING*
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-24.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.2-23.20140202git6ada849
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-21.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-20.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-19.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Raphael Groner <raphgro@fedoraproject.org> - 0.1.2-15.20140202git6ada849
- use cmake macros properly for out-of-source builds 

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12.20140202git6ada849
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3.20140202git6ada849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Raphael Groner <projects.rg@smart.ms> - 0.1.2-2.20140202git6ada849
- add+improve qt5 patch from lubuntu
- enable full debug build

* Fri May 13 2016 Raphael Groner <projects.rg@smart.ms> - 0.1.2-1.20140202git6ada849
- initial
