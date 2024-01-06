%bcond tests 1

%global _description %{expand:
In computer science, a topological sort (sometimes abbreviated topsort or
toposort) or topological ordering of a directed graph is a linear ordering of
its vertices such that for every directed edge uv from vertex u to vertex v, u
comes before v in the ordering.}

Name:           python-toposort
Version:        1.10
Release:        %autorelease
Summary:        Implements a topological sort algorithm

# SPDX
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/toposort
Source0:        %{pypi_source toposort}
BuildArch:      noarch

%description %_description

%package -n python3-toposort
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-toposort %_description

%prep
%autosetup -n toposort-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l toposort

%check
%if %{with tests}
%{py3_test_envvars} '%{python3}' -m test.test_toposort
%endif

%files -n python3-toposort -f %{pyproject_files}
%doc CHANGES.txt
%doc README.md

%changelog
%autochangelog
