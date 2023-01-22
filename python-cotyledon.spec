%global pypi_name cotyledon

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{pypi_name}
Version:        1.7.3
Release:        14%{?dist}
Summary:        Cotyledon provides a framework for defining long-running services

License:        ASL 2.0
URL:            https://cotyledon.readthedocs.io
Source0:        https://pypi.io/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Cotyledon provides a framework for defining long-running services
%{?python_provide:%python_provide python2-cotyledon}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-pbr
# For building documentation
BuildRequires:  python2-sphinx
BuildRequires:  python-setproctitle

Requires:  python-setproctitle

%description -n python2-%{pypi_name}
Cotyledon provides a framework for defining long-running services.


%package -n python2-%{pypi_name}-tests
Summary:          Cotyledon provides a framework for defining long-running services
Requires:         python2-%{pypi_name} = %{version}-%{release}
Requires:         python2-oslotest
Requires:         python2-testrepository
Requires:         python2-testscenarios
Requires:         python2-testtools

%description -n python2-%{pypi_name}-tests
Cotyledon provides a framework for defining long-running services.
%endif

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        Cotyledon provides a framework for defining long-running services
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pbr
# For building documentation
BuildRequires:  python3-sphinx
BuildRequires:  python3-setproctitle

Requires:  python3-setproctitle

%description -n python3-%{pypi_name}
Cotyledon provides a framework for defining long-running services.

%package -n python3-%{pypi_name}-tests
Summary:    Tests for %{name}
Requires:         python3-%{pypi_name} = %{version}-%{release}
Requires:         python3-oslotest
Requires:         python3-testrepository
Requires:         python3-testscenarios
Requires:         python3-testtools

%description -n python3-%{pypi_name}-tests
Cotyledon provides a framework for defining long-running services.

This package contains test files
%endif

%package doc
Summary:    Documentation for %{name}

%description doc
Cotyledon provides a framework for defining long-running services.

This package contains documentation in HTML format.

%description
Cotyledon provides a framework for defining long-running services.

%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%if %{with python2}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
%else
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 -b html doc/source html
%endif

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%install
%if %{with python2}
%{__python2} setup.py install --skip-build --root %{buildroot}
%endif

%if %{with python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%check
%if %{with python3}
%{__python3} setup.py test ||:
rm -rf .testrepository
%endif
%if %{with python2}
%{__python2} setup.py test ||:
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}-tests
%license LICENSE
%{python2_sitelib}/%{pypi_name}/tests/
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python3-%{pypi_name}-tests
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests

%endif

%files doc
%doc html

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.3-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.3-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.7.3-1
- Update to 1.7.3.
- Remove python2 subpackages when building in Fedora.

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.7-9
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.7-7
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.7-5
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 08 2017 Pradeep Kilambi <pkilambi@redhat.com> - 1.6.7-1
- Rebase 1.6.7

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.3-2
- Rebuild for Python 3.6

* Thu Dec  1 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.6.3-1
- Upstream 1.6.3

* Fri Sep 02 2016 Alan Pevec <apevec AT redhat.com> - 1.2.7-2
- python2 subpackage was missing

* Wed Aug 31 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.7-1
- Rebase to 1.2.7
- move sphinx-build to %%build
- move buildRequires/requires to python2-cotyledon 
- run python3 tests

* Fri Jul 15 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.5-3
- Add check section
- added new test dependencies
- fixed tests sub packages

* Thu Jul 14 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.5-2
- Fix source url

* Wed Jul 6 2016 Mehdi Abaakouk <sileht@redhat.com> - 1.2.5-1
- Initial package.
