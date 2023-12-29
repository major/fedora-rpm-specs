%global forgeurl https://github.com/DynamicsAndNeuralSystems/pycatch22

Name:           python-pycatch22
Version:        0.4.4
Release:        %autorelease
Summary:        CAnonical Time-series CHaracteristics in Python

%forgemeta

# Upstream clarified that GPL-3.0-or-later is intended in “Please clarify GPL
# version,” https://github.com/DynamicsAndNeuralSystems/pycatch22/issues/16.
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

# Downstream-only: use unbundled catch22 library
#
# It’s also necessary to remove the bundled (non-Python-wrapper) sources from
# the src/C/ directory.
#
# We use our own Makefile (catch22 lacks an upstream build system) and
# downstream .so versioning to build a shared library in the catch22 package;
# this patch allows us to use that instead of the bundled catch22 C sources.
#
# Upstream has opted to continue bundling because they are uncomfortable with
# shared libraries:
#
#   Generating a shared library for the C implementation (and using that to
#   build pycatch22 etc.)
#   https://github.com/DynamicsAndNeuralSystems/catch22/issues/29
Patch:          0001-Downstream-only-use-unbundled-catch22-library.patch

BuildRequires:  python3-devel
BuildRequires:  gcc

# See comments above the patch to unbundle the catch22 C implementation.
BuildRequires:  catch22-devel

%global common_description %{expand:
catch22 is a collection of 22 time-series features coded in C that can be run
from Python, R, Matlab, and Julia.

This package provides a Python implementation as the module pycatch22.}

%description %{common_description}


%package -n python3-pycatch22
Summary:        %{summary}

# See comments above the patch to unbundle the catch22 C implementation.  If we
# ever have to switch back to the bundled implementation, research suggests
# that (as of pycatch22 0.4.3) the effective version of the bundled catch22
# implementation is 0.4.1.

%description -n python3-pycatch22 %{common_description}


%prep
%autosetup %{forgesetupargs} -p1

# Remove the bundled copy of the catch22 package, but not the Python extension
# module implementation in the same directory.
find src/C -type f ! -name 'catch22_wrap.c' -print -delete


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pycatch22 catch22_C


%check
# We aren’t highly confident that the upstream test scripts have good coverage.
# Let’s run an import ”smoke test” first just to be sure.
%pyproject_check_import

# There is no verification of output values; we are just checking that the
# script *runs*.
%{py3_test_envvars} '%{python3}' tests/testing.py


%files -n python3-pycatch22 -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
