%global desc %{expand: \
Numpoly is a generic library for creating, manipulating and evaluating arrays of polynomials.}

%global pypi_name numpoly

Name:       python-%{pypi_name}
Version:    1.2.3
Release:    6%{?dist}
Summary:    Polynomials as a numpy datatype
License:    BSD
URL:        https://github.com/jonathf/numpoly

# Use the github source to build this package.
Source0:    %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sympy
BuildRequires:  pylint
BuildRequires:  python3-six
BuildRequires:  poetry
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(pydocstyle)
BuildRequires:  python3dist(wheel)

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
%{pytest} test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.2.3-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.3-1
- Update to latest release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Luis Bazan <lbazan@fedoraproject.org> - 1.1.3-1
- New upstream version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.1-1
- Update to latest release

* Sun Nov 29 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-1
- Update to latest release
- Enable tests

* Sat Aug 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.0.6-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.0.3-1
- New upstream version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.2.3-2
- New upstream version

* Wed Apr 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.1.16-2
- Fix comments in BZ1808552

* Wed Apr 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.1.16-1
- Initial Import
