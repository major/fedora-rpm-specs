Name:           python-id
Version:        1.5.0
Release:        %autorelease
Summary:        A tool for generating OIDC identities

License:        Apache-2.0
URL:            https://github.com/di/id
Source:         %{pypi_source id}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pretend


%global _description %{expand:
id is a Python tool for generating OIDC identities. It can automatically
detect and produce OIDC credentials on a number of environments,
including GitHub Actions, GitLab pipelines and Google Cloud.}

%description %_description

%package -n     python3-id
Summary:        %{summary}

%description -n python3-id %_description


%prep
%autosetup -p1 -n id-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files id


%check
%pyproject_check_import
%pytest


%files -n python3-id -f %{pyproject_files}
%license LICENSE


%changelog
%autochangelog
