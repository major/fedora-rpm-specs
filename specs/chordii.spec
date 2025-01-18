Summary: Print songbooks (lyrics + chords)
Name: chordii
Version: 4.5.3b
Release: 24%{?dist}
URL: http://www.chordii.org
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Obsoletes: chordie >= 0 chord >= 0
BuildRequires: gcc
BuildRequires: make

%description
chordii provides guitar players and other musicians with a tool to
produce good looking, self-descriptive music sheets from text files.

chordii reads text files in ChordPro format, containing the lyrics of
songs, the chords to be played, their descriptions and some other
optional data. It produces a PostScript document suitable for viewing
and printing.

chordii features include:
 - centered titles,
 - chord names above the words,
 - chord diagrams at the end of the songs,
 - multiple columns on a page,
 - multiple logical pages per physical pages (1, 2 or 4),
 - configurable fonts and sizes,
 - the complete ISO 8859-1 character set,
 - optionally, ISO 8859-2 character set,
 - chorus marking,
 - automated chord transposition,
 - songbook creation: typeset multiple songs with page numbers and a
   table of contents.

For details on the ChordPro format, see http://www.chordpro.org .

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install

%files
%doc README NEWS COPYING examples/
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.5.3b-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb  2 2020 Johan Vromans <jvromans@squirrel.nl> - 4.5.3b-12
- Upgrade to upstream 4.5.3b (compiler bug fix).

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Johan Vromans <jvromans@squirrel.nl> - 4.5.3-8
- Add buildrequires for gcc.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 10 2016 Johan Vromans <jvromans@squirrel.nl> - 4.5.3-2
- Actualize URLs.

* Thu Mar 10 2016 Johan Vromans <jvromans@squirrel.nl> - 4.5.3-1
- Upgrade to upstream version 4.5.3.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Johan Vromans <jvromans@squirrel.nl> - 4.5.1-1
- Upgrade to upstream version 4.5.1.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr  3 2010 Johan Vromans <jvromans@squirrel.nl> - 4.3-2
- Solve the dist puzzle.

* Mon Jul 13 2009 Johan Vromans <jvromans@squirrel.nl> - 4.3-1
- Rebase on GPL Chord 3.6.4.

* Sat Jan 31 2009 Johan Vromans <jvromans@squirrel.nl> - 4.2-5
- Changed examples/* to examples/ to include all examples in a dir

* Fri Jan 30 2009 Johan Vromans <jvromans@squirrel.nl> - 4.2-4
- Fixed changelog entries involving %% to prevent macro expansion

* Fri Jan 30 2009 Johan Vromans <jvromans@squirrel.nl> - 4.2-3
- Fixed URL and Source urls
- Added %%{?dist} to Release
- Fixed missing (optional) argument to %%defattr
- Changed examples to examples/* to include all examples

* Fri Jan 30 2009 Johan Vromans <jvromans@squirrel.nl> - 4.2-2
- Update description
- Add patch to fix Makefiles to avoid double install of manual pages
- use smp_mflags
- use install -p

* Thu Jan 29 2009 Johan Vromans <jvromans@squirrel.nl> - 4.2-1
- First Fedora version
