%global modname dbusmock

Name:             python-%{modname}
Version:          0.36.0
Release:          3%{?dist}
Summary:          Mock D-Bus objects

License:          LGPL-3.0-or-later
URL:              https://pypi.python.org/pypi/python-dbusmock
Source0:          https://files.pythonhosted.org/packages/source/p/%{name}/python_%{modname}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    git
BuildRequires:    python3-devel
BuildRequires:    python3-gobject
BuildRequires:    python3-pytest
BuildRequires:    dbus-x11
BuildRequires:    upower

%global _description\
With this program/Python library you can easily create mock objects on\
D-Bus. This is useful for writing tests for software which talks to\
D-Bus services such as upower, systemd, ConsoleKit, gnome-session or\
others, and it is hard (or impossible without root privileges) to set\
the state of the real services to what you expect in your tests.

%description %_description

%package -n python3-dbusmock
Summary: %summary (Python3)
Requires:         python3-dbus, python3-gobject, dbus-x11
%description -n python3-dbusmock %_description

%prep
%autosetup -n python_%{modname}-%{version}
rm -rf python-%{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dbusmock

%check
%{__python3} -m unittest -v

%files -n python3-dbusmock -f %{pyproject_files}

%doc README.md COPYING

%changelog
* Tue Jul 29 2025 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Drop redundant manual BuildRequires
- Drop unused BuildRequires on python3dist(wheel)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 15 2025 Packit <hello@packit.dev> - 0.36.0-1
- mockobject: Fix _wrap_in_dbus_variant for Struct and Dict types (thanks Sebastian Wick)
- Drop setup.{cfg,py} and RHEL 9 support, move to pybuild (rhbz#2377609)
- Drop iio-sensor-proxy tests, the template is broken (see #241)

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.35.0-2
- Rebuilt for Python 3.14

* Fri May 23 2025 Packit <hello@packit.dev> - 0.35.0-1
- modemmanager: Add operator code (thanks Guido Günther)
- modemmanager: Allow to set CellBroadcast channel list (thanks Guido Günther)

* Fri Feb 21 2025 Packit <hello@packit.dev> - 0.34.3-1
- tests: Relax libnotify expected format for libnotify 0.8.4

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 27 2024 Packit <hello@packit.dev> - 0.34.2-1
- spec: Adjust %%autosetup to PEP-625 tarball top-level directory

* Wed Dec 11 2024 Packit <hello@packit.dev> - 0.33.0-1
- templates: Add gsd-rfkill (thanks Guido Günther)
- Allow adding objects derived from DBusMockObject (thanks Sebastian Wick)
- Drop Python <= 3.7 support (thanks Tomasz Kłoczko)

* Thu Oct 03 2024 Packit <hello@packit.dev> - 0.32.2-1
- all templates: Drop wrong variant wrapping from all properties
- tests: Skip TestNetworkManager::test_one_wifi_with_accesspoints with NM ≥ 1.49.3

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 14 2024 Packit <hello@packit.dev> - 0.32.1-1
- ModemManager: Add initial mock (thanks Guido Günther)
- bluez5: Add advertising API (thanks Frederik Leonhardt)
- Fix loading of libglib on macOS (thanks peturingi)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.31.1-2
- Rebuilt for Python 3.13

* Fri Feb 23 2024 Packit <hello@packit.dev> - 0.31.1-1
- power_profiles_daemon: Move back to original D-Bus name to avoid breaking compatibility
- Add upower_power_profiles_daemon template for version 0.20 API with new D-Bus name

* Fri Feb 23 2024 Packit <hello@packit.dev> - 0.31.0-1
- power-profiles-daemon: Move to org.freedesktop.UPower.PowerProfiles as in release 0.20.0 (API break!)
- NetworkManager: Add stub ipv4/6 properties in AddWiFiConnection

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Martin Pitt <mpitt@redhat.com> - 0.30.2-1
- bluez5: Fix invalid arguments to PairDevice (thanks Simon McVittie)

* Sat Dec 23 2023 Packit <hello@packit.dev> - 0.30.1-1
- bluez: Clean up static default properties, re-drop PairDevice() `class_` parameter
- Add pre-commit rules (thanks Peter Hutterer)

* Thu Nov 30 2023 Packit <hello@packit.dev> - 0.30.0-1
- api: Add pytest support and helpers
- api: Factor the server spawning into a new SpawnedMock object (thanks Peter Hutterer)
- doc: generate sphinx docs on https://martinpitt.github.io/python-dbusmock/ (thanks Peter Hutterer)
- cli: Add support for running custom commands on the mock environment (thanks Marco Trevisan)

* Thu Jul 27 2023 Packit <hello@packit.dev> - 0.29.1-1
- spec: Update License: to SPDX format
- Test fixes (thanks Marco Trevisan)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.29.0-2
- Rebuilt for Python 3.12

* Thu Apr 20 2023 Packit <hello@packit.dev> - 0.29.0-1
 - Support loading templates from XDG_DATA_DIRS
 - iio-sensors-proxy: Throw proper D-Bus errors instead of Python Exception

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Packit <hello@packit.dev> - 0.28.7-1
<!-- generated by eloquent/github-release-action -->
<!-- original source:
- blue5-obex template: Fix OBEX PullAll (thanks Jan Alexander Steffens)
- power_profiles template: Fix Actions property type (thanks Jonas Ådahl)
- README: Explain container tests and how to debug them
-->

<ul>
<li>blue5-obex template: Fix OBEX PullAll (thanks Jan Alexander Steffens)</li>
<li>power_profiles template: Fix Actions property type (thanks Jonas Ådahl)</li>
<li>README: Explain container tests and how to debug them</li>
</ul>


* Wed Oct 12 2022 Packit <hello@packit.dev> - 0.28.6-1
<!-- generated by eloquent/github-release-action -->
<!-- original source:
- Fix generated _version.py in release tarball (#164)
-->

<ul>
<li>Fix generated _version.py in release tarball (#164)</li>
</ul>


* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Packit <hello@packit.dev> - 0.28.4-1
<!-- generated by eloquent/github-release-action -->
<!-- original source:
- setup.py: Fix ModuleNotFoundError
- ofono template: Fix conversion to f-strings (Debian #1015286)
- Ship FMF tests in release tarballs
-->
<ul>
<li>setup.py: Fix ModuleNotFoundError</li>
<li>ofono template: Fix conversion to f-strings (Debian #1015286)</li>
<li>Ship FMF tests in release tarballs</li>
</ul>



* Sun Jul 17 2022 Packit <hello@packit.dev> - 0.28.3-1
<!-- generated by eloquent/github-release-action -->
<!-- original source:
- Bring back dbusmock.__version__
-->
<ul>
<li>Bring back dbusmock.<strong>version</strong>
</li>
</ul>



* Sat Jul 16 2022 Packit <hello@packit.dev> - 0.28.2-1
<!-- generated by eloquent/github-release-action -->
<!-- original source:
- Dynamically compute version with setuptools-scm
- tests: Adjust to libnotify 0.8 (Debian #1015068)
- tests: Only run pylint on current Fedora release
-->
<ul>
<li>Dynamically compute version with setuptools-scm</li>
<li>tests: Adjust to libnotify 0.8 (Debian #1015068)</li>
<li>tests: Only run pylint on current Fedora release</li>
</ul>



* Tue Jun 28 2022 Packit <hello@packit.dev> - 0.28.1-1
- Again works on RHEL/CentOS 8 (0.27 broke there), now in CI
- Avoid glib GI dependency for main dbusmock, for running in virtualenv (thanks Allison Karlitskaya)


* Sun Jun 19 2022 Packit <hello@packit.dev> - 0.28.0-1
- Drop unmaintained and broken accountsservice template
- testcase: Throw an error when spawning a well-known name that exists (thanks Benjamin Berg)
- mockobject: Allow sending signals with extra details (thanks Peter Hutterer)


* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.27.5-2
- Rebuilt for Python 3.11

* Tue Apr 05 2022 Packit <hello@packit.dev> - 0.27.5-1
- bluez and accountsservice templates: Drop default arguments from D-Bus methods (thanks Simon McVittie)


* Mon Apr 04 2022 Packit <hello@packit.dev> - 0.27.4-1
- Fix D-Bus signature detection regression from 0.27.0 (thanks Peter Hutterer) (#118)


* Tue Mar 22 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.27.3-1
- packit: Fix file name to sync


* Tue Mar 22 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.27.0-1
- Do not register standard session service directories, add API to enable selected services (thanks Benjamin Berg)
- Log static method calls from templates (thanks Peter Hutterer)


* Fri Feb 25 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.26.1-1
- Fix README content type to Markdown, to fix releasing to PyPi


* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.25.0-1
- bluez template: Implement adapter discovery, connect, disconnect, and removal
  (thanks Bastien Nocera)
- Fix changing array properties (thanks Jonas Ådahl)
- Fix CLI upower tests (thanks Marco Trevisan)
- Add testing and Fedora updating through packit


* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Bastien Nocera <bnocera@redhat.com> - 0.23.0-1
+ python-dbusmock-0.23.0-1
- Update to 0.23.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.22.0-4
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Bastien Nocera <bnocera@redhat.com> - 0.22.0-3
+ python-dbusmock-0.22.0-3
- Add bluez agent templates for the benefit of gnome-bluetooth

* Mon Mar 01 2021 Charalampos Stratakis <cstratak@redhat.com> - 0.22.0-2
- Remove redundant dependency on python3-nose

* Fri Feb 12 2021 Bastien Nocera <bnocera@redhat.com> - 0.22.0-1
+ python-dbusmock-0.22.0-1
- Update to 0.22.0
- Disable tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18.3-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Bastien Nocera <bnocera@redhat.com> - 0.18.3-2
+ python-dbusmock-0.18.3-2
- Add low-memory-monitor mock

* Thu Nov 14 2019 Bastien Nocera <bnocera@redhat.com> - 0.18.3-1
+ python-dbusmock-0.18.3-1
- Update to 0.18.3
- Enable tests

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17-8
- Subpackage python2-dbusmock has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17-5
- Rebuilt for Python 3.7

* Fri Mar 30 2018 Bastien Nocera <bnocera@redhat.com> - 0.17-4
+ python-dbusmock-0.17-4
- Patch from Benjamin Berg to correct the python3 subpackage deps
  and summary

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.17-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Bastien Nocera <bnocera@redhat.com> - 0.17-1
- Update to 0.17
- Update source URL

* Tue Oct 17 2017 Bastien Nocera <bnocera@redhat.com> - 0.16.9-1
+ python--0.16.9-1
- Update to 0.16.9

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.16.7-4
- Python 2 binary package renamed to python2-dbusmock
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Bastien Nocera <bnocera@redhat.com> - 0.16.7-1
+ python-dbusmock-0.16.7-1
- Update to 0.16.7

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 08 2014 Matěj Cepl <mcepl@redhat.com> - 0.11.1-1
- Update to 0.11.1

* Thu Jul 17 2014 Bastien Nocera <bnocera@redhat.com> 0.10.3-2
- Add Python3 sub-package

* Thu Jul 17 2014 Bastien Nocera <bnocera@redhat.com> 0.10.3-1
- Update to 0.10.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Bastien Nocera <bnocera@redhat.com> 0.8.1-1
- Update to 0.8.1

* Fri Nov 08 2013 Bastien Nocera <bnocera@redhat.com> 0.8-1
- Update to 0.8

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Bastien Nocera <bnocera@redhat.com> 0.6.3-1
- Update to 0.6.3

* Thu Jun 13 2013 Bastien Nocera <bnocera@redhat.com> 0.6.2-1
- Update to 0.6.2

* Wed Jun 12 2013 Bastien Nocera <bnocera@redhat.com> 0.6-1
- Update to 0.6.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Bastien Nocera <bnocera@redhat.com> 0.4.0-1
- Update to 0.4.0

* Mon Jan 07 2013 Bastien Nocera <bnocera@redhat.com> 0.3.1-1
- Update to 0.3.1

* Wed Dec 19 2012 Matěj Cepl <mcepl@redhat.com> - 0.3-1
- New upstream release.

* Mon Oct 08 2012 Matěj Cepl <mcepl@redhat.com> - 0.1.1-2
- remove the bundled egg-info following the package review.

* Fri Oct 05 2012 Matěj Cepl <mcepl@redhat.com> - 0.1.1-1
- This version should actually work

* Tue Oct 02 2012 Matěj Cepl <mcepl@redhat.com> 0.0.3-1
- initial package for Fedora
