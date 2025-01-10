%define __cmake_builddir build

%global major_so_ver 15

%define libname    libyui
%define develname  libyui-devel

# Define libsuffix.
%global libsuffix yui

#--------------------------------------------------------
# Package libyui-ncurses
%define yui_ncurses_name libyui-ncurses

%define libncurses  libyui-ncurses
%define devncurses  libyui-ncurses-devel
#--------------------------------------------------------
# Package libyui-qt
%define yui_qt_name libyui-qt

%define libqt  libyui-qt
%define devqt  libyui-qt-devel

#--------------------------------------------------------
# Package libyui-qt-graph
%define yui_qt_graph_name libyui-qt-graph

%define libqtgraph  libyui-qt-graph
%define devqtgraph  libyui-qt-graph-devel



Name:     %{libname}
Version:  4.2.16
Release:  20%{?dist}
Summary:  GUI-abstraction library

License:  (LGPLv2 or LGPLv3) and MIT
URL:      https://github.com/%{name}/%{name}
Source0:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  libtool
BuildRequires:  perl-devel
BuildRequires:  rubygems
BuildRequires:  swig
BuildRequires:  fontconfig-devel
BuildRequires:  perl-generators


BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libpng)

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)

BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libyui-mga)

%description
This is the user interface engine that provides the abstraction
from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).

Originally developed for YaST, %{name} can now be used
independently of YaST for generic (C++) applications.

%{name} has very few dependencies.

#----------------------------------------------------------
# libyui

%files
%dir %{_datadir}/%{name}
%license COPYING*
%{_libdir}/%{name}.so.%{major_so_ver}*


#----------------------------------------------------------
# libyui-devel

%package -n %develname
Summary:      libYUI, YaST2 User Interface Engine - header files
Group:        Development/C++
Requires:     %{libname} >= %{version}
Requires:     boost-devel
Provides:     %{name}-devel = %{version}-%{release}
Provides:     yui-devel = %{version}-%{release}

%description -n %develname
This is the development package for libyui user interface engine that provides
the abstraction from graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).

%files -n %develname
%{_libdir}/libyui.so
%{_libdir}/pkgconfig/libyui.pc
%{_includedir}/yui/*.h
%{_datadir}/libyui/buildtools



#-----------------------------------------------------------------------
# libyui-qt

%package -n %libqt
Summary:        Libyui - Qt (graphical) user interface
Group:          System/Libraries
Requires:       qt5-qtx11extras
Provides:       %{yui_qt_name} = %{version}-%{release}


%description -n %libqt
This package contains the Qt (graphical) user interface component for libyui.

%files -n %libqt
%doc COPYING*
%{_libdir}/yui/libyui-qt.so.%{major_so_ver}*

#-----------------------------------------------------------------------
# libyui-qt-devel

%package -n %devqt
Summary:        Libyui - Qt (graphical) user interface header files
Group:          Development/KDE and Qt
Requires:       libyui-devel
Requires:       %{yui_qt_name} = %{version}-%{release}
Provides:       yui-qt-devel = %{version}-%{release}

%description -n %devqt
This package contains the header files for the Qt based user interface
component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-qt.

%files -n %devqt
%{_includedir}/yui/qt
%{_libdir}/yui/libyui-qt*.so
%{_libdir}/pkgconfig/libyui-qt.pc


#-----------------------------------------------------------------------
# libyui-qt-graph


%package -n     %libqtgraph
Summary:        Libyui - Qt graph component for libyui.
Group:          System/Libraries
BuildRequires:  graphviz-devel
Requires:       qt5-qtx11extras
Provides:       %{yui_qt_graph_name} = %{version}-%{release}


%description -n %libqtgraph
This package contains the Qt graph component for libyui.

This is a special widget to visualize graphs such as the
storage device hierarchy (disks, partitions, subvolumes
etc.).  and similar graphviz-generated graphs.


%files -n %libqtgraph
%doc COPYING*
%dir %{_libdir}/yui
%{_libdir}/yui/%libqtgraph.so.*


#-----------------------------------------------------------------------
# libyui-qt-graph-devel


%package -n     %devqtgraph
Summary:        Libyui - Qt (graphical) user interface header files
Group:          Development/KDE and Qt
Requires:       libyui-devel
Requires:       %{yui_qt_graph_name} = %{version}-%{release}
Provides:       yui-qt-devel = %{version}-%{release}

%description -n %devqtgraph
This package contains the header files for the Qt based user interface
component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-qt.

%files -n %devqtgraph
%{_includedir}/yui/qt-graph/*


#-----------------------------------------------------------------------
# libyui-ncurses

%package -n %libncurses
Summary:        Libyui - NCurses (text based) user interface
Group:          System/Libraries
Provides:       %{yui_ncurses_name} = %{version}-%{release}


%description -n %libncurses
This package contains the NCurses (text based) user interface component for
libyui.

%files -n %libncurses
%doc COPYING*
%{_libdir}/yui/libyui-ncurses.so.%{major_so_ver}*

#-----------------------------------------------------------------------
# libyui-ncurses-devel

%package -n %devncurses
Summary:        Libyui - Header fles for the NCurses (text based) user interface
Group:          Development/Other
Requires:       libyui-devel
Requires:       %{yui_ncurses_name} = %{version}-%{release}
Provides:       yui-ncurses-devel = %{version}-%{release}

%description -n %devncurses
This package contains the header files for the NCurses (text based) user
interface component for libyui.

This package is not needed to develop libyui-based applications, only to
develop extensions for libyui-ncurses.

%files -n %devncurses
%{_libdir}/yui/libyui-ncurses*.so
%{_includedir}/yui/ncurses
%{_libdir}/pkgconfig/libyui-ncurses.pc


#----------------------------------------------------------
# libyui-ncurses-tools

%package -n %{yui_ncurses_name}-tools

Summary:        Libyui - tools for the NCurses (text based) user interface
Group:          System/Libraries
Requires:       screen

%description -n %{yui_ncurses_name}-tools
This package contains tools for the NCurses (text based) user interface
component for libyui:

libyui-terminal - useful for testing on headless machines

%files -n %{yui_ncurses_name}-tools
%{_bindir}/libyui-terminal

#----------------------------------------------------------
# ruby-yui

%package -n ruby-yui
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Ruby bindings for libyui
Group:          Development/Ruby

%description -n ruby-yui
This package provides Ruby language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%files -n ruby-yui
%doc libyui-bindings/swig/ruby/examples/*.rb
%{ruby_vendorarchdir}/_yui.so

#----------------------------------------------------------
# python3-yui

%package -n python3-yui
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Python 3 bindings for libyui
Group:          Development/Python


%description -n python3-yui
This package provides Python 3 language bindings to access functions of libyui,
the YaST User Interface engine that provides the abstraction from graphical
user interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%files -n python3-yui
%doc libyui-bindings/swig/python/examples/*.py
%{python3_sitearch}/_yui.so
%{python3_sitearch}/yui.*
%{python3_sitearch}/__pycache__/*

#----------------------------------------------------------
# perl-yui

%package -n perl-yui
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Perl bindings for libyui
Group:          Development/Perl

%description -n perl-yui
This package provides Perl language bindings to access functions of libyui, the
YaST User Interface engine that provides the abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).

%files -n perl-yui
%doc libyui-bindings/swig/perl/examples/*.pl
%{perl_vendorarch}/yui.so
%{perl_vendorlib}/yui.pm

#----------------------------------------------------------


%prep
%autosetup -p1


%build
  for pkgname in libyui libyui-qt libyui-qt-graph libyui-ncurses libyui-bindings ;do
    pushd $pkgname

    %cmake \
        -DWERROR=FALSE \
        -DBUILD_EXAMPLES=OFF \
        -DWITH_MGA=ON \
        -DWITH_MONO=OFF \
        -DPYTHON_EXECUTABLE=%{python3} \
        -DPYTHON_INCLUDE_DIR=%{_includedir}/python%{python3_version} \
        -DPYTHON_SITEDIR=%{python3_sitearch} \
        -DPYTHON_LIB_DIR=%{python3_sitelib}

    %cmake_build

    popd
  done

%install

for pkgname in libyui libyui-qt libyui-qt-graph libyui-ncurses libyui-bindings ;do
  pushd $pkgname
  %cmake_install
  popd
done

install -m0755 -d %{buildroot}%{_libdir}/yui


%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.16-20
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.16-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.16-17
- Perl 5.40 rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.2.16-16
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.16-13
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.16-11
- Perl 5.38 rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.2.16-10
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.16-8
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Mon Dec 12 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.16-7
- Add BR perl-generators to automatically generates run-time dependencies
  for installed Perl files

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.2.16-5
- Rebuilt for Python 3.11

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.2.16-4
- Perl 5.36 rebuild

* Tue Mar 08 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 4.2.16-3
- Cmake with-mga enabled.

* Tue Feb 22 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 4.2.16-2
- Adding libyui-qt-graph and spec file clean up

* Tue Feb 22 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 4.2.16-1
- Version 4.2.16

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Jeff Law <law@redhat.com> - 3.10.0-2
- Fix dynamic casts to avoid gcc-11 diagnostics

* Sat Aug 01 2020 Neal Gompa <ngompa13@gmail.com> - 3.10.0-1
- Rebase to 3.10.0 (#1669818)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.3-7
- Fix FTBFS - updated path of hardlink

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.3.3-4
- Fix gcc-8 build issue

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.3-1
- New upstream release
- Dependency on cmake-filesystem is autogenerated now
- Skip building of LaTeX-docs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.2-6
- Require cmake-filesystem

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 3.3.2-4
- Rebuilt for Boost 1.64

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.2-3
- Rebuilt for bootstrapping new arch: s390x

* Sun Apr 23 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.2-2
- Fix macros-file

* Tue Apr 18 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.2-1
- New upstream release
- Drop patches, merged upstream
- Improve macros-file

* Sun Apr 16 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.1-6
- Updated patch

* Sat Apr 15 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.1-5
- Updated patches

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.1-4
- Add README.md to %%doc

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.1-3
- Updated patches
- Add some rpm-macros to macros-file

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.1-2
- Add patches adding some improvements

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.1-1
- New upstream release

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.0-1
- New upstream release
- Spec-file cosmetics

* Tue Apr 11 2017 Björn Esser <besser82@fedoraproject.org> - 3.2.9-1
- New upstream release

* Mon Apr 10 2017 Björn Esser <besser82@fedoraproject.org> - 3.2.8-4
- Use rich-dependencies instead of virtual provides
- Add macro to share major so-ver with libyui-*-packages

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.2.8-2
- Rebuilt for Boost 1.63

* Fri Nov 18 2016 Christian Dersch <lupinix@mailbox.org> - 3.2.8-1
- new version

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 3.2.5-1
- new upstream release
- drop Patch0, applied in upstream tarball

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 3.2.4-2
- add Patch0, fix nullptr-checks with GCC6 in YDialog
- do not append '-fno-delete-null-pointer-checks' to %%optflags,
  keeping optimized performance

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 3.2.4-1
- new upstream release
- drop Patch1, applied in upstream tarball
- keep nullptr-checks with GCC6
- handle %%license and %%doc properly

* Wed Feb 10 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.1-5
- Add 0001-Fixed-a-compilation-error-in-YTableCell-with-GCC-6-b.patch
  (Fix F24FTBFS)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.2.1-3
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.2.1-2
- Rebuilt for Boost 1.59

* Thu Aug 27 2015 Björn Esser <bjoern.esser@gmail.com> - 3.2.1-1
- new upstream release

* Thu Aug 27 2015 Björn Esser <bjoern.esser@gmail.com> - 3.2.1-0.1
- bootstrapping for so-name-bump

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.1.5-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.5-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 3.1.5-2
- Rebuild for boost 1.57.0

* Mon Jan 19 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.5-1
- new upstream release (#1183540)
- release-build

* Mon Jan 19 2015 Björn Esser <bjoern.esser@gmail.com> - 3.1.5-0.1
- new upstream release (#1183540)
- bootstrap-build for so-name-bump
- purged ldconf-override
- keep doc-files in unfied %%{_pkgdocdir}
- small improvements to spec-file

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Björn Esser <bjoern.esser@gmail.com> - 3.0.13-6
- fix dir: ldconf.so.conf.d ---> ld.so.conf.d

* Sat May 24 2014 Björn Esser <bjoern.esser@gmail.com> - 3.0.13-5
- add %%{_sysconfdir}/ldconf.so.conf.d/%%{name}-%%{_arch}.conf
- add COPYING.gpl-3

* Sat May 24 2014 Björn Esser <bjoern.esser@gmail.com> - 3.0.13-4
- no need to provide `%%{name}-devel-common`

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 3.0.13-3
- rebuilt with dependency on yui-ui with strict abi

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 3.0.13-2
- remove build of pdf-autodocs
- minor improvents on spec

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.0.13-1
- Rebuild for boost 1.55.0

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 3.0.13-0
- new upstream release (#1048445)

* Fri Aug 30 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.10-1
- new upstream version

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 3.0.9-2
- Rebuild for boost 1.54.0

* Sat Jul 27 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.9-1
- new upstream version
- restructured spec for better readability
- removed %%commit, using direct github-tarball
- removed hardening flags and Group-tag
- removed CMake-Requires from devel-pkg
- added devel-common-pkg
- fixed License
- installing docs manually, adding PDF to doc-pkg

* Thu May 16 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.5-2
- fixed -doc licensing html/ is LGPLv2 or LGPLv3 examples/ is MIT

* Thu May 16 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.5-1
- new upstream version: obsoletes Patch0/1
- modified Requires: yui_ui to to depend on %%{major_so_ver}
- install lib*.so.%%{major_so_ver}* in main-pkg not lib*.so.*
- add `-DRESPECT_FLAGS=ON`

* Wed May 15 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.4-2
- readded Requires: yui_ui with conditional for ABI changes as proposed:
  https://bugzilla.redhat.com/show_bug.cgi?id=959926#c9

* Wed May 15 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.4-1
- new upstream version
- add Patch1 to skip generation of pdf-docs if doxygen-latex is installed.
- added needed bootstrap to prep

* Tue May 14 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.3-3
- removed macro from Patch0.
- fixed typo -> s/pakage/package/
- removed Provides/Requires: yui_ui

* Mon May 13 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.3-2
- fixup as suggested in https://bugzilla.redhat.com/show_bug.cgi?id=959926#c2
- add Patch0 to obey conventions about the compiler flags set in the system
  rpm configuration. See:
  https://fedoraproject.org/wiki/Packaging:Guidelines#Compiler_flags
- fixup as suggested in https://bugzilla.redhat.com/show_bug.cgi?id=959926#c4
- build a hardened version just in case
- add Requires: yui-ui, because libyui without UI-plugins is as
  useful as a car without gas and tires.
- add -devel Provides: yui-ui to provide a FAKE yui-ui to
  satisfy dependencies during rpmbuild of the UI-plugins and made sure this
  is known by documenting this in libyui-devel description.
- add -devel Requires: cmake to solve the /usr/lib*/cmake/ ownership-problem,
  which is needed for libyui*-builds anyways.

* Mon May 06 2013 Björn Esser <bjoern.esser@gmail.com> - 3.0.3-1
- Initial RPM release.
