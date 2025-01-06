%bcond cpp_tests 1
# Disabled for now because protobuf-devel does not provide CMake files
%bcond cpp_grpc_test 0
%bcond py_tests 1

%bcond mingw 1

Name:           flatbuffers
Version:        24.12.23
# The .so version is equal to the project version since upstream offers no ABI
# stability guarantees. We manually repeat it here and and use the macro in the
# file lists as a reminder to avoid undetected .so version bumps. See
# https://github.com/google/flatbuffers/issues/7759.
%global so_version 24.12.23
Release:        %autorelease
Summary:        Memory efficient serialization library

# The entire source code is Apache-2.0. Even code from grpc, which is
# BSD-3-Clause in its upstream, is intended to be Apache-2.0 in this project.
# (Google is the copyright holder for both projects, so it can relicense at
# will.) See https://github.com/google/flatbuffers/pull/7073.
License:        Apache-2.0
URL:            https://google.github.io/flatbuffers
%global forgeurl https://github.com/google/flatbuffers
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Hand-written for Fedora in groff_man(7) format based on --help output
Source1:        flatc.1

# Adjust library installation under mingw
# https://github.com/google/flatbuffers/pull/8365
Patch:          flatbuffers_mingw-lib.patch

# NumPy 2.x fix
# https://github.com/google/flatbuffers/issues/8332
Patch:          %{forgeurl}/pull/8346.patch

# Fix a minor typo in flatc --help output
# https://github.com/google/flatbuffers/pull/8468
Patch:          %{forgeurl}/pull/8468.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# The ninja backend should be slightly faster than make, with no disadvantages.
BuildRequires:  ninja-build
%if %{with cpp_tests} && %{with cpp_grpc_test}
BuildRequires:  cmake(absl)
BuildRequires:  cmake(protobuf)
BuildRequires:  grpc-devel
%endif

BuildRequires:  python3-devel
# Enables numpy integration tests
BuildRequires:  python3dist(numpy)

%if %{with mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw32-python3-numpy

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
BuildRequires:  mingw64-python3-numpy
%endif

# From grpc/README.md:
#
#   NOTE: files in `src/` are shared with the GRPC project, and maintained
#   there (any changes should be submitted to GRPC instead). These files are
#   copied from GRPC, and work with both the Protobuf and FlatBuffers code
#   generator.
#
# It’s not clearly documented which GPRC version is excerpted, but see
# https://github.com/google/flatbuffers/pull/4305 for more details. We use
# _GRPC_VERSION from the WORKSPACE file as the bundled GRPC version, but we are
# not 100% certain that this is entirely correct.
#
# It is not possible to unbundle this because private/internal APIs are used.
Provides:       bundled(grpc) = 1.49.0

%global common_description %{expand:
FlatBuffers is a cross platform serialization library architected for maximum
memory efficiency. It allows you to directly access serialized data without
parsing/unpacking it first, while still having great forwards/backwards
compatibility.}

%description %{common_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains libraries and header files for developing applications
that use FlatBuffers.


%package        compiler
Summary:        FlatBuffers compiler (flatc)
# The flatc compiler does not link against the shared library, so this could
# possibly be removed; we leave it for now to ensure there is no version skew
# across subpackages.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    compiler %{common_description}

This package contains flatc, the FlatBuffers compiler.


%package        doc
Summary:        Documentation and examples for FlatBuffers

BuildArch:      noarch

%description    doc %{common_description}

This package contains documentation and examples for FlatBuffers.


%package -n     python3-flatbuffers
Summary:        FlatBuffers serialization format for Python

BuildArch:      noarch

Recommends:     python3dist(numpy)

Provides:       flatbuffers-python3 = %{version}-%{release}
Obsoletes:      flatbuffers-python3 < 2.0.0-6

%description -n python3-flatbuffers %{common_description}

This package contains the Python runtime library for use with the Flatbuffers
serialization format.


%if %{with mingw}
# Win32
%package -n mingw32-%{name}
Summary:        MinGW Windows %{name} library

%description -n mingw32-%{name}
Summary:        MinGW Windows %{name} library.


%package -n mingw32-python3-%{name}
Summary:        MinGW Windows %{name} Python 3 bindings

%description -n mingw32-python3-%{name}
Summary:        MinGW Windows %{name}  Python 3 bindings.


# Win64
%package -n mingw64-%{name}
Summary:        MinGW Windows %{name} library

%description -n mingw64-%{name}
Summary:        MinGW Windows %{name} library.


%package -n mingw64-python3-%{name}
Summary:        MinGW Windows %{name} Python 3 bindings

%description -n mingw64-python3-%{name}
Summary:        MinGW Windows %{name}  Python 3 bindings.


%{?mingw_debug_package}
%endif


%prep
%autosetup -p1
# Remove unused directories that contain pre-compiled .jar files:
rm -rvf android/ kotlin/

%py3_shebang_fix samples
# Fix paths in the Python test script to match how our build is organized:
#   - Use flatc from the buildroot, not the root of the extracted sources
#   - Use the proper python3 interpreter path from the RPM macro
#   - Don’t attempt to run tests with interpreters other than python3
#   - Add the buildroot python3_sitelib to PYTHONPATH so the flatbuffers
#     package can be found; the appropriate PYTHONPATH is supplied by could be
#     handled by %%{py3_test_envvars}, but the test script overrides it
#   - Make sure we don’t do coverage analysis even if python3-coverage is
#     somehow installed as an indirect dependency
sed -r -i.upstream \
    -e 's|[^[:blank:]]*(/flatc)|%{buildroot}%{_bindir}\1|' \
    -e 's| python3 | %{python3} |' \
    -e 's|run_tests [^/]|# &|' \
    -e 's|PYTHONPATH=|&%{buildroot}%{python3_sitelib}:|' \
    -e 's|which coverage|/bin/false|' \
    tests/PythonTest.sh


%generate_buildrequires
pushd python >/dev/null
%pyproject_buildrequires
popd >/dev/null


%conf
# Needed for correct Python wheel version
export VERSION='%{version}'
%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
%if %{with cpp_tests}
    -DFLATBUFFERS_BUILD_TESTS:BOOL=ON \
%if %{with cpp_grpc_test}
    -DFLATBUFFERS_BUILD_GRPCTEST:BOOL=ON \
    -DGRPC_INSTALL_PATH:PATH=%{_prefix} \
%endif
%else
    -DFLATBUFFERS_BUILD_TESTS:BOOL=OFF \
    -DFLATBUFFERS_BUILD_GRPCTEST:BOOL=OFF \
%endif
    -DFLATBUFFERS_BUILD_SHAREDLIB=ON \
    -DFLATBUFFERS_BUILD_FLATLIB=OFF \
    -DFLATBUFFERS_BUILD_FLATC=ON

%if %{with mingw}
(
%mingw_cmake \
    -DFLATBUFFERS_BUILD_TESTS:BOOL=OFF \
    -DFLATBUFFERS_BUILD_GRPCTEST:BOOL=OFF \
    -DFLATBUFFERS_BUILD_SHAREDLIB=ON \
    -DFLATBUFFERS_BUILD_FLATLIB=OFF \
    -DFLATBUFFERS_BUILD_FLATC=ON
)
%endif


%build
%cmake_build

pushd python
%pyproject_wheel
popd

%if %{with mingw}
(
%mingw_make_build

pushd python
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
popd
)
%endif


%install
%cmake_install
pushd python
%pyproject_install
%pyproject_save_files flatbuffers
popd
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'

%if %{with mingw}
(
%mingw_make_install

pushd python
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
popd
%mingw_debug_install_post
)
%endif


%check
%if %{with cpp_tests}
%ctest
%endif
%if %{with py_tests}
# The test script overrides PYTHONPATH and PYTHONDONTWRITEBYTECODE, but we’d
# like to pass through any other environment variables that are set by
# %%{py3_test_envvars}.
%{py3_test_envvars} ./tests/PythonTest.sh
%endif
# Do an import-only “smoke test” even if we ran the Python tests; we are not
# convinced that they cover all modules in the package.
%pyproject_check_import


%files
%license LICENSE
%{_libdir}/libflatbuffers.so.%{so_version}


%files devel
%{_includedir}/flatbuffers/

%{_libdir}/libflatbuffers.so

%{_libdir}/cmake/flatbuffers/
%{_libdir}/pkgconfig/flatbuffers.pc


%files compiler
%{_bindir}/flatc
%{_mandir}/man1/flatc.1*


%files doc
%license LICENSE
%doc CHANGELOG.md
%doc SECURITY.md
%doc README.md

%doc examples/
%doc samples/


%files -n python3-flatbuffers -f %{pyproject_files}
%license LICENSE


%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/flatc.exe
%{mingw32_bindir}/libflatbuffers-%{so_version}.dll
%{mingw32_libdir}/libflatbuffers.dll.a
%{mingw32_libdir}/pkgconfig/flatbuffers.pc
%{mingw32_libdir}/cmake/flatbuffers/
%{mingw32_includedir}/flatbuffers/

%files -n mingw32-python3-%{name}
%{mingw32_python3_sitearch}/flatbuffers/
%{mingw32_python3_sitearch}/flatbuffers-%{version}.dist-info/


%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/flatc.exe
%{mingw64_bindir}/libflatbuffers-%{so_version}.dll
%{mingw64_libdir}/libflatbuffers.dll.a
%{mingw64_libdir}/pkgconfig/flatbuffers.pc
%{mingw64_libdir}/cmake/flatbuffers/
%{mingw64_includedir}/flatbuffers/

%files -n mingw64-python3-%{name}
%{mingw64_python3_sitearch}/flatbuffers/
%{mingw64_python3_sitearch}/flatbuffers-%{version}.dist-info/
%endif


%changelog
%autochangelog
