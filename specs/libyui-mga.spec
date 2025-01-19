# Define libsuffix, minimum libyui-devel version
# and so-version of libyui.
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build


Name:			%{libname}-mga
Version:		1.2.1
Release:		10%{?dist}
Summary:		Libyui extensions for Mageia tools

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:			https://github.com/manatools/%{name}
Source0:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	ghostscript

BuildRequires:	%{libname}-devel >= %{devel_min_ver}

%description
This package contains the Libyui extensions for Mageia tools.


%package devel
Summary:		Files needed for developing with %{name}

Requires:		%{libname}-devel%{?_isa}	>= %{devel_min_ver}
Requires:		%{name}%{?_isa}			== %{version}-%{release}

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
%cmake \
    -DBUILD_EXAMPLES=NO
%cmake_build

%install
%cmake_install

%files
%license COPYING*
%{_libdir}/%{name}.so.15*

%files devel
%{_includedir}/yui
%{_libdir}/libyui-mga.so
%{_libdir}/pkgconfig/libyui-mga.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.2.1-2
- Rebuilt for libyui

* Tue Feb 22 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.2.1-1
- Version 1.2.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Neal Gompa <ngompa13@gmail.com> - 1.1.0-1
- Rebase to 1.1.0 (#1852269)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.21.gita6a160e.20160313
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.20.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.19.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.8-0.18.gita6a160e.20160313
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.17.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.16.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.15.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.14.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.13.gita6a160e.20160313
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.12.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.11.gita6a160e.20160313
- Require cmake-filesystem

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.10.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.9.gita6a160e.20160313
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.8.gita6a160e.20160313
- Rebuilt for bootstrapping new arch: s390x

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.7.gita6a160e.20160313
- Rebuilt for libyui.so.8

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.6.gita6a160e.20160313
- Use rich-dependencies instead of virtual provides
- Get major so-ver from macro

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-0.5.gita6a160e.20160313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.4.gita6a160e.20160313
- Rebuilt for Boost 1.63

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.3.gita6a160e.20160313
- Rebuilt with dependency on MGA-UI

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.2.gita6a160e.20160313
- Initial import (rhbz#1418661)

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-0.1.gita6a160e.20160313
- Initial rpm-release (rhbz#1418661)
