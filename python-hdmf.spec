# XXX: note for maintainers
# Do NOT update HDMF without checking if packages that depend on it, for example python-pynwb can be installed with the new version

%bcond_without tests

%global desc %{expand:
The Hierarchical Data Modeling Framework The Hierarchical Data Modeling
Framework, or *HDMF* is a Python package for working with hierarchical data. It
provides APIs for specifying data models, reading and writing data to different
storage backends, and representing data with Python object.Documentation of
HDMF can be found at Release. Documentation of HDMF can be found at 
https://hdmf.readthedocs.io}

Name:           python-hdmf
Version:        3.6.0
Release:        %autorelease
Summary:        A package for standardizing hierarchical object data

License:        BSD-3-Clause-LBNL
URL:            https://github.com/hdmf-dev/hdmf
Source0:        %{url}/releases/download/%{version}/hdmf-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on help output
Source1:        validate_hdmf_spec.1

# Downstream-only: Patch out coverage from pytest invocation
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Patch-out-coverage-from-pytest-invocation.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
# Enables an optional integration test with this library:
BuildRequires:  python3dist(tqdm)
%endif

%description %{desc}

%package -n python3-hdmf
Summary:        %{summary}

# The source directory src/hdmf/common/hdmf-common-schema (installed as
# %%{python3_sitelib}/hdmf/common/hdmf-common-schema) is a git submodule
# corresponding to https://github.com/hdmf-dev/hdmf-common-schema, which
# contains no script or configuration for installing it separately system-wide.
# Nonetheless, as it is separately versioned, it may be a candidate for
# unbundling.
#
# The version number can be read from
# src/hdmf/common/hdmf-common-schema/common/namespace.yaml, in
# ['namespaces'][0]['version'].
#
# It is released under the same BSD-3-Clause-LBNL as python-hdmf.
Provides:       bundled(hdmf-common-schema) = 1.6.0

%description -n python3-hdmf %{desc}

%pyproject_extras_subpkg -n python3-hdmf zarr

%prep
%autosetup -n hdmf-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x zarr

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hdmf
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'

%check
%if %{with tests}
%pytest
%endif

%files -n python3-hdmf -f %{pyproject_files}
%license license.txt
%doc README.rst Legal.txt
%{_bindir}/validate_hdmf_spec
%{_mandir}/man1/validate_hdmf_spec.1*

%changelog
%autochangelog
