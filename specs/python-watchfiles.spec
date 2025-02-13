Name:           python-watchfiles
Version:        1.0.4
Release:        %autorelease
Summary:        Simple, modern and high performance file watching and code reload in python
# The main source code is under the MIT license.  See the license field of the
# python3-watchfiles subpackage for the licenses of statically linked rust
# dependencies.
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
Source:         %{pypi_source watchfiles}

# Update notify dependency to 8.0.0, bumping MSRV to 1.77
# https://github.com/samuelcolvin/watchfiles/pull/327
#
# (We take only the commits changing Cargo.toml, not the ones updating
# Cargo.lock and the CI configuration.)
#
# Update notify to version 8.0.0
Patch:          %{url}/pull/327/commits/a3f7c8d61615d5831b60056aa8e0001a29989416.patch
# Bump MSRV to 1.77 for notify 8.0.0
Patch:          %{url}/pull/327/commits/d05eadcd47447f5abefbf5e158586aa820ecd13b.patch

# Downstream-only: allow a slightly older pytest to support EPEL10
Patch:          0001-Downstream-only-allow-a-slightly-older-pytest-to-sup.patch

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24

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
# Apache-2.0 OR MIT
# CC0-1.0
# ISC
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
                MIT AND
                Apache-2.0 AND
                CC0-1.0 AND
                ISC AND
                (MIT OR Apache-2.0) AND
                (Unlicense OR MIT)
                }


%description -n python3-watchfiles %_description


%prep
%autosetup -n watchfiles-%{version} -p1

# Remove unnecessary Python test requirements
sed -e '/"coverage\b/d' \
    -e '/"pytest-pretty\b/d' \
    -e '/"pytest-timeout\b/d' \
    -i pyproject.toml
# Loosen the minimum maturin version for testing
# https://bugzilla.redhat.com/show_bug.cgi?id=2329012
sed -e 's/maturin>=1.8.1/maturin>=1.7.4/' -i pyproject.toml

# Remove pytest timeout config
sed -e '/timeout =/d' -i pyproject.toml

# Remove "generate-import-lib" feature for pyo3; applicable only on Windows,
# and not packaged.
sed -e 's/\(pyo3.*\), "generate-import-lib"/\1/' -i Cargo.toml

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
%pyproject_save_files watchfiles

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
