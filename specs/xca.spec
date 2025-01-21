%global gitproject0	xca
%global gitowner0	chris2511

Summary:	Graphical X.509 certificate management tool
Name:		xca
Version:	2.7.0
Release:	2%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://hohnstaedt.de/xca/
Source0:	https://github.com/%{gitowner0}/%{gitproject0}/releases/download/RELEASE.%{version}/%{name}-%{version}.tar.gz
Source1:	xca-2.5.0-README.IMPORTANT

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-linguist
BuildRequires:	openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:	openssl-devel-engine
%endif
BuildRequires:	xdg-utils
BuildRequires:	libtool-ltdl-devel
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinxcontrib-qthelp

Requires:	hicolor-icon-theme

Suggests:	qt5-qtbase-mysql
Suggests:	qt5-qtbase-postgresql
Suggests:	qt5-qtbase-odbc


%description
  X Certificate and Key management is a graphic interface for managing
asymmetric keys like RSA or DSA, certificates and revocation lists. It is
intended as a small CA for creation and signing certificates. It uses the
OpenSSL library for the cryptographic operations.
  Certificate signing requests (PKCS#10), certificates (X509v3), the signing
of requests, the creation of self-signed certificates, certificate revocation
lists and SmartCards are supported. For an easy company-wide use, customizable
templates can be used for certificate and request generation. The PKI structures
can be imported and exported in several formats like PKCS#7, PKCS#12, PEM,
DER, PKCS#8. All cryptographic data are stored in a byte order agnostic file
format, portable across operating systems.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%autosetup -p 1
cp '%{SOURCE1}' README.IMPORTANT


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

export CXXFLAGS='%{optflags} -DDOCDIR=\"%{_docdir}/xca\"'
%cmake	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
%cmake_build


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

%cmake_install

#	Do not include db statistics program and man.
find '%{buildroot}' -name 'xca_db_stat*' -delete

#	Do not use pixmaps directory.
rm -rf '%{buildroot}%{_datadir}/pixmaps'

#	Reinstall documentation.
rm -rf '%{buildroot}%{_docdir}/xca'/*
mv '%{buildroot}%{_datadir}/xca/html' '%{buildroot}%{_docdir}/xca/'

#	Install mime file types.
install -d -m 755 '%{buildroot}%{_datadir}/mime/packages'
install -p -m 644 misc/xca.xml '%{buildroot}%{_datadir}/mime/packages/'

#	Install desktop application file.
desktop-file-install --mode 0644					\
	--dir '%{buildroot}%{_datadir}/applications'			\
	--delete-original						\
	--add-mime-type application/x-xca-database			\
	--remove-category QT						\
	'%{buildroot}%{_datadir}/applications/xca.desktop'

#	Tag translation files.
%find_lang '%{name}' --with-qt


#-------------------------------------------------------------------------------
%files -f %{name}.lang
#-------------------------------------------------------------------------------

%doc AUTHORS COPYRIGHT README.IMPORTANT
%doc %{_docdir}/xca/*
%{_bindir}/*
%dir %{_datadir}/xca
%{_datadir}/xca/*.txt
%{_datadir}/xca/*.xca
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/mime/packages/%{name}.*
%{_datadir}/applications/*
%{_datadir}/bash-completion/
%{_metainfodir}/*
%attr(0644, root, root) %{_mandir}/*/*


#-------------------------------------------------------------------------------
%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

#-------------------------------------------------------------------------------

* Fri Sep  6 2024 Patrick Monnerat <patrick@monnerat.net> 2.7.0-1
- New upstream release.

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.0-5
- convert license to SPDX

* Tue Jul 23 2024 Patrick Monnerat <patrick@monnerat.net> 2.6.0-4
- BR openssl-devel-engine for Fedora >= 41.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May  6 2024 Patrick Monnerat <patrick@monnerat.net> 2.6.0-2
- Fix application icon.
  https://bugzilla.redhat.com/show_bug.cgi?id=2279161

* Sun Mar 17 2024 Patrick Monnerat <patrick@monnerat.net> 2.6.0-1
- New upstream release.

* Mon Jan 22 2024 Patrick Monnerat <patrick@monnerat.net> 2.5.0-3
- Patch "pastekey" fixes a crash pasting an encrypted private key.
  https://github.com/chris2511/xca/commit/d29d55a
- Patch "revokedel" fixes a freeze when deleting a certificate.
  https://github.com/chris2511/xca/commit/43e1b33
- Patch "delete_after_revoke" fixes a crash deleting+revoking a certificate.
  https://bugzilla.redhat.com/show_bug.cgi?id=2259477

* Tue Nov 07 2023 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Explicitly BuildRequire python3-sphinxcontrib-qthelp

* Fri Oct  6 2023 Patrick Monnerat <patrick@monnerat.net> 2.5.0-1
- New upstream release.
- Build using cmake.
- Doc file "README.IMPORTANT" for needed passord reset.
  https://github.com/chris2511/xca/issues/458#issuecomment-1740106691

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Patrick Monnerat <patrick@monnerat.net> 2.4.0-1
- New upstream release.
- Patch "openssl3" for openssl version 3 compatibility.
- Patch "noclean" fixes building in symlinked directory.
- Patch "mimeicons" to declare mime types icons as generic.
- Patch "lang-it" to update italian translation.
- Patch "lang-fr" to update french translation.
- Uses sphinx instead of SGML for documentation.
- Use new icons.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.3.0-5
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Patrick Monnerat <patrick@monnerat.net> 2.3.0-2
- BR translate-toolkit is not needed anymore.

* Thu Aug  6 2020 Patrick Monnerat <patrick@monnerat.net> 2.3.0-1
- New upstream relase.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  8 2020 Patrick Monnerat <patrick@monnerat.net> 2.2.1-1
- New upstream relase.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  9 2019 Patrick Monnerat <patrick@monnerat.net> 2.1.2-4
- Patch "bz1779029-segv" fixes a segmentation fault.
  https://github.com/chris2511/xca/commit/262c805
  https://bugzilla.redhat.com/show_bug.cgi?id=1779029

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Patrick Monnerat <patrick@monnerat.net> 2.1.2-1
- New upstream release.
- Require qt database backends for external database support.
- Do not install images: they are already linked into the xca binary program.
- Improve language tagging.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Patrick Monnerat <patrick@monnerat.net> 1.4.1-1
- New upstream release.
- New URL and source location.
  Fixes BZ #1568760.

* Wed Mar  7 2018 Patrick Monnerat <patrick@monnerat.net> 1.4.0-3
- "Modernize" spec file.
- BR gcc-g++.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Patrick Monnerat <patrick@monnerat.net> 1.4.0-1
- New upstream release 1.4.0.
- Use qt5.
- Remove obsolete rpm scriptlets.

* Mon Aug  7 2017 Patrick Monnerat <patrick@monnerat.net> 1.3.2-7
- Remove xca_db_stat from install (fixes FTBFS on rawhide).

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Patrick Monnerat <patrick@monnerat.net> 1.3.2-4
- Patch "openssl11" for OpenSSL 1.1 support.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild


* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Patrick Monnerat <patrick.monnerat@dh.com> 1.3.2-1
- New upstream release.
- Patch "oidfieldcursor" to restore normal cursor behavior on OID resolver
  input field.
- Drop README.update.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 24 2014 Patrick Monnerat <pm@datasphere.ch> 1.1.0-1
- New upstream release

* Mon Nov 17 2014 Patrick Monnerat <pm@datasphere.ch> 1.0.0-2
- Patch "nonstdext" avoids segfault when viewing cert with
  non-standard extension.
  https://bugzilla.redhat.com/show_bug.cgi?id=1164340

* Tue Oct 28 2014 Patrick Monnerat <pm@datasphere.ch> 1.0.0-1
- New upstream release.
  Set-up a larger desktop icon.

* Wed Oct 15 2014 Patrick Monnerat <pm@datasphere.ch> 0.9.3-9
- Patch "openssl101i" for openssl-1.0.1i compatibility.
  https://bugzilla.redhat.com/show_bug.cgi?id=1152043
- Patch "desktopicon" removes the icon file extension in desktop entry file.
  https://sourceforge.net/p/xca/patches/15/

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-7
- fix/update scriptlets

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Patrick Monnerat <pm@datasphere.ch> - 0.9.3-5
- Rebuild for elliptic curves inclusion.
  https://bugzilla.redhat.com/show_bug.cgi?id=1089245

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.3-3
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Patrick Monnerat <pm@datasphere.ch> 0.9.3-1
- New upstream release.

* Mon May  7 2012 Patrick Monnerat <pm@datasphere.ch> 0.9.2-1
- New upstream release.
- Patch "french" to update french translation.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Patrick Monnerat <pm@datasphere.ch> 0.9.1-1
- New upstream release: all previous patches included in new code.

* Mon Feb 28 2011 Patrick Monnerat <pm@datasphere.ch> 0.9.0-2
- Fix Exec parameter in desktop file.

* Mon Feb 28 2011 Patrick Monnerat <pm@datasphere.ch> 0.9.0-1
- New upstream release.
- Suppress "includes" patch (went upstream).
- Suppress "openssl10" patch (new release is openssl 10 compatible).
- Patches "locale" and "noec" port to new release.
- French localization added.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-1401
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 18 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8.1-1400
- fixed implicit DSO linking (#565073)

* Sat Jan 16 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8.1-1300
- updated to 0.8.1
- reenabled ppc64

* Sun Jan  3 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8.0-1301
- updated to 0.8.0
- added patch to disable elliptic curve code because these algorithms
  are removed in Fedora's openssl

* Sun Sep 13 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7.0-0
- updated to 0.7.0; rediffed patches

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> - 0.6.4-9
- rebuilt with new openssl

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.6.4-7
- include stdint.h for uint32_t

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 0.6.4-5
- rebuild with new openssl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.4-4
- Autorebuild for GCC 4.3

* Sat Jan  5 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.6.4-3
- Add patch by Caolan McNamara (#427619) to build against new openssl

* Sat Aug 25 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.4-1
- updated to 0.6.4
- optimized scriptlets which are dealing with the desktop stuff

* Sat Jun 30 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-2
- improved desktop-integration by registering MIME type and icons
- disabled ppc64 build (bz #246324)

* Thu Jun 14 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-1
- updated to 0.6.3; rediffed patches
- fixed build
- added BR on linuxdoc-tools

* Mon Apr  9 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.1-1
- updated to 0.6.1

* Sat Mar 17 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.0-1
- updated to 0.6.0
- removed old patches

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-6
- rebuilt

* Sat Feb 18 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-5
- rebuilt for FC5

* Sun Dec 25 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-4
- fixed compilation with gcc41 and openssl098
- use SHA1 instead of MD5 as the default hashalgo

* Sat May 21 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-3
- generalized db4 detection
- fixed x86_64 builds

* Thu May 19 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-2
- use %%dist instead of %%disttag

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Mar  8 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1
- updated to 0.5.1
- (re)enabled parallel build
- applied -langinst patch and other ideas from
  https://bugzilla.fedora.us/show_bug.cgi?id=2019 (Ville Skyttä)
- fixed build with gcc4 and db43
- removed old cruft from the specfile

* Sat Dec 13 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.4.6-0.fdr.1
- changed compile/install commands to work with the new, yet-another configure system
- removed libpthread test since it went upstream
- do not package README anymore; it contains installation/build instructions only
- applied gcc3 patch
- updated to 0.4.6
- removed desktop patch which went upstream

* Fri Aug 15 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.5-0.fdr.2
- applied Ville Skyttä's patch to add categories and to fix encoding of desktop-file
  (http://sourceforge.net/tracker/index.php?func=detail&aid=789374&group_id=62274&atid=500027)
- removed '--add-category ...' options which become obsoleted by this
  patch

* Fri Aug 15 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.5-0.fdr.1
- updated to 0.4.5

* Thu Aug  7 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.4-0.fdr.1
- updated to 0.4.4
- use generic download address for Source0

* Sat Jul 26 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.2-0.fdr.1.1
- changed Summary: accordingly the suggestion in Fedora bug #494

* Mon Jul 21 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.2-0.fdr.1
- updated to 0.4.2

* Sun Jul 20 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.1-0.fdr.2
- removed the %%{smp_mflags} since parallel builds are not supported
  by the QT makefiles

* Tue Jul 15 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.1-0.fdr.1
- updated to 0.4.1
- added debian/changelog to %%doc-list

* Tue Jul  8 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.0-0.fdr.1
- updated to 0.4.0
- removed patches which went upstream

* Fri Jul  4 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.3.2-0.fdr.2.1
- fixed Summary

* Tue Jul  1 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.3.2-0.fdr.2
- added icon
- made minor fixes in the %%description
- added explicit epoch
- created a separate .desktop file

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.3.2-0.fdr.1
- prepared for fedora.us

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.3.2-0.0.3
- added dbpriv patch
- added desktop entry

* Fri Jun  6 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- Initial build.
