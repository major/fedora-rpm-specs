Name:           wmctrl
Version:        1.07
Release:        39%{?dist}
Summary:        Command line tool to interact with an X Window Manager

License:        GPL-2.0-or-later
# URL and Source URL is dead now.
# New hosting can be used as https://github.com/Conservatory/wmctrl
URL:            http://sweb.cz/tripie/utils/wmctrl
Source0:        http://sweb.cz/tripie/utils/wmctrl/dist/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libXmu-devel
BuildRequires:  xorg-x11-proto-devel
Patch0:         http://ftp.de.debian.org/debian/pool/main/w/wmctrl/wmctrl_1.07-6.diff.gz
Patch1:         wmctrl-sticky-workspace.patch

%description
The wmctrl program is a UNIX/Linux command line tool to interact with an
EWMH/NetWM compatible X Window Manager. The tool provides command line access
to almost all the features defined in the EWMH specification. It can be used,
for example, to obtain information about the window manager, to get a detailed
list of desktops and managed windows, to switch and resize desktops, to make
windows full-screen, always-above or sticky, and to activate, close, move,
resize, maximize and minimize them. The command line access to these window
management functions makes it easy to automate and execute them from any
application that is able to run a command in response to an event.


%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 28 2024 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.07-37
- Migrate to SPDX license expression

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jens Petersen <petersen@redhat.com> - 1.07-24
- BR gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 24 2012 Jens Petersen <petersen@redhat.com> - 1.07-12
- add patch to allow stick to all workspaces from Jeff Bastien (#524023)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  1 2011 Jens Petersen <petersen@redhat.com> - 1.07-10
- drop INSTALL and ChangeLog from doc files

* Thu Sep 29 2011 Jens Petersen <petersen@redhat.com> - 1.07-9
- revive orphaned package (#742166)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 28 2008 Patrice Dumas <pertusus@free.fr> - 1.07-5
- apply debian patcheset, to fix #426383

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.07-4
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.07-3
- Autorebuild for GCC 4.3

* Wed Oct 04 2006 Michael Rice <errr[AT]errr-online.com> - 1.07-2
- Fix Summary per rpmlint warning
- Fix description per rpmlint warning
- Remove unneeded line from setup
- Remove NEWS from docs since it was empty
- Reformat Changlelog entrys in spec file due to bad formatting
- Changed Group to User Interface/X

* Wed Sep 27 2006 Michael Rice <errr[AT]errr-online.com> - 1.07-1
- Initial RPM release
