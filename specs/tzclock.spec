Name:		tzclock
Version:	3.1.7
Release:	16%{?dist}
Summary:	GTK+ graphical Clock displaying the time around the world

# SPDX confirmed
License:	GPL-2.0-only
URL:		https://theknight.co.uk/
Source0:	http://www.tzclock.org/releases/source/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	desktop-file-utils

%description
TzClock is an X Window GTK+ graphical Clock that can display 
the time around the world. It supports multiple faces showing 
different time zones. 
There is a stopwatch function that is accurate to a tenth of a second, 
plus there are many other nice features for you to discover.

%prep
%setup -q

sed -i.suffix \
	-e 's|^Icon=.*|Icon=tzclock|' \
	%{name}.desktop

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=%{buildroot}

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	%{buildroot}%{_datadir}/applications/tzclock.desktop

%files
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING

%{_bindir}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/*/tzclock*
%{_datadir}/applications/*desktop

%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-13
- SPDX migration

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.6-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.6-1
- 3.0.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-2
- F-19: kill vendorization of desktop file (fpc#247)

* Thu Nov 15 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.1-2
- F-17: rebuild against gcc47

* Sun Nov 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.1-1
- 3.0.1

* Wed Nov  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.7.7-3
- Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun  3 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.7-1
- 2.7.7

* Sun Feb 14 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.6-2
- Fix F-13 DSO linkage issue

* Sat Nov 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.6-1
- 2.7.6

* Thu Jul 30 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.5-1
- 2.7.5

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.4-2
- F-12: Mass rebuild

* Tue Mar 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.4-1
- 2.7.4

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.2-2
- F-11: Mass rebuild

* Thu Sep 25 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.2-1
- 2.7.2

* Thu May 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.1-1
- 2.7.1

* Sat Apr 12 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.1-3
- "New" 2.6.1 (modified tarball with the same version)

* Fri Apr 11 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.1-2
- 2.6.1

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43 (F-9)

* Wed Dec  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.5-1
- Initial packaging

