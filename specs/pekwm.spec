Name:           pekwm
Version:        0.1.17
Release:        30%{?dist}
Summary:        A small and flexible window manager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.pekwm.org/
Source0:        http://www.pekwm.org/projects/pekwm/files/%{name}-%{version}.tar.bz2

Patch0:         %{name}-0.1.15-menu.patch
Patch1:		%{name}-0.1.15-gcc10.patch

BuildRequires: make
BuildRequires:  libX11-devel libpng-devel libXrandr-devel
BuildRequires:  libXft-devel libXext-devel libXinerama-devel
BuildRequires:  libXpm-devel libjpeg-devel libICE-devel libSM-devel
BuildRequires: 	gcc-c++

%description
Pekwm is a window manager that once up on a time was based on the aewm++ window
manager, but it has evolved enough that it no longer resembles aewm++ at all.
It has a much expanded feature-set, including window grouping (similar to ion,
pwm, or fluxbox), autoproperties, xinerama, keygrabber that supports keychains,
and much more.

* Lightweight and Unobtrusive, a window manager shouldn't be noticed.
* Very configurable, we all work and think in different ways.
* Automatic properties, for all the lazy people, make things appear as they
should when starting applications.
* Chainable Keygrabber, usability for everyone. 

%prep
%setup -q

# Exclude/replace menu apps that are not in Fedora or are not free software
%patch -P0 -p0 -b .orig
%patch -P1 -p1 -b .gcc10

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

# Create desktop file
mkdir -p %{buildroot}%{_datadir}/xsessions/
cat << EOF > %{buildroot}%{_datadir}/xsessions/%{name}.desktop
[Desktop Entry]
Name=PekWM
Comment=Very small and fast window manger
Exec=pekwm
TryExec=pekwm
Type=XSession
EOF

# Delete makefiles from contrib folder
find contrib/Makefile* -type f | xargs rm -rf || true
find contrib/lobo/Makefile* -type f | xargs rm -rf || true

# Rearrange the contents of contrib folder
mv contrib/lobo/* contrib/
rm -rf contrib/lobo

# Fix permissions to include scripts in %%doc
find contrib/pekwm_autoprop.pl -type f | xargs chmod 0644 || true
find contrib/pekwm_menu_config.pl -type f | xargs chmod 0644 || true

%files
%doc AUTHORS ChangeLog ChangeLog.aewm++ ChangeLog.until-0.1.6 LICENSE NEWS README contrib/
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/autoproperties
%config(noreplace) %{_sysconfdir}/%{name}/autoproperties_typerules
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/config_system
%config(noreplace) %{_sysconfdir}/%{name}/keys
%config(noreplace) %{_sysconfdir}/%{name}/menu
%config(noreplace) %{_sysconfdir}/%{name}/mouse
%config(noreplace) %{_sysconfdir}/%{name}/mouse_click
%config(noreplace) %{_sysconfdir}/%{name}/mouse_sloppy
%config(noreplace) %{_sysconfdir}/%{name}/mouse_system
%config(noreplace) %{_sysconfdir}/%{name}/vars
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/%{name}/start
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.*
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.17-29
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-19
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.1.17-16
- Fix narrowing conversion problem found by gcc-10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.1.17-13
- Fix BZ #1605397

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.1.17.11
- Fix version
- Fix source
- Fix Upstream

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Luis Bazan <lbazan@fedoraproject.org> - 0.1.18rc1-1
- New upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.17-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Germán A. Racca <skytux@fedoraproject.org> - 0.1.17-1
- Updated to new version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.1.16-2
- rebuild due to "jpeg8-ABI" feature drop

* Tue Nov 20 2012 Germán A. Racca <skytux@fedoraproject.org> - 0.1.16-1
- Updated to new version

* Mon Sep 24 2012 Germán A. Racca <skytux@fedoraproject.org> - 0.1.15-1
- Updated to new version
- Updated the menu patch

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-2
- Rebuilt for c++ ABI breakage

* Fri Jan 20 2012 Germán A. Racca <skytux@fedoraproject.org> 0.1.14-1
- Updated to new version

* Sun Aug 10 2011 Germán A. Racca <skytux@fedoraproject.org> 0.1.13-1
- Updated to new version
- Removed the old patch and applied a new one to fix a similar issue
- Removed indentation of list items in %%{description}

* Tue May 11 2010 German A. Racca <gracca@gmail.com> 0.1.12-4
- Fixed BuildRequires to compile from scratch

* Sun May 09 2010 German A. Racca <gracca@gmail.com> 0.1.12-3
- Deleted makefiles form contrib folder
- Rearranged contents in contrib folder

* Mon Apr 26 2010 German A. Racca <gracca@gmail.com> 0.1.12-2
- Added %%{dist} tag
- Fixed patch
- Added contrib stuff to docs

* Tue Apr 20 2010 German A. Racca <gracca@gmail.com> 0.1.12-1
- New version 0.1.12
- Fixed timestamp for tarball source
- Added BuildRoot tag
- Fixed BuildRequires
- Added menu patch
- Added INSTALL="install -p" to preserve timestamps
- Corrected type in xsession file
- Added ChangeLog.aewm++ and ChangeLog.until-0.1.6 to doc files
- Own directory %%{_datadir}/%%{name}
- Marqued 'start' as config file

* Sat Feb 20 2010 German A. Racca <gracca@gmail.com> 0.1.11-3
- Changed Summary
- Changed BuildRequires
- Modified desktop file
- Added exec attr to 'start' file

* Fri Jan 15 2010 German A. Racca <gracca@gmail.com> 0.1.11-2
- Added Source0 to spec file

* Thu Dec 17 2009 German A. Racca <gracca@gmail.com> 0.1.11-1
- Initial release of RPM package
