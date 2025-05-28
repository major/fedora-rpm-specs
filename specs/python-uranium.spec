Name:           python-uranium
Version:        5.6.0
Release:        %autorelease
Summary:        A Python framework for building desktop applications
License:        LGPL-3.0-or-later
URL:            https://github.com/Ultimaker/Uranium
Source:         %{url}/archive/%{version}.tar.gz#/Uranium-%{version}.tar.gz
Patch:          Uranium-5.3.0-qt-try-ints-then-bytes-for-gl-mask-functions.patch
# Fix asserts for called once in Python 3.12:
Patch:          https://github.com/Ultimaker/Uranium/pull/885.patch#/Uranium-5.3.0-python3.12.patch
# Force test order to fix FTBFS with pytest 8 
# From https://github.com/Ultimaker/Uranium/pull/941
Patch:          Uranium-5.6.0-pytest8.patch
# Fix for Python 3.14
Patch:          https://github.com/Ultimaker/Uranium/pull/997.patch

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2:        mod_bundled_packages_json.py
Source3:        UraniumPluginInstall.cmake
Source4:        UraniumTests.cmake
Source5:        UraniumTranslationTools.cmake
Source6:        CMakeLists.txt
Source7:        CPackConfig.cmake
Source8:        Doxyfile

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  /usr/bin/doxygen
BuildRequires:  /usr/bin/msgmerge
BuildRequires:  cmake
BuildRequires:  git-core

# UM/PluginRegistry.py imports from imp
# https://github.com/Ultimaker/Uranium/issues/765
# https://github.com/Ultimaker/Uranium/pull/915
BuildRequires:  (python3-zombie-imp if python3 >= 3.12)

# Tests
BuildRequires:  python3-arcus >= 5.3.0
BuildRequires:  python3-cryptography
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-shapely
BuildRequires:  python3-pyclipper
BuildRequires:  python3-pyqt6-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-benchmark
BuildRequires:  python3-twisted

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Uranium is a Python framework for building 3D printing related applications.

%package -n python3-uranium
Summary:        %{summary}
Provides:       uranium = %{version}-%{release}

Requires:       python3-arcus >= 5.3.0
Requires:       python3-cryptography
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-shapely
Requires:       python3-pyclipper
Requires:       python3-pyqt6
Requires:       (python3-zombie-imp if python3 >= 3.12)
Recommends:     python3-numpy-stl

%description -n python3-uranium
Uranium is a Python framework for building 3D printing related applications.

%package doc
Summary: Documentation for %{name} package

%description doc
Documentation for Uranium, a Python framework for building 3D printing
related applications.

%prep
%autosetup -n Uranium-%{version} -p1 -S git

mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} cmake/
rm -rf CMakeLists.txt
cp -a %{SOURCE6} %{SOURCE7} %{SOURCE8} .

# fix compile-shaders
sed -i 's|qsb |qsb-qt6 |g' scripts/compile-shaders

%build
# there is no arch specific content, so we set LIB_SUFFIX to nothing
# see https://github.com/Ultimaker/Uranium/commit/862a246bdfd7e25541b04a35406957612c6f4bb7
%cmake -DLIB_SUFFIX:STR=
%cmake_build
%cmake_build -- doc

%check
%{python3} -m pip freeze

# skipping failing tests, see:
# * https://github.com/Ultimaker/Uranium/issues/594
# * https://github.com/Ultimaker/Uranium/issues/603
%{python3} -m pytest -v -k "not (TestSettingFunction and test_init_bad) and not TestHttpRequestManager"


%install
%cmake_install

# Move the cmake files
mv %{buildroot}%{_datadir}/cmake* %{buildroot}%{_datadir}/cmake

# Sanitize the location of locale files
pushd %{buildroot}%{_datadir}
mv uranium/resources/i18n locale
ln -s ../../locale uranium/resources/i18n
rm locale/uranium.pot
rm locale/*/uranium.po
popd

# Bytecompile the plugins
%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/uranium

%find_lang uranium


%files -n python3-uranium -f uranium.lang
%license LICENSE
%doc README.md
%{python3_sitelib}/UM
%{_datadir}/uranium
# Own the dir not to depend on cmake:
%{_datadir}/cmake
%{_prefix}/lib/uranium


%files doc
%license LICENSE
%doc html


%changelog
%autochangelog
