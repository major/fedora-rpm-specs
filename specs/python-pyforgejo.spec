%global pypi_name pyforgejo

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        A client library for accessing the Forgejo API

License:        MIT

URL:            https://codeberg.org/harabat/pyforgejo
Source0:        %{pypi_source %pypi_name}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A client library for accessing the Forgejo API

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A client library for accessing the Forgejo API

%prep
%autosetup -n %{pypi_name}-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %pypi_name -L

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Mon Feb 24 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-1
- 2.0.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-2
- Relax httpx pin

* Wed Mar 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-1
- Initial package.
