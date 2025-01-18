Name:           git-tools
Version:        2022.12
Release:        7%{?dist}
Summary:        Assorted git-related scripts and tools

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/MestreLion/%{name}
Source0:        https://github.com/MestreLion/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       git

BuildRequires:  python3-devel

%description
Assorted git-related scripts and tools:

git-branches-rename:
Batch renames branches with a matching prefix to another prefix

git-clone-subset:
Clones a subset of a git repository

git-find-uncommitted-repos:
Recursively list repos with uncommitted changes

git-rebase-theirs:
Resolve rebase conflicts and failed cherry-picks by favoring 'theirs' version

git-restore-mtime:
Restore original modification time of files based on the date of the most
recent commit that modified them

git-strip-merge:
A git-merge wrapper that deletes files on a "foreign" branch before merging

%prep
%setup -q

# https://python-rpm-porting.readthedocs.io/en/latest/applications.html#fixing-shebangs
sed -i.bak '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' git-restore-mtime
touch -r git-restore-mtime.bak git-restore-mtime
rm -f git-restore-mtime.bak

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp -p git-branches-rename %{buildroot}%{_bindir}/.
cp -p git-clone-subset %{buildroot}%{_bindir}/.
cp -p git-find-uncommitted-repos %{buildroot}%{_bindir}/.
cp -p git-rebase-theirs %{buildroot}%{_bindir}/.
cp -p git-restore-mtime %{buildroot}%{_bindir}/.
cp -p git-strip-merge %{buildroot}%{_bindir}/.
mkdir -p %{buildroot}%{_mandir}/man1
cp -p man1/git-* %{buildroot}%{_mandir}/man1/.

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2022.12-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Greg Bailey <gbailey@lxpro.com> - 2022.12-1
- Update to 2022.12 (#2157291)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Greg Bailey <gbailey@lxpro.com> - 2022.07-1
- Update to 2022.07 (#1881117)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Greg Bailey <gbailey@lxpro.com> - 2019.11-1
- New upstream release 2019.11 (#1777999)
- several performance improvements
- use ISO datetime format
- refactor git calls into a convenience class
- improve documentation
- add several TODO and FIXME notes as a roadmap draft
- remove outdated benchmarks

* Mon Nov 18 2019 Greg Bailey <gbailey@lxpro.com> - 2019.10-1
- New upstream release 2019.10 (#1772903)
- Fix python3 incompatibility (#1748462)
- Drop python2 support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Greg Bailey <gbailey@lxpro.com> - 2018.10-1
- New upstream release 2018.10
- Modify python shebang to specify explicit python version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2017.10-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Greg Bailey <gbailey@lxpro.com> - 2017.10-1
- New upstream release 2017.10
- Python 3 compatibility
- Rename the license to a standard name

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20160313gitd6d55b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20160313gitd6d55b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 13 2016 Greg Bailey <gbailey@lxpro.com> - 0-0.2.20160313gitd6d55b3
- New upstream snapshot with GPLv3 license file
- Remove unnecessary cleanup of buildroot
- Only copy and package the scripts that have manpages

* Mon Feb 15 2016 Greg Bailey <gbailey@lxpro.com> - 0-0.1.20160215gitea09519
- Initial package
