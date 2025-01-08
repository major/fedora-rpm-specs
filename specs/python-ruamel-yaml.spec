# Breaks the circular dependency with ruamel.yaml.clib.
%bcond_with bootstrap

%global commit 04ba5ead9be050430fac2ca1d4e88b8e91f7be02

Name:           python-ruamel-yaml
Version:        0.18.10
Release:        %autorelease
Summary:        YAML 1.2 loader/dumper package for Python

# SPDX
License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml
# The PyPI sdist does not contain tests, so we use a snapshot from SourceForge
Source:         https://sourceforge.net/code-snapshots/hg/r/ru/ruamel-yaml/code/ruamel-yaml-code-%{commit}.zip

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

%description -n python3-ruamel-yaml %{_description}

%prep
%autosetup -n ruamel-yaml-code-%{commit}
# Upstream upper-bounds the Python interpeter versions with which the C
# implementation (ruamel.yaml.clib dependency) may be used. Patch this out.
sed -r -i 's/( and python_version<"[^"]+")(.*ruamel\.yaml\.clib)/\2/' \
    __init__.py
%if %{with bootstrap}
sed -r -i 's/^([[:blank:]]*)(.*ruamel\.yaml\.clib)/\1# \2/' __init__.py
%endif

%generate_buildrequires
%pyproject_buildrequires

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

%changelog
%autochangelog
