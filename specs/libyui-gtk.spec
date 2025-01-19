# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build
%define		major	15

Name:		libyui-gtk
Version:	2.52.5
Release:	4%{?dist}
Summary:	Gtk3 User Interface for libyui

# Automatically converted from old format: LGPLv2 or LGPLv3 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2 OR LGPL-3.0-only
URL:		https://github.com/libyui/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	sane-backends-devel
BuildRequires:	cmake
BuildRequires:	gtk3-devel
BuildRequires:	libyui-devel >= 4.0.0

Supplements:	(libyui%{?_isa} and gtk3%{?_isa})

%description
This package contains the Gtk3 user interface component
for libyui.


%package devel
Summary:	Files needed for developing with %{name}

Requires:	gtk3-devel%{?_isa}
Requires:	libyui-devel%{?_isa}
Requires:	%{name}%{?_isa}		== %{version}-%{release}

%description devel
libyui can be used independently of YaST for generic (C++)
applications and has very few dependencies.

You do NOT need this package for developing with libyui.
Usinglibyui-devel is sufficient for such purpose. This
package is only needed when you want to develop an extension
for %{name} which is not covered within the UI-plugin.

%prep
%autosetup

%build
%cmake							\
	-DENABLE_WERROR=OFF				\
	-DYPREFIX=%{_prefix}				\
	-DLIB_DIR=%{_libdir}				\
	-DCMAKE_BUILD_TYPE=RELEASE			\

%cmake_build

%install
%cmake_install

%files
%license COPYING*
%{_libdir}/yui/%{name}.so.%{major}.0.0
%{_libdir}/yui/%{name}.so.%{major}

%files devel
%{_includedir}/yui/*
%{_libdir}/yui/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.52.5-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.52.5-1
- Update to 2.52.5

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 2.52.0-8
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.52.0-6
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.52.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.52.0-3
- Rebuilt for Boost 1.78

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.52.0-2
- Rebuilt for libyui

* Tue Feb 22 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 2.52.0-1
- Version 2.52.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Neal Gompa <ngompa13@gmail.com> - 2.49.0-1
- Rebase to 2.49.0 (#1669819)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.44.9-14
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-9
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Mon Jul 31 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-8
- Apply patches only on fc25+ or el8+

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-7
- Require cmake-filesystem

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.44.9-5
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-4
- Rebuilt for bootstrapping new arch: s390x

* Wed Apr 19 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-3
- Add patches submitted upstream

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-2
- Change Supplements: back to gtk3, since libYUI provides selection
  of UI-plugin based on used desktop environment

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.9-1
- New upstream release

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-4
- Rebuilt for libyui.so.8

* Wed Apr 12 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-3
- Optimized Supplements: to be not too generic
- Spec-file cosmetics

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-2
- Use rich-dependencies instead of virtual provides
- Get major so-ver from macro

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.44.8-1
- New upstream release fixing GTK-warnings

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.44.7-2
- Rebuilt for Boost 1.63

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 2.44.7-1
- new upstream release
- handle %%license and %%doc properly

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.44.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.44.5-14
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.44.5-13
- Rebuilt for Boost 1.59

* Thu Aug 27 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-12
- rebuilt for so-name-bump in libyui-3.2.1

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.44.5-10
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.5-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-7
- rebuilt for libyui-3.1.5, again

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-6
- Rebuild for boost 1.57.0

* Tue Jan 20 2015 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-5
- rebuilt for libyui-3.1.5
- keep doc-files in unfied %%{_pkgdocdir}
- small improvements to spec-file

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.44.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-2
- no need to provide `%%{name}-devel-common`

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 2.44.5-1
- new upstream release

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 2.43.7-3
- Rebuild for boost 1.55.0

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 2.43.7-2
- rebuilt for libyui-3.0.13
- remove build of pdf-autodocs
- remove the devel-common subpkg
- minor improvents on spec

* Fri Aug 30 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.7-1
- new upstream version
- restructured spec to match with libyui

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-3
- build fails on rawhide with -Werror enabled, because of
  'gtk_widget_modify_fg' is deprecated in gtk3-devel >= 3.9.0,
  use 'gtk_widget_override_color' instead [-Werror=deprecated-declarations]
- informed upstream and provided build-logs
- added cmake -DENABLE_WERROR=OFF

* Thu May 16 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-2
- changed Provides: `yui_ui =` from `version` to `major_so_ver`
- install lib*.so.`major_so_ver`* in main-pkg not lib*.so.*
- add `-DRESPECT_FLAGS=ON`, will be honored by libyui <= 3.0.5
- removed macros from changelog

* Wed May 15 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.3-1
- new upstream version
- adjusted libyui-devel min-version
- added needed bootstrap to prep

* Mon May 13 2013 Björn Esser <bjoern.esser@gmail.com> - 2.43.2-1
- Initial RPM release.
