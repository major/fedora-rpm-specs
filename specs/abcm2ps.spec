Name:           abcm2ps
Version:        8.14.15
Release:        4%{?dist}
Summary:        A program to typeset ABC tunes into Postscript

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://moinejf.free.fr
Source0:        https://github.com/leesavide/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        http://abcplus.sourceforge.net/abcplus_en-2012-03-30.zip
Source2:        http://abcplus.sourceforge.net/abcplus_en-DRAFT3.pdf

BuildRequires:  gcc make
%description
Abcm2ps is a package which converts music tunes from ABC format to
Postscript. Based on abc2ps version 1.2.5, it was developed mainly to
print Baroque organ scores which have independent voices played on one
or many keyboards and a pedal-board. Abcm2ps introduces many
extensions to the ABC language that make it suitable for classical
music.

%package doc
Summary: Example ABC files with output
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Some sample ABC files with output as mp3, mid, and pdf.

%prep
%setup -q
%setup -q -a 1
cp -p %{SOURCE2} .

%build
%configure --enable-a4
%make_build CFLAGS="%{optflags}"


%install
make install \
     prefix=%{buildroot}%{_prefix} \
     bindir=%{buildroot}%{_bindir} \
     libdir=%{buildroot}%{_libdir} \
     datadir=%{buildroot}%{_datadir} \
     mandir=%{buildroot}%{_mandir} \
     docdir=$PWD/_docs_staging


%files 
%doc INSTALL README.md abcplus_en-DRAFT3.pdf _docs_staging/abcm2ps/*
%license COPYING
%{_bindir}/abcm2ps
%{_datadir}/abcm2ps
%{_mandir}/man1/*

%files doc
%doc abcplus_en*/* 

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.14.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 8.14.15-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.14.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Stuart Gathman <stuart@gathman.org> - 8.14.15-1
- New upstream release

* Sat Mar 12 2022 Stuart Gathman <stuart@gathman.org> - 8.14.13-1
- New upstream release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.14.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.14.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.14.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Stuart Gathman <stuart@gathman.org> - 8.14.11-1
- New upstream release

* Fri Nov 20 2020 Stuart Gathman <stuart@gathman.org> - 8.14.10-1
- New upstream release

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.14.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.14.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Stuart Gathman <stuart@gathman.org> - 8.14.7-2
- Move sample ABC output to subpackage

* Tue May 12 2020 Stuart Gathman <stuart@gathman.org> - 8.14.7-1
- New upstream release

* Wed Apr 29 2020 Filipe Rosset <rosset.filipe@gmail.com> - 7.8.14-11
- Fix FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul  9 2015 Gérard Milmeister <gemi@bluewin.ch> - 7.8.14-1
- New release 7.8.14
- Added draft manual

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 5.9.21-7
- Don't ship two copies of most docs, use special %%doc to install them.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Feb 26 2011 Gérard Milmeister <gemi@bluewin.ch> - 5.9.21-3
- Unretired package

* Sat Feb  5 2011 Gérard Milmeister <gemi@bluewin.ch> - 5.9.21-1
- new release 5.9.21

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.9.5-1
- new release 5.9.5

* Fri Jan  2 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.9.3-1
- new release 5.9.3

* Sun Oct  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.9.1-1
- new release 5.9.1

* Sun Sep 28 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.9.0-1
- new release 5.9.0

* Wed Feb 13 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.8.0-1
- new release 5.8.0

* Tue Jan 15 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.3-1
- new release 5.7.3

* Thu Jan 10 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.2-1
- new release 5.7.2

* Thu Dec 13 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.7.0-1
- new release 5.7.0

* Tue Dec  4 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.2-1
- new release 5.6.2

* Sat Nov 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.1-1
- new release 5.6.1

* Sat Nov  3 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.6.0-1
- new release 5.6.0

* Thu Aug 23 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5.2-1
- new release 5.5.2

* Wed Aug  8 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5.1-1
- new release 5.5.1

* Wed Jul  4 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.4.4-1
- new version 5.4.4

* Tue Apr  3 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.4.0-1
- new version 5.4.0

* Fri Mar 16 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.3.1-1
- new version 5.3.1

* Sat Feb 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.3.0-1
- new version 5.3.0

* Tue Jan  9 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.2.3-1
- new version 5.2.3

* Thu Dec 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.2.2-1
- new version 5.2.2

* Wed Dec 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.2.1-1
- new version 5.2.1

* Thu Nov 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.2.0-1
- new version 5.2.0

* Tue Nov 14 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.1.2-1
- new version 5.1.2

* Mon Oct  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-1
- new version 5.1.1

* Wed Aug 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0.5-1
- new version 5.0.5

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0.1-3
- Rebuild for FE6

* Mon Jun 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0.1-1
- new version 5.0.1

* Fri Jun 16 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0.0-1
- new version 5.0.0

* Mon May 22 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.18-1
- new version 4.12.18

* Thu May 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.17-1
- new version 4.12.17

* Fri Apr 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.15-1
- new version 4.12.15

* Tue Apr 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.14-1
- new version 4.12.14

* Thu Mar 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.12-1
- new version 4.12.12

* Wed Mar 15 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.11-1
- new version 4.12.11

* Mon Mar 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.10-1
- new version 4.12.10

* Mon Feb 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.8-1
- new version 4.12.8

* Mon Jan 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.6-1
- new version 4.12.6

* Sun Jan 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.12.5-1
- new version 4.12.5

* Wed Dec 28 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.12.3-1
- New Version 4.12.3

* Wed Nov 30 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.12.2-1
- New Version 4.12.2

* Fri Nov 25 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.12.1-1
- New Version 4.12.1

* Tue Nov  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.12.0-1
- New Version 4.12.0

* Sun Oct 16 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.11.8-1
- New Version 4.11.8

* Thu Sep 29 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.11.6
- New Version 4.11.6

* Thu Sep  8 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.11.4-2
- Updated description

* Wed Sep  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.11.4-1
- New Version 4.11.4

* Sun Aug 21 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.11.3-1
- New Version 4.11.3

* Fri Jun 24 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.11.0-1
- New Version 4.11.0

* Sun May 29 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.10.0-1
- New Version 4.10.0

* Mon May  9 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.9.7-1
- New Version 4.9.7

* Thu Apr 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.9.5-1
- New Version 4.9.5

* Thu Mar 24 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.9.2-1
- New Version 4.9.2

* Thu Mar 17 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.9.1-1
- New Version 4.9.1

* Tue Feb 22 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.11-1
- First Fedora release
