%global pypi_name sphinx-multiversion
%global pypi_version 0.2.4

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        3%{?dist}
Summary:        Add support for multiple versions to sphinx

License:        BSD-2-Clause
URL:            https://holzhaus.github.io/sphinx-multiversion/
Source0:        https://github.com/sphinx-contrib/multiversion/releases/download/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Extension for building self-hosted versioned docs.This extension aims to
provide a clean implementation that tries to avoid messing with Sphinx
internals as much as possible.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx) >= 2.1
%description -n python3-%{pypi_name}
 sphinx-multiversion [![Build Status]( extension for building self-hosted
versioned docs.This extension aims to provide a clean implementation that tries
to avoid messing with Sphinx internals as much as possible.Documentation can be
found at:


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_multiversion
sed -e '1d' -i %{buildroot}%{python3_sitelib}/sphinx_multiversion/__main__.py

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/sphinx-multiversion

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.2.4-2
- Review fixes.

* Wed Dec 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.2.4-1
- Initial package.
