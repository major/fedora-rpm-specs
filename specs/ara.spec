# Don't attempt to build -docs, -tests and -server on rhel/centos until
# missing packages are available.
%global with_docs %{undefined rhel}
%global with_tests %{undefined rhel}
%global with_server %{undefined rhel}
# python3-dynaconf doesn't provide the yaml extra
%global _python_no_extras_requires 1

Name:           ara
Version:        1.7.2
Release:        2%{?dist}
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot

License:        GPL-3.0-or-later
URL:            https://github.com/ansible-community/ara
Source0:        %{pypi_source ara}
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel

%if 0%{?with_tests}
BuildRequires:  python3-factory-boy
BuildRequires:  python3-faker
%endif

%if 0%{?with_docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-programoutput
%endif


%description
%{summary}.


%package -n python3-ara
Summary:        %{summary}
# ara used to be a blank package.
Obsoletes:      ara < 1.6.1-1
Provides:       ara = %{version}-%{release}


%description -n python3-ara
%{summary}.

This package installs the python files and Ansible plugins.


%if 0%{?with_server}
# Ending this with +server tells the Python extras dependency generator
# to add dependencies for the 'server' extra as defined in setup.cfg
#
# We can't use %%pyproject_extras_subpkg, because we need more control over
# included Requires/Provides/Obsoletes and files.
%package -n python3-ara+server
Summary:        %{summary}

# Convenience alias
Provides:       ara-server = %{version}-%{release}
# Obsolete the old name
%py_provides    python3-ara-server
Obsoletes:      python3-ara-server < 1.6.1-1

Requires:       python3-ara = %{version}-%{release}
Requires:       python3-ruamel-yaml

%description -n python3-ara+server
%{summary}.

This package installs the API server dependencies.


%package -n python3-ara+postgresql
Summary:        %{summary}
Requires:       python3-ara+server = %{version}-%{release}


%description -n python3-ara+postgresql
%{summary}.

This package installs the needed dependencies for the API server to use a
PostgreSQL database.


%package -n python3-ara+mysql
Summary:        %{summary}


%description -n python3-ara+mysql
%{summary}.

This package installs the needed dependencies for the API server to use a
MySQL database.
%endif

%if 0%{?with_tests}
%package -n python3-ara-tests
Summary:        %{summary}

Requires:       python3-ara+server = %{version}-%{release}
Requires:       python3-factory-boy
Requires:       python3-faker

%description -n python3-ara-tests
%{summary}.

This package installs the test dependencies.
%endif


%if 0%{?with_docs}
%package doc
Summary:        %{summary}

%description doc
%{summary}.

This package installs the documentation.
%endif



%prep
%autosetup -n ara-%{version} -S git


%generate_buildrequires
%pyproject_buildrequires -x server


%build
%pyproject_wheel

%if 0%{?with_docs}
# XXX: The docs build needs to execute `ara` and 'ara-manage'
%{python3} -m venv dummy_install --system-site-packages
. ./dummy_install/bin/activate
pip install %{_pyproject_wheeldir}/ara-%{version}-*.whl
sphinx-build -b html doc/source doc/build/html
# Remove sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
rm -rf doc/build/html/_{sources,static}
%endif


%install
%pyproject_install


%if 0%{?with_tests}
%check
# Run unit tests
# Set time zone to UTC -- buildsystem's timezone is "local" which isn't valid
ARA_TIME_ZONE=UTC %{__python3} manage.py test ara
%endif


%files -n python3-ara
%doc README.md
%license LICENSE
%{_bindir}/ara
%{python3_sitelib}/ara/
%exclude %{python3_sitelib}/ara/api/tests/
%{python3_sitelib}/ara-*.dist-info/


%if 0%{?with_server}
%files -n python3-ara+server
%{_bindir}/ara-manage
# This is needed for the python extras dependency generator
%ghost %{python3_sitelib}/ara-*.dist-info/


%files -n python3-ara+postgresql
%ghost %{python3_sitelib}/ara-*.dist-info/


%files -n python3-ara+mysql
%ghost %{python3_sitelib}/ara-*.dist-info/
%endif


%if 0%{?with_tests}
%files -n python3-ara-tests
%{python3_sitelib}/ara/api/tests/
%endif


%if 0%{?with_docs}
%files doc
%doc README.md doc/build/html
%license LICENSE
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 4 2024 David Moreau Simard <moi@dmsimard.com> - 1.7.2-1
- Update to latest upstream release
- Includes a fix for python 3.13 compatibility

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 David Moreau Simard <moi@dmsimard.com> - 1.7.0-1
- Update to latest upstream release

* Sun Aug 13 2023 David Moreau Simard <moi@dmsimard.com> - 1.6.1-4
- Include upstream patch to allow recent versions of Django. Fixes rhbz#2225705.
- Remove patch allowing older versions of tzlocal

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Maxwell G <gotmax@e.email> - 1.6.1-1
- Update to 1.6.1.

* Tue Dec 06 2022 Maxwell G <gotmax@e.email> - 1.6.0-1
- Update to 1.6.0.

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
