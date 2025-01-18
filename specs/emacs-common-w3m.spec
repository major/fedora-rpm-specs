%global	pkg		w3m
%global	pkgname		Emacs-w3m
%global ver		1.4.632
%global	snap		e3b87d61


Name:			emacs-common-%{pkg}
Version:		%{ver}~0.%{snap}
Release:		5%{?dist}
Summary:		W3m interface for Emacsen

# GPLv3+ bookmark-w3m.el
License:		GPL-2.0-or-later AND GPL-3.0-or-later
URL:			http://emacs-w3m.namazu.org/
## No real archives available since this version is a snapshot from CVS.
#Source0:		http://emacs-w3m.namazu.org/emacs-w3m-%%{version}.tar.gz
#
# How to generate tarball:
# 1. cvs -d :pserver:anonymous@cvs.namazu.org:/storage/cvsroot login
# 2. CVS password:[enter]
# 3. cvs -d :pserver:anonymous@cvs.namazu.org:/storage/cvsroot co emacs-w3m
# 4. cd emacs-w3m
# 5. autoconf
# 6. make dist
Source0:		emacs-w3m-%{ver}.tar.gz
Source1:		w3m-init.el

BuildArch:		noarch
BuildRequires:		texinfo texinfo-tex
BuildRequires:		emacs emacs-apel flim
%if 0%{?fedora} < 36
BuildRequires:		xemacs xemacs-packages-extra flim-xemacs
%endif
BuildRequires:		make
Requires:		w3m
Provides:		w3m-el-common = %{version}-%{release}
Obsoletes:		w3m-el-common < 1.4.398
%if 0%{?fedora} >= 36
Obsoletes:		xemacs-%{pkg} < 1.4.631-0.9.20180618cvs
%endif

%description
W3m is a text based World Wide Web browser with IPv6 support. It
features excellent support for tables and frames. It can be used as a
standalone pager such as lv, less, and more.

This package contains the files common to both the GNU Emacs and XEmacs
%{pkgname} packages.

%package		-n emacs-%{pkg}
Summary:		Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:		emacs(bin) >= %{_emacs_version}
Requires:		emacs-common-%{pkg} = %{version}-%{release}
Requires:		emacs-apel flim
Provides:		w3m-el = %{version}-%{release}
Obsoletes:		w3m-el < 1.4.398
Provides:		emacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs
Obsoletes:		emacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs

%description		-n emacs-%{pkg}
This package contains the byte compiled elisp packages to run %{pkgname} with GNU
Emacs.


%if 0%{?fedora} < 36
%package		-n xemacs-%{pkg}
Summary:		Compiled elisp files to run %{pkgname} Under XEmacs
Requires:		xemacs(bin) >= %{_xemacs_version}
Requires:		emacs-common-%{pkg} = %{version}-%{release}
Requires:		xemacs-packages-extra flim-xemacs
Provides:		w3m-el-xemacs = %{version}-%{release}
Obsoletes:		w3m-el-xemacs < 1.4.398
Provides:		xemacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs
Obsoletes:		xemacs-%{pkg}-el <= 1.4.531-0.3.20140421cvs

%description		-n xemacs-%{pkg}
This package contains the byte compiled elisp packages to use %{pkgname} with
XEmacs.
%endif


%prep
%setup -q -n emacs-w3m-%{ver}


%build


%install
install -d $RPM_BUILD_ROOT%{_emacs_sitestartdir}
%if 0%{?fedora} < 36
install -d $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
%endif

#
# for Emacs
#
%configure --with-icondir=\$\(prefix\)/share/pixmaps/emacs-%{pkg}
make %{?_smp_mflags}
make install prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} infodir=$RPM_BUILD_ROOT%{_infodir} INSTALL="/usr/bin/install -p"
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}
make install-icons prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} INSTALL="/usr/bin/install -p"

%if 0%{?fedora} < 36
make distclean

#
# for XEmacs
#
%configure --with-xemacs --with-icondir=\$\(datadir\)/pixmaps/emacs-%{pkg}
make %{?_smp_mflags}
make install-package prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{_datadir} INSTALL="/usr/bin/install -p"
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
%endif

## remove unpackaged files.
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/{ChangeLog,ChangeLog.1,sChangeLog}
%if 0%{?fedora} < 36
rm -rf $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/../{etc,info}
rm -rf $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/{ChangeLog,ChangeLog.1,sChangeLog}
%endif

%files
%doc ChangeLog ChangeLog.1 README
%lang(ja) %doc README.ja
%license COPYING
%{_datadir}/pixmaps/emacs-%{pkg}
%{_infodir}/emacs-w3m*

%files	-n emacs-%{pkg}
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.el.gz
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}

%if 0%{?fedora} < 36
%files	-n xemacs-%{pkg}
%{_xemacs_sitelispdir}/%{pkg}/*.el
%{_xemacs_sitelispdir}/%{pkg}/*.el.gz
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/%{pkg}
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.632~0.e3b87d61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.632~0.e3b87d61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.632~0.e3b87d61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.632~0.e3b87d61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Akira TAGOH <tagoh@redhat.com> - 1.4.632~0.e3b87d61-1
- Rebase to 1.4.632 in git.
  Resolves: rhbz#2249352

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.14.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.13.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Akira TAGOH <tagoh@redhat.com> - 1.4.631-0.12.20180618cvs
- Correct License tag
- Convert License tag to SPDX.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.11.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.10.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 1.4.631-0.9.20180618cvs
- Drop XEmacs support in F36 and later

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.8.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.7.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.6.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.5.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.4.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.3.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.631-0.2.20180618cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Akira TAGOH <tagoh@redhat.com> - 1.4.631-0.1.20180618cvs
- Updates to 1.4.631.
- Remove install-info from scriptlet according to
  https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MP2QVJZBOJZEOQO2G7UB2HLXKXYPF2G5/
- Modernize spec file.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.570-0.3.20170213cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.570-0.2.20170213cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Akira TAGOH <tagoh@redhat.com> - 1.4.570-0.1.20170213cvs
- Updates to 1.4.570.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.531-0.6.20140421cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.531-0.5.20140421cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Akira TAGOH <tagoh@redhat.com> - 1.4.531-0.4.20140421cvs
- Merge -el sub-package into main. (#1234537)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.531-0.3.20140421cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.531-0.2.20140421cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Akira TAGOH <tagoh@redhat.com> - 1.4.531-0.1.20140421cvs
- Updates to 1.4.531 (#1083141)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.435-0.5.20110225cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.435-0.4.20110225cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.435-0.3.20110225cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.435-0.2.20110225cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Akira TAGOH <tagoh@redhat.com> - 1.4.435-0.1.20110225cvs
- Updates to 1.4.435.
- Updates BR to emacs-apel instead of apel.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.398-0.5.20100714cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 12 2010 Michel Salim <salimma@fedoraproject.org> - 1.4.398-0.4.20100714cvs%{?dist}
- Move w3m-load.el to main packages; it does not get byte-compiled

* Tue Jul 27 2010 Akira TAGOH <tagoh@redhat.com> - 1.4.398-0.3.20100714cvs
- use install -p to preserve timestamp.
- Add %%{?_smp_mflags} to make.

* Fri Jul 23 2010 Akira TAGOH <tagoh@redhat.com> - 1.4.398-0.2.20100714cvs
- Add the appropriate Provides and Obsoletes.
- Imrpove the spec file.

* Wed Jul 14 2010 Akira TAGOH <tagoh@redhat.com> - 1.4.398-0.1.20100714cvs
- Updates the snapshot.
- Rename the package to meet current packaging guidelines.

* Thu Nov 19 2009 Akira TAGOH <tagoh@redhat.com> - 1.4.371-0.1.20091119cvs
- updates.

* Wed Aug 19 2009 Akira TAGOH <tagoh@redhat.com> - 1.4.367-0.1.20090819cvs
- Snapshot from CVS to fix #518058.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Akira TAGOH <tagoh@redhat.com> - 1.4.4-7
- Rebuild for gcc-4.3.

* Tue Dec 19 2006 Akira TAGOH <tagoh@redhat.com> - 1.4.4-6
- makes it failsafe to run install-info. (#219408)

* Fri Sep 15 2006 Akira TAGOH <tagoh@redhat.com> - 1.4.4-5
- rebuilt

* Thu May 25 2006 Akira TAGOH <tagoh@redhat.com> - 1.4.4-4
- rebuilt to be correct dist tag.

* Wed May 24 2006 Akira TAGOH <tagoh@redhat.com> - 1.4.4-3
- packaged as noarch. (#192610)

* Thu Mar  2 2006 Akira TAGOH <tagoh@redhat.com> - 1.4.4-2
- rebuilt

* Mon May  9 2005 Akira TAGOH <tagoh@redhat.com> - 1.4.4-1
- Updates to 1.4.4.
- import into Extras.
- get back -xemacs package again.

* Tue Feb 22 2005 Elliot Lee <sopwith@redhat.com> 1.4.3-4
- Remove xemacs

* Thu Feb 10 2005 Akira TAGOH <tagoh@redhat.com> - 1.4.3-3
- rebuilt

* Wed Oct  6 2004 Akira TAGOH <tagoh@redhat.com> - 1.4.3-2
- require emacs-common instead of emacs
- require xemacs-common instead of xemacs

* Wed Aug 18 2004 Akira TAGOH <tagoh@redhat.com> 1.4.3-1
- New upstream release.

* Thu Jul 15 2004 Akira TAGOH <tagoh@redhat.com> 1.4.2-1
- New upstream release.

* Fri Jul 09 2004 Akira TAGOH <tagoh@redhat.com> 1.4.1-1
- New upstream release.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 06 2004 Akira TAGOH <tagoh@redhat.com> 1.4-1
- New upstream release.
- w3m-el-1.3.6-m17n.patch: removed.

* Wed Apr 07 2004 Akira TAGOH <tagoh@redhat.com> 1.3.6-6
- w3m-el-1.3.6-m17n.patch: applied a backport patch from CVS to support w3m-0.5.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Sep 30 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- prereq /sbin/install-info

* Wed Sep 03 2003 Akira TAGOH <tagoh@redhat.com> 1.3.6-3
- removed ExcludeArch: ia64.

* Mon Sep 01 2003 Akira TAGOH <tagoh@redhat.com> 1.3.6-2
- fixed missing fi statement. (#102043)
- moved the elisp location to xemacs-packages
- add ExcludeArch: ia64 to build and close a bug.

* Tue Jul 22 2003 Akira TAGOH <tagoh@redhat.com> 1.3.6-1
- New upstream release.

* Mon Jul 07 2003 Elliot Lee <sopwith@redhat.com> 1.3.5-2
- Don't package /usr/share/info/dir

* Mon Jul 07 2003 Akira TAGOH <tagoh@redhat.com> 1.3.5-1
- New upstream release.

* Fri Jun 20 2003 Akira TAGOH <tagoh@redhat.com> 1.3.4-1
- New upstream release.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 14 2003 Elliot Lee <sopwith@redhat.com> 1.3.3-5
- Remove ExcludeArch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 10 2003 Akira TAGOH <tagoh@redhat.com> 1.3.3-3
- according to xemacs 21.4.11, moved the install path for elisp.
- add ExcludeArch alpha ia64 ppc. right now our xemacs doesn't support these arch.
- w3m-el-1.3.3-libdir.patch: removed.

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.3.3-2
- x86_64 has xemacs now, don't excludearch it
- alpha neither

* Wed Oct 30 2002 Akira TAGOH <tagoh@redhat.com> 1.3.3-1
- New upstream release.
- w3m-el-1.3.3-libdir.patch: add libdir to Makefile.
- exclude x86_64 until provides xemacs.

* Mon Oct 21 2002 Akira TAGOH <tagoh@redhat.com> 1.3.2-1
- New upstream release.
- w3m-el-1.3.1-fixwrongtypearg.patch: removed because it's no longer needed.

* Sat Aug 24 2002 Akira TAGOH <tagoh@redhat.com> 1.3.1-1
- New upstream release. contains more bug fix.
- w3m-el-1.3.1-fixwrongtypearg.patch: applied to fix (wrong-type-argument
  integerp nil) error.

* Tue Jul 09 2002 Akira TAGOH <tagoh@redhat.com> 1.3-1
- New upstream release.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 21 2002 Akira TAGOH <tagoh@redhat.com> 1.2.8-1
- New upstream release.

* Thu Jun 06 2002 Akira TAGOH <tagoh@redhat.com> 1.2.7-1
- New upstream release.

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Mar 12 2002 Akira TAGOH <tagoh@redhat.com> 1.2.6-1
- New upstream release.

* Tue Mar 12 2002 Akira TAGOH <tagoh@redhat.com> 1.2.5-1
- New upstream release.
- w3m-el-common: new package, to separated common files.
- w3m-init.el: add w3m-icon-directory.

* Wed Feb 27 2002 Akira TAGOH <tagoh@redhat.com> 1.2.4-4
- Disable alpha because nothing is xemacs for alpha now.
- Enable ia64.

* Fri Feb 22 2002 Akira TAGOH <tagoh@redhat.com> 1.2.4-3
- Build against new environment.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jan  8 2002 Akira TAGOH <tagoh@redhat.com> 1.2.4-1
- New upstream release.

* Thu Dec  6 2001 Akira TAGOH <tagoh@redhat.com> 1.2.2-1
- New upstream release.

* Tue Nov 13 2001 Akira TAGOH <tagoh@redhat.com> 1.2.1-1
- New upstream release.

* Tue Nov  6 2001 Akira TAGOH <tagoh@redhat.com> 1.2-1
- New upstream release.
- s/Copyright/License/
- Added a package for xemacs
- Added requires: w3m
- Added w3m-init.el
- Added directories owner

* Thu Aug 30 2001 SATO Satoru <ssato@redhat.com> - 1.0-4
- fixed %%files (#51982)
- remove the parts commented

* Sat Jun 23 2001 SATO Satoru <ssato@redhat.com>
- get backed build-dependencies.

* Sat Jun 23 2001 SATO Satoru <ssato@redhat.com>
- build as architecture specific rpm.

* Wed Jun 20 2001 SATO Satoru <ssato@redhat.com>
- Initial release (separated from w3m)
