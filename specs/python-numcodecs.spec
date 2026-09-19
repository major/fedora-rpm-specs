%global srcname numcodecs

%global build_backend_args %{shrink:
  -Csetup-args="-Dsystem_blosc=enabled"
  -Csetup-args="-Dsystem_zstd=enabled"
  -Csetup-args="-Dsystem_lz4=enabled"
}

Name:           python-%{srcname}
Version:        0.17.0
Release:        %autorelease
Summary:        Buffer compression and transformation for data storage and communication

License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
Source:         %pypi_source %{srcname}
# https://github.com/zarr-developers/numcodecs/pull/860
Patch:          0001-Allow-building-against-a-system-Zlib.patch
# Fedora is not missing Snappy support in Blosc.
Patch:          0002-Re-add-Snappy-to-tests.patch
# We don't need coverage reports, and don't want to test the current directory.
Patch:          0003-Fix-testing-setup-for-Fedora.patch

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


%pyproject_extras_subpkg -n python3-%{srcname} crc32c msgpack zfpy

%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled blosc
rm -rf c-blosc


%generate_buildrequires
%pyproject_buildrequires -p -x crc32c,docs,msgpack,test,test_extras


%build
%pyproject_wheel %build_backend_args


%install
%pyproject_install
%pyproject_save_files -l %{srcname}

# generate html docs
PYTHONPATH="%{buildroot}%{python3_sitearch}" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo} html/_static/donotdelete


%check
%{pytest}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
%autochangelog
