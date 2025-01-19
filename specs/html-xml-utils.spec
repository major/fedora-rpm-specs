Name:           html-xml-utils
Version:        8.6
Release:        3%{?dist}
Summary:        A number of simple utilities for manipulating HTML and XML files

# All files W3C except openurl.c which has two BSD-3-Clause functions
License:        W3C AND BSD-3-Clause
URL:            https://www.w3.org/Tools/HTML-XML-utils/
Source:         %{url}/html-xml-utils-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libcurl-devel
BuildRequires: libidn2-devel
BuildRequires: make

%description
A number of simple utilities for manipulating HTML and XML files. See Manpages
for each specific command.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
%make_build


%install
%make_install
# Install license separately so it has appropriate metadata
rm %{buildroot}%{_docdir}/html-xml-utils/COPYING

%check
make check

%files
%{_bindir}/hxaddid
%{_bindir}/hxcite
%{_bindir}/hxcite-mkbib
%{_bindir}/hxcount
%{_bindir}/hxextract
%{_bindir}/hxclean
%{_bindir}/hxcopy
%{_bindir}/hxprune
%{_bindir}/hxnsxml
%{_bindir}/hxprintlinks
%{_bindir}/hxincl
%{_bindir}/hxindex
%{_bindir}/hxmkbib
%{_bindir}/hxmultitoc
%{_bindir}/hxname2id
%{_bindir}/hxnormalize
%{_bindir}/hxnum
%{_bindir}/hxpipe
%{_bindir}/hxremove
%{_bindir}/hxselect
%{_bindir}/hxtabletrans
%{_bindir}/hxtoc
%{_bindir}/hxuncdata
%{_bindir}/hxunent
%{_bindir}/hxunpipe
%{_bindir}/hxunxmlns
%{_bindir}/hxwls
%{_bindir}/hxxmlns
%{_bindir}/hxref
%{_bindir}/xml2asc
%{_bindir}/asc2xml
%{_mandir}/man1/hxaddid.1*
%{_mandir}/man1/asc2xml.1*
%{_mandir}/man1/hxcite.1*
%{_mandir}/man1/hxcite-mkbib.1*
%{_mandir}/man1/hxcopy.1*
%{_mandir}/man1/hxcount.1*
%{_mandir}/man1/hxextract.1*
%{_mandir}/man1/hxclean.1*
%{_mandir}/man1/hxprune.1*
%{_mandir}/man1/hxincl.1*
%{_mandir}/man1/hxindex.1*
%{_mandir}/man1/hxmkbib.1*
%{_mandir}/man1/hxmultitoc.1*
%{_mandir}/man1/hxname2id.1*
%{_mandir}/man1/hxnormalize.1*
%{_mandir}/man1/hxnum.1*
%{_mandir}/man1/hxpipe.1*
%{_mandir}/man1/hxprintlinks.1*
%{_mandir}/man1/hxremove.1*
%{_mandir}/man1/hxtabletrans.1*
%{_mandir}/man1/hxtoc.1*
%{_mandir}/man1/hxuncdata.1*
%{_mandir}/man1/hxunent.1*
%{_mandir}/man1/hxunpipe.1*
%{_mandir}/man1/hxunxmlns.1*
%{_mandir}/man1/hxwls.1*
%{_mandir}/man1/xml2asc.1*
%{_mandir}/man1/hxxmlns.1*
%{_mandir}/man1/hxref.1*
%{_mandir}/man1/hxselect.1*
%{_mandir}/man1/hxnsxml.1*
%license COPYING
%doc AUTHORS TODO README 



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 17 2024 Benson Muite <benson_muite@emailplus.org> - 8.6-1
- Unretire package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 6.3-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.3-1
- Update to 6.3

* Thu Oct 04 2012 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.2-1
- Update to 6.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.1-1
- Update to 6.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 20 2011 Miloš Jakubíček <xjakub@fi.muni.cz> - 6.0-1
- Update to 6.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Milos Jakubicek <xjakub@fi.muni.cz> - 5.9-1
- Update to 5.9

* Wed Jan 19 2011 Milos Jakubicek <xjakub@fi.muni.cz> - 5.8-1
- Update to 5.8

* Wed Apr 28 2010 Milos Jakubicek <xjakub@fi.muni.cz> - 5.7-1
- Update to 5.7

* Tue Apr 27 2010 Milos Jakubicek <xjakub@fi.muni.cz> - 5.6-1
- Update to 5.6
- Dropped html-xml-utils-5.5-hxpipe-man.patch (merged upstream)

* Sun Oct 25 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 5.5-2
- Added html-xml-utils-5.5-hxpipe-man.patch, resolves BZ#527655

* Fri Aug 22 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 5.5-1
- Update to 5.5 (bugfix for self-URL references)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 19 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 5.4-1
- Update to 5.4 (bug in removal of /./ fixed. Now leaves one / instead of none).

* Sat May 16 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 5.3-1
- Update to 5.3: many bugfixes, most binaries have now a "hx" prefix
- Removed Conflicts: surfraw, normalize
- Fixed license tag: W3C

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 3.7-7
- Add explicit "Conflicts: surfraw" (#208781).
  Add explicit "Conflicts: normalize" (#208781). 
  Both are fixed in upstream releases >= 5.0 (!)

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.7-6
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.7-5
- Autorebuild for GCC 4.3

* Mon Oct 09 2006 Gavin Henry <ghenry[AT]suretecsystems.com> - 3.7-4
- FC6 Rebuild

* Mon Sep 26 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 3.7-3
- Added README again, removed NEWS by mistake.

* Mon Sep 26 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 3.7-2
- Removed the emtpy README and changed name back to 
  html-xml-utils

* Wed Sep 21 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 3.7-1
- Initial Build 
