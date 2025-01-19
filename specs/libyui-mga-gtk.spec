# Define libsuffix, minimum libyui-devel version
# and so-version of libyui.
%global libsuffix yui
%global libname lib%{libsuffix}
%global devel_min_ver 3.10.0
%global _libyui_major_so_ver 15


# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build


Name:			%{libname}-mga-gtk
Version:		1.2.0
Release:		14%{?git_rel}%{?dist}
Summary:		Libyui-Gtk extensions for Mageia tools

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:			https://github.com/manatools/%{name}
Source0:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:		gcc-c++
BuildRequires:		boost-devel
BuildRequires:		cmake
BuildRequires:		%{libname}-devel			>= %{devel_min_ver}
BuildRequires:		%{libname}-mga-devel		>= 1.2.0
BuildRequires:		%{libname}-gtk-devel		>= 2.49.0

Supplements:		(libyui-mga%{?_isa} and libyui-gtk%{?_isa})

%description
This package contains the Libyui-Gtk extensions for Mageia tools.


%package devel
Summary:		Files needed for developing with %{name}

Requires:		%{libname}-devel%{?_isa}		>= %{devel_min_ver}
Requires:		%{libname}-gtk-devel%{?_isa}
Requires:		%{libname}-mga-devel%{?_isa}
Requires:		%{name}%{?_isa} == %{version}-%{release}

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
%doc README.md
%{_libdir}/%{libsuffix}/%{name}.so.%{_libyui_major_so_ver}*

%files devel 
%doc ChangeLog 
%{_includedir}/yui/mga/gtk/
%{_libdir}/%{libsuffix}/%{name}.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-9
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-7
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.2.0-4
- Rebuilt for Boost 1.78

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.2.0-3
- Rebuilt for mga

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.2.0-2
- Rebuilt for libyui (with mg enabled)

* Sun Feb 27 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.2.0-1
- Version 1.2.0 and fix Install fail (#2057223)

* Sun Feb 27 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.0-7
- Rebuild for libyui-4.2.16 with libyui.so.15

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-5
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-2
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Neal Gompa <ngompa13@gmail.com> - 1.1.0-1
- Rebase to 1.1.0 (#1539457)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.22.git22f2cf6.20131215
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.21.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.20.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.2-0.19.git22f2cf6.20131215
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.18.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.17.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.16.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.15.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.14.git22f2cf6.20131215
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.13.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.12.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.11.git22f2cf6.20131215
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.10.git22f2cf6.20131215
- Rebuilt for bootstrapping new arch: s390x

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.9.git22f2cf6.20131215
- Rebuilt for libyui.so.8

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.8.git22f2cf6.20131215
- Use rich-dependencies instead of virtual provides
- Get major so-ver from macro

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.7.git22f2cf6.20131215
- Add Provides: %%{libsuffix}-mga-gui without isa-bits, too

* Thu Mar 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.6.git22f2cf6.20131215
- Add Provides: %%{libsuffix}-mga-gui

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.5.git22f2cf6.20131215
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.4.git22f2cf6.20131215
- Fix %%description

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.3.git22f2cf6.20131215
- Rebuilt for Boost 1.63

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.2.git22f2cf6.20131215
- Initial import (rhbz#1418785)

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.2-0.1.git22f2cf6.20131215
- Initial rpm-release (rhbz#1418785)
