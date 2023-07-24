%global maj 0
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:       suil
Version:    0.10.12
Release:    4%{?dist}
Summary:    A lightweight C library for loading and wrapping LV2 plugin UIs

License:    MIT 
URL:        https://drobilla.net/software/suil/
Source0:    https://download.drobilla.net/%{name}-%{version}.tar.bz2
Patch0:     %{name}-doc-installation-dir.patch

BuildRequires:  doxygen
BuildRequires:  graphviz
# https://fedoraproject.org/wiki/Packaging:Python#Dependencies
BuildRequires:  python3
BuildRequires:  lv2-devel >= 1.16.0
# we need to track changess to these toolkits manually due to the 
# requires filtering below
BuildRequires:  gtk2-devel >= 2.18.0
BuildRequires:  gtk3-devel >= 3.14.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core) >= 5.1.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.1.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.1.0
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme

# Lets not necessarily pull in toolkits dependancies. They will be provided by
# the host and or the plugin
%define __requires_exclude ^lib.*$

%description
%{name} makes it possible to load a UI of any toolkit in a host using any other 
toolkit (assuming the toolkits are both supported by %{name}). Hosts do not need
to build against or link to foreign toolkit libraries to use UIs written with 
that toolkit (%{name} performs its magic at runtime using dynamically 
loaded modules). 

%package devel
Summary:    Development libraries and headers for %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
This package contains the headers and development libraries for %{name}.

%prep
%autosetup -p1
# Don't run ldconfig
sed -i -e "s|bld.add_post_fun(autowaf.run_ldconfig)||" wscript

%build
%set_build_flags
%{python3} waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --docdir=%{_pkgdocdir} \
    --no-cocoa \
    --docs
%{python3} waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} %{python3} waf install
chmod +x %{buildroot}%{_libdir}/lib%{name}-0.so.*
install -pm 644 AUTHORS NEWS README.md %{buildroot}%{_pkgdocdir}

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/%{name}-%{maj}
%license COPYING
%dir %{_libdir}/suil-%{maj}
%{_libdir}/lib%{name}-*.so.%{maj}*
%{_libdir}/suil-%{maj}/libsuil_x11_in_gtk2.so
%{_libdir}/suil-%{maj}/libsuil_gtk2_in_qt5.so
%{_libdir}/suil-%{maj}/libsuil_x11_in_qt5.so
%{_libdir}/suil-%{maj}/libsuil_qt5_in_gtk2.so
%{_libdir}/suil-%{maj}/libsuil_x11.so
%{_libdir}/suil-%{maj}/libsuil_x11_in_gtk3.so
%{_libdir}/suil-%{maj}/libsuil_qt5_in_gtk3.so

%files devel
%{_libdir}/lib%{name}-%{maj}.so
%{_libdir}/pkgconfig/%{name}-%{maj}.pc
%{_includedir}/%{name}-%{maj}/
%{_pkgdocdir}/%{name}-%{maj}

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.12-1
- Update to 0.10.12
- Drop deprecated qt4 support

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.8-1
- Update to 0.10.8

* Thu Sep 03 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.6-7
- Remove old style dependency generators
- Correctly glob shared libraries
- Set all compiler flags

* Wed Aug 12 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.6-6
- Fix FTBFS in Fedora rawhide/f33
- Add minimal qt5 BRs
- Correct wrong date in changelog

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Jeff Law <law@redhat.com> - 0.10.6-3
- Drop qt5-devel buildrequires

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.6-1
- Update to 0.10.6

* Tue Sep 10 2019 Jan Beran <jaberan@redhat.com> - 0.10.2-5
- Do not use explicit compress formats
 
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.2-2
- Fix wrong Cocoa detection on some arches
- Enable Gtk3 support

* Fri Dec 28 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.2-1
- New upstream release 0.10.2
- Use ldconfig_scriptlets macro
- Use python3

* Sun Jul 15 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.0-4
- Fix FTBFS due to the move of /usr/bin/python into a separate package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.0-1
- New upstream release 0.10.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.4-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Tue Mar 14 2017 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.4-1
- Update to 0.8.4
- Use hardened LDFLAGS
- Remove deprecated Groups tags
- Enable Qt5 Support
- Use license macro

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Kevin Fenzi <kevin@scrye.com> - 0.8.2-2
- Rebuild for rpm bug 1131892

* Wed Aug 20 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.8.2-1
- Update to 0.8.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 11 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.8.0-1
- Update to 0.8.0

* Mon Dec 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.16-2
- Install docs to %%{_pkgdocdir} where available (#994119).

* Mon Sep 23 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.6.16-1
- Update to 0.6.16 (minor Qt fix, NULL extension data)

* Sun Aug 25 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.6.14-1
- Update to version 0.6.14

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.6.12-1
- New upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.6.10-1
- New upstream

* Sat Dec 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.6.6-1
- New upstream

* Tue Jul 24 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.6.0-4
- Remove unwanted man file generated from doxygen

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.6.0-2
- New upstream release

* Sat Apr 07 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.4-6
- Add filter_from_requires macro to remove unwanted Gtk/Qt dependancies

* Fri Mar 30 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.4-5
- License change to MIT, adjust descriptions

* Wed Feb 22 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.4-4
- Split into Qt and GTK packages

* Mon Feb 06 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.4-3
- Correct directory ownsership and runtime library placement

* Wed Jan 25 2012 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.4-2
- Correct build requires

* Fri Dec 23 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.4-1
- Initial build
