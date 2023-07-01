%global srcname netmiko
%global sum Multi-vendor library to simplify Paramiko SSH connections to network devices

Name:           python-%{srcname}
Version:        4.1.1
Release:        4%{?dist}
Summary:        %{sum}

License:        MIT and ASL 2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{sum}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
Requires:       python3-paramiko >= 2.6.0
Requires:       python3-scp >= 0.13.2
Requires:       python3-pyserial
Requires:       python3-tenacity
Requires:       python3-textfsm
# For import test, keep the same as requirements
BuildRequires:  python3-paramiko
BuildRequires:  python3-scp
BuildRequires:  python3-pyserial
BuildRequires:  python3-tenacity
BuildRequires:  python3-textfsm
BuildRequires:  python3-setuptools
%if 0%{?rhel}
BuildRequires:  python3-importlib-resources
%endif

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum} - package for Python 3.

# FIXME: build the documentation, when upstream starts shipping its sources:
# https://github.com/ktbyers/netmiko/issues/507

%prep
%autosetup -n %{srcname}-%{version}
# NOTE(dtantsur): ntc-templates is not packaged, we're using python3-textfsm
# instead. Fixes https://bugzilla.redhat.com/show_bug.cgi?id=1927400.
sed -i '/ntc-templates/d' setup.py

%build
%py3_build

%install
%py3_install

%check
# FIXME: run unit tests, when/if upstream creates them:
# https://github.com/ktbyers/netmiko/issues/509
%{__python3} -c "from netmiko import ConnectHandler"

%files -n python3-%{srcname}
%{_bindir}/netmiko-cfg
%{_bindir}/netmiko-grep
%{_bindir}/netmiko-show
%license LICENSE
%doc README.md
%{python3_sitelib}/*


%changelog
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
