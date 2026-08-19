%global forgeurl https://github.com/pyinfra-dev/pyinfra
Version:        3.10.0
%forgemeta

Name:           python-pyinfra
Release:        %autorelease
Summary:        Provision, manage and deploy infrastructure

License:        MIT
URL:            https://pyinfra.com
Source:         %{forgesource}
Patch:          pyproject-toml-static-version.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
pyinfra turns Python code into shell commands and runs them on your
servers. Execute ad-hoc commands and write declarative operations.
Target SSH servers, local machine and Docker containers.}

%description %_description

%package -n     python3-pyinfra
Summary:        %{summary}

%description -n python3-pyinfra %_description


%prep
%forgesetup
%autopatch -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pyinfra pyinfra_cli


%check
%pyproject_check_import
# Unit tests require pyinfra-testing which is not packaged in Fedora


%files -n python3-pyinfra -f %{pyproject_files}
%{_bindir}/pyinfra
%doc README.md
%doc CHANGELOG.md
%doc docs

%changelog
%autochangelog
