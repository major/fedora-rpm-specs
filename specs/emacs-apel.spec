%global		pkg		apel
%global		pkgname		APEL
%global		ver	10.8
%global		snap	82eb232
%global		snapver	^1.git%{snap}

Name:		emacs-%{pkg}
Version:	%{ver}%{?snapver}
Release:	0.5%{?dist}
Summary:	A Portable Emacs Library

License:	GPL-2.0-or-later
URL:		https://github.com/wanderlust/apel/tree/apel-wl
# No releases
Source0:	%{pkg}-%{ver}-%{snap}.tar.gz

BuildArch:	noarch
BuildRequires:	emacs
BuildRequires: make
Requires:	emacs(bin) >= %{_emacs_version}
Provides:	apel = %{version}-%{release}
Obsoletes:	apel < 10.8-1
Provides:	emacs-apel-el <= 10.8-8
Obsoletes:	emacs-apel-el <= 10.8-8

Patch0:		APEL-CFG.patch
Patch1:		apel-10.4-missing-el.patch

%description
%{pkgname} (A Portable Emacs Library) is a library to support
to write portable Emacs Lisp programs.

%prep
%autosetup -n %{pkg}-%{ver}-%{snap} -p1

%build


%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LISPDIR=$RPM_BUILD_ROOT%{_emacs_sitelispdir} \
	INSTALL="install -p"  install

%files
%doc README.en ChangeLog.1
%lang(ja) %doc README.ja
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%dir %{_emacs_sitelispdir}/%{pkg}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.8^1.git82eb232-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.8^1.git82eb232-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.8^1.git82eb232-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.8^1.git82eb232-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Akira TAGOH <tagoh@redhat.com> - 10.8^1.git82eb232-0.1
- Rebase to apel-wl from git.
- Fix compile error.
  Resolves: rhbz#2240897

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Akira TAGOH <tagoh@redhat.com> - 10.8-24
- Convert License tag to SPDX.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Akira TAGOH <tagoh@redhat.com> - 10.8-15
- Escape characters in doc.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Tue Jun 23 2015 Akira TAGOH <tagoh@redhat.com> - 10.8-9
- Merge -el sub-package into main (#1234536)
- Borrow some packages from Debian.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Akira TAGOH <tagoh@redhat.com> - 10.8-1
- New upstream release.
- Rename the package to meet the packaging guidelines.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  1 2008 Akira TAGOH <tagoh@redhat.com> - 10.7-2
- Update the spec file.

* Wed Aug  8 2007 Akira TAGOH <tagoh@redhat.com> - 10.7-1
- New upstream release.
- Update License tag.

* Fri Sep 15 2006 Akira TAGOH <tagoh@redhat.com> - 10.6-9
- rebuilt

* Wed Jul 20 2005 Akira TAGOH <tagoh@redhat.com> - 10.6-8.fc5
- Disabled apel-xemacs package to avoid a chicken-egg problem.

* Tue Jul 19 2005 Akira TAGOH <tagoh@redhat.com> - 10.6-7.fc5
- Import into Extras.

* Tue Feb 22 2005 Elliot Lee <sopwith@redhat.com> 10.6-6
- Remove xemacs

* Wed Oct  6 2004 Akira TAGOH <tagoh@redhat.com> - 10.6-5
- require emacs-common instead of emacs.

* Wed Oct  6 2004 Akira TAGOH <tagoh@redhat.com> - 10.6-4
- require xemacs-common instead of xemacs. (#134479)

* Mon Sep 27 2004 Akira TAGOH <tagoh@redhat.com> - 10.6-3
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jul 07 2003 Akira TAGOH <tagoh@redhat.com> 10.6-1
- New upstream release.

* Wed May 14 2003 Akira TAGOH <tagoh@redhat.com> 10.4-4
- apel-10.4-missing-el.patch: contains atype.el and file-detect.el (#90604)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan  3 2003 Jens Petersen <petersen@redhat.com> 10.4-2
- rebuild

* Wed Jan  1 2003 Jens Petersen <petersen@redhat.com> 10.4-1
- update to 10.4
- resurrect -xemacs subpackage, required by latest xemacs package
- install xemacs package under datadir
- own xemacs package lisp dir

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 10.3-8
- rebuild

* Thu Jul 18 2002 Akira TAGOH <tagoh@redhat.com> 10.3-7
- s/Copyright/License/
- add the owned directory.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Feb 24 2002 Tim Powers <timp@redhat.com>
- rebuilt in new environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jun 23 2001 SATO Satoru <ssato@redhat.com>
- apel-xemacs removed because XEmacs already includes it.
- made "emu" modules installed in apel/ subdirectory

* Wed Jun 20 2001 SATO Satoru <ssato@redhat.com>
- initial release (separated from semi)
