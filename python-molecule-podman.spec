%global srcname molecule-podman
%global setup_flags SKIP_PIP_INSTALL=1 PBR_VERSION=%{version}

Name: python-molecule-podman
Version: 1.0.1
Release: 4%{?dist}
Summary: Molecule Podman plugin
License: MIT

URL: https://github.com/ansible-community/molecule-podman
Source0: %{pypi_source}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(toml)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(setuptools-scm-git-archive)

%description
Molecule Podman Plugin is designed to allow use podman containers for
provisioning test resources.

%package -n python3-molecule-podman
Summary: %summary

Requires: python3dist(podman)
Requires: python3dist(molecule) >= 3.4
Requires: python3dist(ansible-compat) >= 0.5


%{?python_disable_dependency_generator}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-molecule-podman
Molecule Podman Plugin is designed to allow use podman containers for
provisioning test resources.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-molecule-podman
%license LICENSE
%{python3_sitelib}/molecule_podman-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/molecule_podman/
%doc *.rst

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.0.1-1
- Update to version 1.0.1 (#2018838)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.3.0-1
- update to version 0.3.0

* Thu Oct 15 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.1-1
- initial package
