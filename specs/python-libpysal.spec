%global srcname libpysal

Name:           python-%{srcname}
Version:        4.14.1
Release:        %autorelease
Summary:        Python Spatial Analysis Library core components

License:        BSD-3-Clause
URL:            https://pysal.org
Source0:        %pypi_source %{srcname}
# Test example datasets.
Source1:        https://geodacenter.github.io/data-and-lab/data/ncovr.zip
Source2:        https://github.com/sjsrey/newHaven/archive/master/newHaven.zip
Source3:        https://github.com/sjsrey/rio_grande_do_sul/archive/master/rio_grande_do_sul.zip
Source4:        https://github.com/sjsrey/taz/archive/master/taz.zip
# The real pandoc is installed, no need for the Python package.
Patch:          0001-Remove-unused-build-requirements.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(networkx)
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
# Needed for the ipython3 pygments lexer.
BuildRequires:  python3dist(ipython)

%description -n python-%{srcname}-doc
Documentation files for python-libpysal


%prep
%autosetup -n %{srcname}-%{version} -p1

pushd docs
# We aren't yet installed in a way that importlib.metadata will find the
# version, so manually set it.
sed -i 's/libpysal.__version__/"%{version}"/g' conf.py
# Make notebooks visible to docs.
ln -s ../notebooks
popd

mkdir -p pysal_data/pysal
unzip %SOURCE1 -d pysal_data/pysal/NCOVR
unzip %SOURCE2 -d pysal_data/pysal/newHaven
unzip %SOURCE3 -d pysal_data/pysal/Rio_Grande_do_Sul
unzip %SOURCE4 -d pysal_data/pysal/taz

%generate_buildrequires
%pyproject_buildrequires -x docs,tests

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
export XDG_DATA_HOME=$PWD/pysal_data
%{pytest} -m 'not network'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%files -n python-%{srcname}-doc
%doc html libpysal/examples
%license LICENSE.txt

%changelog
%autochangelog
