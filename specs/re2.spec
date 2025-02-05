# The Python extension tests now segfault on i686. Starting with Fedora 42, we
# no longer build the Python extension on i686; in the medium term, we wish to
# drop i686 support altogether, but we must coordinate all reverse dependencies
# doing so first; see the notes in %%check.
%bcond python %{expr:0%{?__isa_bits} != 32} || %{defined fc41} || %{defined fc40}}

Name:           re2
%global tag 2024-07-02
%global so_version 11
Version:        %(echo '%{tag}' | tr -d -)
Epoch:          1
Release:        %autorelease
Summary:        C++ fast alternative to backtracking RE engines

# The entire source is BSD-3-Clause, except:
#   - lib/git/commit-msg.hook is Apache-2.0, but is not used in the build and
#     is removed in %%prep
License:        BSD-3-Clause
SourceLicense:  %{license} AND Apache-2.0
URL:            https://github.com/google/re2
Source:         %{url}/archive/%{tag}/re2-%{tag}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

BuildRequires:  cmake(absl)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(benchmark)

%if %{with python}
# Python extension
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pybind11}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  pybind11-static

# Python extension tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist absl-py}
%endif

%global common_description %{expand:
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python. It is a C++
library.}

%description %{common_description}


%package        devel
Summary:        C++ header files and library symbolic links for re2

Requires:       re2%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel %{common_description}

This package contains the C++ header files and symbolic links to the shared
libraries for re2. If you would like to develop programs using re2, you will
need to install re2-devel.


%if %{with python}
%package -n     python3-google-re2
Summary:        RE2 Python bindings

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       re2%{?_isa} = %{epoch}:%{version}-%{release}

Conflicts:      python3-fb-re2
Obsoletes:      python3-fb-re2 < 1.0.7-19

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-re2

%description -n python3-google-re2
A drop-in replacement for the re module.

It uses RE2 under the hood, of course, so various PCRE features (e.g.
backreferences, look-around assertions) are not supported. See
https://github.com/google/re2/wiki/Syntax for the canonical reference, but
known syntactic ”gotchas” relative to Python are:

  • PCRE supports \Z and \z; RE2 supports \z; Python supports \z,
    but calls it \Z. You must rewrite \Z to \z in pattern strings.

Known differences between this module’s API and the re module’s API:

  • The error class does not provide any error information as attributes.
  • The Options class replaces the re module’s flags with RE2’s options as
    gettable/settable properties. Please see re2.h for their documentation.
  • The pattern string and the input string do not have to be the same type.
    Any str will be encoded to UTF-8.
  • The pattern string cannot be str if the options specify Latin-1 encoding.
%endif


%prep
%autosetup -n re2-%{tag}
# Show that a file licensed Apache-2.0 is not used in the build and does not
# contribute to the licenses of the binary RPMs:
rm lib/git/commit-msg.hook


%if %{with python}
%generate_buildrequires
cd python
%pyproject_buildrequires
%endif


%conf
%cmake \
    -DRE2_BUILD_TESTING:BOOL=ON \
    -DRE2_USE_ICU:BOOL=ON \
    -GNinja

%if %{with python}
cat >> python/setup.cfg <<EOF
[build_ext]
include_dirs=${PWD}
library_dirs=${PWD}/%{_vpath_builddir}
EOF
%endif


%build
%cmake_build
%if %{with python}
cd python
%pyproject_wheel
%endif


%install
%cmake_install

%if %{with python}
cd python
%pyproject_install
%pyproject_save_files -l re2
%endif


%check
%ctest

%if %{with python}
# Python tests now segfault on i686, but we cannot drop support under
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval because re2
# is not yet a leaf package on that architecture. Instead, we skip the Python
# tests on i686.
#
# The following directly-dependent packages are ExcludeArch: %%{ix86}:
#   bloaty, ceph, credentials-fetcher, CuraEngine_grpc_definitions, dnsdist,
#   libarrow, mtxclient, nheko, onnx, onnxruntime, parlaylib,
#   perl-re-engine-RE2, python-torchtext
#
# The following are not (yet):
# - grpc:
#   Not blocked by: CuraEngine_grpc_definitions, bear, buildbox, buildstream,
#                   ceph, credentials-fetcher, frr, libarrow, libphonenumber,
#                   syslog-ng
#     Note that syslog-ng does depend on grpc *and* builds on i686, but grpc
#     support is disabled on i686, so all is well.
#   Blocked by:
#   - duplicity (indirect, via noarch intermediate packages:
#     grpc <- python-google-api-core <- google-api-python-client <- duplicity)
#     - Not blocked by: duply
#     - Blocked by:
#       - deja-dup
#   - fastnetmon: https://src.fedoraproject.org/rpms/fastnetmon/pull-request/2
#   - matrix-synapse (indirect, via noarch intermediate package:
#     grpc <- python-sentry-sdk <- matrix-synapse)
#   - nanopb
#   - perl-grpc-xs
#   - qt6-qtgrpc
#   TBD:
#     There are many more packages that depend directly or indirectly on
#     python3-grpcio in particular at install time, but not at build time. We
#     must explore the entire tree looking for arched packages that build on
#     i686.
# Run the tests from the top-level directory to make sure we don’t accidentally
# import the “un-built” package instead of the one in the buildroot.
ln -s python/re2_test.py
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %pytest re2_test.py
%endif


%files
%license LICENSE
%doc README
%{_libdir}/libre2.so.%{so_version}{,.*}


%files          devel
%doc doc/syntax.{html,txt}
%{_includedir}/re2/
%{_libdir}/libre2.so
%{_libdir}/pkgconfig/re2.pc
%{_libdir}/cmake/re2/


%if %{with python}
%files -n       python3-google-re2 -f %{pyproject_files}
%endif


%changelog
%autochangelog
