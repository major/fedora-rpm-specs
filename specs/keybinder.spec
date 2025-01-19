Name:		keybinder
Version:	0.3.1
Release:	31%{?dist}
Summary:	A library for registering global keyboard shortcuts
# python-keybinder/__init__.py	unused
# SPDX confirmed
License:	MIT
URL:		https://github.com/engla/keybinder
Source0:	%url/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gtk2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	/usr/bin/gtkdocize
Obsoletes:		python2-%{name} < 0.3.1-16


%description
keybinder is a library for registering global keyboard shortcuts. 
Keybinder works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- An examples directory with programs in C, Lua, and Vala.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the development files for %{name}.


%prep
%setup -q -n %{name}-%{version}
sed -i -e 's@-rpath @@g' libkeybinder/Makefile.in \
	lua-keybinder/Makefile.in python-keybinder/Makefile.in
autoreconf -fiv

%build
PY2_STATUS=disable
%configure --disable-static --${PY2_STATUS}-python --disable-lua \
	--disable-silent-rules
%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la'| xargs rm -f


%ldconfig_scriptlets

%files
%doc NEWS
%doc AUTHORS
%doc README
%license COPYING
%{_libdir}/libkeybinder.so.0{,.*}
%{_libdir}/girepository-1.0/Keybinder-*.typelib
%{_datadir}/gir-1.0/Keybinder-*.gir

%files devel
%{_includedir}/keybinder.h
%{_libdir}/pkgconfig/keybinder.pc
%{_libdir}/libkeybinder.so
%{_datadir}/gtk-doc/html/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-29
- SPDX confirmation, add license file

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-21
- BR: gtkdocize for autoconf-271 -fi

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-17
- Kill python2 binding for F-31+
- Enable gobject-instrospection on F-31+

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-14
- Rebuild for F-31 unretirement

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.3.1-12
- Fix f29 FTBFS (rhbz#1604486)
- spec file clean up

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.1-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.1-8
- Python 2 binary package renamed to python2-keybinder
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.3.1-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Johannes Lips <hannes@fedoraproject.org> - 0.3.1-1
- update to 0.3.1
- change of upstream URL

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Johannes Lips <hannes@fedoraproject.org> - 0.3.0-4
- disabled the lua bindings to make it buildable again

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Johannes Lips <hannes@fedoraproject.org> - 0.3.0-1
- update to version 0.3.0
- added the gtk-doc file to the devel package

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.2-7
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Johannes Lips <Johannes.Lips googlemail com> 0.2.2-5
- moved the pkgconfig into the devel subpackagae

* Mon Nov 01 2010 Johannes Lips <Johannes.Lips googlemail com> 0.2.2-4
- added the %%{release} tag to the Requires section of the subpackages

* Sun Oct 17 2010 Johannes Lips <Johannes.Lips googlemail com> 0.2.2-3
- removed the *.la file from python subpackage
- added the GPLv2+ license tag for the python subpackage
- fixed ownership of the lua-directory

* Sat Oct 16 2010 Johannes Lips <Johannes.Lips googlemail com> 0.2.2-2
- added an additional lua subpackage
- added the MIT license
- fixed issues with files in the wrong subpackage
- added a filter macro in the python subpackage
- added a %%postun section

* Thu Oct 07 2010 Johannes Lips <Johannes.Lips googlemail com> 0.2.2-1
- initial fedora spec
