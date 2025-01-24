%bcond tests 1

# Do not build docs, bundle JS etc.
# Point to upstream docs instead

%global desc %{expand: \
Brian2 is a simulator for spiking neural networks available on almost all
platforms. The motivation for this project is that a simulator should not only
save the time of processors, but also the time of scientists.

It is the successor of Brian1 and shares its approach of being highly flexible
and easily extensible. It is based on a code generation framework that allows
to execute simulations using other programming languages and/or on different
devices.

Please report issues to the github issue tracker
(https://github.com/brian-team/brian2/issues) or to the brian support mailing
list (http://groups.google.com/group/briansupport/)

Documentation for Brian2 can be found at http://brian2.readthedocs.org}

%global forgeurl https://github.com/brian-team/brian2

Name:           python-brian2
Version:        2.8.0.1
Release:        %autorelease
Summary:        A clock-driven simulator for spiking neural networks

%global tag %{version}

%forgemeta


License:        CECILL-2.0
URL:            https://briansimulator.org
Source0:        %forgesource

# Drop i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++ gcc
BuildRequires:  gsl-devel

%description
%{desc}

%package -n python3-brian2
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

Suggests:       %{py3_dist ipython}
%py_provides python3-brian2

%description -n python3-brian2
%{desc}

%package doc
Summary:    %{summary}
BuildArch:  noarch

%description doc
Documentation and examples for %{name}.


%prep
%forgeautosetup

# remove pre-compiled standalone binary example---the scripts there regenerate it
rm -rf examples/multiprocessing/standalone307987

# Relax numpy and pytest version constraints
sed -r \
    -e 's/"numpy>=2.*",/"numpy",/' \
    -e 's/pytest>=8/pytest/' \
    -i pyproject.toml


# Remove unnecessary files
find . -name ".gitignore" -print -delete
rm -rvf Brian2.egg-info
rm -f brian2/synapses/cythonspikequeue.cpp

# Correct shebang for examples
find examples -name "*.py" -print -exec sed -i 's|^#!/usr/bin/env python|#!/usr/bin/python3|' '{}' \;

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r %{?with_tests:-x test}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l "brian2*"

%check
%pyproject_check_import -e brian2.hears -t

%if %{with tests}
export PYTHONDONTWRITEBYTECODE=1
# https://github.com/brian-team/brian2/blob/master/dev/continuous-integration/run_test_suite.py
# https://brian2.readthedocs.io/en/stable/developer/guidelines/testing.html
# prevent direct import
pushd ../
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitearch}/ %{python3} -c 'import brian2; brian2.test(test_openmp=True, test_GSL=True, test_codegen_independent=True, test_in_parallel=["codegen_independent", "numpy", "cpp_standalone"])'
popd
%endif

# remove pytest_cache
rm -rf $RPM_BUILD_ROOT/%{python3_sitearch}/brian2/{tests,}/.pytest_cache/

%files -n python3-brian2 -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc examples

%changelog
%autochangelog
