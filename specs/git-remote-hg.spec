%global debug_package %{nil}
Name:           git-remote-hg
Version:        1.0.4
Release:        5%{?dist}
BuildArch:      noarch
Summary:        Mercurial wrapper for git
License:        GPL-2.0-or-later
URL:            https://github.com/mnauw/git-remote-hg
Source0:        https://github.com/mnauw/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc >= 8.4.1
BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  mercurial >= 5.4
Requires:       python3
Requires:       git-core >= 2.0.0
Requires:       mercurial >= 5.4

%description
git-remote-hg is the semi-official Mercurial bridge from Git project.
Once installed, it allows you to clone, fetch and push to and from Mercurial
repositories as if they were Git ones.

%prep
%autosetup
sed -i -e "1 s|^#!.*|#!%{__python3}|" git-remote-hg
sed -i -e 's|\tinstall|\tinstall -p|' Makefile

%build
make doc

%check
#make test

%install
export HOME=%{_prefix}
export DESTDIR=%{buildroot}
export PYTHON=%{python3}
make install
make install-doc

%files
%doc LICENSE
%{_bindir}/git-remote-hg
%{_bindir}/git-hg-helper
%{_mandir}/man1/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Ondřej Pohořelský <opohorel@redhat.com> - 1.0.4-1
- update to 1.0.4
- spdx license update

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Ondřej Pohořelský <opohorel@redhat.com> - 1.0.2.1-7
- Dropped %%{py3_dist mercurial} require
- Removed unused patch
- Use autosetup
- Drop git-hg obsolete
- Resolves: rhbz#2072627

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Nils Philippsen <nils@tiptoe.de> - 1.0.2.1-3
- use macro for Python dependency

* Tue Dec 01 2020 Todd Zullinger <tmz@pobox.com> - 1.0.2.1-2
- require git-core rather than git to reduce dependencies

* Tue Dec 01 2020 Petr Stodulka <pstodulk@redhat.com> - 1.0.2.1-1
- Rebase to 1.0.2.1
- Transfer to Python3
- Requires Mercurial v5.4+ for Python3 (mercurial-py3)
- Resolves: rhbz#1738965, rhbz#1893525

* Tue Dec 01 2020 Petr Stodulka <pstodulk@redhat.com> - 1.0.0-7
- Apply url encoding for additional refname sanitizing
- Resolves: #1893525

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Petr Stodulka <pstodulk@redhat.com> - 1.0.0-4
- drop build dependency on hg-git which is here by mistake since the start

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Dan Horák <dan[at]danny.cz> - 1.0.0-1
- Rebase to 1.0.0

* Mon Aug 20 2018 Petr Stodulka <pstodulk@redhat.com> - 0.4-1
- Rebase to v0.4
- Compatible with Mercurial v4.6
- Remove patches applied in upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Tomas Korbar <tomas.korb@seznam.cz> - 0.3-8
- Add patches to fix known issues

* Sat Apr 28 2018 Tomas Korbar <tomas.korb@seznam.cz> - 0.3-7
- Change upstream to mnauws fork

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Petr Stodulka <pstodulk@redhat.com> - 0.3-2
- Fix incompatibility with mercurial 4.0

* Wed May 25 2016 Petr Stodulka <pstodulk@redhat.com> - 0.3-1
- Rebase to v0.3
- remove patches applied in upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Petr Stodulka <pstodulk@redhat.com> - 0.2-7
- Mercurial v3.5 has changed API - function context.memfilectx
  requires object repo as first parameter (#1265115)
- changed requires to mercurial >= 3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Adam Williamson <awilliam@redhat.com> - 0.2-5
- backport an upstream PR to make it work with Mercurial 3.2

* Mon Dec 8 2014 Petr Stodulka <pstodulk@redhat.com> - 0.2-4
- added obsoletes of git-hg

* Mon Jun 23 2014 Ondrej Oprala <ooprala@redhat.com> - 0.2-3
- Explicitly disable debug_package, (noarch by itself
  still runs find-debuginfo.sh)

* Sun Jun 22 2014 Ondrej Oprala <ooprala@redhat.com> - 0.2-2
- Every single test fails(suspicious), disabling them for now

* Thu Jun 19 2014 Ondrej Oprala <ooprala@redhat.com> - 0.2-1
- initial git-remote-hg spec file
