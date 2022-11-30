%global desc %{expand: \
LFPy is a Python-module for calculation of extracellular potentials from
multi-compartment neuron models. It relies on the NEURON simulator ( and uses
the Python interface ( it provides.LFPy provides a set of easy-to-use Python
classes for setting up your model, running your simulations and calculating the
extracellular potentials arising from activity in your model neuron. If you
have a model...}

Name:           python-lfpy
Version:        2.2.6
Release:        %autorelease
Summary:        Model extracellular potentials of multicompartment neuron models built on NEURON

License:        GPLv3
URL:            http://LFPy.readthedocs.io
Source0:        %{pypi_source LFPy}

# Requires NEURON, so limited to arches that NEURON and Random123 support
ExcludeArch:    mips64r2 mips32r2
# Upstream does not support powerpc or 32bit arches
# https://github.com/LFPy/LFPy/issues/173
# Bug: ppc: https://bugzilla.redhat.com/show_bug.cgi?id=1838565
# Bug: armv7hl: https://bugzilla.redhat.com/show_bug.cgi?id=1838564
ExcludeArch:    %{power64} %{ix86} armv7hl


BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

# Automatic dep generator doesn't like the mod files mentioned in the setup.py file, and tries to parse them as deps:
# error: Dependency tokens must begin with alpha-numeric, '_' or '/': "./expsyni.mod" "./sinsyn.mod"
# Should maybe reported as a pyproject rpm macro bug?
# So we install these manually

BuildRequires:  python3-Cython
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-lfpykit >= 0.4
BuildRequires:  python3-h5py
BuildRequires:  python3-neuron
BuildRequires:  neuron-devel
BuildRequires:  python3-pytest

# not included in setup.py
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3-neuron-openmpi
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  python3-neuron-mpich
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks

%description
%{desc}


%package -n     python3-lfpy
Summary:        %{summary}

Requires:   python3-mpi4py-openmpi
Requires:   python3-mpi4py-mpich
Requires:   neuron-devel


%description -n python3-lfpy
%{desc}

%prep
%autosetup -n LFPy-%{version}

# Remove mpi4py from requirements
sed -i '/mpi4py/ d' setup.py

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files LFPy


%check
# https://github.com/LFPy/LFPy/blob/master/continuous_integration/test_script.sh#L16
%{_mpich_load}
%{pytest} LFPy/test/

%pyproject_check_import -e *x86_64* -e *test*
%{_mpich_unload}

%{_openmpi_load}
%{pytest} LFPy/test/

%pyproject_check_import -e *x86_64* -e *test*
%{_openmpi_unload}

%files -n python3-lfpy -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
