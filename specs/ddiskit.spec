# Use the forge macros to simplify packaging.
# See https://fedoraproject.org/wiki/Forge-hosted_projects_packaging_automation
%global forgeurl https://gitlab.com/redhat/centos-stream/src/dup/ddiskit
# When we no longer need to build against a git commit,
# Simply remove the commit variable and update the Version
# Then forge will pick up the release
%global commit 82d44fc79582396cf634f6e1ac4edb06688ea524

Name:           ddiskit
Version:        3.6

%forgemeta

Release:        36%{?dist}
Summary:        Tool for Red Hat Enterprise Linux Driver Update Disk creation

License:        GPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       rpm createrepo
Requires:       /usr/bin/mkisofs
Suggests:       quilt git
Recommends:     kernel-devel redhat-rpm-config rpm-build
Recommends:     mock

%description -n %{name}
Ddiskit is a little framework for simplifying creation of proper
Driver Update Disks (DUD) used for providing new or updated out-of-tree
kernel modules.

%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
# Resource files are bundled as package data in python3_sitelib/ddiskit/
# but also installed to system paths for conventional system-wide use
install -Dpm 0644 src/ddiskit/ddiskit.config \
    %{buildroot}%{_datadir}/ddiskit/ddiskit.config
install -Dpm 0644 src/ddiskit/templates/spec \
    %{buildroot}%{_datadir}/ddiskit/templates/spec
install -pm 0644 src/ddiskit/templates/config \
    %{buildroot}%{_datadir}/ddiskit/templates/config
install -Dpm 0644 src/ddiskit/profiles/default \
    %{buildroot}%{_datadir}/ddiskit/profiles/default
install -pm 0644 src/ddiskit/profiles/rh-testing \
    %{buildroot}%{_datadir}/ddiskit/profiles/rh-testing
install -pm 0644 src/ddiskit/profiles/rh-release \
    %{buildroot}%{_datadir}/ddiskit/profiles/rh-release
install -Dpm 0644 src/ddiskit/keyrings/rh-release/fd431d51.key \
    %{buildroot}%{_datadir}/ddiskit/keyrings/rh-release/fd431d51.key
install -Dpm 0644 src/ddiskit/etc/ddiskit.config \
    %{buildroot}%{_sysconfdir}/ddiskit.config
install -Dpm 0644 ddiskit.1 \
    %{buildroot}%{_mandir}/man1/ddiskit.1
install -Dpm 0644 ddiskit \
    %{buildroot}%{_datadir}/bash-completion/completions/ddiskit
find %{buildroot} -size 0 -delete

%files -n %{name}
%doc README
%license COPYING
%{python3_sitelib}/ddiskit/
%{python3_sitelib}/ddiskit-*.dist-info
%{_bindir}/ddiskit
%{_mandir}/man1/ddiskit.1*
%{_datadir}/bash-completion/completions/ddiskit

%dir %{_datadir}/ddiskit
%dir %{_datadir}/ddiskit/keyrings
%dir %{_datadir}/ddiskit/keyrings/rh-release
%dir %{_datadir}/ddiskit/profiles
%dir %{_datadir}/ddiskit/templates
%{_datadir}/ddiskit/templates/spec
%{_datadir}/ddiskit/templates/config
%{_datadir}/ddiskit/profiles/*
%{_datadir}/ddiskit/keyrings/rh-release/*.key
%{_datadir}/ddiskit/ddiskit.config

%config(noreplace) /etc/ddiskit.config

%check
%pytest

%changelog
* Wed Aug 05 2026 Oleksii Baranov <olebaran@redhat.com> - 3.6-36
- Migrate to pyproject.toml, restructure as proper Python package
- Drop deprecated setup.py and data_files, install data files explicitly
- Bundle resource files as package data for editable/dev installs
- Add GitLab CI pipeline with pytest happy-path tests

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 3.6-34
- Rebuilt for Python 3.15

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 3.6-30
- Rebuilt for Python 3.14

* Thu Feb 06 2025 Eugene Syromiatnikov <esyr@redhat.com> - 3.6-29
- Update to the latest version.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Charalampos Stratakis <cstratak@redhat.com> - 3.6-27
- Remove unused %check section
Resolves: rhbz#2319624

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.6-25
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Eugene Syromiatnikov <esyr@redhat.com> - 3.6-22
- Migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.6-20
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Lumír Balhar <lbalhar@redhat.com> - 3.6-17
- Fix build with new setuptools

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.6-16
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.6-13
- Rebuilt for Python 3.10

* Thu Apr 29 2021 Eugene Syromiatnikov <esyr@redhat.com> - 3.6-12
- Change "Requires: genisoimage" dependency to "Requires: /usr/bin/mkisofs"
  to enable xorriso-provided drop-in replacement implementation usage.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Cestmir Kalina <ckalina@redhat.com> - 3.6-10
- Remove Python 2 relevant chunks
- Fixes #1885256

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6-8
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Zamir SUN <zsun@fedoraproject.org> - 3.6-6.20191129gitde1f684
- Update to Python3 support in de1f6847223085dcdd177e02a7298c835fae12a3
- Fixes RHBZ#1777623

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Petr Oros <poros@redhat.com> - 3.6-1
- New upstream release

* Mon Jun 26 2017 Petr Oros <poros@redhat.com> - 3.5-1
- New upstream release

* Thu Jun 22 2017 Petr Oros <poros@redhat.com> - 3.4-1
- New upstream release

* Mon Apr 24 2017 Petr Oros <poros@redhat.com> - 3.3-1
- New upstream release

* Tue Mar 14 2017 Petr Oros <poros@redhat.com> - 3.2-1
- New upstream release

* Tue Feb 28 2017 Petr Oros <poros@redhat.com> - 3.1-1
- New upstream release

* Mon Feb 13 2017 Petr Oros <poros@redhat.com> - 3.0-2
- Bump version after few important fixes

* Mon Sep 5 2016 Petr Oros <poros@redhat.com> - 3.0-1
- Initial package.
