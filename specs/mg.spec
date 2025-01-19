Name:          mg
Version:       20240709
Release:       4%{?dist}
Summary:       Tiny Emacs-like editor
License:       LicenseRef-Fedora-Public-Domain
URL:           https://github.com/hboetes/mg
Source0:       https://github.com/hboetes/%{name}/archive/%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel
BuildRequires: libbsd-devel >= 0.7.0

%description
mg is a tiny, mostly public-domain Emacs-like editor included in the base 
OpenBSD system. It is compatible with Emacs because there shouldn't be any 
reason to learn more editor types than Emacs or vi.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{optflags} -lncurses" libdir="%{_libdir}"

%install
rm -rf %{buildroot}
%make_install prefix=%{_prefix} mandir=%{_mandir}

%files
%doc README tutorial
%{_bindir}/mg
%{_mandir}/man1/mg.1.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20240709-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Mark McKinstry <mmckinst@fedoraproject.org> - 20240709-3
- change license to LicenseRef-Fedora-Public-Domain (RHBZ#2328778)

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 20240709-2
- convert license to SPDX

* Mon Aug  5 2024 Mark McKinstry <mmckinst@fedoraproject.org> - 20240709-1
- upgrade to 20240709 (RHBZ#1941656)
- fix some linting

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200723-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Mark McKinstry <mmckinst@fedoraproject.org> - 20200723-1
- upgrade to 20200723 (RHBZ#1860213)

* Wed Jul 22 2020 Tom Stellard <tstellar@redhat.com> - 20200215-2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Thu Mar 26 2020 Mark McKinstry <mmckinst@fedoraproject.org> - 20200215-1
- upgrade to 20200215 (RHBZ#1803396)
- remove _legacy_common_support workaround for https://github.com/hboetes/mg/issues/12

* Thu Jan 30 2020 Mark McKinstry <mmckinst@fedoraproject.org> - 20180927-1
- upgrade to 20180927

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180408-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180408-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180408-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180408-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun  7 2018 Mark McKinstry <mmckinst@umich.edu> - 20180408-1
- upgrade to 20180408

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170828-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Mark McKinstry <mmckinst@umich.edu> - 20170828-1
- upgrade to 20170828 (RHBZ#1486083)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170401-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170401-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr  7 2017 Mark McKinstry <mmckinst@umich.edu> - 20170401-1
- upgrade to 20170401 (RHBZ#1438167)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 15 2016 Mark McKinstry <mmckinst@umich.edu> - 20161005-1
- upgrade to 20161005 (RHBZ#1382190)

* Sun Sep 25 2016 Mark McKinstry <mmckinst@umich.edu> - 20160912-1
- upgrade to 20160912 (RHBZ#1376263)

* Mon Sep  5 2016 Mark McKinstry <mmckinst@umich.edu> - 20160905-2
- remove patch for ncurses5 workaround, upstream fixed at
  https://github.com/hboetes/mg/commit/1af3d28e

* Mon Sep  5 2016 Mark McKinstry <mmckinst@umich.edu> - 20160905-1
- upgrade to 20160905 (RHBZ#1373172)

* Fri Sep  2 2016 Mark McKinstry <mmckinst@umich.edu> - 20160901-2
- patch to work with ncurses 6

* Fri Sep  2 2016 Mark McKinstry <mmckinst@umich.edu> - 20160901-1
- upgrade to 20160901 (RHBZ#1372497)

* Fri Apr 22 2016 Mark McKinstry <mmckinst@umich.edu> - 20160421-1
- upgrade to 20160421 (RHBZ#1329445)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20160118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Mark McKinstry <mmckinst@umich.edu> - 20160118-1
- upgrade to 20160118 (RHBZ#1300117)

* Fri Jan 15 2016 Mark McKinstry <mmckinst@umich.edu> - 20160115-1
- upgrade to 20160115 (RHBZ#1298920)
- remove bsd-only-tcsasoft.patch since upstream (Han Boetes) fixed the problem

* Thu Jan 14 2016 Mark McKinstry <mmckinst@umich.edu> - 20150325-1
- upgrade to 20150325 (RHBZ#1296922)
- add bsd-only-tcsasoft.patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150323-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Mark McKinstry <mmckinst@nexcess.net> - 20150323-1
- upgrade to 20150323 (RHBZ#1204740)

* Wed Mar 18 2015 Mark McKinstry <mmckinst@nexcess.net> - 20150316-1
- upgrade to 20150316 (RHBZ#1202792)
- require libbsd >= 0.7.0 which added the 'reallocarray' function

* Fri Dec  5 2014 Mark McKinstry <mmckinst@nexcess.net> - 20141127-1
- upgrade to 20141127 (RHBZ#1170992)

* Thu Oct 30 2014 Mark McKinstry <mmckinst@nexcess.net> - 20141007-1
- upgrade to 20141007 (RHBZ#1150492)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140414-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 Mark McKinstry <mmckinst@nexcess.net> - 20140414-1
- upgrade to 20140414 (RHBZ#1010897)
- add libbsd-devel as a requirement

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110905-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110905-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110905-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110905-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110905-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 08 2011 Mark McKinstry <mmckinst@nexcess.net> - 20110905-1
- upgrade to version 20110905

* Wed Mar 02 2011 Mark McKinstry <mmckinst@nexcess.net> - 20110120-1
- upgrade to version 20110120

* Wed Oct 6 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-6
- update Source0 line to use macros

* Tue Oct 5 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-4
- add libdir to build
- update license

* Sat May 8 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-3
- switch to one style of RPM macros
- include LDFLAGS

* Wed Apr 28 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-2
- update license
- apply patch from Terje Rosten to preserve timstamps on man page, handle
  changes in compression of man pages more robustly, include CFLAGS, and include
  debug info

* Tue Apr 27 2010 Mark McKinstry <mmckinst@nexcess.net> - 20090107-1
- initial build
