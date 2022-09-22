# what it's called on pypi
%global srcname graphviz

%global common_description %{expand:
This package facilitates the creation and rendering of graph descriptions in
the DOT language of the Graphviz graph drawing software (master repo) from
Python.

Create a graph object, assemble the graph by adding nodes and edges, and
retrieve its DOT source code string. Save the source code to a file and
render it with the Graphviz installation of your system.}

Name:           python-%{srcname}
Version:        0.20.1
Release:        %autorelease
# Set Epoch to avoid being obsoleted by graphviz-python
Epoch:          1
Summary:        Simple Python interface for Graphviz

License:        MIT
URL:            https://github.com/xflr6/graphviz
Source0:        %url/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Requires:       graphviz

%description -n python3-%{srcname} %{common_description}

%package -n python-%{srcname}-doc
Summary:        Documentation for %{name}

%description -n python-%{srcname}-doc
%{common_description}

This is the documentation package for %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

sed -i 's/\r//' docs/*.rst
sed -i 's/\r//' README.rst

%generate_buildrequires
%pyproject_buildrequires -t -x docs
echo "graphviz"

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname} 

%check
%pytest --skip-exe \
        --only-exe \
        --collect-only \
        --verbose \
        --pdb \
        --exitfirst \
        --doctest-report none

%files -n python3-%{srcname} -f %{pyproject_files}

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt

%changelog
%autochangelog
