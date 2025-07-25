# Created by pyp2rpm-3.3.10
%global pypi_name optuna

Name:           python-%{pypi_name}
Version:        4.4.0
Release:        2%{?dist}
Summary:        A hyperparameter optimization framework

License:        MIT AND BSD-3-Clause AND SunPro
URL:            https://optuna.org/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(alembic)
BuildRequires:  python3dist(colorlog)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(tqdm)

BuildArch:      noarch

%description
Optuna is an automatic hyperparameter optimization software framework,
particularly designed for machine learning. It features an imperative,
define-by-run style user API. Thanks to our define-by-run API, the
code written with Optuna enjoys high modularity, and the user of
Optuna can dynamically construct the search spaces for the hyperparameters.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Optuna is an automatic hyperparameter optimization software framework,
particularly designed for machine learning. It features an imperative,
define-by-run style user API. Thanks to our define-by-run API, the
code written with Optuna enjoys high modularity, and the user of
Optuna can dynamically construct the search spaces for the hyperparameters.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Tests require fakeredis, not in Fedora

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/optuna
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 16 2025 Gwyn Ciesla <gwync@protonmail.com> - 4.4.0-1
- 4.4.0

* Thu Jun 05 2025 Python Maint <python-maint@redhat.com> - 4.3.0-2
- Rebuilt for Python 3.14

* Mon Apr 14 2025 Gwyn Ciesla <gwync@protonmail.com> - 4.3.0-1
- 4.3.0

* Wed Feb 12 2025 Gwyn Ciesla <gwync@protonmail.com> - 4.2.1-1
- 4.2.1

* Wed Feb 05 2025 Gwyn Ciesla <gwync@protonmail.com> - 4.2.0-2
- Drop BR -t

* Thu Jan 23 2025 Gwyn Ciesla <gwync@protonmail.com> - 4.2.0-1
- 4.2.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 4.1.0-1
- 4.1.0

* Thu Apr 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.6.1-2
- Fix license tags

* Tue Apr 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.6.1-1
- Initial package.
