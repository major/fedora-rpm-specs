Name:           python-rignore
Version:        0.6.4
Release:        %autorelease
Summary:        Python bindings for the ignore crate

License:        MIT
URL:            https://github.com/patrick91/rignore
Source:         %{url}/archive/v%{version}/rignore-%{version}.tar.gz

# Update PyO3 to 0.26
# https://github.com/patrick91/rignore/pull/13
# (without changes to Cargo.lock)
Patch:          rignore-0.6.4-pyo3-0.26.patch

BuildSystem:            pyproject
BuildOption(install):   -l rignore

BuildRequires:  tomcli
BuildRequires:  cargo-rpm-macros >= 24

# Test dependencies; see [tool.pdm.dev-dependencies]
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist typing-extensions}

%global common_description %{expand:
rignore is a Python module that provides a high-performance, Rust-powered file
system traversal functionality. It wraps the Rust ignore crate using PyO3,
offering an efficient way to walk through directories while respecting various
ignore rules.}

%description %{common_description}


%package -n     python3-rignore
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
                MIT AND
                Unicode-DFS-2016 AND
                (MIT OR Apache-2.0) AND
                (Unlicense OR MIT)
                }

%description -n python3-rignore %{common_description}


%prep -a
%cargo_prep


%generate_buildrequires -a
%cargo_generate_buildrequires


%build -p
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%check -a
%pytest


%files -n python3-rignore -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
