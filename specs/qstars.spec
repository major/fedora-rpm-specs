
%if 0%{?fedora} > 8
# KDE4
%define kdessconfigdir %{_datadir}/kde4/services/ScreenSavers
%else
# KDE3
%define kdessconfigdir %{_datadir}/applnk/System/ScreenSavers
%endif

Name:           qstars
Version:        0.4
Release:        38%{?dist}
Summary:        A screensaver simulating planets and asteroids in space

# COPYING	GPL-2.0-or-later
# vroot.h	HPND
# SPDX confirmed
License:        GPL-2.0-or-later AND HPND
URL:            http://qt.osdn.org.ua/qstars.html
Source0:        http://qt.osdn.org.ua/%{name}-%{version}.tar.gz
Source1:        %{name}.setup
Source2:        %{name}.conf
Patch0:         %{name}-0.4-desktop.patch
# Patch to build with -Werror=format-security
Patch1:         qstars-0.4-format-security.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  qt3-devel >= 3.3

%description
A screensaver which simulates planets, asteroids and ships in a moving
starfield.


%package            xscreensaver
Summary:            XScreenSaver support for %{name}
Requires:           %{name} = %{version}-%{release}
Requires(post):     xscreensaver-base
Requires(postun):   xscreensaver-base

%description        xscreensaver
A screensaver which simulates planets, asteroids and ships in a moving
starfield. This package contains the files needed to use the hack with
xscreensaver.

%prep
%setup -q
%patch -P0 -p0 -b .orig
%patch -P1 -p1 -b .format

# Set installation in project file
sed -i 's|/local/|/|' %{name}.pro

%build
qmake
make clean
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

# For xscreensaver
mkdir -p %{buildroot}%{_datadir}/xscreensaver/hacks.conf.d
install -p -m0644 %{SOURCE2} %{buildroot}%{_datadir}/xscreensaver/hacks.conf.d/


# For KDE
install -p -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -m0755 %{SOURCE1} %{buildroot}%{_bindir}/
cp -a ships galaxies planets asteroids %{buildroot}%{_datadir}/%{name}/



%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi


%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi


%files
%license COPYING
%doc ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}.setup
%{_datadir}/%{name}


%files xscreensaver
%{_datadir}/xscreensaver/hacks.conf.d/%{name}.conf


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4-36
- SPDX migration

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4-29
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4-16
- Obsoletes -kde subpackage on F-22+

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4-14
- Patch to compile with -Werror=format-security

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4-10
- F-17: rebuild against gcc47

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4-8
- F-12: Mass rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> 0.4-6
- -kde: drop Requires: kdebase (kdeartwork-kxs dep is good enough) 
- set/use correct dir for kde4 screensavers (f9+)

* Fri Mar 21 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-5
- qt -> qt3 BR change

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4-4
- Autorebuild for GCC 4.3

* Tue Oct  2 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-3
- Minor SPEC changes
- Removed gnome support, appears to be incompatible.

* Tue Oct  2 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>  0.4-2
- Support xscreensaver, gnome-screensaver as wall as kxscreensaver

* Sat Sep 29 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.4-1
- Initial release
