%global pypi_name markups

Name:           python-%{pypi_name}
Version:        4.1.1
Release:        %autorelease
Summary:        A wrapper around various text markups

License:        BSD-3-Clause
URL:            https://github.com/retext-project/pymarkups
Source0:        %{pypi_source markups}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)


%description
This module provides a wrapper around various text markup languages. Available
by default are Markdown, reStructuredText and Textile, but you can easily
add your own markups.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module provides a wrapper around various text markup languages. Available
by default are Markdown_, reStructuredText_ and Textile_, but you can easily
add your own markups.


%package -n python-%{pypi_name}-doc
Summary:        markups documentation
%description -n python-%{pypi_name}-doc
Documentation for markups


%pyproject_extras_subpkg -n python3-markups markdown restructuredtext textile asciidoc

%prep
%autosetup -p1 -n markups-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x markdown -x asciidoc -x textile -x highlighting


%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pytest -v tests/


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html


%changelog
%autochangelog
