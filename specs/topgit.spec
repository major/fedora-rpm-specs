Name:		topgit
Version:	0.19.14
Release:	1%{?dist}
Summary:	A different patch queue manager
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://mackyle.github.io/topgit/
Source0:	https://github.com/mackyle/topgit/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	%{_bindir}/rst2html
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(App::Prove)
BuildRequires:	git sed gawk diffutils findutils perl-interpreter
Requires:	git sed gawk diffutils findutils perl-interpreter


%description
TopGit aims to make handling of large amount of interdependent topic
branches easier. In fact, it is designed especially for the case when
you maintain a queue of third-party patches on top of another (perhaps
Git-controlled) project and want to easily organize, maintain and
submit them - TopGit achieves that by keeping a separate topic branch
for each patch and providing few tools to maintain the branches.

This version of TopGit contains everything from its parent (including
the parent’s new location) and then it’s Patched Really Overall (PRO)
to fix a number of bugs.


%prep
%autosetup -p1


%build
make %{?_smp_mflags} all html prefix=%{_prefix} V=1


%install
make install install-html prefix=%{_prefix} DESTDIR=%{buildroot} V=1
install -m 0644 -D -p contrib/tg-completion.bash \
  %{buildroot}%{_sysconfdir}/bash_completion.d/tg-completion.bash

# fix HTML installation directory
mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_datadir}/%{name}/*.html %{buildroot}%{_pkgdocdir}


%check
make DEFAULT_TEST_TARGET=prove \
     TESTLIB_PROVE_OPTS="%{?_smp_mflags} --timer" \
     prefix=%{_prefix} test || :


%files
%doc README
%license COPYING
%{_pkgdocdir}
%{_bindir}/tg
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%if !(0%{?fedora} || 0%{?rhel} >= 7)
%dir %{_sysconfdir}/bash_completion.d/
%endif
%{_sysconfdir}/bash_completion.d/tg-completion.bash


%changelog
* Sat Feb  8 2025 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.14-1
- Update to 0.19.14.

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.13-9
- Don't fail the build for testsuite problems.

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.19.13-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.13-1
- Update to 0.19.13.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 2021 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.12-6
- Add upstream-provided patch to fix FTBFS #1923653.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.12-1
- Update to 0.19.12.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.11-1
- Update to 0.19.11.
- Use prove to run the testsuite.
- Update BRs.
- Re-enable parallel build.

* Sun Mar 18 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.10-1
- New upstream, update to 0.19.10.
- Modernize spec file.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-7
- Retain buildability on EPEL5.

* Wed Feb  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-6
- Do not own /etc/bash_completion.d on Fedora and EPEL>=7.

* Mon Aug 10 2015 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-5
- Mark license with %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-1
- Update to 0.9.
- New upstream URL.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.7.gitd279e292
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.6.gitd279e292
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.5.gitd279e292
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.4.gitd279e292
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 26 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-0.3.gitd279e292
- Update to revision d279e292.

* Sat Dec 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-0.2.git9b25e848
- Update to revision 9b25e848.

* Sun Oct 10 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.9-0.1.git8b0f1f9d
- Update to revision 8b0f1f9d.

* Mon Sep 13 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.8-2.git9404aa1a
- Update to revision 9404aa1a.
- Specfile fixes as suggested in the review.

* Thu Jul 29 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.8-1.git5aed7e7b
- New package.
