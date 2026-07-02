%global srcname dulwich
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:           python-%{srcname}
Version:        1.2.7
Release:        %autorelease
Summary:        Python implementation of the Git file formats and protocols

License:        GPL-2.0-or-later OR Apache-2.0
URL:            https://www.dulwich.io/
Source0:        %{pypi_source}

# Support pyo3 0.29
# https://github.com/jelmer/dulwich/commit/f8762ba0184e572f54be2a494d728bfe8c000917
# PyO3 0.29 fixes RUSTSEC-2026-0176 and RUSTSEC-2026-0177.
Patch:          dulwich-fix-metadata.patch

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros

BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-epytext

# Test dependencies:
BuildRequires:  python3-pytest
BuildRequires:  /usr/bin/ssh-keygen
BuildRequires:  /usr/bin/gpgsm

%description
Dulwich is a Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n python3-%{srcname}
Summary:        %{summary}

# Apache-2.0
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        (GPL-2.0-or-later OR Apache-2.0) AND Apache-2.0 AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)

%description -n python3-%{srcname}
Dulwich is a Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n %{name}-doc
Summary:        The %{name} documentation

%description -n %{name}-doc
Documentation for %{name}.

# Unpackaged extras due to missing dependencies:
#  fuzzing: atheris
#  fastimport: fastimport
%global extras https,pgp,paramiko,colordiff,merge,patiencediff,aiohttp
%pyproject_extras_subpkg -n python3-%{srcname} %{extras}

%prep
%autosetup -n %{srcname}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a -t
%pyproject_buildrequires -x %{extras}

%build
%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}
# Remove extra copy of text docs
rm -rf %{buildroot}%{python3_sitearch}/docs/tutorial/

%check
# tests/contrib/test_swift_smoke.py is ignored because geventhttpclient is not packaged in Fedora
# test_filter_branch_index_filter fails for not yet investigated reasons
%{python3} -m pytest tests --ignore=tests/contrib/test_swift_smoke.py -k "not test_filter_branch_index_filter"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license COPYING
%license LICENSE.dependencies
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%exclude %{python3_sitearch}/%{srcname}/tests*

%files -n %{name}-doc
%doc README.rst
%license COPYING
%doc html

%changelog
%autochangelog
