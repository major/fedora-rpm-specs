%global srcname numcodecs

Name:           python-%{srcname}
Version:        0.14.1
Release:        %autorelease
Summary:        Buffer compression and transformation for data storage and communication

License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
Source0:        %pypi_source %{srcname}
# Fedora specific
Patch:          0001-Unbundle-blosc.patch
Patch:          0002-Unbundle-zstd.patch
Patch:          0003-Unbundle-lz4.patch
# Fedora is not missing Snappy support in Blosc.
Patch:          0004-Re-add-Snappy-to-tests.patch
# We don't need coverage reports, and don't want to test the current directory.
Patch:          0005-Fix-testing-setup-for-Fedora.patch
# Allow older NumPy.
Patch:          0006-Reduce-numpy-build-requirement.patch

# Fix a bug in delta filter.
Patch:          https://github.com/zarr-developers/numcodecs/pull/677.patch

# Stop building on i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3-devel

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

%description -n python-%{srcname}-doc
Documentation for numcodecs


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled blosc
rm -rf c-blosc


%generate_buildrequires
%pyproject_buildrequires -x crc32c,docs,msgpack,test,test_extras


%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo} html/_static/donotdelete


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
rm pyproject.toml
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
