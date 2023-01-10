%global pkg ddskk
%global pkgname Daredevil SKK

Summary: Daredevil SKK - Simple Kana to Kanji conversion program for Emacs
Name: emacs-common-ddskk
Version: 16.2
Release: 14%{?dist}
License: GPLv2+
URL: http://openlab.ring.gr.jp/skk/main.html
Source0: http://openlab.ring.gr.jp/skk/maintrunk/ddskk-%{version}.tar.gz
Source1: ddskk-init.el
BuildArch: noarch
BuildRequires: emacs
%if 0%{?fedora} < 36
BuildRequires: xemacs, apel-xemacs
%endif
BuildRequires: make
Requires(post): info
Requires(preun): info

%description
Daredevil SKK is a branch of SKK (Simple Kana to Kanji conversion program,
an input method of Japanese). It forked from the maintrunk, SKK version 10.56.
It consists of a simple core and many optional programs which provide extensive
features, however, our target is to more simplify core, and more expand its
optional features.

This package does not include dictionaries or a skkserver. Please install them
separately.

%package -n emacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:	emacs(bin) >= %{_emacs_version}
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	ddskk = %{version}-%{release}
Obsoletes:	ddskk < %{version}-%{release}
Provides:	emacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	emacs-%{pkg}-el < %{version}-%{release}
%if 0%{?fedora} >= 36
Obsoletes:	xemacs-%{pkg} < 16.2-11
%endif

%description -n emacs-%{pkg}
This package contains the byte compiled elisp packages to run %{pkgname}
with GNU Emacs.


%if 0%{?fedora} < 36
%package -n xemacs-%{pkg}
Summary:	Compiled elisp files to run %{pkgname} under XEmacs
Requires:	xemacs(bin) >= %{_xemacs_version}
Requires:	apel-xemacs
Requires:	emacs-common-%{pkg} = %{version}-%{release}
Provides:	ddskk = %{version}-%{release}
Provides:	xemacs-%{pkg}-el = %{version}-%{release}
Obsoletes:	xemacs-%{pkg}-el < %{version}-%{release}

%description -n xemacs-%{pkg}
This package contains the byte compiled elisp packages to use %{pkgname} with
XEmacs.
%endif


%prep
%setup -q -n %{pkg}-%{version}

# We can't set SKK-MK-texinfo-coding-system in SKK-CFG since it is
# defined with defconst.

sed -ie "s!\(SKK-MK-texinfo-coding-system\) 'iso-2022-jp!\1 'utf-8!" SKK-MK

# We don't need information about other platforms
rm READMEs/README.MacOSX.ja
rm READMEs/README.w32.ja.org

# avoid buildroot in tutorial path
sed -ie "s!@TUT@!%{_datadir}/skk/SKK.tut!" skk-setup.el.in


%build


%install
# needed for make install-info
mkdir -p %{buildroot}%{_datadir}/info

cat >> SKK-CFG <<EOF
(setq PREFIX "%{buildroot}%{_prefix}")
(setq SKK_LISPDIR "%{buildroot}%{_emacs_sitelispdir}/ddskk")
EOF

make EMACS=emacs install

mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

%if 0%{?fedora} < 36
make clean
cat >> SKK-CFG <<EOF
(setq SKK_PREFIX "ddskk")
(setq PACKAGEDIR "%{buildroot}%{_xemacs_sitepkgdir}")
EOF
make package
make install-package

mkdir -p %{buildroot}%{_xemacs_sitestartdir}
install -p -m 644 %SOURCE1 %{buildroot}%{_xemacs_sitestartdir}

rm %{buildroot}%{_xemacs_sitepkgdir}/info/skk.info*
%endif
rm -f %{buildroot}%{_infodir}/dir

%files
%doc ChangeLog READMEs
%{_datadir}/skk
%{_infodir}/*


%files -n emacs-%{pkg}
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}


%if 0%{?fedora} < 36
%files -n xemacs-%{pkg}
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%{_xemacs_sitelispdir}/%{pkg}/*.el
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/%{pkg}
%{_xemacs_sitepkgdir}/etc/%{pkg}/*
%dir %{_xemacs_sitepkgdir}/etc/%{pkg}
%endif


%changelog
* Sat Jan  7 2023 Jens Petersen <petersen@redhat.com> - 16.2-14
- do not compile ddskk-setup.el (#2109358)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 16.2-11
- Drop XEmacs support in F36 and later

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar  6 2017 Daiki Ueno <dueno@redhat.com> - 16.2-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct  5 2016 Daiki Ueno <dueno@redhat.com> - 16.1-1
- new upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Daiki Ueno <dueno@redhat.com> - 15.2-3
- drop -el subpackages (#1234541)
- fix wrong dates in changelog

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Daiki Ueno <dueno@redhat.com> - 15.2-1
- new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Daiki Ueno <dueno@redhat.com> - 15.1-1
- new upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan  4 2012 Daiki Ueno <dueno@redhat.com> - 14.4-1
- new upstream release

* Mon Jul  4 2011 Daiki Ueno <dueno@redhat.com> - 14.3-1
- new upstream release
- drop %%defattr(-,root,root,-) from each %%files

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Daiki Ueno <dueno@redhat.com> - 14.2-1
- new upstream release
- drop dependency on apel

* Fri Nov 12 2010 Daiki Ueno <dueno@redhat.com> - 14.1-7
- unown %%_xemacs_sitepkgdir/etc/ since xemacs-common now owns it (#645621)

* Fri Nov  5 2010 Daiki Ueno <dueno@redhat.com> - 14.1-6
- fix typo

* Fri Nov  5 2010 Daiki Ueno <dueno@redhat.com> - 14.1-5
- fix upgrade path from ddskk

* Fri Oct 22 2010 Daiki Ueno <dueno@redhat.com> - 14.1-4
- own %%{_xemacs_sitepkgdir}/etc/ instead of etc/ddskk, as a
  workaround of #645621
- use curly braces where %%buildroot macro is used

* Thu Oct 21 2010 Daiki Ueno <dueno@redhat.com> - 14.1-3
- remove Emacs coding cookie for this spec

* Thu Oct 21 2010 Daiki Ueno <dueno@redhat.com> - 14.1-2
- drop buildroot, %%clean and cleaning of buildroot in %%install
- use correct scriptlet for texinfo files
- remove %%apel_minver since the current apel is newer
- use correct file attributes for the main package
- remove "skk" and "ddskk-el" from Obsoletes: since they are even
  missing in the current dist

* Mon Sep  6 2010 Daiki Ueno <dueno@redhat.com> - 14.1-1
- new upstream release
- remove ddskk-char.patch (already applied in the upstream tarball)
- pass "-p" option to install

* Thu Apr 15 2010 Daiki Ueno <dueno@redhat.com> - 13.1-3
- rename the package from ddskk to emacs-common-ddskk (closes #531688)
  and split into subpackages following the emacs packaging policy.
- enable XEmacs build again (patch from Jerry James, #532624).
- change the encoding of Japanese docs/info to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Jens Petersen <petersen@redhat.com> - 13.1-1
- update to 13.1
  - bump apel_minver to 10.7
  - all 3 old patches for 12.2.0 are now upstream
  - use SKK-CFG for install prefixes
- add bcond for xemacs and disable for now since no apel 10.7 for xemacs


* Mon Jun 22 2009 Jens Petersen <petersen@redhat.com> - 12.2.0-13
- fix skk-e21 error with emacs22 (patch from Masatake Yamato, #503185)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 10 2007 Jens Petersen <petersen@redhat.com>
- specify license is GPL 2 or later

* Tue Jan  2 2007 Jens Petersen <petersen@redhat.com> - 12.2.0-11
- fix preun script for upgrades (#219398)
- fix buildroot path in tutorial path
- remove redundant tutorial manual installation

* Wed Dec 20 2006 Jens Petersen <petersen@redhat.com> - 12.2.0-10
- make install-info failsafe (Ville Skyttä, #219398)
- add post and preun requires for install-info
- drop old skk provides

* Wed Sep 27 2006 Jens Petersen <petersen@redhat.com> - 12.2.0-9
- add ddskk-string-to-char-list-201524.patch to use string-to-list instead of
  string-to-char-list for XEmacs 21.5 (Ville Skytta, #201524)

* Fri Aug  4 2006 Jens Petersen <petersen@redhat.com> - 12.2.0-8
- add ddskk-12.2.0-xemacs-21.5-fixup-autoload.patch for autoload generation
  in xemacs 21.5

* Wed Nov 16 2005 Jens Petersen <petersen@redhat.com> - 12.2.0-7
- require and buildrequire apel version 10.6

* Wed Jul 13 2005 Jens Petersen <petersen@redhat.com> - 12.2.0-6
- initial import to Fedora Extras
- bring back the xemacs subpackages

* Wed Feb 23 2005 Elliot Lee <sopwith@redhat.com> 12.2.0-5
- Remove xemacs

* Wed Oct  6 2004 Jens Petersen <petersen@redhat.com> - 12.2.0-4
- drop requirements on emacs/xemacs for -nox users
  (Lars Hupfeldt Nielsen, 134479)

* Wed Sep 22 2004 Jens Petersen <petersen@redhat.com> - 12.2.0-3
- clean up ddskk-init.el

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov  5 2003 Jens Petersen <petersen@redhat.com> - 12.2.0-1
- 12.2.0 release
- ddskk-11.6.0-tmp-file.patch no longer needed

* Mon Jul 28 2003 Jens Petersen <petersen@redhat.com> - 11.6.0-12
- ddskk no longer provides ddskk-el
- don't compress Japanese info files
- install/uninstall info manual in info dir file during post/preun

* Thu Jul 10 2003 Jens Petersen <petersen@redhat.com> - 11.6.0-11
- apply ddskk-11.6.0-tmp-file.patch from debian to fix temp file vulnerability
  CAN-2003-0539 (#98924)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Dec 24 2002 Jens Petersen <petersen@redhat.com> 11.6.0-9
- place xemacs package under datadir
- setup quietly
- use buildroot macro instead of RPM_BUILD_ROOT
- include info files except info dir file
- own mule-packages and down
- update url
- encode spec file in utf-8

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar 11 2002 Jens Petersen <petersen@redhat.com> 21.6.0-6
- provide ddskk-el to make rpmlint happy
- don't buildrequire semi

* Mon Feb 25 2002 Jens Petersen <petersen@redhat.com> 21.6.0-5
- free ride through the build system

* Thu Jan 31 2002 Jens Petersen <petersen@redhat.com> 21.6.0-4
- install in mule-packages not site-packages
- own lisp/skk dir

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 21.6.0-3
- automated rebuild

* Tue Jan 8 2002 Jens Petersen <petersen@redhat.com> 21.6.0-2
- Updated changelog entry below for 21.6.0-1

* Tue Jan 8 2002 Jens Petersen <petersen@redhat.com> 21.6.0-1
- Update to 11.6.0 release
- Make XEmacs package
- Add filevar for iso-8859-1 coding for teg
- Don't need to mkdir site-lisp/ddskk datadir/skk, but need datadir/info

* Wed Aug 29 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.3.20010617-2
- Add semi as a BuildPrereq (#45159)
- s/Copyright/License/
- Don't define a name on top and then use it in the header

* Mon Jun 25 2001 SATO Satoru <ssato@redhat.com> 21.3.20010617-1
- 2001.6.17
- fix the dependency (now we have the apel alone).
- ddskk-el is disused

* Wed Feb 28 2001 SATO Satoru <ssato@redhat.com>
- fix the Group

* Wed Feb 28 2001 SATO Satoru <ssato@redhat.com>
- fix the dependencies: [Build]Requires
- add ddskk-init.el

* Wed Feb 28 2001 SATO Satoru <ssato@redhat.com>
- rebuild to re-import into the tree
- new upstream snapshot

* Thu Dec 28 2000 SATO Satoru <ssato@redhat.com>
- fix SPEC

* Mon Dec 25 2000 SATO Satoru <ssato@redhat.com>
- new upstream (cvs current snapshot)

* Mon Sep 11 2000 Matt Wilson <msw@redhat.com>
- added %%defattr(-,root,root) to the el subpackage

* Wed Sep  6 2000 Satoru Sato <ssato@redhat.com>
- fix SPEC (check dependencies)

* Tue Sep  5 2000 Satoru Sato <ssato@redhat.com>
- Initial release
