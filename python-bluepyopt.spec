%global forgeurl https://github.com/BlueBrain/BluePyOpt

# versioneer is used, so no tags for patch versions
# use git tar since pypi does not include examples that are needed for tests.
# Upstream tags with every push to master (why?)
# Use commit found in bluepyopt/_version.py of the PyPI release
%global commit 5232a8f2e278cf0d32fe7008a81d82b0ad10b992

%bcond_without tests

%global _description %{expand:
The Blue Brain Python Optimisation Library (BluePyOpt) is an extensible
framework for data-driven model parameter optimisation that wraps and
standardises several existing open-source tools. It simplifies the task of
creating and sharing these optimisations, and the associated techniques and
knowledge. This is achieved by abstracting the optimisation and evaluation
tasks into various reusable and flexible discrete elements according to
established best-practices.}

Name: python-bluepyopt
Version: 1.14.6
Release: %autorelease
Summary: Bluebrain Python Optimisation Library (bluepyopt)

# This package is not noarch because it's tests are arch dependent but it does
# not install any arch dependent files and so does not generate debuginfo
%global debug_package %{nil}

# pyedflib excludes s390x, so all deps also exclude it
# lfpy excludes ppc64le, se we follow suite
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    s390x %{ix86} %{power64}

License: LGPL-3.0-only

%forgemeta

URL: %forgeurl
Source0: %forgesource
# use _version file from pypi tar to trick versioneer
Source1: _version.py

# Update Versioneer to fix AttributeError in configparser
# https://github.com/BlueBrain/BluePyOpt/pull/466
Patch:          https://github.com/BlueBrain/BluePyOpt/pull/466.patch

# Fix exclusion in setup.py (these are globs)
# https://github.com/BlueBrain/BluePyOpt/pull/467
Patch:          https://github.com/BlueBrain/BluePyOpt/pull/467.patch

# Not all requirements are listed, so we need to use explicit BRs also
BuildRequires:  python3-devel
# Required to compile neuron based models
BuildRequires:  neuron-devel
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  %{py3_dist matplotlib}

# To run tests
%if %{with tests}
BuildRequires:  %{py3_dist future}
BuildRequires:  python3-jupyter-client
BuildRequires:  python3-nbconvert
BuildRequires:  python3-neuron
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist lfpy}
BuildRequires:  %{py3_dist papermill}
BuildRequires:  %{py3_dist meautility}
BuildRequires:  python3-arbor
%endif

%description %_description

%package -n python3-bluepyopt
Summary:        %{summary}

# Only need to list ones not listed in setup.py
Requires: neuron-devel
Requires: python3-neuron
Requires: python3dist(setuptools)

%description -n python3-bluepyopt %_description

%package -n python3-bluepyopt-doc
BuildArch:      noarch
Summary:        Documentation for bluepyopt


%description -n python3-bluepyopt-doc %_description

%prep
%forgeautosetup -p1
cp -v %{SOURCE1} "bluepyopt/_version.py"

# Optional dependency, remove so that automatic dep generator does not pick it up
sed -i '/scoop/ d' setup.py

# For tests, we install jupyter as BuildRequires
# remove all Makefile deps on the jupyter target
# need to check this for each update, in case the makefile changes
sed -i 's/^\(.*:.*\)jupyter$/\1/' Makefile
# convert python to python3
sed -i 's/python l5pc_validate_neuron_arbor_pm.py/python3 l5pc_validate_neuron_arbor_pm.py/g' Makefile

# remove neuroml test script: pyneuroml cannot be packaged for Fedora because of java issues
rm -f bluepyopt/tests/test_neuroml_fcts.py



# Remove gitignore files in the examples
find examples/ -name ".gitignore" -delete
# Remove dummy files that keep the folder tracked in git for upstream
find examples/ -name "dummy.inc" -delete

# Correct shebangs
find examples/ -type f -name "*.py" -exec sed -i 's|^#![  ]*/usr/bin/env.*$|#!/usr/bin/python3/|' '{}' 2>/dev/null \;
find examples/ -type f -name "*.py" -exec chmod -x '{}' \;

# Correct end of line encodings
find examples/ -type f -name "*.mod" -exec sed -i 's/\r$//' '{}' \;
find examples/ -type f -name "*.asc" -exec sed -i 's/\r$//' '{}' \;
find examples/ -type f -name "*.csv" -exec sed -i 's/\r$//' '{}' \;

# Makefile hard codes x86_64
# Tests also hard code the platform
# Need to make sure it matches the arch used in NEURON
# Macros don't work on 32bit builds, where we may get 1686 packages on i386 etc.
export MODSUBDIR=$(grep "^MODSUBDIR" /usr/bin/nrnivmodl | cut -d "=" -f2)
sed -i "s/x86_64/$MODSUBDIR/" Makefile
sed -i "s/x86_64/$MODSUBDIR/" bluepyopt/tests/test_l5pc.py
sed -i "s/x86_64/$MODSUBDIR/" bluepyopt/tests/test_stochkv.py

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -r}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l bluepyopt

%check
%pyproject_check_import -e *neuroml* -e bluepyopt.tests*
%if %{with tests}
# Prepare for tests
# Refer to: https://github.com/BlueBrain/BluePyOpt/blob/master/tox.ini
# and https://github.com/BlueBrain/BluePyOpt/blob/master/Makefile
%{py3_test_envvars} %make_build \
    stochkv_prepare l5pc_prepare sc_prepare meta_prepare
# test fail with a very slight approximation error
# neuroml test requires pyneuroml which cannot be included in fedora because of java things
k="${k-}${k+ and }not test_metaparameter"
k="${k-}${k+ and }not test_NrnRampPulse_instantiate"
k="${k-}${k+ and }not test_DEAPOptimisation_run"
k="${k-}${k+ and }not test_DEAPOptimisation_run_from_parents"
k="${k-}${k+ and }not test_optimisationsCMA_SO_run"
k="${k-}${k+ and }not test_optimisationsCMA_MO_run"
# This tests still fails after (fixed) `abor` has been added as BR
k="${k-}${k+ and }not test_LFPySquarePulse_instantiate"
k="${k-}${k+ and }not test_write_acc_expsyn"
# Why do we run pytest twice?
%{pytest} bluepyopt/tests/ -m "unit and not neuroml" "${k:+-k $k}"
%{pytest} bluepyopt/tests/ -m "not unit and not neuroml" "${k:+-k $k}"
# clean up whatever files were temporarily generated for tests
make clean
%endif

%files -n python3-bluepyopt -f %{pyproject_files}
%doc README.rst
%{_bindir}/bpopt_tasksdb

%files -n python3-bluepyopt-doc
%license COPYING COPYING.lesser
%doc examples

%changelog
%autochangelog
