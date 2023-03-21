# Tests don't currently run:
# using hatch requires setting up a local dev environment
# using pytest breaks as sources are split between src/fixit and legacy
%bcond_with tests

%global pypi_name fixit

%global common_description %{expand:
Fixit is a lint framework that complements Flake8. It’s based on LibCST
which makes it possible to provide auto-fixes. Lint rules are made easy to
build through pattern matching, a test toolkit, and utility helpers (e.g.
scope analysis) for non-trivial boilerplate. It is optimized for efficiency,
easy to customize and comes with many builtin lint rules.}

%global date 20230223
%global commit d2b59da3f822555e433eb6776e1f40f4b92c18d5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        0.1.5~%{date}g%{shortcommit}
Release:        %autorelease
Summary:        A lint framework that writes better Python code for you

License:        MIT
URL:            https://github.com/Instagram/Fixit
# PyPI tarball doesn't include docs
# Source:         %%{url}/archive/v%%{version}/Fixit-%%{version}.tar.gz
Source:         %{url}/archive/%{commit}/%{pypi_name}-%{shortcommit}.tar.gz
Patch:          %{name}-pregenerate_version.diff
Patch:          %{name}-rm-unused-inventories.diff
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-mdinclude)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}

%package        doc
Summary:        %{name} documentation
Requires:       python3-docs

%description    doc
Documentation for %{name}

%prep
%autosetup -n Fixit-%{commit} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD}/src sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import
%if %{with tests}
hatch run test
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md
%{_bindir}/fixit


%files doc
%doc html
%license LICENSE


%changelog
%autochangelog
