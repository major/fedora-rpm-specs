%global srcname netmiko
%global sum Multi-vendor library to simplify Paramiko SSH connections to network devices

Name:           python-%{srcname}
Version:        4.4.0
Release:        4%{?dist}
Summary:        %{sum}

# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{sum}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
# See prep section below on textfsm
Requires:       python3-textfsm >= 1.1.3
BuildRequires:  python3-textfsm
%if 0%{?rhel}
BuildRequires:  python3-importlib-resources
%endif
# TODO(dtantsur): one of the optional modules requires pysnmp, but it's not
# usable in Python 3.12. Add it when a version that does not require asyncore
# is uploaded.

%py_provides python3-%{srcname}

%description -n python3-%{srcname}
%{sum} - package for Python 3.

# FIXME: build the documentation, when upstream starts shipping its sources:
# https://github.com/ktbyers/netmiko/issues/507

%prep
%autosetup -n %{srcname}-%{version}
# NOTE(dtantsur): ntc-templates is not packaged, we're using python3-textfsm
# instead. Fixes https://bugzilla.redhat.com/show_bug.cgi?id=1927400.
sed -i '/^ntc-templates/d' pyproject.toml
# FIXME(dtantsur): auto-generating this dependency does not work. No idea why.
sed -i '/^textfsm/d' pyproject.toml
# NOTE(dtantsur): 1.17.0rc1 is not packaged yet but the required Python 3.13
# fix is already in Fedora.
sed -i '/^cffi/s/1.17.0rc1/1.16.0/' pyproject.toml
# Years after Python 2 removal, Fedora still considers just "python" ambiguous.
# Let's assume they shouldn't be invoked directly, only via generated scripts.
sed -si '/^#!\/usr\/bin\/env python/d' netmiko/cli_tools/netmiko_*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files netmiko

%check
# FIXME: run unit tests, when/if upstream creates them:
# https://github.com/ktbyers/netmiko/issues/509
%pyproject_check_import -e '*.snmp_autodetect'

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/netmiko-cfg
%{_bindir}/netmiko-grep
%{_bindir}/netmiko-show
%license LICENSE
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 9 2024 Dmitry Tantsur <dtantsur@proton.me> - 4.4.0-1
- Update to 4.4.0 (fixes #2291789, #2296411)
- Remove the poetry hack, fixed upstream
- Downgrade the cffi dependency - the Python 3.13 fix is already here

* Sun Apr 21 2024 Dmitry Tantsur <dtantsur@proton.me> - 4.3.0-1
- Update to 4.3.0
- Use poetry instead of explicit setup.py, switch to new packaging macros
- Patch out the hardcoded poetry version, we have a much newer one

* Sun Apr 21 2024 Dmitry Tantsur <dtantsur@proton.me> - 4.1.2-1
- Update to 4.1.2 (in preparation to much large updates)
- Synchronize dependencies with upstream setup.py

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 4.1.1-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Karolina Kula <kkula@redhat.com> - 4.1.1-2
- Revert removal of ntc-templates removing sed

* Mon Jul 25 2022 Karolina Kula <kkula@redhat.com> - 4.1.1-1
- Update to version 4.1.1
- Remove ntc-templates removing sed
- Add generated executables to files

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.3.3-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.3-3
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Dmitry Tantsur <divius.inside@gmail.com> - 3.3.3-2
- Fix missing dependency (#1927400)

* Tue Feb 09 2021 Joel Capitao <jcapitao@redhat.com> - 3.3.3-1
- Update to 3.3.3 (#1791581)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Yatin Karel <ykarel@redhat.com> - 3.3.0-1
- Update to 3.3.0 (#1791581)

* Sun Aug 30 2020 Dmitry Tantsur <divius.inside@gmail.com> - 3.2.0-1
- Update to 3.2.0 (#1791581)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Dmitry Tantsur <divius.inside@gmail.com> - 3.0.0-1
- Update to 3.0.0 (#1791581)

* Tue Dec 03 2019 Dmitry Tantsur <divius.inside@gmail.com> - 2.4.2-1
- Update to 2.4.2 (#1727660)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Dmitry Tantsur <divius.inside@gmail.com> - 2.3.3-1
- Update to 2.3.3

* Mon Feb 11 2019 Yatin Karel <ykarel@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Dmitry Tantsur <divius.inside@gmail.com> - 2.2.2-2
- Disable Python 2 subpackage for Fedora (rhbz#1627402)

* Thu Jul 19 2018 Dmitry Tantsur <divius.inside@gmail.com> - 2.2.2-1
- Update to 2.2.2 (rhbz#1559654)

* Tue Jul 17 2018 Dmitry Tantsur <divius.inside@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Alan Pevec <alan.pevec@redhat.com> 2.1.0-1
- Update to 2.1.0 (rhbz#1532228)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 4 2018 Dmitry Tantsur <divius.inside@gmail.com> - 1.4.3-1
- Update to 1.4.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Dmitry Tantsur <divius.inside@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Mon Jul 24 2017 Dmitry Tantsur <divius.inside@gmail.com> - 1.4.1-1
- Initial packaging (#1465006)
