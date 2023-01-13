%global pypi_name gnocchiclient

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


%global common_desc \
This is a client library for Gnocchi built on the Gnocchi API. It \
provides a Python API (the gnocchiclient module) and a command-line tool.

Name:             python-gnocchiclient
Version:          7.0.7
Release:          7%{?dist}
Summary:          Python API and CLI for OpenStack Gnocchi

License:          ASL 2.0
URL:              https://github.com/openstack/%{name}
Source0:          https://pypi.io/packages/source/g/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# FIXME(jpena): remove this patch once a version > 7.0.1 is released
%if "%{version}" == "7.0.1"
Patch0001:        0001-Avoid-using-openstack-doc-tools.patch
%endif
BuildArch:        noarch


%package -n python-%{pypi_name}-doc
Summary:          Documentation for OpenStack Gnocchi API Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-cliff >= 2.10
BuildRequires:    python3-keystoneauth1
BuildRequires:    python3-six
BuildRequires:    python3-futurist
BuildRequires:    python3-ujson
BuildRequires:    python3-sphinx_rtd_theme
# test
BuildRequires:    python3-babel
# Runtime requirements needed during documentation build
BuildRequires:    python3-osc-lib
BuildRequires:    python3-dateutil

%description      doc
%{common_desc}

This package contains auto-generated documentation.

%package -n python3-%{pypi_name}
Summary:          Python API and CLI for OpenStack Gnocchi

%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-setuptools
BuildRequires:    python3-tools
BuildRequires:    python3-monotonic

Requires:         python3-cliff >= 2.10
Requires:         python3-osc-lib >= 1.8.0
Requires:         python3-keystoneauth1 >= 2.0.0
Requires:         python3-six >= 1.10.0
Requires:         python3-futurist
Requires:         python3-ujson
Requires:         python3-pbr
Requires:         python3-monotonic
Requires:         python3-iso8601
Requires:         python3-dateutil
Requires:         python3-debtcollector

%description -n python3-%{pypi_name}
%{common_desc}

%package -n python3-%{pypi_name}-tests
Summary:          Python API and CLI for OpenStack Gnocchi Tests
Requires:         python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
%{common_desc}


%description
%{common_desc}


%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}


# Remove bundled egg-info
rm -rf gnocchiclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%py3_build


%install
%py3_install

# Some env variables required to successfully build our doc
export PYTHONPATH=.
# %{__python3} setup.py build_sphinx -b html

# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.doctrees doc/build/html/.buildinfo

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/gnocchi
%{python3_sitelib}/gnocchiclient
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/gnocchiclient/tests

%files -n python3-%{pypi_name}-tests
%license LICENSE
%{python3_sitelib}/gnocchiclient/tests

%files -n python-%{pypi_name}-doc
# %doc doc/build/html

%changelog
* Wed Jan 11 2023 Alfredo Moralejo <amoralej@redhat.com> - 7.0.7-7
- Rebuild for Fedora 38

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.0.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Matthias Runge <mrunge@redhat.com> - 7.0.7-1
- updated to 7.0.7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Miro Hrončok <mhroncok@redhat.com> - 7.0.4-2
- Subpackages python2-gnocchiclient, python2-gnocchiclient-tests have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 09 2018 RDO <dev@lists.rdoproject.org> 7.0.4-1
- Update to 7.0.4

