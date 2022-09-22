%global srcname healpy
%global sum Python healpix maps tools

Name:           python-%{srcname}
Version:        1.16.1
Release:        %autorelease -b 2
Summary:        %{sum}

License:        GPLv2+ 
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz


# Upstream only supports 64 bit architectures, 32 Bit builds, but tests fail
# and we don't want to provide a non reliable software.
# Check https://github.com/healpy/healpy/issues/194
# Also explicitly exclude known unsupported architectures
ExcludeArch:    %{ix86} %{arm}

# Common build requirements
BuildRequires:  cfitsio-devel
BuildRequires:  gcc-c++
BuildRequires:  healpix-c++-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  zlib-devel

# tests requirements
BuildRequires:  python3dist(astropy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-astropy)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(requests)


%description
Healpy provides a python package to manipulate healpix maps. It is based on the
standard numeric and visualisation tools for Python, Numpy and matplotlib.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Healpy provides a python package to manipulate healpix maps. It is based on the
standard numeric and visualisation tools for Python, Numpy and matplotlib.

This package contains the Python 3 modules.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# kill rpath forcely (mtasaka, 20210704)
# "runtime_library_dirs" seems to invoke ""-Wl,--enable-new-dtags,-R"
# from python3-setuptools: runtime_library_dir_option (unixccompiler.py) <-
#                          gen_lib_options (ccompiler.py),
# so remove setting "runtime_library_dirs" for now
# sed -i setup.py -e 's|"runtime_library_dirs"||'

# Fedora doesn't have 'oldest-supported-numpy'
sed -i pyproject.toml -e 's|"oldest-supported-numpy"|"numpy"|'

# Remove pre-generated CPython files
# not strictly necessary as these files are not used from bundled cfitsio
find -type f -name '*.c' -print -delete

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
rm -f %{buildroot}%{_bindir}/healpy_get_wmap_maps.sh
%pyproject_save_files healpy


%check
%pyproject_check_import

pushd %{buildroot}/%{python3_sitearch}
# For skipped tests: They require internet access and therefore have to be disabled
%pytest -q -k "not (test_astropy_download_file or test_rotate_map_polarization or test_pixelweights_local_datapath)" healpy
# Remove relict from tests
rm -rf .pytest_cache
popd


%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc CHANGELOG.rst CITATION README.rst


%changelog
%autochangelog
