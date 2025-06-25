Name:           python-watchfiles
Version:        1.1.0
Release:        %autorelease
Summary:        Simple, modern and high performance file watching and code reload in python
# The main source code is under the MIT license.  See the license field of the
# python3-watchfiles subpackage for the licenses of statically linked rust
# dependencies.
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
Source:         %{pypi_source watchfiles}

# Downstream-only: allow a slightly older pytest to support EPEL10
Patch:          0001-Downstream-only-allow-a-slightly-older-pytest-to-sup.patch

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
Simple, modern and high performance file watching and code reload in python.
Underlying file system notifications are handled by the Notify rust library.}


%description %_description


%package -n python3-watchfiles
Summary:        %{summary}
# The main source code is under the MIT license. This license field includes
# the licenses of statically linked rust dependencies, based on the output of
# %%{cargo_license_summary}:
#
# CC0-1.0
# ISC
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
                MIT AND
                CC0-1.0 AND
                ISC AND
                (MIT OR Apache-2.0) AND
                (Unlicense OR MIT)
                }


%description -n python3-watchfiles %_description


%prep
%autosetup -n watchfiles-%{version} -p1

# Remove unnecessary Python test requirements
tomcli set pyproject.toml lists delitem \
    'dependency-groups.dev' '^(coverage|pytest-(pretty|timeout)).*'

# Remove pytest timeout config
tomcli set pyproject.toml del 'tool.pytest.ini_options.timeout'

# Remove "generate-import-lib" feature for pyo3; applicable only on Windows,
# and not packaged.
tomcli set Cargo.toml lists delitem 'dependencies.pyo3.features' \
    'generate-import-lib'

# Remove unused Cargo config that contains buildflags for Darwin
rm .cargo/config.toml

%cargo_prep


%generate_buildrequires
%pyproject_buildrequires -g dev
%cargo_generate_buildrequires


%build
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

export RUSTFLAGS='%{build_rustflags}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l watchfiles

# The maturin build backend includes the license files, but currently the
# pyproject macros don't mark these files as licenses.
sed -e '/LICENSE/ s/^/%%license /' -i %{pyproject_files}


%check
# We must set the import mode during tests to avoid the watchfiles directory
# (which will not have the compiled module) taking precedence for the import.
# https://docs.pytest.org/en/7.4.x/explanation/pythonpath.html
%pytest --import-mode append -k "${k-}" -v --full-trace


%files -n python3-watchfiles -f %{pyproject_files}
%doc README.md
%{_bindir}/watchfiles


%changelog
%autochangelog
