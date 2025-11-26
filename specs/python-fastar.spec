Name:           python-fastar
Version:        0.7.0
Release:        %autorelease
Summary:        High-level bindings for the Rust tar crate

License:        MIT
URL:            https://github.com/DoctorJohn/fastar
Source:         %{url}/archive/v%{version}/fastar-%{version}.tar.gz

# Update pyo3 to 0.27 
# https://github.com/DoctorJohn/fastar/pull/44
#
# Downstream, also allow PyO3 0.26, RHBZ#2404994, and don’t include changes to
# Cargo.lock since we don’t use it.
Patch:          fastar-0.6.0-pyo3-0.27.patch

BuildSystem:            pyproject
BuildOption(install):   -l fastar

BuildRequires:  tomcli
BuildRequires:  cargo-rpm-macros >= 24

# Test dependencies; see the “dev” dependency group, which also contains
# unwanted linters, type-checkers, benchmarking tools, etc.,
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
BuildRequires:  %{py3_dist psutil}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist typing-extensions}

%global common_description %{expand:
The fastar library wraps the Rust tar, flate2, and zstd crates, providing a
high-performance way to work with compressed and uncompressed tar archives in
Python.}

%description %{common_description}


%package -n     python3-fastar
Summary:        %{summary}
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
License:        %{shrink:
                MIT AND
                (0BSD OR MIT OR Apache-2.0) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (MIT OR Apache-2.0) AND
                (MIT OR Zlib OR Apache-2.0)
                }

%description -n python3-fastar %{common_description}


%prep -a
%cargo_prep


%generate_buildrequires -a
%cargo_generate_buildrequires


%build -p
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%check -a
# These tests assume there are no open file descriptors inherited from the
# environment, which is not a good assumption. They fail because the process
# has /usr/lib/sysimage/rpm/.rpm.lock open.
k="${k-}${k+ and }not test_close_closes_archive"
k="${k-}${k+ and }not test_context_manager_closes_archive"
k="${k-}${k+ and }not test_unpack_preserves_file_modification_time_only_if_option_is_true"

# We are not interested in benchmarks
ignore="${ignore-} --ignore=tests/benchmarks/"

%pytest -k "${k-}" ${ignore} -v



%files -n python3-fastar -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
