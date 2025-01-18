Name:           abcMIDI
Version:        2022.12.09
Release:        8%{?dist}
Summary:        ABC to/from MIDI conversion utilities

Group:          Applications/Multimedia
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://ifdo.ca/~seymour/runabc/top.html
Source0:        https://ifdo.ca/~seymour/runabc/%{name}-%{version}.zip

BuildRequires:  gcc dos2unix
BuildRequires: make

%description 
The abcMIDI package contains four programs: abc2midi to convert ABC
music notation to MIDI, midi2abc to convert MIDI files to (a first
approximation to) the corresponding ABC, abc2abc to reformat and/or
transpose ABC files, and yaps to typeset ABC files as PostScript.

For a description of the ABC syntax, please see the ABC userguide
which is a part of the abcm2ps.

A mirror github repo is at https://github.com/sdgathman/abcmidi


%prep
%setup -q -n abcmidi
find . -type f | xargs dos2unix
# make license easier to find in files
mv doc/gpl.txt doc/LICENSE

%build
%configure
%{make_build} 

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 abc2midi %{buildroot}%{_bindir}
install -p -m 755 abcmatch %{buildroot}%{_bindir}
install -p -m 755 midi2abc %{buildroot}%{_bindir}
install -p -m 755 midicopy %{buildroot}%{_bindir}
install -p -m 755 abc2abc %{buildroot}%{_bindir}
install -p -m 755 mftext %{buildroot}%{_bindir}
install -p -m 755 yaps %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 doc/abc2abc.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/abc2midi.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/mftext.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/midi2abc.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/midicopy.1 %{buildroot}%{_mandir}/man1
install -p -m 644 doc/yaps.1 %{buildroot}%{_mandir}/man1


%files
%license doc/LICENSE
%doc doc/programming VERSION doc/*.txt doc/AUTHORS doc/CHANGES
%{_mandir}/man*/*
%{_bindir}/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2022.12.09-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Stuart Gathman <stuart@gathman.org> - 2022.12.09-1
- New upstream release, removes compiled binaries :-{

* Tue Dec 06 2022 Peter Fordham <peter.fordham@gmail.com> - 2022.12.05-8
- New upstream release, fixes C99 issues

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.29-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.06.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Stuart Gathman <stuart@gathman.org> - 2020.06.29-1
- New upstream release

* Tue Jun 02 2020 Stuart Gathman <stuart@gathman.org> - 2020.05.06-2
- Patch some warnings and dup globals

* Mon Jun 01 2020 Stuart Gathman <stuart@gathman.org> - 2020.05.06-1
- New upstream release

* Sun Mar 22 2020 Stuart Gathman <stuart@gathman.org> - 2020.02.12-1
- New release 2020-02-12

* Sun Nov 12 2017 Stuart Gathman <stuart@gathman.org> - 2013.04.30-1
- New release 2013-04-30

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090317-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090317-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Gerard Milmeister <gemi@bluewin.ch> - 20090317-1
- new release 2009-03-17

* Wed Sep 24 2008 Gerard Milmeister <gemi@bluewin.ch> - 20080924-1
- new release 2008-09-24

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20070106-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20070106-2
- Autorebuild for GCC 4.3

* Tue Jan  9 2007 Gerard Milmeister <gemi@bluewin.ch> - 20070106-1
- new version 20070106

* Wed Dec 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 20061211-1
- new version 20061211

* Mon Nov  6 2006 Gerard Milmeister <gemi@bluewin.ch> - 20061103-1
- new version 20061103

* Tue Oct 31 2006 Gerard Milmeister <gemi@bluewin.ch> - 20061027-1
- new version 20061027

* Mon Oct 16 2006 Gerard Milmeister <gemi@bluewin.ch> - 20061015-1
- new version 20061015

* Mon Oct  9 2006 Gerard Milmeister <gemi@bluewin.ch> - 20061005-1
- new version 20061005

* Mon Sep 11 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060910-1
- new version 20060910

* Wed Aug 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060829-1
- new version 20060829

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060805-2
- Rebuild for FE6

* Tue Aug  8 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060805-1
- new version 2006-08-05

* Mon Jul 31 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060730-1
- new version 2006-07-30

* Mon Jun 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060625-1
- new version 2006-06-25

* Thu Jun 15 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060608-1
- new version 2006-06-08

* Sun Jun  4 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060422-1
- new version 2006-04-22

* Tue Mar  7 2006 Gerard Milmeister <gemi@bluewin.ch> - 20060207-1
- First Fedora release

