%global pypi_name rjsmin
%global desc %{expand: \
The minifier is based on the semantics of jsmin.c by Douglas Crockford.

The module is a re-implementation aiming for speed, so it can be used at
runtime (rather than during a preprocessing step). Usually it produces the
same results as the original jsmin.c.}

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        %autorelease
Summary:        Javascript Minifier

License:        Apache-2.0
URL:            http://opensource.perlig.de/rjsmin/
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme

%description %{desc}

%package -n python3-%{pypi_name}
Summary:	Javascript Minifier

%description -n python3-%{pypi_name}
%{desc}

%package docs
Summary:	Javascript Minifier - docs

%description docs
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

# strip bang path from rjsmin.py
sed -i '1d' rjsmin.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sphinx-build -b html docs/_userdoc docs/_userdoc/html
# Remove the sphinx-build leftovers.
rm -rf docs/_userdoc/html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
	
%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_%{pypi_name}.cpython*

%files docs
%license LICENSE
%doc README.md docs/_userdoc/html

%changelog
%autochangelog
