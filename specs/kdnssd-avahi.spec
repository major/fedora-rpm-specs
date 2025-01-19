
%define beta 20080116svn

Summary: KDE zeroconf implementation based on avahi
Name:	 kdnssd-avahi
Version: 0.1.3
Release: 0.47.%{beta}%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:	 http://helios.et.put.poznan.pl/~jstachow/pub/
Source0: kdnssd-avahi-%{beta}.tar.bz2
Source1: kdnssd-avahi-svn_checkout.sh

# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
Patch303: kde3-autoconf-version.patch

Patch399: kdnssd-avahi-fedora-c99.patch

BuildRequires: avahi-qt3-devel
BuildRequires: automake libtool
BuildRequires: kdelibs3-devel
BuildRequires: make

## A hint so other pkgs (like kdelibs3) can Requires: libkdnssd
Provides: libkdnssd

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: kdelibs3-devel
Requires: avahi-devel
## .la file dep
#Requires: avahi-qt3-devel
## A hint so other pkgs (like kdelibs3-devel) can Requires: libkdnssd-devel
Provides: libkdnssd-devel
%description devel
%{summary}


%prep
%setup -q -n %{name}

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .autoconf2.7x
%patch -P399 -p1 -b .c99

make -f admin/Makefile.common cvs

# hack/fix for self-dependency on having it's headers already in /usr/include/...
ln -s . kdnssd-avahi/dnssd


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

export CXXFLAGS="%{optflags} -std=gnu++98"

%configure \
  --includedir=%{_includedir}/kde \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final

%make_build


%install
%make_install

# Unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/libkdnssd.la

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001

%ldconfig_scriptlets

%files
%doc kdnssd-avahi/README
%{_libdir}/libkdnssd.so.*

%files devel
%{_includedir}/kde/dnssd/
%{_libdir}/libkdnssd.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.47.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.3-0.46.20080116svn
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.45.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.44.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.43.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.42.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 DJ Delorie <dj@redhat.com> - 0.1.3-0.41.20080116svn
- Fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.40.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.39.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.38.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 16 2021 Than Ngo <than@redhat.com> - 0.1.3-0.37.20080116svn
- Fixed FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.36.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.35.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.34.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.33.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.32.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.31.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.30.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.1.3-0.29.20080116svn
- .spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.28.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.27.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.26.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.25.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Rex Dieter <rdieter@fedoraproject.org> 0.1.3-0.24.20080116svn
- FTBFS in rawhide (#1307688)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-0.23.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.22.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.3-0.21.20080116svn
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.20.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.19.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.18.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.3-0.17.20080116svn
- use automake --force-missing to get aarch64 support (#925029/#925627)
- also use automake --copy (the default is symlinking)

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.3-0.16.20080116svn
- unify KDE 3 autotools fixes between packages

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.15.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.14.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.13.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 05 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.3-0.12.20080116svn
- kdnssd-avahi uses include headers from earlier version of itself during build (#743524)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.11.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.1.3-0.10.20080116svn
- fix typo in --disable-dependency-tracking configure switch
- work around various libtool problems (use system libtool, edit some options)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.9.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.3-0.8.20080116svn
- FTBFS kdnssd-avahi-0.1.3-0.7.20080116svn.fc11 (#511519)
- -devel: Requires: %%name%%?_isa ...

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-0.7.20080116svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.3-0.6.20080116svn
- Autorebuild for GCC 4.3

* Wed Jan 16 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 0.1.3-0.5.20080116svn
- 20080116svn
- -devel: Requires: kdelibs3-devel

* Sun Dec 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.1.3-0.4.20060713svn
- drop Req: kdelibs3 (no longer worries about conflicts) 

* Sat Dec 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.1.3-0.3.20060713svn
- BR: kdelibs3-devel
- License: LGPLv2+

* Wed Aug 29 2007 Martin Bacovsky <mbacovsk@redhat.com> - 0.1.3-0.2.20060713svn
- Resolves: #246628: build with automake 1.10

* Tue Jul 18 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.1.3-0.1.20060713svn
- since using snapshot, consider it a pre-release of next version

* Thu Jul 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.1.2-6.20060713svn
- update to 20060713svn

* Tue May 30 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.1.2-5
- Requires: kdelibs >= 3.5.2

* Sat May 27 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.1.2-4
- -devel: Requires: avahi-devel

* Thu May 18 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.1.2-3
- omit .la file
- use --no-undefined

* Thu May 18 2006 Rex Dieter 0.1.2-2
- devel: Requires: avahi-qt3-devel

* Wed May 17 2006 Rex Dieter 0.1.2-1
- first try

