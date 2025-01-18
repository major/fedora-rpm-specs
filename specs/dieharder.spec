Summary:        Random number generator tester and timer
Name:           dieharder
Version:        3.31.1
Release:        41%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        http://www.phy.duke.edu/~rgb/General/%{name}/%{name}-%{version}.tgz
URL:            http://www.phy.duke.edu/~rgb/General/dieharder.php
Patch0:         dieharder-3.31.1_urandom_64bit.patch 
Patch1:         dieharder-3.31.1_aarch64.patch
Patch2:         dieharder-3.31.1_BZ1100855.patch
Patch3:         dieharder-3.31.1_autoconf_c99.patch

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
# Needed for building manual
BuildRequires:  texlive-latex
BuildRequires:  latex2html

BuildRequires:  gsl-devel
BuildRequires: make automake autoconf libtool

%define _legacy_common_support 1

%description 
dieharder is a fairly involved random number/uniform deviate generator
tester.  It can either test any of its many pre-built and linked
generators (basically all of those in the Gnu Scientific Library plus
some others) or a potentially random data-set in a file.  With file
input, it can manage either a variety of ASCII-formatted input or a raw
binary bit string.  It is thus suitable for use in testing both software
RNG's and hardware RNG's.

dieharder does all of its work with a standalone, extensible library,
libdieharder. Therefore its tests can be integrated into other programs.

dieharder encapsulates following random number tests: George Marsaglia's
"Diehard" battery of tests, STS (v1.6) from NIST FIPS, Knuth's tests,
and more.  Check the documentation for complete list of the tests and
references where possible. It is intended to be the "Swiss army knife of
random number testers", or "the last suite of random number testers
you'll ever wear".

########################################################################
# LIBRARY: This is the basic dieharder library
########################################################################

%package libs
Summary:        A library of random number generator tests and timing routines

%description libs

libdieharder is the core library of dieharder designed to be "the last
suite of random number testers you'll ever wear".  It can test any of
its many pre-built and library linked generators (basically all of those
in the Gnu Scientific Library plus a number of others from various
sources) or a potentially random data-set in either an ASCII-formatted
or raw (presumed 32 bit unsigned int) binary file.  It is fairly
straightforward to wrap new software generators for testing, or to add
hardware generators that have a software interface for testing, and the
file input method permits pretty much any software or hardware RNG to be
tested using libdieharder calls.

libdieharder has as a design goal the full encapsulation in an
extensible shell of basically all the random number tests: George
Marsaglia's "Diehard" battery of tests, STS (v1.6) from NIST FIPS,
Knuth's tests, and more.  Check the documentation for complete list.  


%package devel
Summary: A library of random number generator tests and timing routines
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}


########################################################################
# The main section common to all builds.
########################################################################
%prep
%autosetup -p1

%build
autoreconf -vi
%configure
###SMP build is not working
###make %{?_smp_mflags} V=1
make V=1

# Build pdf manual
pushd manual
make


%check
make check


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
rm -rf %{buildroot}%{_libdir}/libdieharder.la
rm -rf %{buildroot}%{_libdir}/libdieharder.a

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -p ChangeLog Copyright README COPYING NOTES %{name}.html manual/%{name}.pdf %{buildroot}%{_defaultdocdir}/%{name}


########################################################################
# Command to execute post install or uninstall of libdieharder
########################################################################
%ldconfig_scriptlets libs

########################################################################
# Files installed with the dieharder tty UI
########################################################################
%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_defaultdocdir}/*

%files libs
%{_libdir}/*.so.*
%{_mandir}/man3/lib%{name}.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.31.1-40
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Peter Fordham <peter.fordham@gmail.com> - 3.31.1-34
- Port autoconf check to C99 and add autoreconf to build.

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.31.1-33
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr  6 2020 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-27
- Fixed compilation issue on F32 - see BZ1799280. Use -fcommon GCC flag to compile it

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.31.1-25
- Rebuilt for GSL 2.6.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.31.1-17
- Drop unneeded explicit requires on gsl

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.31.1-16
- Rebuild for gsl 2.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-12
- Fixed compilation issue on F21 - see BZ1106140

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 05 2014 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-10
- Unversioned docdir change, more info on 
  https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sat Jan 04 2014 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-9
- Fixed issue when testing /dev/random and /dev/urandom 9generators 500 and 501)
  on 64-bit architecture. Refer to 
  https://bugzilla.redhat.com/show_bug.cgi?id=803292
- Added support for the ARM 64 bit CPU architecture (aarch64)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-4
  - Fix building for EPEL5
* Wed Nov 16 2011 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-3
  - Updates according to https://bugzilla.redhat.com/show_bug.cgi?id=744339#c14
* Tue Nov 15 2011 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-2
  - Updates according to https://bugzilla.redhat.com/show_bug.cgi?id=744339#c11
* Mon Nov 14 2011 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-1
  - Updates according to https://bugzilla.redhat.com/show_bug.cgi?id=744339#c9
* Sat Oct 15 2011 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.1-0
  - Update to 3.31.1
  - It fixes build warnings
* Fri Oct 07 2011 Jirka Hladky <hladky.jiri@gmail.com> - 3.31.0-0
 - Initial package

