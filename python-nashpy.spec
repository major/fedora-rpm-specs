%bcond_with docs
%bcond_without tests

%global pypi_name nashpy
%global pretty_name Nashpy

%global _description %{expand:
This library implements the following algorithms for Nash equilibria
on 2 player games: Support enumeration, Best response polytope vertex
enumeration, Lemke Howson algorithm.}

Name:           python-%{pypi_name}
Version:        0.0.41
Release:        %autorelease
Summary:        A library to compute equilibria of 2 player normal form games

License:        MIT
URL:            https://github.com/drvinceknight/%{pretty_name}
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
#missing for now
#BuildRequires:  python3dist(sphinx-togglebutton)
# For tests
BuildRequires:  python3dist(pytest-benchmark)

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
%autosetup -n %{pretty_name}-%{version}

# Remove deps on code checkers/linters
sed -i '/^    darglint\b/d' tox.ini

%generate_buildrequires	
%pyproject_buildrequires -t


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
%pytest
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
