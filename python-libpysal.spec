%global srcname libpysal

Name:           python-%{srcname}
Version:        4.6.2
%global tag     v%{version}
Release:        %autorelease
Summary:        Python Spatial Analysis Library core components

License:        BSD
URL:            https://pysal.org
# PyPI source doesn't include test data or docs.
Source0:        https://github.com/pysal/libpysal/archive/%{tag}/%{srcname}-%{version}.tar.gz
# Test example datasets.
Source1:        https://geodacenter.github.io/data-and-lab//data/ncovr.zip
Source2:        https://github.com/sjsrey/newHaven/archive/master/newHaven.zip
Source3:        https://github.com/sjsrey/rio_grande_do_sul/archive/master/rio_grande_do_sul.zip
# Hard-code the list of datasets to not use the network.
Patch:          0001-Hard-code-list-of-example-datasets.patch
# We just use pytest directly.
Patch:          0002-Drop-use-of-pytest-runner.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(numpy) >= 1.3
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(scipy) >= 0.11
BuildRequires:  python3dist(setuptools)

BuildRequires:  python3dist(geomet)
BuildRequires:  python3dist(geopandas) >= 0.2
BuildRequires:  python3dist(matplotlib) >= 1.5.1
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(numba)
BuildRequires:  python3dist(rtree) >= 0.8
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(xarray)

%description
Core components of PySAL - A library of spatial analysis functions. Modules
include computational geometry, input and output, spatial weights, and built-in
example datasets.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Core components of PySAL - A library of spatial analysis functions. Modules
include computational geometry, input and output, spatial weights, and built-in
example datasets.


%package -n     python-%{srcname}-doc
Summary:        Documentation for python-libpysal

BuildRequires:  pandoc

%description -n python-%{srcname}-doc
Documentation files for python-libpysal


%prep
%autosetup -n %{srcname}-%{version} -p1

# The real pandoc is installed, no need for the Python package.
sed -i '/pandoc/d' requirements_docs.txt

mkdir -p pysal_data/pysal
unzip %SOURCE1 -d pysal_data/pysal/NCOVR
unzip %SOURCE2 -d pysal_data/pysal/newHaven
unzip %SOURCE3 -d pysal_data/pysal/Rio_Grande_do_Sul

%generate_buildrequires
%pyproject_buildrequires -x docs

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="%{pyproject_site_lib}" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
export XDG_DATA_HOME=$PWD/pysal_data
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n python-%{srcname}-doc
%doc html libpysal/examples
%license LICENSE.txt

%changelog
%autochangelog
