%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.4.3}
%global dnf_plugins_extra_obsolete 2.0.0
%global rpmconf_lowest_compatible 1.1.3

%undefine __cmake_in_source_build

Name:           dnf-plugins-extras
Version:        4.1.2
Release:        4%{?dist}
Summary:        Extras Plugins for DNF
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-packaging

%description
Extras Plugins for DNF.

%package -n python3-%{name}-common
Summary:        Common files for Extras Plugins for DNF
Requires:       python3-dnf >= %{dnf_lowest_compatible}
%{?python_provide:%python_provide python3-%{name}-common}
Provides:       %{name}-common = %{version}-%{release}
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      python3-%{name}-common < %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
Obsoletes:      %{name}-common-data < %{version}-%{release}

%description -n python3-%{name}-common
Common files for Extras Plugins for DNF.

%package -n python3-dnf-plugin-kickstart
Summary:        Kickstart Plugin for DNF
Requires:       python3-%{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-kickstart}
BuildRequires:  python3-kickstart
Requires:       python3-kickstart
Provides:       dnf-command(kickstart)
Provides:       %{name}-kickstart = %{version}-%{release}
Provides:       dnf-plugin-kickstart = %{version}-%{release}
Provides:       python3-%{name}-kickstart = %{version}-%{release}
Conflicts:      python2-dnf-plugin-kickstart < %{version}-%{release}
Obsoletes:      python3-%{name}-kickstart < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-kickstart
Kickstart Plugin for DNF, Python 3 version. Install packages listed in a
Kickstart file.

%package -n python3-dnf-plugin-rpmconf
Summary:        RpmConf Plugin for DNF
BuildRequires:  python3-rpmconf >= %{rpmconf_lowest_compatible}
Requires:       python3-%{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-rpmconf}
Requires:       python3-rpmconf >= %{rpmconf_lowest_compatible}
Provides:       %{name}-rpmconf = %{version}-%{release}
Provides:       dnf-plugin-rpmconf = %{version}-%{release}
Provides:       python3-%{name}-rpmconf = %{version}-%{release}
Obsoletes:      python3-%{name}-rpmconf < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-rpmconf
RpmConf Plugin for DNF, Python 3 version. Handles .rpmnew, .rpmsave every
transaction.

%package -n python3-dnf-plugin-snapper
Summary:        Snapper Plugin for DNF
Requires:       python3-%{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-snapper}
Requires:       python3-dbus
Requires:       snapper
Provides:       %{name}-snapper = %{version}-%{release}
Provides:       dnf-plugin-snapper = %{version}-%{release}
Provides:       python3-%{name}-snapper = %{version}-%{release}
Conflicts:      python2-dnf-plugin-snapper < %{version}-%{release}
Obsoletes:      python3-%{name}-snapper < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-snapper
Snapper Plugin for DNF, Python 3 version. Creates snapshot every transaction.

%package -n python3-dnf-plugin-tracer
Summary:        Tracer Plugin for DNF
Requires:       python3-%{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-tracer}
Requires:       python3-tracer >= 0.6.12
Provides:       dnf-plugin-tracer = %{version}-%{release}
Provides:       %{name}-tracer = %{version}-%{release}
Provides:       python3-%{name}-tracer = %{version}-%{release}
Conflicts:      python2-dnf-plugin-tracer < %{version}-%{release}
Obsoletes:      python3-%{name}-tracer < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-tracer
Tracer Plugin for DNF, Python 3 version. Finds outdated running applications in
your system every transaction.

%package -n python3-dnf-plugin-torproxy
Summary:        Tor Proxy Plugin for DNF
Requires:       python3-%{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-torproxy}
Requires:       python3-pycurl
Provides:       dnf-plugin-torproxy = %{version}-%{release}
Provides:       %{name}-torproxy = %{version}-%{release}
Provides:       python3-%{name}-torproxy = %{version}-%{release}
Obsoletes:      python3-%{name}-torproxy < %{dnf_plugins_extra_obsolete}

%description -n python3-dnf-plugin-torproxy
Tor proxy plugin forces DNF to use Tor to download packages. It makes sure that
Tor is working and avoids leaking the hostname by using the proper SOCKS5 interface.

%package -n python3-dnf-plugin-showvars
Summary:        showvars Plugin for DNF
Requires:       python3-%{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-showvars}
Provides:       dnf-plugin-showvars = %{version}-%{release}
Provides:       python3-%{name}-showvars = %{version}-%{release}

%description -n python3-dnf-plugin-showvars
This plugin dumps the current value of any defined DNF variables.  For example
$releasever and $basearch.


%prep
%autosetup -p1

%build
  %cmake -DPYTHON_DESIRED:FILEPATH=%{__python3}
  %cmake_build
  %cmake_build --target doc-man

%install
  %cmake_install

%find_lang %{name}

%check
%pytest

%files -n python3-%{name}-common -f %{name}.lang
%{python3_sitelib}/dnfpluginsextras/
%dir %{python3_sitelib}/dnf-plugins/__pycache__/
%license COPYING
%doc AUTHORS README.rst

%files -n python3-dnf-plugin-kickstart
%{python3_sitelib}/dnf-plugins/kickstart.*
%{python3_sitelib}/dnf-plugins/__pycache__/kickstart.*
%{_mandir}/man8/dnf-kickstart.*

%files -n python3-dnf-plugin-rpmconf
%config(noreplace) %{_sysconfdir}/dnf/plugins/rpmconf.conf
%{python3_sitelib}/dnf-plugins/rpm_conf.*
%{python3_sitelib}/dnf-plugins/__pycache__/rpm_conf.*
%{_mandir}/man8/dnf-rpmconf.*

%files -n python3-dnf-plugin-snapper
%config(noreplace) %{_sysconfdir}/dnf/plugins/snapper.conf
%{python3_sitelib}/dnf-plugins/snapper.*
%{python3_sitelib}/dnf-plugins/__pycache__/snapper.*
%{_mandir}/man8/dnf-snapper.*

%files -n python3-dnf-plugin-tracer
%{python3_sitelib}/dnf-plugins/tracer.*
%{python3_sitelib}/dnf-plugins/__pycache__/tracer.*
%{_mandir}/man8/dnf-tracer.*

%files -n python3-dnf-plugin-torproxy
%config(noreplace) %{_sysconfdir}/dnf/plugins/torproxy.conf
%{python3_sitelib}/dnf-plugins/torproxy.*
%{python3_sitelib}/dnf-plugins/__pycache__/torproxy.*
%{_mandir}/man8/dnf-torproxy.*

%files -n python3-dnf-plugin-showvars
%{python3_sitelib}/dnf-plugins/showvars.*
%{python3_sitelib}/dnf-plugins/__pycache__/showvars.*
%{_mandir}/man8/dnf-showvars.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.1.2-2
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Jan Kolarik <jkolarik@redhat.com> - 4.1.2-1
- Update to 4.1.2
- snapper: Add support for specifying snapper config name (RhBug:2089544)
- rpmconf: Implement unattended config option

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Jan Kolarik <jkolarik@redhat.com> - 4.1.1-1
- Update to 4.1.1
- Translations update

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.12
- Fixes: rhbz#2219977

* Wed Apr 05 2023 Jan Kolarik <jkolarik@redhat.com> - 4.1.0-1
- Update to 4.1.0
- Move system-upgrade plugin to core (RhBug:2054235)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 09 2022 Jaroslav Rohel <jrohel@redhat.com> - 4.0.17-1
- Update to 4.0.17
- Translations update

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 4.0.16-2
- Rebuilt for Python 3.11

* Mon Mar 14 2022 Pavla Kratochvilova <pkratoch@redhat.com> - 4.0.16-1
- Fix cleaning up destdir after system-upgrade (RhBug:2024430)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Pavla Kratochvilova <pkratoch@redhat.com> - 4.0.15-1
- Update to 4.0.15
- Add symlink for man pages of offline-upgrade and offline-distrosync commands (RhBug:1917378)
- system-upgrade: Handle empty transaction on download (RhBug:1917639)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.13-5
- Rebuilt for Python 3.10

* Tue Feb  2 2021 Matthew Miller <mattdm@fedoraproject.org> - 4.0.13-4
- add Provides for offline-upgrade and offline-distrosync commands

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Nicola Sella <nsella@redhat.com> - 4.0.13-2
- Set minimun dnf version to 4.4.3

* Mon Nov 23 2020 Nicola Sella <nsella@redhat.com> - 4.0.13-1
- Update to 4.0.13
- system-upgrade: Use Transaction Store/Replay
- system-upgrade: Pretty-print the state json

* Thu Oct 08 2020 Nicola Sella <nsella@redhat.com> 4.0.12-1
- Update Cmake to pull translations from weblate
- Drop Python 2 support
- README: Add Installation, Contribution, etc
- Add the DNF_SYSTEM_UPGRADE_NO_REBOOT env variable to control system-upgrade reboot.
- [system-upgrade] Upgrade groups and environments (RhBug:1845562,1860408)

* Wed Aug 12 2020 Nicola Sella <nsella@redhat.com> - 4.0.10-5
- spec: Fix building with new cmake macros
- Drop python 2 support

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.10-2
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Ales Matej <amatej@redhat.com> - 4.0.10-1
- Update to 4.0.10
- Ensure plymouth progressbar is filled up only once (RhBug:1809096)

* Mon Feb 24 2020 Ales Matej <amatej@redhat.com> - 4.0.9-2
- [doc] move manpages for plugins to "dnf-PLUGIN" (RhBug:1706386)
- Add offline-upgrade and offline-distrosync commands
- [doc] Add description for new offline command
- Store reason for system-upgrade plugin
- Do not show Operation aborted as an error (RhBug:1797427)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 4.0.8-1
- Update to 4.0.8
- Set clean_requirements_on_remove=False during remove (RhBug:1764169)

* Tue Oct 15 2019 Ales Matej <amatej@redhat.com> - 4.0.7-1
- Fix kickstart plugin

* Mon Oct 14 2019 Ales Matej <amatej@redhat.com> - 4.0.6-1
- [system-upgrade] Use --system-upgrade plymouth mode (RhBug:1681584)
- [system-upgrade] Fix traceback caused by setting gpgcheck options (RhBug:1751103,1746346)
- Fix kickstart plugin (RhBug:1649093)
- [system-upgrade] Ensure identical transaction in download and update steps (RhBug:1758588)
- [system-upgrade] Provide distro specific url for help with system-upgrade

* Fri Sep 27 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 4.0.5-3
- Backport patch to fix traceback in system-upgrade (RhBug:1751103,1746346)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.5-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 4.0.5-1
- Update to 4.0.5
- [system-upgrade] Save gpgcheck and repo_gpgcheck repo options (RhBug:1693677)
- Add showvars plugin for showing what DNF vars are set for the dnf runtime

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 4.0.4-1
- Update to 4.0.4
- Use improved config parser that preserves order of data
- [system-upgrade] Save module_platform_id option through system upgrade (RhBug:1656509)
- [system-upgrade] On modular systems, system upgrade requires the next module_platform_id

* Wed Feb 13 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 4.0.2-1
- Update to 4.0.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Jaroslav Mracek <jmracek@redhat.com> - 4.0.1-1
- Update to 4.0.1

* Thu Nov 22 2018 Jaroslav Mracek <jmracek@redhat.com> - 4.0.0-1
- Update to 4.0.0

* Fri Nov 09 2018 Adam Williamson <awilliam@redhat.com> - 3.0.1-2
- Backport fixes for two significant bugs from master

* Mon Jul 23 2018 Marek Blaha <mblaha@redhat.com> - 3.0.1-1
- Update to 3.0.1
- Resolves: rhbz#1603806

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jaroslav Mracek <jmracek@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Jaroslav Mracek <jmracek@redhat.com> - 3.0.0-1
- Update to 3.0.0
- Resolves: rhbz#1531356
- Resolves: rhbz#1513823

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.5-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Dec 14 2017 Jaroslav Mracek <jmracek@redhat.com> - 2.0.5-1
- Update to 2.0.5
- Resolves: rhbz#1519543 -  Fedora 27 offline updates (gnome-software intitiated) are failing

* Thu Nov 23 2017 Jaroslav Mracek <jmracek@redhat.com> - 2.0.4-1
- Update to 2.0.4
- Resolves: rhbz#1499284 - dnf crashes with CalledProcessError during upgrade F26->F27
- Resolves: rhbz#1516234 - Upgrade is not possible if a kernel from rawhide has been used in the system

* Mon Oct 02 2017 Jaroslav Mracek <jmracek@redhat.com> - 2.0.3-1
- Update to 2.0.3
- Resolves: rhbz#1473933 - [abrt] dnf-automatic: resolved(): rpm_conf.py:58:resolved:AttributeError: 'Rpmconf' object has no attribute '_interactive'
- Resolves: rhbz#1473435 - [abrt] dnf: subprocess.py:271:check_call:subprocess.CalledProcessError: Command '['journalctl', '--boot', 'd5318db518e541fcbc8ce51dd469c2f0']' returned non-zero exit status -13
- Resolves: rhbz#1490832 - dnf system-upgrade: dnf.exceptions.MarkingError: no package matched
- Resolves: rhbz#1492036 - system-upgrade fails to connect to online mirrors during upgrade when caches are missing

* Mon Aug 07 2017 Jaroslav Mracek <jmracek@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Jaroslav Mracek <jmracek@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Tue May 02 2017 Jaroslav Mracek <jmracek@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Fri Feb 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-0.4rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.10.0-0.3rc1
- Rebuild for Python 3.6

* Mon Nov 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10.0-0.2rc1
- Add obsoletes for main package (RHBZ #1399863)

* Mon Nov 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10.0-0.1rc1
- 0.10.0-rc1
- Adapt to python packaging guidelines

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.0.12-3
- Apply leaves speedups and test suite fixes from upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> 0.0.12-1
- relnotes: 0.0.1[12] (Igor Gnatenko)
- spec: python2_sitelib (Igor Gnatenko)
- spec: nosetests fixup (Igor Gnatenko)
- spec: python3 sourcedir (Igor Gnatenko)
- spec: drop hooks for f21 (Igor Gnatenko)
- spec: python2-nose (Igor Gnatenko)
- local: use _dnf_local as name (RhBug:1237237) (Igor Gnatenko)
- spec: use %%license macro (Igor Gnatenko)
- spec: move mans to one package (RhBug:1210002) (Igor Gnatenko)
- po: update from zanata (Igor Gnatenko)
- po: fix message text (Igor Gnatenko)
- usage of dnf.i18n.translation (Igor Gnatenko)
- local: do not rebuild the repo unnecessarily. (Quy Tonthat)
- local: fixed crashing when installing from rpm files (localinstall). (Quy
  Tonthat)
- local: Fixed a crashing bug with python3. (Quy Tonthat)
- pull translations (Igor Gnatenko)
- versionlock: add missing import (Alon Bar-Lev)
- add Catalan (Robert Antoni Buj Gelonch)
- add zanata.xml (Robert Antoni Buj Gelonch)

* Tue Oct 13 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> 0.0.11-1
- spec: kickstart conflicts with previous version of plugins core (Jan Silhan)

* Mon Oct 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> 0.0.10-1
- Add BaseCliStub() class to tests/support.py (Neal Gompa (ニール・ゴンパ))
- Disable kickstart plugin for Python 3 (Neal Gompa (ニール・ゴンパ))
- Add kickstart plugin to extra plugins (Neal Gompa (ニール・ゴンパ))
- Add repoclosure --check option (Paul Howarth)
- leaves: fix depth-first search (Emil Renner Berthing)
- snapper: set cleanup type to avoid snapshots accumulating indefinitely
  (RhBug:1263699) (Daniel Miranda)
- snapper: don't run if nothing in transaction (Igor Gnatenko)
- spec: adapt to dnf-1.1.2 packaging in F23 (Jan Silhan)
- tracer: don't run tracer when nothing to do; Fix FrostyX/tracer#38 (Jakub
  Kadlčík)
- migrate: groups: skips not found group (RhBug:1225894) (Jan Silhan)

* Tue Jun 30 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> 0.0.9-1
- repomanage: specify that keep is int (RhBug:1230503) (Igor Gnatenko)
- migrate: hide stderr of yum (RhBug:1225282) (Jan Silhan)
- migrate: don't throw error when yum execution failed (Jan Silhan)
- migrate: stop yum from crushing by setting skip_if_unavailable=1
  (RhBug:1226607) (Jan Silhan)
- implemented package (version)locking (Michael Mraka)
- Initial DNF port of the yum show-leaves plugin (Ville Skyttä)

* Fri May 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> 0.0.8-1
- migrate: use Unicodes when migrating YUMDB (RhBug:1223034) (Radek Holy)
- migrate: don't raise error when no groups installed by yum (RhBug:1214807)
  (Jan Silhan)
- migrate: use of LANG C env in yum output (Jan Silhan)
- packaging: allow DNF 1.x.x (Radek Holy)
- packaging: add createrepo_c to requires (RhBug:1211596) (Igor Gnatenko)
- local: drop hook to keep packages cache (Igor Gnatenko)
- packaging: dnf version upper boundaries (Jan Silhan)
- packaging: added plugin command provides (Related:RhBug:1208773) (Jan Silhan)

* Tue Apr 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> 0.0.7-1
- doc: release notes 0.0.7 (Igor Gnatenko)
- packaging: fix orphans for leaves subpkg (Igor Gnatenko)
- po: update translations (Igor Gnatenko)
- plugins: rename --repoid to --repo (Michael Mraka)
- tracer: decode subprocess output explicitly from utf8 (Jakub Kadlčík)
- migrate: initialize cursor before commit (Michael Mraka)
- po: update translations (Igor Gnatenko)
- packaging: remove main package which requires others (Igor Gnatenko)
- packaging: fix url for new releases (Igor Gnatenko)
- migrate: do not convert group types (Jan Silhan)
- packaging: migrate requires python-dnf (Jan Silhan)
- migrate: trans_end record may not exist (RhBug:1209043) (Michael Mraka)
- plugins: rename orphans to leaves (RhBug:1209864) (Igor Gnatenko)
- Initialized to use tito. (Igor Gnatenko)
- local: fix crashing if plugin disabled in main section (RhBug:1208614) (Igor Gnatenko)

* Tue Mar 31 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.6-2
- migrate: set LANG env to C in system calls (Jan Silhan)
- migrate: added logging to history and groups process (Jan Silhan)
- doc: migrate: changed arguments to dnf migrate [all|groups|history|yumdb] (Radek Holy)
- migrate: added YUMDB support (Radek Holy)
- migrate: added groups support (Jan Silhan)

* Tue Mar 31 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.6-1
- doc: include orphans plugin to index (Igor Gnatenko)
- po: update translations (Igor Gnatenko)
- plugins: add migrate plugin (Michael Mraka)
- orphans: use Kosaraju's algorithm (Emil Renner Berthing)
- plugins: add orphans plugin (Emil Renner Berthing)
- tracer: don't print 'nothing to restart' when traceback occurs (RhBug:1201471) (Jakub Kadlčík)

* Mon Mar 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.5-4
- packaging: properly obsolete common subpkg for f23+ (Igor Gnatenko)

* Fri Feb 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.5-3
- packaging: add real package python-dnf-plugins-extras (Igor Gnatenko)

* Fri Feb 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.5-2
- packaging: handle tracer and snapper plugins (Igor Gnatenko)

* Fri Feb 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.5-1
- po: update translations (Igor Gnatenko)
- packaging: adapt to dnf 0.6.4-2 package split (Jan Silhan)
- plugins: add debug plugin (Michael Mraka)
- tracer: fix printing binary on py3 (RhBug:1192779) (Igor Gnatenko)
- tracer: define installed, erased vars (RhBug:1187763) (Igor Gnatenko)

* Fri Feb 13 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.4-1
- packaging: require rpmconf plugin only for f22+ (Igor Gnatenko)
- build: simple script to build test package (Michael Mraka)
- build: more standard way to find out latest commit (Michael Mraka)
- packaging: let gitrev be specified on rpmbuild commandline (Michael Mraka)
- doc: include man pages (Igor Gnatenko)

* Thu Jan 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.3-1
- po: update translations (Igor Gnatenko)
- packaging: include rpmconf plugin only for F22+ (Igor Gnatenko)
- trivial: drop note about bug (Igor Gnatenko)
- local: prefer verbose option on quiet (Igor Gnatenko)
- local: simplidy parsing code (Igor Gnatenko)
- local: fix output from spawning createrepo (Igor Gnatenko)
- doc: improve documentation for local plugin (Igor Gnatenko)
- repoclosure: store requirements as is (Igor Gnatenko)
- repoclosure: optimize performance and memory usage (Igor Gnatenko)
- build: distribute forgotten files (Igor Gnatenko)
- po: update translations (Igor Gnatenko)
- plugins: add repoclosure plugin (Igor Gnatenko)
- packaging: fix files for common subpkg after one of merges (Igor Gnatenko)
- local: use createrepo_c instead of createrepo (Igor Gnatenko)
- plugins: add local plugin (RhBug:991014) (Igor Gnatenko)
- repograph: set decimal places to 12 for colors (Igor Gnatenko)
- tests: fix indentation in repograph (Igor Gnatenko)
- plugins: add repograph plugin (Igor Gnatenko)
- repomanage: replace dnfpluginscore with dnfpluginsextras (Igor Gnatenko)
- plugins: fix typo in if/else (Igor Gnatenko)
- doc: add note that --new by default for repomanage (Igor Gnatenko)
- snapper: don't make snapshots if user removing snapper (RhBug:1177631) (Igor Gnatenko)
- tests: add tests for repomanage (Igor Gnatenko)
- tests: add initial framework (Igor Gnatenko)
- repomanage: use native pkg.location without path join (Igor Gnatenko)
- packaging: obsolete and provide dnf-plugin-tracer correctly (Igor Gnatenko)

* Sun Jan 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.2-1
- po: update translations (Igor Gnatenko)
- Revert "rename rpm_conf to rpmconf" (Igor Gnatenko)
- po: update translations (Igor Gnatenko)
- packaging: update descriptions with tracer plugin (Igor Gnatenko)
- plugins: add repomanage plugin (RhBug:1048541) (Igor Gnatenko)
- Don't run tracer if --installroot is set; Fix FrostyX/tracer#15 (Jakub Kadlčík)
- po: update translations (Igor Gnatenko)
- packaging: obsolete dnf-plugin-tracer by dnf-plugins-extras-tracer (Igor Gnatenko)
- doc: include rpmconf to index (Igor Gnatenko)
- packaging: add tracer plugin to distribute (Igor Gnatenko)
- plugins: tracer plugin (Jakub Kadlčík)
- packaging: include rpmconf as Requires for main package (Igor Gnatenko)
- rpmconf: fix super-init-not-called (Igor Gnatenko)
- po: update translations (Igor Gnatenko)
- packaging: archive script the same as in dnf (Igor Gnatenko)
- rename rpm_conf to rpmconf (Igor Gnatenko)
- Add rpmconf plugin (Igor Gnatenko)
- snapper: set description snapshot as command line (Igor Gnatenko)
- packaging: fix requires and email (Igor Gnatenko)
- snapper: change log level for debug stage to debug (Igor Gnatenko)
- snapper: don't do any with snapper config (Igor Gnatenko)
- packaging: split into subpackages (Igor Gnatenko)
- packaging: handle all python files (Igor Gnatenko)
- transifex update (Igor Gnatenko)

* Wed Dec 17 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-2
- Fix Requires for py3 dbus
- Fix email address in changelog

* Fri Dec 12 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.1-1
- The initial package version.
