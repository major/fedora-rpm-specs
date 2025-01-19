%global        cvs 20080502

Summary:       Library of Assorted Spiffy Things
Name:          libast
Version:       0.7.1
Release:       0.44.%{cvs}cvs%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           http://www.eterm.org/
# Sources are pulled from cvs:
# $ cvs -z3 -d :pserver:anonymous@anoncvs.enlightenment.org:/var/cvs/e \
#      co -d libast-20080502 -D 20080502 eterm/libast
# $ tar czvf libast-20080502.tar.gz libast-20080502
Source:        libast-%{cvs}.tar.gz
Source1:       libast-wrapper.h
Patch0:        libast-m4-include.patch
Patch1: libast-configure-c99.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: imlib2-devel
BuildRequires: libXt-devel
BuildRequires: libtool
BuildRequires: make

%description
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

It's not documented yet, mostly because it's not finished.  Hence the
version number that begins with 0.

%package       devel
Summary:       Header files, libraries and development documentation for libast
Requires:      libast = %{version}-%{release}

%description devel
This package contains the header files, static libraries and
development documentation for libast. If you like to develop programs
using libast, you will need to install libast-devel.

%prep
%autosetup -p1 -n libast-%{cvs}

%build
./autogen.sh
autoupdate
%configure --with-regexp=posix
%make_build

%install
%make_install

for header in sysdefs types ; do
    mv %{buildroot}%{_includedir}/libast/$header.h \
       %{buildroot}%{_includedir}/libast/$header-%{_arch}.h
    install -m 0644 -c %{SOURCE1} %{buildroot}%{_includedir}/libast/$header.h
    sed -i -e 's/<HEADER>/'$header'/g' %{buildroot}%{_includedir}/libast/$header.h
    touch -r ChangeLog %{buildroot}%{_includedir}/libast/$header.h
done
sed -i -e '/^LDFLAGS=/d' %{buildroot}%{_bindir}/libast-config
touch -r ChangeLog %{buildroot}%{_bindir}/libast-config

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog DESIGN README
%{_libdir}/libast.so.*

%files devel
%dir %{_includedir}/libast
%{_bindir}/libast-config
%{_libdir}/libast.so
%{_includedir}/libast.h
%{_includedir}/libast/*.h
%{_datadir}/aclocal/libast.m4
%exclude %{_libdir}/*.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.44.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-0.43.20080502cvs
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.42.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.41.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.40.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.39.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 0.7.1-0.38.20080502cvs
- Rebuild fo new imlib2

* Tue Apr 11 2023 Florian Weimer <fweimer@redhat.com> - 0.7.1-0.37.20080502cvs
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.36.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Terje Rosten <terje.rosten@ntnu.no>- 0.7.1-0.35.20080502cvs
- Add armv7 support

* Wed Oct 26 2022 Terje Rosten <terje.rosten@ntnu.no>- 0.7.1-0.34.20080502cvs
- Switch to POSIX regex

* Wed Sep 14 2022 Terje Rosten <terje.rosten@ntnu.no>- 0.7.1-0.33.20080502cvs
- Fix typos

* Tue Sep 13 2022 Terje Rosten <terje.rosten@ntnu.no>- 0.7.1-0.32.20080502cvs
- Fix for rhbz#2113215

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.31.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.30.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.29.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.28.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.27.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.26.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.25.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.24.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.23.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.22.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.21.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.20.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.19.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.18.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.17.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.16.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.15.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.14.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.13.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.12.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.7.1-0.11.20080502cvs
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.10.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.9.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.8.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.7.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May  2 2008 Terje Røsten <terje.rosten@ntnu.no> - 0.7.1-0.6.20080502cvs
- Fix source url

* Sat Feb 11 2008 Terje Røsten <terje.rosten@ntnu.no> - 0.7.1-0.5.20060818cvs
- Fix date

* Sat Feb  9 2008 Terje Røsten <terje.rosten@ntnu.no> - 0.7.1-0.4.20060818cvs
- Rebuild

* Sat Jan 20 2008 Terje Røsten <terje.rosten@ntnu.no> - 0.7.1-0.3.20060818cvs
- Fix multiarch stuff
- Some style cleanup

* Tue Aug 28 2007 Terje Røsten <terje.rosten@ntnu.no> - 0.7.1-0.2.20060818cvs
- Rebuild

* Sat Sep  2 2006 Terje Røsten <terje.rosten@ntnu.no> - 0.7.1-0.1.20060818cvs
- 0.7.1 (from CVS)
- LICENCE now included in upstrean package

* Sun Feb 26 2006 Terje Røsten <terje.rosten@ntnu.no> - 0.7-3
- Add LICENSE

* Tue Feb 21 2006 Terje Røsten <terje.rosten@ntnu.no> - 0.7-2
- Fix buildroot var
- Clean buildroot before install
- Remove static libs
- Add imlib2 to buildrequires

* Sun Feb 19 2006 Terje Røsten <terje.rosten@ntnu.no> - 0.7-1
- Initial packaging based on upstream spec file.

