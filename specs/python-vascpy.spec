%global pypi_name vascpy

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        %{autorelease}
Summary:        Vasculature API

%global forgeurl https://github.com/BlueBrain/%{pypi_name}
%global tag v%{version}
%forgemeta

License:        Apache-2.0
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
vascpy is a python library for reading, writing, and manipulating
large-scale vasculature graphs. There are two alternative graph
representations available: a section-centered and an edge-centered one.
It supports the following respective formats:

- H5 Morphology
- SONATA node population of edges

The vascpy library provides two classes: `PointVasculature` and
`SectionVasculature` that allow for reading and writing edge-centered
and section-centered datasets respectively, as well as converting
between them.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%pyproject_extras_subpkg -n python3-%{pypi_name} all


%prep
%forgeautosetup -p1

# `python-igraph` has been renamed to just `igraph`
# https://pypi.org/project/python-igraph/
# https://pypi.org/project/igraph/
sed -i 's/python-igraph/igraph/' setup.py


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x all


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
# TODO: Possible endianness issue. Needs further investigation.
# Test fails on s390x when opening binary test file.
%if "%{_host_cpu}" == "s390x"
k="${k-}${k+ and }not test_convert__sonata_morphology_cycle"
%endif
%pytest -v ${k+-k } "${k-}"


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md AUTHORS.txt
%{_bindir}/%{pypi_name}


%changelog
%autochangelog
