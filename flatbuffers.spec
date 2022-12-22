%bcond_without tests
# Disabled for now because protobuf-devel does not provide CMake files
%bcond_with grpctest
# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We could potentially enable the Doxygen PDF documentation as a substitute,
# but currently Doxygen generates invalid LaTeX.
%bcond_with doc_pdf

Name:           flatbuffers
Version:        22.12.06
# The .so version is explicitly constructed from project version—search
# CMakeLists.txt for FlatBuffers_Library_SONAME_MAJOR and
# FlatBuffers_Library_SONAME_FULL—but we manually repeat the SOVERSION here,
# and use the macro in the file lists, as a reminder to avoid undetected .so
# version bumps.
%global so_version 22
Release:        %autorelease
Summary:        Memory efficient serialization library

# The entire source code is Apache-2.0. Even code from grpc, which is
# BSD-3-Clause in its upstream, is intended to be Apache-2.0 in this project.
# (Google is the copyright holder for both projects, so it can relicense at
# will.) See https://github.com/google/flatbuffers/pull/7073.
License:        Apache-2.0
URL:            https://google.github.io/flatbuffers
Source0:        https://github.com/google/flatbuffers/archive/v%{version}/%{name}-%{version}.tar.gz
# Hand-written for Fedora in groff_man(7) format based on --help output
Source1:        flatc.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# The ninja backend should be slightly faster than make, with no disadvantages.
BuildRequires:  ninja-build
%if %{with tests} && %{with grpctest}
BuildRequires:  cmake(absl)
BuildRequires:  cmake(protobuf)
BuildRequires:  grpc-devel
%endif

BuildRequires:  python3-devel

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

%if %{with doc_pdf}
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
# Required to format Python comments appropriately. Not yet packaged.
# BuildRequires: python3dist(doxypypy)
%endif

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


%prep
%autosetup -p1
# Remove unused directories that contain pre-compiled .jar files:
rm -rvf android/ kotlin/

%if %{with doc_pdf}
# We enable the Doxygen PDF documentation as a substitute for HTML. We must
# enable GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and
# should already be set as we like them. We also disable GENERATE_HTML, since
# we will not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    ./docs/source/doxyfile
%endif

%py3_shebang_fix samples


%generate_buildrequires
pushd python >/dev/null
%pyproject_buildrequires
popd >/dev/null


%build
# Needed for correct Python wheel version
export VERSION='%{version}'
%set_build_flags
%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
%if %{with tests}
    -DFLATBUFFERS_BUILD_TESTS:BOOL=ON \
%if %{with grpctest}
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
%cmake_build

pushd python
%pyproject_wheel
popd

%if %{with doc_pdf}
pushd docs/source
doxygen
popd
%make_build -C docs/latex
%endif


%install
%cmake_install
pushd python
%pyproject_install
%pyproject_save_files flatbuffers
popd
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %SOURCE1 %{buildroot}%{_mandir}/man1/flatc.1


%check
%if %{with tests}
%ctest
%endif
# Upstream does not appear to provide any dedicated Python tests.
%pyproject_check_import


%files
%license LICENSE.txt

%{_libdir}/libflatbuffers.so.%{so_version}
%{_libdir}/libflatbuffers.so.%{version}


%files devel
%{_includedir}/flatbuffers/

%{_libdir}/libflatbuffers.so

%{_libdir}/cmake/flatbuffers/
%{_libdir}/pkgconfig/flatbuffers.pc


%files compiler
%{_bindir}/flatc
%{_mandir}/man1/flatc.1*


%files doc
%license LICENSE.txt
%doc SECURITY.md
%doc readme.md

%if %{with doc_pdf}
%doc docs/latex/refman.pdf
%endif

%doc samples/


%files -n python3-flatbuffers -f %{pyproject_files}
%license LICENSE.txt


%changelog
%autochangelog
