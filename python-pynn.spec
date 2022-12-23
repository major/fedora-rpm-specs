%bcond_without mpich
%bcond_without openmpi

# Tests
# https://github.com/NeuralEnsemble/PyNN/blob/master/ci/test_script.sh
# Use nose, so disabled by default, but tested locally with --with-nosetests
# Issue filed upstream: https://github.com/NeuralEnsemble/PyNN/issues/705
%bcond_with nosetests

# Issue filed about warnings while compiling NEURON mod files:
# https://github.com/NeuralEnsemble/PyNN/issues/707


# Exclude privately used libnrnmech from provides
%global __provides_exclude ^libnrnmech\\.so.*$

%global _description %{expand:
PyNN (pronounced 'pine') is a simulator-independent language for building
neuronal network models.

In other words, you can write the code for a model once, using the PyNN API and
the Python programming language, and then run it without modification on any
simulator that PyNN supports (currently NEURON, NEST and Brian) and on a number
of neuromorphic hardware systems.

The PyNN API aims to support modelling at a high-level of abstraction
(populations of neurons, layers, columns and the connections between them)
while still allowing access to the details of individual neurons and synapses
when required. PyNN provides a library of standard neuron, synapse and synaptic
plasticity models, which have been verified to work the same on the different
supported simulators. PyNN also provides a set of commonly-used connectivity
algorithms (e.g. all-to-all, random, distance-dependent, small-world) but makes
it easy to provide your own connectivity in a simulator-independent way.

Even if you don’t wish to run simulations on multiple simulators, you may
benefit from writing your simulation code using PyNN’s powerful, high-level
interface. In this case, you can use any neuron or synapse model supported by
your simulator, and are not restricted to the standard models.

Documentation: http://neuralensemble.org/docs/PyNN/
Mailing list: https://groups.google.com/forum/?fromgroups#!forum/neuralensemble

This package supports the NEURON, NEST, and Brian simulators.}

Name:           python-pynn
Version:        0.10.0
Release:        %autorelease
Summary:        A package for simulator-independent specification of neuronal network models

License:        CeCILL
URL:            http://neuralensemble.org/PyNN/
Source0:        %pypi_source PyNN

# Random123 does not build on these, so neither can NEURON, so nothing that
# depends on NEURON supports them either
# https://github.com/neuronsimulator/nrn/issues/114
# python-pyedflib does not support s390x, so the complete dep tree needs to also exclude it
# https://src.fedoraproject.org/rpms/python-pyedflib/blob/rawhide/f/python-pyedflib.spec
ExcludeArch:    mips64r2 mips32r2 s390x

# Disable pynn's way of building extensions
# We do it ourselves
Patch0:         0001-Disable-nest-extension-build-by-setup.patch
# Merged upstream: https://github.com/NeuralEnsemble/PyNN/pull/744
Patch1:         0002-fix-correct-sized-import.patch

Patch2:         0003-Fix-errors-of-type-error-implicit-declaration-of-fun.patch

# For extensions
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gsl-devel
BuildRequires:  libneurosim-devel
BuildRequires:  ncurses-devel
BuildRequires:  nest-devel >= 3.0
BuildRequires:  neuron-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  readline-devel

BuildRequires:  python3-brian2
BuildRequires:  python3-cheetah
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist lazyarray}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist neo}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist nose-testconfig}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  python3-nest >= 3.0
BuildRequires:  nest >= 3.0
BuildRequires:  python3-neuron
BuildRequires:  %{py3_dist quantities}

%if %{with mpich}
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  python3-nest-mpich >= 3.0
BuildRequires:  nest-mpich >= 3.0
BuildRequires:  python3-neuron-mpich
BuildRequires:  rpm-mpi-hooks
BuildRequires:  mpich
BuildRequires:  mpich-devel
%endif

%if %{with openmpi}
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3-nest-openmpi >= 3.0
BuildRequires:  nest-openmpi >= 3.0
BuildRequires:  python3-neuron-openmpi
BuildRequires:  rpm-mpi-hooks
BuildRequires:  openmpi
BuildRequires:  openmpi-devel
%endif


%{?python_enable_dependency_generator}

%description %_description

%package devel
Summary:        %{summary}
Requires:       python3-pynn%{?_isa} = %{version}-%{release}

%description devel %_description

%package -n python3-pynn
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-pynn %_description

%package doc
Summary:        %{summary}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n PyNN-%{version} -S git
rm -rfv PyNN-%{version}/pyNN.egg-info

%build
%py3_build

# Build NEURON modules
pushd ./build/lib/pyNN/neuron/nmodl/ || exit 1
    nrnivmodl .
popd
# The tests however, look for these here, so we also build them
pushd pyNN/neuron/nmodl || exit 1
    nrnivmodl .
popd

# NEST extensions: we build and install them ourselves
pushd ./build/lib/pyNN/nest/extensions/ || exit 1
    %cmake -Dwith-nest=%{_bindir}/nest-config
    %cmake_build
popd

%install
%py3_install

# NEST extensions
pushd ./build/lib/pyNN/nest/extensions/ || exit 1
    %cmake_install
popd

# Includes compiled arch specific files but installs in /lib
# Manually move to arch specific folder
%if "%{python3_sitelib}" != "%{python3_sitearch}"
mkdir -p 0644 $RPM_BUILD_ROOT/%{python3_sitearch}/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/pyNN $RPM_BUILD_ROOT/%{python3_sitearch}/
mv $RPM_BUILD_ROOT/%{python3_sitelib}/PyNN-%{version}-py%{python3_version}.egg-info $RPM_BUILD_ROOT/%{python3_sitearch}/
%endif

# Delete temporary files that do not need to be installed
rm -rf $RPM_BUILD_ROOT/%{python3_sitearch}/pyNN/nest/extensions

%check
%py3_check_import pyNN pyNN.nest pyNN.neuron pyNN.brian2

%if %{with nosetests}
pushd test
export PYTHONPATH=$PYTHONPATH:$RPM_BUILD_ROOT/%{python3_sitearch}:$RPM_BUILD_ROOT/%{python3_sitelib}
nosetests-%{python3_version} -e backends --verbosity=3 --tests=unittests
unset PYTHONPATH
popd
%endif

%if %{with mpich}
%{_mpich_load}
export PYTHONPATH=$PYTHONPATH:$RPM_BUILD_ROOT/%{python3_sitearch}:$RPM_BUILD_ROOT/%{python3_sitelib}:$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH:$MPI_PYTHON3_SITEARCH
%py3_check_import pyNN pyNN.nest pyNN.neuron pyNN.brian2

%if %{with nosetests}
pushd test
nosetests-%{python3_version} -e backends --verbosity=3 --tests=unittests
popd
%{_mpich_unload}
%endif
unset PYTHONPATH
%endif

%if %{with openmpi}
%{_openmpi_load}
export PYTHONPATH=$PYTHONPATH:$RPM_BUILD_ROOT/%{python3_sitearch}:$RPM_BUILD_ROOT/%{python3_sitelib}:$RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH:$MPI_PYTHON3_SITEARCH
%py3_check_import pyNN pyNN.nest pyNN.neuron pyNN.brian2

%if %{with nosetests}
pushd test
nosetests-%{python3_version} -e backends --verbosity=3 --tests=unittests
popd
%{_openmpi_unload}
%endif
unset PYTHONPATH
%endif

# These files are NEURON files that are required by PyNN to run bits using the NEURON backend
# The libnrnmech.so file, along with the .libs/libnrnmech.so symlink are both required
# So is the "special" script that loads these libraries
# We can remove some temporary compilation files, though:
find $RPM_BUILD_ROOT/%{python3_sitearch}/pyNN/neuron/nmodl/*/ -name "*.c" -o -name "*.c" -o -name "*.mod" -delete


%files -n python3-pynn
%license LICENSE
%doc README.rst AUTHORS changelog
%{_libdir}/nest/
%{_datadir}/nest/sli/pynn_extensions-init.sli
%{python3_sitearch}/pyNN
%{python3_sitearch}/PyNN-%{version}-py%{python3_version}.egg-info

%files devel
%{_includedir}/pynn_extensions.h

%files doc
%license LICENSE
%doc examples


%changelog
%autochangelog
