%global srcname numcodecs

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        Buffer compression and transformation for data storage and communication

License:        MIT
URL:            https://github.com/alimanfoo/numcodecs
Source0:        %pypi_source %{srcname}
# Fedora specific
Patch:          0001-Unbundle-blosc.patch
Patch:          0002-Unbundle-zstd.patch
Patch:          0003-Unbundle-lz4.patch
# Fedora is not missing Snappy support in Blosc.
Patch:          0004-Re-add-Snappy-to-tests.patch
# We don't need coverage reports.
Patch:          0005-Remove-coverage-from-testing-requirements.patch
# Fix compatibility with NumPy 1.24.
Patch:          https://github.com/zarr-developers/numcodecs/pull/417.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)

%description
Numcodecs is a Python package providing buffer compression and transformation
codecs for use in data storage and communication applications.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Numcodecs is a Python package providing buffer compression and transformation
codecs for use in data storage and communication applications.


%package -n python-%{srcname}-doc
Summary:        numcodecs documentation

BuildArch:      noarch

BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-issues)

%description -n python-%{srcname}-doc
Documentation for numcodecs


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled blosc
rm -rf c-blosc

# Remove generated Cython files
rm numcodecs/{blosc,compat_ext,lz4,_shuffle,vlen,zstd}.c


%generate_buildrequires
%pyproject_buildrequires -r -x msgpack


%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo} html/_static/donotdelete


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
cd docs  # Avoid using unbuilt existing copy.
ln -s ../fixture
%{pytest} --pyargs numcodecs


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
%autochangelog
