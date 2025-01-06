%global srcname healpy
%global sum Python healpix maps tools

Name:           python-%{srcname}
Version:        1.18.0
Release:        %autorelease
Summary:        %{sum}

License:        GPL-2.0-or-later
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
# Fedora doesn't have pykg-config (we use pkg-config)
Patch:          pykg-config_requirements.patch
# pytest-cython has been retired in Fedora
# skip cython doctests for now
Patch:          no_pytest-cython_doctests.patch


# Upstream only supports 64 bit architectures, 32 Bit builds, but tests fail
# and we don't want to provide a non reliable software.
# Check https://github.com/healpy/healpy/issues/194
# Also explicitly exclude known unsupported architectures
ExcludeArch:    %{ix86} %{arm}

# Common build requirements
BuildRequires:  cfitsio-devel
BuildRequires:  gcc-c++
BuildRequires:  healpix-c++-devel
BuildRequires:  pkg-config
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  zlib-devel


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

# Remove pre-generated CPython files
# not strictly necessary as these files are not used from bundled cfitsio
find -type f -name '*.c' -print -delete

# Remove conftest.py from lib/healpy
# we don't want pytest to inject source directory in sys path for tests
rm -f lib/healpy/conftest.py


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
rm -f %{buildroot}%{_bindir}/healpy_get_wmap_maps.sh
%pyproject_save_files healpy


%check
%pyproject_check_import

# For skipped tests: They require internet access and therefore have to be disabled
%pytest -q -k "not (test_astropy_download_file or test_rotate_map_polarization or test_pixelweights_local_datapath)"


%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc CHANGELOG.rst CITATION README.rst


%changelog
%autochangelog
