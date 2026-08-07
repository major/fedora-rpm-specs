%global forgeurl https://github.com/mrijken/toml-cli
Version:        0.8.2
%forgemeta

Name:           python-toml-cli
Release:        %autorelease
Summary:        Read and write keys/values to/from toml files

License:        Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

# Lower tomlkit dependency to match Fedora Rawhide (0.13.2)
Patch0:         0002-lower-tomlkit-dependency.patch
# Skip test_set_in_out_of_order_table on tomlkit < 0.13.3 due to lack of upstream fix
Patch1:         0003-skip-out-of-order-table-test-on-older-tomlkit.patch

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
