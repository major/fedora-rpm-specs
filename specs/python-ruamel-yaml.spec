# Breaks the circular dependency with ruamel.yaml.clib.
%bcond_with bootstrap

Name:           python-ruamel-yaml
Version:        0.19.1
Release:        %autorelease
Summary:        YAML 1.2 loader/dumper package for Python

# SPDX
License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml
# The PyPI sdist does not contain tests, so we use a snapshot from SourceForge
Source:         https://yaml.dev/ruamel-dl-tagged-releases/ruamel.yaml-%{version}.tar.xz

BuildArch:      noarch

%global _description %{expand:
ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of
comments, seq/map flow style, and map key order.}

%description %{_description}

%package -n     python3-ruamel-yaml
Summary:        YAML 1.2 loader/dumper package for Python

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%py_provides python3-ruamel.yaml

%if !%{with bootstrap}
# ruamel.yaml.clibz is not available in Fedora (and probably never will
# be), so require the old clib backend
Requires:       python3-ruamel-yaml+oldlibyaml = %{version}-%{release}
%endif

%description -n python3-ruamel-yaml %{_description}

%prep
%autosetup -n ruamel.yaml-%{version}

%generate_buildrequires
%pyproject_buildrequires %{!?with_bootstrap:-x oldlibyaml}

%build
%pyproject_wheel

%install
%pyproject_install
# RFE: Add option for namespace packages to %%pyproject_save_files
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%pyproject_save_files -l ruamel

%check
%if %{with bootstrap}
k="${k-}${k+ and }not test_load_cyaml"
k="${k-}${k+ and }not test_load_cyaml_1_2"
k="${k-}${k+ and }not test_dump_cyaml_1_2"
%endif
%pytest -k "${k-}" _test/test_*.py

%files -n python3-ruamel-yaml -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-ruamel-yaml oldlibyaml

%changelog
%autochangelog
