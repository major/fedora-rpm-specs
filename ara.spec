# Don't attempt to build -docs, -tests and -server on rhel/centos until
# missing packages are available.
%if 0%{?rhel}
%global with_docs 0
%global with_tests 0
%global with_server 0
%else
%global with_docs 1
%global with_tests 1
%global with_server 1
%endif

%global srcname ara

Name:           %{srcname}
Version:        1.5.7
Release:        5%{?dist}
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot

License:        GPLv3
URL:            https://github.com/ansible-community/ara
Source0:        https://pypi.io/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git

Requires:       python3-%{srcname} = %{version}-%{release}

%description
%{summary}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr

Requires:       python3-requests
Requires:       python3-cliff
Requires:       python3-pbr

%description -n python3-%{srcname}
%{summary}

This package installs the python files and Ansible plugins

%if 0%{?with_server}
%package -n python3-%{srcname}-server
Summary:        %{summary}

Provides:       %{srcname}-server = %{version}-%{release}

# Test dependencies for check macro
BuildRequires:  python3-django
BuildRequires:  python3-django-cors-headers
BuildRequires:  python3-django-health-check
BuildRequires:  python3-django-filter
BuildRequires:  python3-django-rest-framework
BuildRequires:  python3-dynaconf
BuildRequires:  python3-factory-boy
BuildRequires:  python3-faker
BuildRequires:  python3-pygments
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-requests
BuildRequires:  python3-tzlocal
BuildRequires:  python3-whitenoise

Requires:       python3-%{srcname}
Requires:       python3-django
Requires:       python3-django-cors-headers
Requires:       python3-django-health-check
Requires:       python3-django-filter
Requires:       python3-django-rest-framework
Requires:       python3-dynaconf
Requires:       python3-pygments
Requires:       python3-ruamel-yaml
Requires:       python3-tzlocal
Requires:       python3-whitenoise

%description -n python3-%{srcname}-server
%{summary}

This package installs the API server dependencies
%endif

%if 0%{?with_tests}
%package -n python3-%{srcname}-tests
Summary:        %{summary}

Requires:       python3-%{srcname}-server = %{version}-%{release}
Requires:       python3-factory-boy
Requires:       python3-faker

%description -n python3-%{srcname}-tests
%{summary}

This package installs the test dependencies
%endif

%if 0%{?with_docs}
%package doc
Summary:        %{summary}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-programoutput
# The API server dependencies need to be installed so the snippets from
# sphinxcontrib-programoutput can be generated
BuildRequires:  python3-%{srcname}-server

%description doc
%{summary}

This package installs the documentation
%endif

%prep
%autosetup -n %{srcname}-%{version} -S git

%build
# Substitute python3 shebang for the one provided by the distribution
sed -i -e 's|/usr/bin/env python3|/usr/bin/python3|' ara/server/__main__.py

%py3_build
%if 0%{?with_docs}
sphinx-build -b html doc/source doc/build/html
# Remove sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%if 0%{?with_tests}
%check
# Run unit tests
cd %{_builddir}/%{srcname}-%{version}
# Set time zone to UTC -- buildsystem's timezone is "local" which isn't valid
ARA_TIME_ZONE=UTC %{__python3} manage.py test %{srcname}
%endif

%files
%doc README.rst
%license LICENSE

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info
%exclude %{python3_sitelib}/%{srcname}/api/tests
%{_bindir}/ara
# TODO: ara-manage probably shouldn't get set up if django isn't installed
%exclude %{_bindir}/ara-manage

%if 0%{?with_server}
%files -n python3-%{srcname}-server
%doc README.rst
%license LICENSE
%{_bindir}/ara-manage
%endif

%if 0%{?with_tests}
%files -n python3-%{srcname}-tests
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}/api/tests
%endif

%if 0%{?with_docs}
%files doc
%doc README.rst doc/build/html
%license LICENSE
%endif

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.5.7-4
- Rebuilt for Python 3.11

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.5.7-3
- Bootstrap for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 3 2021 David Moreau Simard <moi@dmsimard.com> - 1.5.7-1
- Update to latest upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 06 2021 Python Maint <python-maint@redhat.com> - 1.5.6-3
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.6-2
- Bootstrap for Python 3.10

* Thu Apr 15 2021 David Moreau Simard <moi@dmsimard.com> - 1.5.6-1
- Update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 David Moreau Simard <moi@dmsimard.com> - 1.5.4-1
- Update to latest upstream release

* Fri Oct 23 2020 David Moreau Simard <moi@dmsimard.com> - 1.5.3-1
- Update to latest upstream release

* Wed Sep 23 2020 David Moreau Simard <moi@dmsimard.com> - 1.5.1-2
- Add missing requirement on pbr

* Wed Sep 23 2020 David Moreau Simard <moi@dmsimard.com> - 1.5.1-1
- Update to latest upstream release
- Add requirement on python3-cliff (new CLI client)

* Tue Aug 11 2020 David Moreau Simard <moi@dmsimard.com> - 1.4.3-1
- Update to latest upstream release
- Change pyyaml to ruamel.yaml as preferred by dynaconf

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Bootstrap for Python 3.9

* Mon Apr 20 2020 David Moreau Simard <dmsimard@redhat.com> - 1.4.0-1
- Update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 David Moreau Simard <dmsimard@redhat.com> - 1.3.2
- Update to latest upstream release

* Tue Dec 3 2019 David Moreau Simard <dmsimard@redhat.com> - 1.3.0
- Update to latest upstream release

* Wed Nov 6 2019 David Moreau Simard <dmsimard@redhat.com> - 1.2.0-2
- Add missing pygments dependency

* Wed Nov 6 2019 David Moreau Simard <dmsimard@redhat.com> - 1.2.0-1
- Update to latest upstream release

* Tue Oct 8 2019 David Moreau Simard <dmsimard@redhat.com> - 1.1.0-3
- Add an ara-server package alias to python3-ara-server

* Tue Sep 10 2019 David Moreau Simard <dmsimard@redhat.com> - 1.1.0-1
- Update to latest upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 David Moreau Simard <dmsimard@redhat.com> - 0.16.1
- Update to latest upstream release
- Default to python3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.14.6-2
- Rebuilt for Python 3.7

* Sat Feb 24 2018 David Moreau Simard <dmsimard@redhat.com> - 0.14.6-1
- Update to upstream 0.14.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 5 2017 David Moreau Simard <dmsimard@redhat.com> - 0.14.0-1
- First packaged version of ARA
