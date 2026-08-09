#global commit 0e12e41b52deb8ea746bc760cddd6e100ca5cfd8
#global shortcommit %%(c=%{commit}; echo ${c:0:7})

Name:           moose
Version:        4.3.1
Release:        %autorelease
Summary:        Multiscale Neuroscience and Systems Biology Simulator
# The shipped files (compiled _moose module and the moose/rdesigneur Python
# packages) are under a mix of licenses:
# - LGPL-2.1-only: bulk of the compiled C++ core (basecode/, biophysics/,
#   builtins/, device/, diffusion/, hsolve/, intfire/, kinetics/, ksolve/,
#   mesh/, mpi/, msg/, scheduling/, shell/, signeur/, synapse/, utility/)
# - GPL-2.0-only: basecode/Cinfo.h, builtins/Streamer*, device/PIDController.h,
#   device/RC.h, randnum/Distributions.h, randnum/test_normal_dist.cpp
# - GPL-2.0-or-later: utility/simple_logger.hpp,
#   python/rdesigneur/{jardesigner,rdes2json,rdesigneur}.py
# - GPL-3.0-only: ksolve/VoxelPools.cpp, pymoose/MooseVec.h,
#   randnum/{Definitions.h,NormalDistribution.hpp}
# - GPL-3.0-or-later: several biophysics/, builtins/ and python/moose files
# - LGPL-3.0-only: builtins/TableBase.h
# - LGPL-3.0-or-later: biophysics/VClamp.cpp, ksolve/FuncRateTerm.h
# - MIT: basecode/testGlobals.cpp, pymoose/MooseVec.cpp, randnum/{RNG.cpp,randnum.h},
#   utility/utility.cpp, plus bundled exprtk and libsoda
# - BSL-1.0: utility/current_function.hpp, utility/simple_assert.hpp
License:        LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND MIT AND BSL-1.0
URL:            https://mooseneuro.github.io/
%if %{defined commit}
Source0:        https://github.com/MooseNeuro/moose-core/archive/%{commit}.tar.gz#/moose-core-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/MooseNeuro/moose-core/archive/v%{version}.tar.gz#/moose-core-%{version}.tar.gz
%endif

# Generated and housed here: https://github.com/sanjayankur31/moose-core/tree/feat-version-4.3.1-fedora
Patch:          0001-Replace-python-with-python3.patch
Patch:          0002-Use-system-nanobind.patch
Patch:          0003-Make-neuroml-optional-dependency.patch
Patch:          0004-Remove-pybind11-check-in-test.patch
Patch:          0005-Use-system-fmt.patch
Patch:          0006-Add-missing-includes.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

ExcludeArch: s390x

BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  python3-devel
BuildRequires:  python3-libsbml
BuildRequires:  robin-map-devel
BuildRequires:  %{py3_dist nanobind}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pint}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist setuptools}

%description
MOOSE is the base and numerical core for large, detailed simulations
including Computational Neuroscience and Systems Biology. MOOSE spans
the range from single molecules to subcellular networks, from single
cells to neuronal networks, and to still larger systems. It is
backwards-compatible with GENESIS, and forward compatible with Python
and XML-based model definition standards like SBML and NeuroML.

MOOSE uses Python as its primary scripting language. For backward
compatibility we have a GENESIS scripting module, but this is
deprecated. MOOSE numerical code is written in C++.

%package -n python3-%{name}
Summary:  %{summary}

# libsoda and exprtk are bundled in the compiled module; they are not
# packaged in Fedora and upstream has no mechanism to build against system
# versions.
Provides: bundled(libsoda)
Provides: bundled(exprtk)

Requires: python3-libsbml
Requires: python3-matplotlib-qt5
Requires: %{py3_dist lxml}
Requires: %{py3_dist matplotlib}
Requires: %{py3_dist numpy}
Requires: %{py3_dist pint}

%description -n python3-%{name}
This package contains the %{summary}.

%prep
%autosetup -n moose-core-%{version} -S git
rm -f python/rdesigneur/.gitignore
# remove unused bundled bits
rm -rf external/fmt external/tinyexpr external/getopt external/boost-numeric-bindings
sed -i '/^#!/d' python/moose/channels/build_icg_meta.py python/moose/channels/update_citations_icg.py

%conf
%meson -Duse_hdf5=true

%build
# On armv7 we get a failure with LTO.
# Disable LTO for armv7
%ifarch armv7hl
%define _lto_cflags %{nil}
%endif

%meson_build

%install
%meson_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -c "import moose; moose.le()"
%global _docdir_fmt %{name}

%files -n python3-%{name}
%{python3_sitearch}/moose
%{python3_sitearch}/rdesigneur
%license LICENSE
%doc README.md

%changelog
%autochangelog
