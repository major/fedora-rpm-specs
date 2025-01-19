Name:           libirman
Epoch:          1
Version:        0.5.2
Release:        23%{?dist}
Summary:        Library for IRMAN hardware


#The files which make up the library are covered under the GNU Library
#General Public License, which is in the file COPYING.lib.
#The files which make up the test programs and the documentation are covered
#under the GNU General Public License, which is in the file COPYING.
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/libirman/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf, automake, libtool
BuildRequires:  lirc-devel >= 0.9.4
BuildRequires: make

%description
Runtime libraries for accessing the IrMan hardware.

The IrMan hardware((http://www.intolect.com/irmandetail.htm) is  nowadays
discontinued. However, some modern hardware (notably the irtoy) is able to
emulate the irman protocol.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    devel
Libraries and header files for developing applications that use %{name}.

The IrMan hardware((http://www.intolect.com/irmandetail.htm) is  nowadays
discontinued. However, some modern hardware (notably the irtoy) is able to
emulate the irman protocol.


%package  -n    lirc-drv-irman
Summary:        lircd(8) plugin for handling IrMan devices.
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       lirc >= 0.9.4

%description  -n lirc-drv-irman
A lirc plugin with a single driver, replacing the irman support which
was built-in in lirc prior to 0.9.4.


%prep
%setup -q


%build
libtoolize --force --copy --install
autoreconf -i
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete
rm  $RPM_BUILD_ROOT%{_docdir}/libirman/TECHNICAL


%ldconfig_scriptlets


%files
%doc COPYING* README TODO NEWS
%config(noreplace) %{_sysconfdir}/irman.conf
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%doc TECHNICAL
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libirman.pc

%files -n lirc-drv-irman
%{_libdir}/lirc/plugins/irman.so
%{_docdir}/lirc/plugindocs/irman.html
%{_datadir}/lirc/configs/irman.conf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.5.2-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1:0.5.2-3
- Added Epoch.

* Thu Jun 02 2016 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.5.2-1
- Update to upstream.

* Mon Jan 11 2016 Alec Leamas <leamas.alec@gmail.com> - 0.5.1-2
- Adding patch for updated lirc logging.

* Thu Jan 07 2016 Alec Leamas <leamas.alec@gmail.com> - 0.5.1-1
- Updating to upstream version 0.5.1
- New upstream URL.
- Build the lirc-drv-irman plugin package  (-> R: lirc >= 0.9.4)
- Removing outdated stuff.

* Sun Oct 18 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.5.0-2
- Renew "missing" file using autoreconf -f -i.

* Mon Oct 12 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.5.0-1
- Update to upstream.
- Updated source URL.
- Added libirman.pc file.
- Removed missing option --disable-rpath.

* Thu Jun 18 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.5-14
- Fix build problems.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.5-9
- udpdate URL
- added autoreconf to prep section (bz#925781)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.5-3
- added libtoolize to fix build for f11

* Sat Apr 18 2009 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.5-2
- added autoreconf and --disable-rpath

* Fri Apr 10 2009 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.5-1
- new upstream
- updated Source0 to sourceforge
- removed autoconf things

* Thu Apr 02 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.4-5.20090314cvs
- removed cvs patch, added instructions to create cvs snapshot tar package,
  which is now defined as Source0

* Sat Mar 14 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.4-4.20090314cvs
- applied cvs patch, which fixed dynamic library build and IRMAN restart
- added BuildRequires: autoconf, automake, libtool

* Sat Dec  6 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.4.4-3
- initial release
