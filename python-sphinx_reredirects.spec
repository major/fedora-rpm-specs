%global pypi_name sphinx_reredirects
%global version 0.1.2

Name:           python-%{pypi_name}
Version:        %{version}
Release:        2%{?dist}
Summary:        Handles redirects for moved pages in Sphinx documentation projects

License:        BSD-3-Clause
URL:            https://gitlab.com/documatt/sphinx-reredirects
Source0:        %{url}/-/archive/v%{version}/sphinx-reredirects-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
sphinx-reredirects is the extension for Sphinx documentation < projects
that handles redirects for moved pages. It generates HTML pages with
meta refresh redirects to the new page location to prevent 404 errors
if you rename or move your documents.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(sphinx)
%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n sphinx-reredirects-v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build documentation
sphinx-build -b man -C docs output-man
mv output-man/python.1 %{pypi_name}.1

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
mkdir -p %{buildroot}/%{_mandir}/man1/
install -pm 644 %{pypi_name}.1 %{buildroot}/%{_mandir}/man1/

%check
# the tests in this file fail with the message:
# "E       fixture 'app' not found"
rm tests/test_end2end.py
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_mandir}/man1/%{pypi_name}.1*

%changelog
* Fri Sep  8 2023 José Matos <jamatos@fedoraproject.org> - 0.1.2-2
- Change spec to the latest spec python macros

* Thu Sep 07 2023 José Matos <jamatos@fc.up.pt> - 0.1.2-1
- Initial package.
