%if 0%{?rhel} && 0%{?rhel} <= 7
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e '/^.*\/usr\/lib\/rpm\/brp-python-bytecompile.*$/d')
%endif

Name: btrbk
Version: 0.32.6
Release: 7%{?dist}
Summary: Tool for creating snapshots and remote backups of btrfs sub-volumes
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://digint.ch/btrbk/
Source0: https://digint.ch/download/%{name}/releases/%{name}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: python3-devel
%if 0%{?rhel} && 0%{?rhel} == 7
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif
BuildRequires: perl-generators
BuildRequires: rubygem-asciidoctor
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: make
Requires: btrfs-progs >= 4.12
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: openssh-clients
Requires: pv
Requires: mbuffer
%else
Recommends: openssh-clients
Recommends: pv
Recommends: mbuffer
%endif


%description
Backup tool for btrfs sub-volumes, using a configuration file, allows
creation of backups from multiple sources to multiple destinations,
with ssh and flexible retention policy support (hourly, daily,
weekly, monthly)


%prep
%autosetup


%install
%make_install
rm -rf %{buildroot}/%{_docdir}/%{name}
%if 0%{?rhel} && 0%{?rhel} <= 7
find %{buildroot}%{_datadir}/%{name} -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +
%else
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}
%endif


%post
%systemd_post %{name}.service
%systemd_post %{name}.timer


%preun
%systemd_preun %{name}.service
%systemd_preun %{name}.timer


%postun
%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}.timer


%files
%doc README.md ChangeLog doc/FAQ.md doc/upgrade_to_v0.23.0.md
%license COPYING
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/btrbk.conf.example
%{_unitdir}/%{name}.*
%{_datadir}/%{name}
%{_bindir}/btrbk
%{_bindir}/lsbtr
%{_datadir}/bash-completion/completions/btrbk
%{_datadir}/bash-completion/completions/lsbtr
%{_mandir}/man1/btrbk.1*
%{_mandir}/man1/lsbtr.1*
%{_mandir}/man1/ssh_filter_btrbk.1*
%{_mandir}/man5/btrbk.conf.5*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.32.6-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 30 2023 Juan Orti Alcaine <jortialc@redhat.com> - 0.32.6-1
- Version 0.32.6 (RHBZ#2181762)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0.32.5-1
- Version 0.32.5 (RHBZ#2137114)

* Mon Sep 05 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0.32.4-1
- Version 0.32.4 (RHBZ#2116134)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0.32.2-1
- Version 0.32.2 (#2101120)

* Sun Feb 27 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0.32.1-1
- Version 0.32.1 (#2058899)

* Sun Feb 06 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0.32.0-1
- Version 0.32.0 (#2051020)

* Fri Jan 21 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0.31.3-3
- Restore executable permissions in /usr/share scripts (#2043479)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Juan Orti Alcaine <jortialc@redhat.com> - 0.31.3-1
- Version 0.31.3 (#1765928)
- Remove executable permissions from scripts in /usr/share (#1994989)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Michael Goodwin <xenithorb@fedoraproject.org> - 0.28.3-1
- Update to 0.28.3 (#1692924)
- Update build deps to include `rubygem-asciidoctor`
- Update rumtime deps to include `mbuffer` replacing `pv`

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.27.0-1
- Update to 0.27.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.1-3
- rebuilt

* Mon Mar 26 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.1-2
- Force correct python3 path:
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3#Transition_Steps

* Tue Mar 06 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.1-1
- Update to 0.26.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.0-1
- Update to 0.26.0 (#1501520)
  - Assorted bugfixes
- MIGRATION NEEDED: For raw targets see ChangeLog in docs, or:
   - https://github.com/digint/btrbk/blob/v0.26.0/ChangeLog
- Resume deprecated from "-r" to "replace"

* Mon Jul 31 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.25.1-1
- Update to 0.25.1 (#1476626)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.25.0-4
- Removed perl from Requires, auto-generated
- Removed %%{?systemd_requires}, for scriptlets only

* Wed Jul  5 2017 Mike Goodwin <xenithorb@fedoraproject.org> - 0.25.0-3
- License was GPLv3+ not GPLv3
- Add perl-generators for BuildRequires
- Add -p to all install commands in Makefile and in spec (with sed)
  - Patch submitted upstream: https://github.com/digint/btrbk/pull/164
- Fix if statement for RHEL detection
- Spelling of subvolumes -> sub-volumes to satisfy rpmlint
- Removed %%{?perl_default_filter} macro, unnecessary

* Wed Jul  5 2017 Mike Goodwin <xenithorb@fedoraproject.org> - 0.25.0-2
- Added a more verbose description per the developer
- Changed Source0 to the official source tarball
- Include pv as a weak dependency, as well as openssh-clients
- Add if statement because <= RHEL7 doesn't have Recommends:

* Tue Jul  4 2017 Mike Goodwin <xenithorb@fedoraproject.org> - 0.25.0-1
- Initial packaging
