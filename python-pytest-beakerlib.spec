%global srcname pytest-beakerlib
%global modulename pytest_beakerlib
# Define tar version. TODO: remove with future releases.
%global tar_version 1

Name:       python-%{srcname}
Version:    0.7.1
Release:    20%{?dist}
Summary:    A pytest plugin that reports test results to the BeakerLib framework

License:    GPLv3+
URL:        https://pagure.io/python-pytest-beakerlib
Source0:    https://releases.pagure.org/%{name}/%{srcname}-%{version}-%{tar_version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

# Test requirements:
BuildRequires:  beakerlib

%description
Allows results of running a test suite under pytest to be reported to
an active BeakerLib session.


%package -n python3-%{srcname}
Summary:    %{summary}
Requires:   python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Allows results of running a test suite under pytest to be reported to
an active BeakerLib session.


%prep
%setup -q -n %{srcname}-%{version}

# Doc files should not be executable.
chmod -x smoketest.sh


%build
%py3_build

%install
%py3_install


%check
. /usr/share/beakerlib/beakerlib.sh
rlJournalStart
# There are failures in smoketest output as both success
# and failure tests are being run with beakerlib plugin enabled.
PYTHON=%{__python3} bash smoketest.sh


%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%doc test_demo.py
%doc smoketest.sh
%{python3_sitelib}/%{modulename}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modulename}.py
%{python3_sitelib}/__pycache__/%{modulename}.cpython-3*.py*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.7.1-19
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.1-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Petr Viktorin <pviktori@redhat.com> - 0.7.1-7
- Remove the Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.1-2
- Conform to the naming policy in dependency declaration

* Tue Mar 21 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.1-1
- Update source URL and run tests with bash
- Remove python-rpm dependency as bz#1185866 was fixed

* Fri Feb 17 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.7-1
- Bump version to 0.7
- Add python2- subpackage and modernize spec file

* Tue Aug 16 2016 Scott Poore <spoore@redhat.com> - 0.6-1
- Bump version to 0.6

* Tue Aug 16 2016 Scott Poore <spoore@redhat.com> - 0.5-4
- Add support for --short-phase-name

* Mon Mar 2 2015 Petr Viktorin <encukou@gmail.com> - 0.5-3
- Don't use licence macro on RHEL 6

* Tue Jan 27 2015 Petr Viktorin <encukou@gmail.com> - 0.5-2
- Also install COPYING as a license on the Python 3 version

* Mon Jan 26 2015 Petr Viktorin <encukou@gmail.com> - 0.5-1
- Run tests
- Install COPYING as a license

* Fri Jan 9 2015 Petr Viktorin <encukou@gmail.com> - 0.4-2
- Use correct macro for python2_sitelib

* Thu Nov 13 2014 Petr Viktorin <encukou@gmail.com> - 0.4-1
- Update to upstream 0.4

* Thu Nov 13 2014 Petr Viktorin <encukou@gmail.com> - 0.3-1
- "Upstream" packaging fixes

* Thu Nov 13 2014 Petr Viktorin <encukou@gmail.com> - 0.2-3
- Update links to Fedorahosted

* Mon Nov 3 2014 Petr Viktorin <encukou@gmail.com> - 0.2-2
- initial public version of package
