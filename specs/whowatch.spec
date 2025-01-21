Summary: Display information about users currently logged on 
Name: whowatch
Version: 1.8.6
Release: 19%{?dist}
License: GPL-2.0-only
URL: http://wizard.ae.krakow.pl/~mike/

Source0: https://github.com/mtsuszycki/whowatch/archive/whowatch-%{version}.tar.gz
Patch0: whowatch-configure-c99.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel

%description
Whowatch is an interactive who-like program that displays information about the
users currently logged on to the machine, in real time. Besides standard
information (login name, tty, host, user's process), the type of the connection
(ie. telnet or ssh) is shown. You can toggle display between users' command or
idle time. You can watch processes tree, navigate in it and send INT and KILL
signals.

%prep
%autosetup -p1

%build
# Avoid regenerating configure script because whowatch-configure-c99.patch
# updates it directly.
touch aclocal.m4 Makefile.in src/config.h.in
%configure
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_bindir}
%makeinstall

%files
%doc AUTHORS ChangeLog PLUGINS.readme README TODO
%doc %{_mandir}/man1/whowatch.1*
%license COPYING
%{_bindir}/whowatch

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 1.8.6-14
- Use SPDX license identifier

* Sat Nov 26 2022 Florian Weimer <fweimer@redhat.com> - 1.8.6-13
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> - 1.8.6-7
- Use %%license

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> - 1.8.6-3
- Don't remove buildroot in %%install section

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Richard Fearn <richardfearn@gmail.com> - 1.8.6-1
- Update to 1.8.6 (bug #1567514)

* Sat Feb 24 2018 Richard Fearn <richardfearn@gmail.com> - 1.8.5-13
- Add BuildRequires: gcc
  (see https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> 1.8.5-11
- Remove unnecessary Group: tag, BuildRoot: tag, and %%clean section

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 03 2016 Richard Fearn <richardfearn@gmail.com> 1.8.5-7
- Fix incorrect FSF address in COPYING

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Richard Fearn <richardfearn@gmail.com> - 1.8.5-5
- Remove unnecessary %%defattr

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Richard Fearn <richardfearn@gmail.com> - 1.8.5-1
- Update to 1.8.5 (rhbz#1068965)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Mar 05 2011 Adrian Reber <adrian@lisas.de> - 1.4-9
- fix error in patch:
  "/usr/bin/patch: **** rejecting target file name with ".." component: ../process.c"

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-5
- Autorebuild for GCC 4.3

* Mon Sep 24 2007 Subhodip Biswas <440volt.tux@gmail.com> - 1.4-4
- fixed broken patch
* Mon Sep 24 2007 Subhodip Biswas <440volt.tux@gmail.com> - 1.4-3
- fixed issues regarding patch
* Mon Sep 24 2007 Subhodip Biswas <440volt.tux@gmail.com> - 1.4-2
- fixed few issues  
* Sat Sep 22 2007 Subhodip Biswas <440volt.tux@gmail.com> - 1.4-1
-Initial packaging. 

