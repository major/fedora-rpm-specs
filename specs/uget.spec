%global	mainver	2.2.3
%global	minorver	1

Name:		uget
Version:	%{mainver}
Release:	14%{?minorver:.respin%minorver}%{?dist}
Summary:	Download manager using GTK+ and libcurl

# Overall		LGPL-2.1-or-later
# uget/pwmd.c	GPL-2.0-or-later (unused)
# SPDX confirmed
License:	LGPL-2.1-or-later
URL:		http://ugetdm.com/
Source0:	http://downloads.sourceforge.net/urlget/%{name}-%{mainver}%{?minorver:-%minorver}.tar.gz
Patch0:		uget-2.2.3-gcc10-fno-common.patch
Patch1:		uget-2.2.3-c23-function-proto.patch

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	intltool
BuildRequires:	libcurl-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(libnotify)

Obsoletes:	urlgfe < 1.0.4
Provides:	urlgfe = %{version}

%description
uGet is a download manager with downloads queue, pause/resume, 
clipboard monitor, batch downloads, browser integration (Firefox & Chrome), 
multiple connections, speed limit controls, powerful category based control
and much more. Each Category has an independent configuration that can
be inherited by each download in that category.

%prep
%setup -q -n %{name}-%{mainver}
%patch -P0 -p1 -b .gcc10
%patch -P1 -p1 -b .c23

%global optflags_orig %optflags
%global optflags %optflags -Werror=implicit-function-declaration

%build
%configure \
	--with-gnutls \
	--without-openssl

%make_build

%install
%make_install
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}-gtk.desktop

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING
%doc	ChangeLog
%doc	README
%{_bindir}/%{name}-gtk
%{_bindir}/%{name}-gtk-1to2

%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/sounds/%{name}/
%dir	%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/logo.png

%changelog
* Fri Jan 17 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-14.respin1
- Support C23 strict prototype

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-13.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 15 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-12.respin1
- SPDX migration

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-11.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-10.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-9.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-8.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3.respin1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-2.respin1
- Fix for gcc10 -fno-common

* Wed Jan  1 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.3-1.respin1
- 2.2.3-1
- A Happy New Year

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.2-1
- 2.2.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.1-1
- 2.2.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Fri Sep  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.6-1
- 2.1.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild


* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.5-1
- 2.1.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.4-1
- 2.1.4

* Wed Apr 27 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.3-2.respin2
- Update to 2.1.3-2

* Tue Apr 12 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.3-1
- 2.1.3

* Thu Apr 07 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.2-1
- 2.1.2

* Wed Mar 23 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-1
- 2.1.1

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-1
- 2.1.0

* Tue Feb  9 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.5-1
- 2.0.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan  2 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.4-1
- 2.0.4

* Fri Nov 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.3-1
- 2.0.3

* Thu Sep 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-1
- 2.0.2

* Mon Aug 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-1
- 2.0.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May  2 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-1
- 2.0

* Fri Mar 27 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.6-1
- 1.99.6

* Tue Jan 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.5-1
- 1.99.5

* Mon Nov 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.4-1
- 1.99.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.4-1
- 1.10.4 (bug 1055090)
- Update URL and summary (bug 1055092)
- Not activate gnutls support for now

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.10.3-1
- 1.10.3

* Fri Oct  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.10.2-1
- 1.10.2

* Fri Sep 21 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.10.1-1
- 1.10.1

* Thu Sep  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.10-1.respin2
- Update to 1.10-2

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 31 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.2-1
- 1.8.2

* Thu Apr 19 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.1-1
- 1.8.1

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.0-4
- F-17: rebuild against gcc47

* Wed Nov  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.0-3
- F-17: Use deprecated declaration in GTK 3 for now

* Wed Nov  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.0-2
- Rebuild

* Wed Jun  8 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.0-1
- 1.8.0

* Thu May 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.6-1
- 1.7.6

* Fri Apr 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.5-1
- 1.7.5

* Tue Apr 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.4-1
- 1.7.4

* Thu Mar 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.3-1
- 1.7.3

* Thu Mar  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7.2a-1
- 1.7.2a
- Use GTK 3 on F-15+

* Wed Feb  9 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.7.1-1
- 1.7.1
- Try adding aria2 plugin support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.7.0-1
- 1.7.0

* Thu Dec 16 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.2a-1
- 1.6.2a

* Fri Nov 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.1-3
- Patch for libnotify 0.7.0 API

* Sat Nov  6 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.1-2
- F-15: kill libnotify suuport for now

* Fri Oct 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.1-1
- 1.6.1

* Sun Sep  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.0-2
- Apply upstream patch for build issue with recent libnotify

* Wed Aug 18 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.0-1
- 1.6.0

* Fri Jul 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.9.3-1
- 1.5.9.3

* Fri Jun  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.9.2-1
- 1.5.9.2

* Thu Apr 22 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.9.1-1
- 1.5.9.1

* Sun Mar 21 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0.3-1
- 1.5.0.3

* Thu Mar  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0.2-1
- 1.5.0.2

* Fri Jan 22 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0.1-2
- Fix segv when invalid uri is passed to the argument (bug 556907)

* Wed Dec 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0.1-1
- 1.5.0.1 (which should fix bug 546289)

* Fri Oct  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.0-1
- 1.5.0

* Thu Sep  3 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9.3-1
- 1.4.9.3

* Wed Aug  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9.2-1
- 1.4.9.2

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9.1-2
- F-12: Mass rebuild

* Wed Jul 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9.1-1
- 1.4.9.1

* Wed Jul  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.9-1
- 1.4.9

* Wed Jun 17 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.8.5-2
- F-12: Rebuild to create valid debuginfo rpm again (ref: 505774)

* Mon Jun 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.8.5-1
- 1.4.8.5

* Wed Jun 10 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.8.4-1
- 1.4.8.4

* Mon May 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.8.3-1
- 1.4.8.3

* Sun May 17 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.8.2-1
- 1.4.8.2

* Thu May 14 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.8.1-1
- 1.4.8.1

* Mon May  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.7-2
- More detailed summary/description suggested by Christoph Wickert
  <fedora@christoph-wickert.de>

* Sat May  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.7-1
- Initial packaging
