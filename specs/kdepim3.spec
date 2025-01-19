
Name:    kdepim3
Summary: Compatibility support for kdepim3 
Version: 3.5.10
Release: 45%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdepim-%{version}.tar.bz2
Patch0: kdepim-3.5.10-gcc.patch
# FTBFS with perl-5.22+, see https://bugzilla.redhat.com/show_bug.cgi?id=1239630
Patch1: kdepim-3.5.10-perl5_22.patch
# FTBFS with gcc7
Patch2: kdepim3-gcc7.patch
# FTBFS on aarch64
Patch3: kdepim-3.5.10-aarch64.patch
# FTBFS with perl
Patch4: kdepim3-perl.patch
Patch5: kdepim3-configure-c99.patch

BuildRequires: gcc-c++
BuildRequires: bison flex flex-static
BuildRequires: desktop-file-utils
BuildRequires: kdelibs3-devel >= %{version}
BuildRequires: zlib-devel
BuildRequires: libart_lgpl-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: lockdev-devel
BuildRequires: python-devel
## Crypto Stuff from http://kmail.kde.org/kmail-pgpmime-howto.html
BuildRequires: gpgme-devel
BuildRequires: libXpm-devel libXScrnSaver-devel
BuildRequires: perl(Data::Dumper)
BuildRequires: make

Provides: bundled(libical) = 0.24

%description
%{summary}, including libkcal.

%package libs
Summary: Runtime files for %{name}
%description libs
%{summary}, including libkcal.

%package devel
Summary: Development files for %{name} 
Requires: %{name}-libs = %{version}-%{release}
Requires: kdelibs3-devel
# kdepimlibs-devel-4.2.1-2 fixed to avoid conflicts -- Rex
Conflicts: kdepimlibs-devel < 4.2.1-2
%description devel
%{summary}.


%prep
%setup -q -n kdepim-%{version}

%patch -P0 -p1 -b .gcc47
%patch -P1 -p1 -b .perl5_22
%patch -P2 -p1 -b .gcc7
%ifarch aarch64
%patch -P3 -p1 -b .linker
%endif
%patch -P4 -p1

%patch -P5 -p1 -b .c99
# Restore the timestamps to prevent autotools rebuilds.
for p in *.c99; do
    touch -r "$p" "`basename "$p" .c99`"
done

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%configure \
   --disable-dependency-tracking \
   --disable-rpath \
   --disable-debug --disable-warnings \
   --includedir=%{_includedir}/kde \
   --with-gpg=%{_bindir}/gpg \
   --with-gpgsm=%{_bindir}/gpgsm \
   --with-sasl \
  %{?_with_gnokii} %{!?_with_gnokii:--without-gnokii} \
  %{?_with_mal} %{!?_with_mal:--without-mal} \
  %{?_with_pilot_link} %{!?_with_pilot_link:--without-pilot-link}

for lib in ktnef libkmime libemailfunctions libkcal libkdepim; do
make %{?_smp_mflags} -C ${lib}
done


%install
rm -rf %{buildroot} 

for lib in ktnef libkmime libemailfunctions libkcal libkdepim; do
make install DESTDIR=%{buildroot} -C $lib
done

#unpackaged files
rm -f  %{buildroot}%{_libdir}/lib*.la
rm -f  %{buildroot}%{_libdir}/libkdepim*
rm -rf %{buildroot}%{_datadir}/apps/libkdepim/
rm -rf %{buildroot}%{_datadir}/apps/kdepimwidgets/
rm -f  %{buildroot}%{_libdir}/kde3/plugins/designer/*
rm -f  %{buildroot}%{_libdir}/lib{kmime,ktnef}.so
rm -rf %{buildroot}%{_includedir}/kde/ktnef/
rm -rf %{buildroot}%{_datadir}/applications
rm -rf %{buildroot}%{_datadir}/icons
rm -rf %{buildroot}%{_datadir}/mimelnk
rm -rf %{buildroot}%{_datadir}/apps/ktnef
rm -f  %{buildroot}%{_bindir}/ktnef

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001


%ldconfig_scriptlets libs



%files libs
%doc README korganizer/COPYING
%{_datadir}/config.kcfg/pimemoticons.kcfg
%{_datadir}/apps/libical/
%{_datadir}/services/kresources/kcal*
%{_libdir}/libkcal.so.2*
%{_libdir}/kde3/kcal*
%{_libdir}/libkmime.so.2*
%{_libdir}/libktnef.so.1*

%files devel
%{_includedir}/kde/kdepimmacros.h
%{_includedir}/kde/libemailfunctions/
%{_includedir}/kde/libkcal/
%{_libdir}/libkcal.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.5.10-44
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Florian Weimer <fweimer@redhat.com> - 3.5.10-38
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Than Ngo <than@redhat.com> - 3.5.10-35
- Fixed FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Than Ngo <than@redhat.com> - 3.5.10-32
- Fixed build failure

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Than Ngo <than@redhat.com> - 3.5.10-27
- fixed FTBFS on aarch64

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-25
- BR: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 26 2017 Than Ngo <than@redhat.com> - 3.5.10-22
- fixed FTBFS with gcc7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-18
- Provides: bundled(libical) = 0.24 (#1079727)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-16
- kdepim3 FTBFS (#1239630)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.5.10-14
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-9
- BR: perl(Data::Dumper)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 Than Ngo <than@redhat.com> - 3.5.10-7
- fix build failure with gcc-4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Ondrej Vasik <ovasik@redhat.com> - 3.5.10-4
- BuildRequire flex-static (-lfl) (#660785)

* Tue Jan 12 2010 Radek Novacek <rnovacek@redhat.com> - 3.5.10-3
- Fixed "macro in summary" error

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-1
- first try at kdepim3 compat pkg, including libkcal

