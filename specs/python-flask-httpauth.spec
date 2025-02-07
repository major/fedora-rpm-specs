%global pypi_name Flask-HTTPAuth
%global pkg_name flask-httpauth

Name:           python-%{pkg_name}
Version:        4.8.0
Release:        4%{?dist}
Summary:        Basic and Digest HTTP authentication for Flask routes

License:        MIT
URL:            http://github.com/miguelgrinberg/flask-httpauth/
Source0:        https://files.pythonhosted.org/packages/source/F/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# https://github.com/miguelgrinberg/Flask-HTTPAuth/commit/52a13b15b
Patch0:         python-flask-httpauth-toml.patch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-flask+async
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildArch:      noarch

%description
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

%package -n     python-%{pkg_name}-doc
Summary:        Documentation for Flask-HTTPAuth

%description -n python-%{pkg_name}-doc
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

This package provides the documentation.

%package -n     python3-%{pkg_name}
Summary:        Basic and Digest HTTP authentication for Flask routes
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
 
# Build docs
pushd docs
make PYTHONPATH=%{buildroot}/%{python3_sitelib} SPHINXBUILD=sphinx-build-3 html
rm -v _build/html/.buildinfo
popd

%install
%pyproject_install
%pyproject_save_files flask_httpauth

%check
%pytest

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc docs/_build/html

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Wed Feb 05 2025 Javier Peña <jpena@redhat.com> - 4.8.0-5
- Remove -t from pyproject_buildrequires

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Terje Rosten <terje.rosten@ntnu.no> - 4.8.0-1
- 4.8.0
- Fix doc build
- Switch to toml based build (based on upstream patch)
- Remove legacy Python 2 refs

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.2.3-27
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 3.2.3-23
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.2.3-20
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.3-17
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.3-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.3-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.3-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Javier Peña <jpena@redhat.com> - 3.2.3-9
- Remove Python2 subpackage in Fedora 30+ (bz#1671976)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Sep 15 2017 Javier Peña <jpena@redhat.com> - 3.2.3-3
- Fix provides for python2 and python3 subpackages

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Javier Peña <jpena@redhat.com> - 3.2.3-1
- Updated to upstream version 3.2.3
- Added %%check, doc and test subpackages
* Tue May 16 2017 Javier Peña <jpena@redhat.com> - 3.2.2-1
- Initial package.
