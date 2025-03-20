%global pypi_name ANNarchy

# Running all tests is time consuming. Allow skipping of tests.
%bcond tests 1

Name:           python-annarchy
Version:        4.8.2.5
Release:        %{autorelease}
Summary:        Artificial Neural Networks architect

%global forgeurl https://github.com/ANNarchy/ANNarchy
%global tag %{version}
%forgemeta

# ANNarchy/thirdparty/randutils.hpp is MIT
License:        GPL-2.0-or-later AND MIT
URL:            https://annarchy.github.io/
Source:         %forgesource

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Tests fail on ppc64le (under investigation)
ExcludeArch:    %{ix86} ppc64le
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
ANNarchy 🏴 (Artificial Neural Networks architect) is a parallel and
hybrid simulator for distributed rate-coded or spiking neural networks.
The core of the library is written in C++ and distributed using OpenMP
or CUDA. It provides an interface in Python for the definition of the
networks.

NOTE: Since CUDA support requires proprietary Nvidia drivers, this
package only supports OpenMP and single thread.}

%description %_description


%package -n python3-annarchy
Summary:        %{summary}
Requires:       (flexiblas-openblas-openmp or openblas-openmp)
# Also `tensorflow` and `tensorboardX` (not availabale in Fedora)
Recommends:     python3dist(h5py)
Recommends:     python3dist(lxml)
Recommends:     pandoc

%description -n python3-annarchy %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%if %{with tests}
%pytest -v tests/test_openmp.py
%pytest -v tests/test_single_thread.py
%endif


%files -n python3-annarchy -f %{pyproject_files}
%doc README.md AUTHORS CHANGELOG


%changelog
%autochangelog
