%global srcname  molecule-docker
%global pkgname  python-molecule-docker
%global forgeurl https://github.com/ansible-community/molecule-docker

%global common_description %{expand:
Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.
}

Name:           %{pkgname}
Version:        2.1.0
%forgemeta
Release:        %autorelease
Summary:        Molecule Docker plugin
License:        MIT
URL:            %{forgeurl}
Source:         %{pypi_source}
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%description %{common_description}

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%doc *.rst
%license LICENSE
%{python3_sitelib}/molecule_docker-%{version}.dist-info
%{python3_sitelib}/molecule_docker/

%changelog
%autochangelog