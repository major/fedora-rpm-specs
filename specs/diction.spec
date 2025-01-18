Name:           diction
Version:        1.14
Release:        10%{?dist}
Summary:        Identifies diction and style errors

License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/diction/diction.html
Source0:        http://www.moria.de/~michael/diction/diction-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires: make

%description
Diction and style are two old standard UNIX commands. Diction identifies wordy
and commonly misused phrases. Style analyses surface characteristics of a
document, including sentence length and other readability measures.

These programs cannot help you structure a document well, but they can help to
avoid poor wording and compare the readability (not the understandability!) of
your documents with others. Both commands support English and German documents.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}
# convert manpages to unicode
for FILE in *.1; do
    /usr/bin/iconv -f iso-8859-1 -t utf-8 $FILE > $FILE.utf8
    mv -f $FILE.utf8 $FILE
done


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}



%files -f %{name}.lang
%doc COPYING README NEWS
%{_bindir}/*
%{_datadir}/diction
%{_mandir}/man*/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.14-5
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.14-1
- 1.14

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.11-2
- Autorebuild for GCC 4.3

* Sun Dec 23 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.11-1
- Upstream 1.11 (#423901)
- Update license version to GPLv3+
- Update source links

* Sun Sep 03 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10-0.1.1.rc4
- Bump for rebuild.

* Sun Jul 23 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10-0.1.rc4
- version 1.10-rc4
- convert manpages to utf-8

* Mon Feb 13 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.08-1.2
- FC5 rebuild

* Tue Jan 31 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.08-1.1
- FC5 rebuild

* Thu Jun 30 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.08-1
- Version 1.08
- Do not list locale files namely in addition to findlang
- Add NEWS to doc
- Disttagging
- Remove epoch

* Fri Jul 23 2004 Michel Salim <michel.salim[AT]gmail.com> - 0:1.06-0.fdr.2
- Added version info to changelog entries
- Use find_lang

* Tue Jul 20 2004 Michel Salim <michel.salim[AT]gmail.com> - 0:1.06-0.fdr.1
- Update to new version

* Sat Jul 17 2004 Michel Salim <michel.salim[AT]gmail.com> - 0:1.05-0.fdr.1
- Initial Fedora release
