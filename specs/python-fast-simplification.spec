# Some tests (and some VTK integration features) require python-pyvista, but we
# do not find it worthwhile to package it for that purpose alone.
%bcond pyvista 0

%bcond tests 1

Name:           python-fast-simplification
Version:        0.2.0
Release:        %autorelease
Summary:        Wrapper around the Fast-Quadric-Mesh-Simplification library

# The entire source is (SPDX) MIT. While the python3-nanobind package is not a
# header-only library, it functions rather like one, in that it ships C++
# sources that are compiled into extensions that use it. Furthermore, it brings
# in an indirect dependency on the header-only robin-map library.
#   - python3-nanobind is BSD-3-Clause
#   - robin-map-static is MIT
License:        MIT AND BSD-3-Clause
SourceLicense:  MIT
URL:            https://github.com/pyvista/fast-simplification
# The GitHub archive contains many ancillary files, like the README, the
# examples, and the list of test requirements, that the PyPI sdist lacks.
Source:         %{url}/archive/v%{version}/fast-simplification-%{version}.tar.gz

# Downstream-only: do not override system compiler flags
# 
# Don’t compile with -O3 unless we can point to benchmarks that justify it.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags
Patch:          0001-Downstream-only-do-not-override-system-compiler-flag.patch

# Exclude C++ sources and headers from built wheels
# https://github.com/pyvista/fast-simplification/pull/99
Patch:          %{url}/pull/99.patch

BuildSystem:    pyproject
%if %{with tests}
BuildOption(generate_buildrequires): requirements_test.txt
%endif
# https://scikit-build-core.readthedocs.io/en/latest/configuration/index.html
BuildOption(build): %{shrink:
    --config-settings logging.level=INFO
    --config-settings build.verbose=true
    --config-settings cmake.build-type="RelWithDebInfo"
    }
BuildOption(install): --no-assert-license fast_simplification

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++

%global common_description %{expand:
This is a python wrapping of the Fast-Quadric-Mesh-Simplification Library
(https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification/). Having arrived
at the same problem as the original author, but needing a Python library, this
project seeks to extend the work of the original library while adding
integration to Python and the PyVista (https://github.com/pyvista/pyvista)
project.

For the full documentation visit:
https://pyvista.github.io/fast-simplification/}

%description %{common_description}


%package -n python3-fast-simplification
Summary:        %{summary}

# The source file fast_simplification/Simplify.h is based on src.cmd/Simplify.h
# from https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification, which is
# not currently packaged. It does not make sense to attempt to unbundle this,
# because:
#
#   - The Simplify.h header is part of the implementation of a command-line
#     tool, and is not designed to be used as a library
#   - Changes have been made for this project, e.g.
#     https://github.com/pyvista/fast-simplification/commit/d55a7dcf2066099e3efe341d201b9c5ab22b100a.
#     Normally we would ask our upstream to offer these to the original project
#     so that they could eventually return to using it unmodified, but since
#     the copied and forked header is not really a library, and the changes
#     aren’t relevant to the command-line tool it supports, this doesn’t make
#     sense.
#
# The version was determined by careful inspection of sources and commit
# history; the changes from 4aeffce360279bd070492487426f3e6715c22562 are
# present, but those from the following commit
# f958f696c05b4b7a18ca85bc5c89d4f8e60288ad are not.
Provides:       bundled(Fast-Quadric-Mesh-Simplification) = 0^20201008git4aeffce

%description -n python3-fast-simplification %{common_description}


%prep -a
%if %{without pyvista}
%pyproject_patch_dependency pyvista:ignore
%endif


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%if %{with tests}
%pytest --verbose -rs
%endif


%files -n python3-fast-simplification -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
