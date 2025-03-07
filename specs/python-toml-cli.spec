Name:           python-toml-cli
Version:        0.7.0
Release:        %autorelease
Summary:        Read and write keys/values to/from toml files

License:        MIT
URL:            https://github.com/mrijken/toml-cli
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/toml-cli-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Command line interface for toml files.}

%description %_description

%package -n     python3-toml-cli
Summary:        %{summary}

%description -n python3-toml-cli %_description

%package -n     toml-cli
Summary:        %{summary}
Requires:       python3-toml-cli
# Provides a binary at the same path
Conflicts:      libtoml

%description -n toml-cli %_description

%prep
%autosetup -p1 -n toml-cli-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L toml_cli

%check
%pytest -v

%files -n python3-toml-cli -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%files -n toml-cli
%{_bindir}/toml

%changelog
%autochangelog
