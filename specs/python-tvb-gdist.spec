%global desc %{expand:
The Virtual Brain Project (TVB Project) has the purpose of offering some modern
tools to the Neurosciences community, for computing, simulating and analyzing
functional and structural data of human brains.

The gdist module is a Cython interface to a C++ library
(http://code.google.com/p/geodesic/) for computing geodesic distance which is
the length of shortest line between two vertices on a triangulated mesh in
three dimensions, such that the line lies on the surface.

The algorithm is due Mitchell, Mount and Papadimitriou, 1987; the
implementation is due to Danil Kirsanov and the Cython interface to Gaurav
Malhotra and Stuart Knock.

Original library (published under MIT license):
http://code.google.com/p/geodesic/

We added a python wrapped and made small fixes to the original library, to make
it compatible with cython.
}

# Test the C++ library, independent of the Python wrapper?
%ifnarch x86_64 %{ix86}
# Test failure with GCC/Linux on non-x86 architectures at -O2
# https://github.com/the-virtual-brain/tvb-gdist/issues/76
%bcond_with cxx_tests
%else
%bcond_without cxx_tests
%endif

%global forgeurl https://github.com/the-virtual-brain/tvb-gdist
%global tag 2.9.2


Name:           python-tvb-gdist
Version:        %tag
Release:        %autorelease
Summary:        Cython interface to geodesic

%forgemeta

License:        GPL-3.0-or-later
URL:            %forgeurl
# GitHub archive has tests etc., which the PyPI sdist lacks.
Source0:        %forgesource

BuildRequires:  python3-devel
BuildRequires:  gcc-c++

# Test dependencies (not well-documented):
BuildRequires:  python3dist(pytest)
%if %{with cxx_tests}
BuildRequires:  pkgconfig(gtest)
%endif

%description %{desc}

%package -n python3-tvb-gdist
Summary:        %{summary}

# The contents of geodesic_library/ are a header-only C++ library that can be
# used on its own. It was originally published at
# https://code.google.com/archive/p/geodesic/, but is no longer developed
# independently of this package. It was never explicitly versioned; the bundled
# code appears to be based on the final release of 2008-03-02. If there were a
# need to package it separately, it would probably be best to do so as a
# subpackage of this package, perhaps assigning it the same version as the
# Python Package. At least this bundled copy is actively maintained.
Provides:       bundled(geodesic) = 0

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-gdist

%description -n python3-tvb-gdist %{desc}

%prep
%forgeautosetup

# we don't want to use "oldest-supported-numpy"
# https://req.thevirtualbrain.org/browse/TVB-2890
sed -i 's/oldest-supported-numpy/numpy/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%set_build_flags
%pyproject_wheel
%if %{with cxx_tests}
"${CXX}" ${CXXFLAGS} -I./tests $(pkgconf --cflags gtest) \
     tests/test_geodesic_utils.cpp -o tests/test_geodesic_utils \
     ${LDFLAGS} $(pkgconf --libs gtest)
%endif


%install
%pyproject_install
%pyproject_save_files -l gdist


%check
%pytest -v
%if %{with cxx_tests}
# The program must be run from inside the tests/ directory.
pushd tests >/dev/null
./test_geodesic_utils
popd >/dev/null
%endif


%files -n python3-tvb-gdist -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
