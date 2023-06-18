%global pypi_name Flask-HTTPAuth
%global pkg_name flask-httpauth

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{pkg_name}
Version:        3.2.3
Release:        23%{?dist}
Summary:        Basic and Digest HTTP authentication for Flask routes

License:        MIT
URL:            http://github.com/miguelgrinberg/flask-httpauth/
Source0:        https://files.pythonhosted.org/packages/source/F/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

%if %{with python2}
%package -n     python2-%{pkg_name}
Summary:        Basic and Digest HTTP authentication for Flask routes
%{?python_provide:%python_provide python2-%{pkg_name}}
BuildRequires:  python2-devel
BuildRequires:  python2-flask
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
Requires:       python2-flask
Requires:       python2-werkzeug

%description -n python2-%{pkg_name}
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.
%endif

%package -n     python-%{pkg_name}-doc
Summary:        Documentation for Flask-HTTPAuth

%description -n python-%{pkg_name}-doc
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

This package provides the documentation.


%if %{with python3}
%package -n     python3-%{pkg_name}
Summary:        Basic and Digest HTTP authentication for Flask routes
%{?python_provide:%python_provide python3-%{pkg_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-flask
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
Requires:       python3-flask
Requires:       python3-werkzeug

%description -n python3-%{pkg_name}
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.
%endif # with_python3

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
# generate html docs
%{__python2} setup.py build_sphinx
%endif
%if %{with python3}
%py3_build
# generate html docs
%{__python3} setup.py build_sphinx
%endif # with_python3

# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}


%install
%if %{with python3}
%py3_install
%endif # with_python3
%if %{with python2}
%py2_install
%endif

%check
%if %{with python3}
%{__python3} setup.py test
%endif # with_python3
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python2}
%files -n python2-%{pkg_name}
%license LICENSE
%doc README.md
%{python2_sitelib}/flask_httpauth.py*
%{python2_sitelib}/Flask_HTTPAuth-%{version}-py?.?.egg-info
%endif

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc build/sphinx/html

%if %{with python3}
%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/flask_httpauth.py
%{python3_sitelib}/Flask_HTTPAuth-%{version}-py%{python3_version}.egg-info
%endif # with_python3

%changelog
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
- Added %check, doc and test subpackages
* Tue May 16 2017 Javier Peña <jpena@redhat.com> - 3.2.2-1
- Initial package.
