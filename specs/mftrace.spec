Name:		mftrace
Version:	1.2.20
Release:	15%{?dist}
Summary:	Utility for converting TeX bitmap fonts to Type 1 or TrueType fonts

License:	GPL-2.0-only
URL:		http://lilypond.org/mftrace/
Source0:	http://lilypond.org/download/sources/mftrace/%{name}-%{version}.tar.gz
Patch0:		mftrace-shebang.patch
Patch1:         mftrace-1.2.20-man.patch
Patch2:         python3.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:	python3-devel autotrace
Requires:	autotrace fontforge t1utils texlive-collection-fontsrecommended

%description
mftrace is a small Python program that lets you trace a TeX bitmap
font into a PFA or PFB font (A PostScript Type1 Scalable Font) or TTF
(TrueType) font.

Scalable fonts offer many advantages over bitmaps, as they allow
documents to render correctly at many printer resolutions. Moreover,
Ghostscript can generate much better PDF, if given scalable PostScript
fonts.

%prep
%setup -q
%py3_shebang_fix .

sed -i -e "s|-Wall -O2|$RPM_OPT_FLAGS -std=gnu17|" GNUmakefile.in

%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p0

%build
PYTHON=%{__python3} %configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc README.txt ChangeLog
%license COPYING
%{_bindir}/*
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2.20-11
- Drop dependency on 2to3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2.20-9
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.2.20-1
- 1.2.20

* Fri Aug 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.2.19-9
- Fix shebang.

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.2.19-8
- Move to Python 3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.2.19-1
- 1.2.19.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2.18-7
- Use '|' as sed-pattern delimiter (Fix F23FTBFS, RHBZ#1239679).
- Modernize spec.
- Add %%license.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.18-1
- Latest upstream, fixed tex requires.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.15-5
- recompiling .py files against Python 2.7 (rhbz#623337)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.15-2
- Rebuild for Python 2.6

* Wed Aug 27 2008 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.15-1
- Update to new release.

* Fri Aug  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.14-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.14-4
- Autorebuild for GCC 4.3

* Fri Jan  4 2008 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.14-3
- Change tetex-fonts dependency to texlive-fonts.

* Wed Aug 22 2007 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.14-2
- Rebuild.

* Mon Jul 30 2007 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.14-1
- New release.
- Update URLs.

* Mon Nov  6 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.5-1
- New release.

* Mon Aug 28 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.4-4
- Rebuild for FC6.

* Sat May 20 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.4-2
- Make sure $RPM_OPT_FLAGS are used

* Sat May 13 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.2.4-1
- New upstream release.

* Tue Apr 25 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.1.19-3
- Update description

* Tue Apr 25 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.1.19-2
- ghost .pyo files

* Thu Mar 30 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.1.19-1
- First version.
