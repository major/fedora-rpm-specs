Name:          openpgm
Version:       5.2.122
%global name_alias        pgm
%global version_main      5.2
%global version_dash_main 5-2
%global version_dash      %{version_dash_main}-122
Release:       37%{?dist}
Summary:       An implementation of the PGM reliable multicast protocol

License:       LGPL-2.1-or-later
# New URL is https://github.com/steve-o/openpgm
# The files are now on https://code.google.com/archive/p/openpgm/downloads
URL:           https://github.com/steve-o/%{name}
Source0:       https://github.com/steve-o/%{name}/archive/release-%{version_dash}.tar.gz#/%{name}-%{version}.tar.gz

# All the following patches have been submitted upstream
# as a merge request: https://github.com/steve-o/openpgm/pull/64
Patch2:        openpgm-02-c-func.patch
Patch3:        openpgm-03-pkgconfig.patch
Patch4:        openpgm-04-py-version-gen.patch
Patch5:        openpgm-05-fix-setgid.patch
Patch6:        openpgm-configure-c99.patch
Patch7:        openpgm-c99.patch

BuildRequires: make
BuildRequires: libtool automake autoconf
BuildRequires: gcc
BuildRequires: python3
BuildRequires: dos2unix
BuildRequires: perl-interpreter


%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.


%package devel
Summary:       Development files for openpgm
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains OpenPGM related development libraries and header files.


%prep
%setup -q -n %{name}-release-%{version_dash}/%{name}/%{name_alias}
%patch -P2 -p3
%patch -P3 -p3
%patch -P4 -p3
%patch -P5 -p3
%patch -P6 -p3
%patch -P7 -p3
dos2unix examples/getopt.c examples/getopt.h

%build
libtoolize --force --copy
aclocal
autoheader
automake --copy --add-missing
autoconf
%configure

# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful, even on
# architectures were the ASM is not valid when compiling with LTO.
#
# -ffat-lto-objects is sufficient to address this issue.  It is the default
# for F33, but is expected to only be enabled for packages that need it in
# F34, so we use it here explicitly
%define _lto_cflags -flto=auto -ffat-lto-objects

%make_build

%install
%make_install

# Remove the static libraries and the temporary libtool artifacts
rm -f %{buildroot}%{_libdir}/lib%{name_alias}.{a,la}

# Move the header files into /usr/include
mv -f %{buildroot}%{_includedir}/%{name_alias}-%{version_main}/%{name_alias} %{buildroot}%{_includedir}/

%files
%doc COPYING LICENSE
%{_libdir}/*.so.*


%files devel
%doc examples/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openpgm-5.2.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 5.2.122-36
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan  3 2023 Florian Weimer <fweimer@redhat.com> - 5.2.122-30
- C99 compatibility fixes

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Jeff Law <law@redhat.com> - 5.2.122-25
- Re-enable LTO

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jeff Law <law@redhat.com> - 5.2.122-23
- Disable LTO

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 5.2.122-21
- The header files are now installed directly in /usr/include

* Wed Oct 30 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 5.2.122-20
- Suppressed the dependency on SCons (as autotools are used instead)
- Fixed the generated version minor number (from 127 to 122)
- Fixed the target include directory

* Wed Oct 30 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 5.2.122-19
- Merged with the EPEL 8 version, i.e., with modernized way of packaging

* Sat Oct 26 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 5.2.122-18
- Updated the source URL and Python to Python 3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 5.2.122-15
- Remove non-existent directory from pkgconfig file

* Wed Sep 19 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 5.2.122-14
- Use python2 explicitly (#1605329).
- Remove unnecessary calls to ldconfig.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.2.122-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 5.2.122-8
- Add perl to the build requirements list (required by galois_generator.pl)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.122-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.122-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.122-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.122-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.2.122-1
- Update to 5.2.122

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.118-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.1.118-3
- Build requires python (no longer available by default in F18+ buildroots)

* Fri Dec 21 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.1.118-2
- Renamed the tarball (replaced '%7E' by '~')
- Removed the defattr lines

* Wed Dec 19 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.1.118-1
- Change license from LGPLv2.1 to LGPLv2 (867182#c13)

* Tue Dec 18 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.1.118-0
- First Fedora specfile

# vim:set ai ts=4 sw=4 sts=4 et:
