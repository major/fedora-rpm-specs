
%define major 15
%global libsuffix yui
%global libname lib%{libsuffix}


# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build


Name:       %{libname}-mga-qt
Version:    1.2.0
Release:    11%{?dist}
Summary:    Libyui-Qt extensions for Mageia tools

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:        https://github.com/manatools/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(libyui-mga)

BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Svg)

BuildRequires:	ghostscript
BuildRequires:	graphviz
BuildRequires:	pkgconfig(fontconfig)

Requires:	libyui-qt%{?_isa}
Supplements:	(libyui-mga%{?_isa} and libyui-qt%{?_isa})

%description
This package contains the Libyui-Qt extensions for Mageia tools.


%package devel
Summary:		Files needed for developing with %{name}

Requires:	libyui-devel
Requires:	%{name} = %{version}-%{release}
Provides:	yui-mga-qt-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description devel
%{libname} can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with %{libname}.
Using %{libname}-devel is sufficient for such purpose. This
package is only needed when you want to develop an extension
for %{name}.


%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install


%files
%license COPYING*
%{_libdir}/yui/libyui-mga-qt.so.%{major}*

%files devel
%{_includedir}/yui/mga/qt/
%{_libdir}/yui/libyui-mga-qt.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 18 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.2.0-3
- Add missing runtime dependency for libyui-qt (#2075989)

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.2.0-2
- Rebuilt for mga

* Tue Feb 22 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.2.0-1
- Version 1.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 28 2021 Neal Gompa <ngompa13@gmail.com> - 1.1.0-3
- Disable Werror to fix FTBFS (#1923464)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Neal Gompa <ngompa13@gmail.com> - 1.1.0-1
- Rebase to 1.1.0 (#1539459)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.22.gitb508e88.20140119
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.21.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.20.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.3-0.19.gitb508e88.20140119
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.18.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.17.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.16.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.15.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.14.gitb508e88.20140119
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.13.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.12.gitb508e88.20140119
- Require cmake-filesystem

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.11.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.10.gitb508e88.20140119
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.9.gitb508e88.20140119
- Rebuilt for bootstrapping new arch: s390x

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.8.gitb508e88.20140119
- Rebuilt for libyui.so.8

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.7.gitb508e88.20140119
- Use rich-dependencies instead of virtual provides
- Get major so-ver from macro

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.6.gitb508e88.20140119
- Add Provides: %%{libsuffix}-mga-gui without isa-bits, too

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.5.gitb508e88.20140119
- Add Provides: %%{libsuffix}-mga-gui

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.4.gitb508e88.20140119
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.3.gitb508e88.20140119
- Rebuilt for Boost 1.63

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.2.gitb508e88.20140119
- Initial import (#1418882)

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-0.1.gitb508e88.20140119
- Initial rpm-release (#1418882)
