%bcond_with docs
%bcond_without tests

%global pypi_name nashpy
%global pretty_name Nashpy

%global forgeurl https://github.com/drvinceknight/Nashpy
Version:        0.0.43
%global tag     v%{version}
%forgemeta

%global _description %{expand:
This library implements the following algorithms for Nash equilibria
on 2 player games: Support enumeration, Best response polytope vertex
enumeration, Lemke Howson algorithm.}

Name:           python-%{pypi_name}
Release:        %autorelease
Summary:        A library to compute equilibria of 2 player normal form games

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with docs}
# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
#missing for now
#BuildRequires:  python3dist(sphinx-togglebutton)
%endif

%if %{with tests}
# For tests
# See testenv.deps in tox.ini, but note that it is mostly linters etc.,
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.
%endif

%prep
%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%if %{with docs}
# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files nashpy

%check
%if %{with tests}
%pytest --ignore-glob='benchmarks/*' -v
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES.md CITATION.md paper paper.bib

%if %{with docs}
%files doc
%license LICENSE
%doc html/
%endif

%changelog
%autochangelog
