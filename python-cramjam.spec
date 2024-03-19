%bcond tests 1

Name:           python-cramjam
Version:        2.8.2
Release:        %autorelease
Summary:        Thin Python bindings to de/compression algorithms in Rust

# SPDX
License:        MIT
URL:            https://github.com/milesgranger/cramjam
# The PyPI sdist is structured like the git repository, but with pyproject.toml
# moved to the top level from cramjam-python/ and
#   manifest-path = "cramjam-python/Cargo.toml"
# added to the [tool.maturin] section. We find it easiest to just build from
# the GitHub source archive.
Source:         %{url}/archive/v%{version}/cramjam-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  tomcli
BuildRequires:  cargo-rpm-macros >= 24

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-cramjam
Summary:        %{summary}
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# BSD-3-Clause
# BSD-3-Clause AND MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
License:        %{shrink:
                (0BSD OR MIT OR Apache-2.0) AND
                Apache-2.0 AND
                BSD-3-Clause AND
                MIT AND
                (MIT OR Apache-2.0) AND
                (MIT OR Zlib OR Apache-2.0)
                }
# LICENSE.dependencies contains a full license breakdown

%description -n python3-cramjam %{common_description}


%prep
%autosetup -n cramjam-%{version}

# Do not strip the compiled Python module; we need useful debuginfo. Upstream
# set this intentionally, so this makes sense to keep downstream-only.
tomcli set cramjam-python/pyproject.toml false 'tool.maturin.strip'

# Downstream-only: patch out linters/formatters/etc. from the “dev” extra so we
# can use it to generate test dependencies.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set cramjam-python/pyproject.toml lists delitem --type regex \
    'project.optional-dependencies.dev' '(black)\b.*'

# Remove bundled rust-libcramjam and the sources for cramjam-cli, which is
# versioned and released separately. Keep only the contents of cramjam-python/
# and the LICENSE file.
find . -mindepth 1 -maxdepth 1 ! -type d ! -name LICENSE -print -delete
find . -mindepth 1 -maxdepth 1 -type d ! -name cramjam-python \
    -exec rm -rv '{}' '+'

cd cramjam-python
%cargo_prep


%generate_buildrequires
cd cramjam-python
%pyproject_buildrequires %{?with_tests:-x dev}
%cargo_generate_buildrequires


%build
export RUSTFLAGS='%{build_rustflags}'
cd cramjam-python
%cargo_license_summary
%{cargo_license} > ../LICENSES.dependencies
%pyproject_wheel


%install
cd cramjam-python
%pyproject_install
%pyproject_save_files cramjam


%check
cd cramjam-python
%pyproject_check_import
%if %{with tests}
%pytest -v -n auto --ignore-glob='benchmarks/*'
%endif


%files -n python3-cramjam -f %{pyproject_files}
%license LICENSE LICENSES.dependencies
%doc cramjam-python/README.md


%changelog
%autochangelog
