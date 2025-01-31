%bcond_without check

Name:           python-tomli-w
Version:        1.2.0
Release:        %autorelease
Summary:        A Python library for writing TOML

# SPDX
License:        MIT
URL:            https://github.com/hukkin/tomli-w
Source0:        %{url}/archive/%{version}/tomli-w-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Tomli-W is a Python library for writing TOML. It is a write-only counterpart
to Tomli, which is a read-only TOML parser. Tomli-W is fully compatible
with TOML v1.0.0.}

%description %_description

%package -n python3-tomli-w
Summary:        %{summary}

%description -n python3-tomli-w %_description


%prep
%autosetup -p1 -n tomli-w-%{version}
# Measuring coverage is discouraged in Python packaging guidelines:
sed -i '/pytest-cov/d' tests/requirements.txt
# We don't need tomli on Python 3.11+
%if v"%{python3_version}" >= v"3.11"
sed -i '/tomli/d' tests/requirements.txt
sed -Ei 's/tomli(\.|$)/tomllib\1/' tests/*.py
%endif
# This testing dependency is optional and we don't have it in (EP)EL,
# it has many missing transitive dependencies that we don't want to maintain
%if 0%{?rhel}
sed -i '/pytest-randomly/d' tests/requirements.txt
%endif


%generate_buildrequires
# We intentionally don't use tox here to avoid a dependency on it in ELN/RHEL,
# the tox deps only list -r tests/requirements.txt anyway and sometimes
# did not run any tests at all.
%pyproject_buildrequires %{?with_check:tests/requirements.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tomli_w


%check
%pyproject_check_import tomli_w
%if %{with check}
%pytest -v
%endif


%files -n python3-tomli-w -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE


%changelog
%autochangelog
