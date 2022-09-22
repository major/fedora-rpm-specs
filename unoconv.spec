Summary:   A tool to convert documents from/to any format supported by LibreOffice
Name:      unoconv
Version:   0.9.0
Release:   8%{?dist}
License:   GPLv2
URL:       https://github.com/unoconv/unoconv/
Source:    https://github.com/unoconv/unoconv/archive/%{version}.tar.gz

Patch0:    0001-python3-added-compatibility.patch
Patch1:    0001-update-FSF-address.patch
Patch2:    0001-make-LaTeX-export-usable-with-writer2latex-ext.patch
Patch3:    0001-libreoffice-or-OO.o-has-never-had-wps-export.patch
Patch4:    0002-remove-export-formats-dropped-by-LibreOffice.patch

BuildArch: noarch

BuildRequires: make
BuildRequires: asciidoc
BuildRequires: xmlto

Requires:  libreoffice-filters
Requires:  libreoffice-pyuno
Suggests:  libreoffice-writer2latex
Suggests:  openoffice.org-diafilter

%description
Universal Office Converter (unoconv) is a command line tool to convert any
document format that LibreOffice can import to any document format that
LibreOffice can export. It makes use of the LibreOffice's UNO bindings for
non-interactive conversion of documents.

Supported document formats include Open Document Format (.odg, .odp, .ods,
.odt), MS Word (.doc), MS Office Open/MS OOXML (.docx, .pptx, .xlsx), PDF,
HTML, RTF, and many more.

%prep
%autosetup -p1
rm doc/%{name}.1

%build
make %{?_smp_mflags}
asciidoc README.adoc

%install
make install DESTDIR="%{buildroot}"

%files
%doc AUTHORS ChangeLog README.html
%doc doc/errcode.html doc/filters.html doc/formats.html doc/selinux.html
%license COPYING
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 David Tardon <dtardon@redhat.com> - 0.9.0-2
- upload fixed tarball

* Sat Sep 28 2019 David Tardon <dtardon@redhat.com> - 0.9-1
- new upstream release

* Sat Aug 31 2019 David Tardon <dtardon@redhat.com> - 0.8.2-1
- new upstream release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7-4
- Rebuild for Python 3.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 David Tardon <dtardon@redhat.com> - 0.7-2
- don't install obscure filter deps by default

* Fri Jul 10 2015 David Tardon <dtardon@redhat.com> - 0.7-1
- new upstream release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 David Tardon <dtardon@redhat.com> - 0.6-10
- Resolves: rhbz#1076275 unoconv trips over '-f latex'
- do not show unusable export formats

* Thu Apr 17 2014 David Tardon <dtardon@redhat.com> - 0.6-9
- Resolves: rhbz#1076275 unonconv trips over '-f latex'

* Wed Feb 12 2014 David Tardon <dtardon@redhat.com> - 0.6-8
- Resolves: rhbz#1047539 --stdout option does not work

* Thu Jan 30 2014 David Tardon <dtardon@redhat.com> - 0.6-7
- pull in all libreoffice filters

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 David Tardon <dtardon@redhat.com> - 0.6-5
- Resolves: rhbz#987046 drop env from shebang

* Wed May 29 2013 David Tardon <dtardon@redhat.com> - 0.6-4
- rhbz#957776 cannot open office documents

* Mon Apr 08 2013 David Tardon <dtardon@redhat.com> - 0.6-3
- Resolves: rhbz#947096 unoconv doesn't work with Libreoffice 4.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 David Tardon <dtardon@redhat.com> - 0.6-1
- new upstream release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 David Tardon <dtardon@redhat.com> - 0.5-1
- new upstream release

* Mon Mar 26 2012 David Tardon <dtardon@redhat.com> - 0.4-6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4-3
- Add missing Requires on openoffice.org-brand/libreoffice-core. RHBZ#658576

* Sat Nov 13 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4-2
- Backport some upstream fixes (LD_LIBRARY_PATH issue and -o flag issue)

* Fri Nov 12 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4-1
- Update to 0.4

* Sat Oct 30 2010 Caolán McNamara <caolanm@redhat.com> - 0.3-5
- rebuild for LibreOffice

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3-3
- Fix rpmlints
- Prepare package for Fedora review

* Sun Feb 22 2009 Peter Hanecak <hany@hany.sk> 0.3-2
- used %%{?dist} in release number
- license GPLv2

* Wed Dec 19 2007 Dag Wieers <dag@wieers.com> - 0.3-2 - 5993+/dag
- Fixed openoffice.org2 dependency on RHEL4.

* Sat Sep 01 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Sun May 20 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Updated to release 0.2.

* Sat May 19 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
