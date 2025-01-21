%define		pkgtimestamp	20081027

Name:           tempest
# There is no version, so we use pre-release style versioning with a date
Version:        0
Release:        0.40.%{pkgtimestamp}%{?dist}
Summary:        Tempest OpenGL screensaver

# tempest.c	GPL-2.0-or-later
# vroot.h		HPND
# SPDX confimed
License:        GPL-2.0-or-later AND HPND
URL:            http://www.personal.utulsa.edu/~dan-guernsey
Source0:        http://www.personal.utulsa.edu/~dan-guernsey/dist/%{name}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.xml
Source3:        %{name}-gss.desktop
Patch0:         %{name}-20070929-desktop.patch
BuildRequires:  gcc
BuildRequires:  libGL-devel

%description
Tempest is a screensaver based on a physical model whereby particles are
attracted to their neighbors.


%package            xscreensaver
Summary:            XScreenSaver support for %{name}
Requires:           %{name} = %{version}-%{release}
Requires(post):     xscreensaver-base
Requires(postun):   xscreensaver-base
Requires:           xscreensaver-gl-base

%description        xscreensaver
Tempest is a screensaver based on a physical model whereby particles are
attracted to their neighbors. This package contains the files needed to use the
hack with xscreensaver.

%prep
%setup -q -n %{name}
%patch -P0 -p0 -b .orig

#Cleanups for the debuginfo package
chmod -x %{name}.c
sed -i 's/\r//' %{name}.c


%build
gcc %{optflags} -o tempest tempest.c -lGL -lm -lX11


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}

# For xscreensaver
mkdir -p %{buildroot}%{_datadir}/xscreensaver/{config,hacks.conf.d}
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/xscreensaver/hacks.conf.d/
install -p -m0644 %{SOURCE2} %{buildroot}%{_datadir}/xscreensaver/config/


%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi


%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi


%files
%{_bindir}/%{name}

%files xscreensaver
%{_datadir}/xscreensaver/config/%{name}.xml
%{_datadir}/xscreensaver/hacks.conf.d/%{name}.conf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.40.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.39.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.38.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.37.20081027
- SPDX migration

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.35.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.34.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.33.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 josef radinger <cheese@nosuchhost.net> - 0-0.29.20081027
- obsolete tempest-gnome-screensaver for fc33 onwards
- fix bug #1841250

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.19.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0-0.18.20081027
- Obsoletes -kde subpackage on F-22+

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.17.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.16.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0-0.12.20081027
- F-17: rebuild against gcc47

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20081027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0-0.10.20081027
- Fix F-13 DSO linkage issue

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0-0.9.20081027
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0-0.8.20081027
- F-11: Mass rebuild

* Fri Nov 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0-0.7.20081027
- Upstream tarball slightly changed

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 0-0.6.20070929 
- -kde: drop Requires: kdebase (kdeartwork dep is enough)
- fix %%kdessconfigdir for kde4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0-0.5.20070929
- Autorebuild for GCC 4.3

* Fri Oct 19 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0-0.4.20070929
- Fix xscreensaver xml file
- Make xscreensaver subpackage xscreensaver-gl-base (bug 336331)

* Mon Oct  1 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0-0.3.20070929
- Minor SPEC changes
- Fixed gnome support. Missing symlink

* Mon Oct  1 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>  0-0.2.20070929
- Support xscreensaver, gnome-screensaver as well as kscreensaver

* Sat Sep 29 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0-0.1.20070929
- Initial release
