Name:           python-watchfiles
Version:        0.20.0
Release:        %autorelease
Summary:        Simple, modern and high performance file watching and code reload in python
# The main source code is under the MIT license.  See the license field of the
# python3-watchfiles subpackage for the licenses of statically linked rust
# dependencies.
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
Source:         %{pypi_source watchfiles}

BuildRequires:  python3-devel
BuildRequires:  rust-packaging

%global _description %{expand:
Simple, modern and high performance file watching and code reload in python.
Underlying file system notifications are handled by the Notify rust library.}


%description %_description


%package -n python3-watchfiles
Summary:        %{summary}
# The main source code is under the MIT license.  This license field includes
# the licenses of statically linked rust dependencies.
License:        MIT AND Apache-2.0 AND CC0-1.0 AND ISC AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)


%description -n python3-watchfiles %_description


%prep
%autosetup -n watchfiles-%{version}

# Remove unnecessary Python test requirements
sed -e '/^coverage\b/d' \
    -e '/^pytest-pretty\b/d' \
    -e '/^pytest-timeout\b/d' \
    -i requirements/testing.in

# Remove pytest timeout config
sed -e '/timeout =/d' -i pyproject.toml

# Remove unused Cargo config that contains buildflags for Darwin
rm .cargo/config.toml

%cargo_prep


%generate_buildrequires
%pyproject_buildrequires requirements/testing.in
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
%pytest --import-mode append -v


%files -n python3-watchfiles -f %{pyproject_files}
%doc README.md
%{_bindir}/watchfiles


%changelog
%autochangelog