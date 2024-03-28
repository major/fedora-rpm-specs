# This command-line tool is written in Rust, not Python, but it is distributed
# on PyPI (so it can be installed using pip, even though it does not provide an
# importable Python module), and it uses Python for testing. Since we judge
# that cramjam-cli is distributed on PyPI only for convenience of installation
# for pip users (similar to the cmake and ninja projects on PyPI), we choose to
# use %%cargo_build/%%cargo_install directly. This diverges slightly from
# upstream’s practice but is more straightforward.
#
# If we used %%pyproject_wheel/%%pyproject_install, we would get Python
# metadata in %%{python3_sitearch}/cramjam_cli-%%{version}.dist-info/ that
# would allow us to provide python3dist(cramjam-cli), but this would also
# create an otherwise-unnecessary dependency on the Python interpreter. If we
# needed to package this metadata, we would probably want to do it via a
# python3-cramjam-cli subpackage that contained only the metadata (and had a
# fully-versioned dependency on the base package) in order to keep the base
# package from depending on Python.

Name:           cramjam-cli
Version:        0.1.1
Release:        %autorelease
Summary:        Simple CLI to a variety of compression algorithms

# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# BSD-3-Clause
# BSD-3-Clause AND MIT (duplicate)
# MIT
# MIT OR Apache-2.0 (duplicate)
# MIT OR Zlib OR Apache-2.0
License:        %{shrink:
                (0BSD OR MIT OR Apache-2.0) AND
                Apache-2.0 AND
                (Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                MIT AND
                (MIT OR Zlib OR Apache-2.0)
                }
# LICENSE.dependencies contains a full license breakdown
URL:            https://pypi.org/project/cramjam-cli/
# Currently, releases appear on PyPI but are not tagged in the GitHub
# repository, https://github.com/milesgranger/cramjam, where this is developed
# together with rust-libcramjam and python-cramjam. Since the PyPI sdist
# contains everything we need to build and test this package, there is no
# problem with treating it as the canonical source.
Source0:        %{pypi_source cramjam_cli}
# Hand-written for Fedora in groff_man(7) format based on --help output
Source1:        cramjam-cli.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Remove relative libcramjam dep for python builds
# See: https://github.com/milesgranger/cramjam/pull/131
# Update libcramjam crate to 0.3.0 in cramjam-cli
# See: https://github.com/milesgranger/cramjam/pull/152
# Combined and rebased on the released PyPI sdist
Patch:          cramjam-cli-0.1.1-system-libcramjam-crate.patch
# Fix missing LICENSE file in cramjam-cli
# https://github.com/milesgranger/cramjam/pull/137
# Rebased on the released PyPI sdist
Patch:          cramjam-cli-0.1.1-license-file.patch

BuildRequires:  python3-devel
BuildRequires:  tomcli
BuildRequires:  cargo-rpm-macros >= 24

# Required for tests, but not in the dev extra (probably because it is built
# from the same workspace):
BuildRequires:  %{py3_dist cramjam}

%description
%{summary}.


%prep
%autosetup -n cramjam_cli-%{version} -p1

# Do not strip the compiled executable; we need useful debuginfo. Upstream set
# this intentionally, so this makes sense to keep downstream-only. Note that
# this patch is not strictly needed unless we start building with
# %%pyproject_wheel/%%pyproject_install.
tomcli set pyproject.toml false 'tool.maturin.strip'

# Remove bundled rust-libcramjam.
rm -rv local_dependencies/

%cargo_prep


%generate_buildrequires
%pyproject_buildrequires -x dev
%cargo_generate_buildrequires


%build
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies
%cargo_build


%install
%cargo_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
%pytest -v


%files
%license LICENSE LICENSES.dependencies
%doc README.md
%{_bindir}/cramjam-cli
%{_mandir}/man1/cramjam-cli.1*


%changelog
%autochangelog
