Name:           mdbtools
Version:        1.0.0
Release:        8%{?dist}
Summary:        Access data stored in Microsoft Access databases
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/mdbtools/mdbtools/
Source0:        https://github.com/mdbtools/mdbtools/releases/download/v%{version}/mdbtools-%{version}.tar.gz
Patch1:         mdbtools-0.9.3-mdb-sql-compile-fix.patch
Patch2:         mdbtools-1.0.0-s390x-build-fix.patch
BuildRequires:  make gcc
BuildRequires:  libxml2-devel glib2-devel unixODBC-devel readline-devel gettext-devel
BuildRequires:  bison flex txt2man rarian-compat bash-completion
BuildRequires:  libtool autoconf automake
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# No provides this is here because starting with 0.9.y upstream has dropped gmdb2
Obsoletes:      %{name}-gui <= 0.7.1-99

%description
MDB Tools is a suite of programs for accessing data stored in Microsoft
Access databases.


%package libs
Summary:        Library for accessing data stored in Microsoft Access databases
License:        LGPLv2+

%description libs
This package contains the MDB Tools library, which can be used by applications
to access data stored in Microsoft Access databases.


%package        devel
Summary:        Development files for %{name}
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}, glib2-devel, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        odbc
Summary:        MDB Unix-ODBC driver
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    odbc
The mdbtools-odbc package contains a Unix-ODBC driver using
the mdbtools SQL front-end for MDB files.


%prep
%autosetup -p1
autoreconf -vif


%build
%configure --disable-static --with-unixodbc="%{_prefix}"
%make_build V=1


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete


%ldconfig_scriptlets libs


%files
%license COPYING
%{_bindir}/mdb-*
%{_mandir}/man1/mdb-*.1.gz
%{_datadir}/bash-completion

%files libs
%doc AUTHORS NEWS README.md
%license COPYING.LIB
%{_libdir}/libmdb*.so.*

%files devel
%doc HACKING.md
%{_libdir}/libmdb*.so
%{_libdir}/pkgconfig/libmdb*.pc
%{_includedir}/mdb*.h

%files odbc
%{_libdir}/odbc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Hans de Goede <hdegoede@redhat.com> - 1.0.0-5
- Fix FTBFS (rhbz#2261371)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 23 2023 Hans de Goede <hdegoede@redhat.com> - 1.0.0-1
- New upstream release 1.0.0
- Fix FTBFS (rhbz#2171606)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul  8 2021 Hans de Goede <hdegoede@redhat/com> - 0.9.3-1
- New upstream release 0.9.3 (rhbz#1912551)
- This no longer includes the gmdb2 GUI, drop the -gui subpackage
- Add a new -odbc subpackage for the Unix-ODBC drivers
- Modernize the specfile a bit

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-13
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.1-6
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-1
- Update to 0.7.1
- Update site/source to github urls
- Cleanup spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.14.cvs20051109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-0.13.cvs20051109
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.12.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.11.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.10.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6-0.9.cvs20051109.1
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.8.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.7.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Karsten Hopp <karsten@redhat.com> 0.6-0.6.cvs20051109.1
- bump and rebuild for current unixODBC libs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.6.cvs20051109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.5.cvs20051109
- Fix several issues with the odbc interface (rh 472692)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6-0.4.cvs20051109
- Autorebuild for GCC 4.3

* Tue Aug 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.3.cvs20051109
- Stop gmdb from crashing when selecting close without a file being open
  (bz 251419)
- Change release field from 0.x.pre1 to 0.x.cvs20051109, as that more acurately
  reflects our upstream base (bz 251419)

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.2.pre1
- Stop gmdb from crashing when selecting file->properties without having a file
  loaded (bz 251419)
- Don't install headers used to build tools (install only those of libmdb)
- Add glib2-devel to the -devel Requires

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.1.pre1
- There were lots of compile warnings, looking for a fix I found that upstream
  is dead, but that Debian has sort of continued as upstream based on the
  0.6pre1 release; Switching to Debian "upstream" release 0.6pre1 (20051109-4)

* Wed Aug  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5-1
- Initial Fedora package (based on specfile by Dag Wieers, thanks!)
