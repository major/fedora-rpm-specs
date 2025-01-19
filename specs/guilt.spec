Name:		guilt
Version:	0.36
Release:	24%{?dist}
Summary:	Scripts to manage quilt-like patches on top of git

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://repo.or.cz/guilt.git
Source:		%{name}-%{version}.tar.gz
Requires:	git, gawk, sed, bash

BuildArch:	noarch
BuildRequires:	asciidoc, xmlto, git-core
BuildRequires: make

Patch0:		guilt-0.36-git-decorate.patch
Patch1:		guilt-0.36-filter-dd.patch
Patch2:		guilt-0.36-fix-regressions-newer-git.patch
Patch3:		guilt-0.36-fix-portability-problem-with-using-find-perm-111.patch

%description
Guilt allows one to use quilt functionality on top of a Git repository.
Changes are maintained as patches which are committed into Git.  Commits can
be removed or reordered, and the underlying patch can be refreshed based on
changes made in the working directory. The patch directory can also be
placed under revision control, so you can have a separate history of changes
made to your patches.

%prep
%autosetup -p1

%build
make ASCIIDOC='asciidoc --unsafe' %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/usr
make install-doc PREFIX=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/usr/share/man

%check
make test

%files
%doc COPYING Documentation/HOWTO Documentation/Contributing Documentation/Features
%{_bindir}/guilt
%{_prefix}/lib/*
%{_mandir}/man1/guilt*.1*
%{_mandir}/man7/guilt*.7*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.36-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 08 2023 Eric Sandeen <sandeen@redhat.com> - 0.36-18
- fix portability problem with using find -perm +111

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018  Eric Sandeen <sandeen@redhat.com> - 0.36-7
- Fix regression tests for newer git versions
- Update URL for proper git repo

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 15 2016 Eric Sandeen <sandeen@redhat.com> 0.36-3
- Fix up dd filter in regression tests

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 28 2015 Eric Sandeen <sandeen@redhat.com> 0.36-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Eric Sandeen <sandeen@redhat.com> 0.35-10
- Drop git version check altogether, per upstream

* Thu May 08 2014 Eric Sandeen <sandeen@redhat.com> 0.35-9
- Allow use with git v1.9

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Eric Sandeen <sandeen@redhat.com> 0.35-6
- Conflict with next major version of git, not minor versions past 1.8

* Thu Dec 20 2012 Eric Sandeen <sandeen@redhat.com> 0.35-5
- Allow guilt to work w/ git 1.8 (#887245)

* Fri Aug 03 2012 Eric Sandeen <sandeen@redhat.com> 0.35-4
- Work around regression tests failures due to git change w.r.t. empty patches

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Eric Sandeen <sandeen@redhat.com> 0.35-1
- New upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 21 2010 Eric Sandeen <sandeen@redhat.com> 0.34-1
- New upstream version

* Fri Apr 16 2010 Eric Sandeen <sandeen@redhat.com> 0.33-1
- New upstream version

* Thu Jan 14 2010 Eric Sandeen <sandeen@redhat.com> 0.32.2-1
- New upstream version

* Sat Jul 11 2009 Eric Sandeen <sandeen@redhat.com> 0.32.1-2
- Fix asciidoc call so it works.

* Sat Jul 11 2009 Eric Sandeen <sandeen@redhat.com> 0.32.1-1
- New upstream version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Eric Sandeen <sandeen@redhat.com> 0.32-2
- New upstream version, supports newer git (1.6)
- Fix minor regression test problem

* Tue Jun 03 2008 Eric Sandeen <sandeen@redhat.com> 0.30-2
- Fix regression test output for new versions of git (#440169)

* Fri Apr 11 2008 Eric Sandeen <sandeen@redhat.com> 0.30-1
- New upstream version

* Mon Apr 07 2008 Eric Sandeen <sandeen@redhat.com> 0.29-1
- Initial build
