# Try to download data, so a few are disabled.
# We test these in mock using --with=net_tests --enable-network
%bcond_with net_tests

%global pypi_name elephant

Name:       python-elephant
Version:    0.11.1
Release:    %autorelease
Summary:    Elephant is a package for analysis of electrophysiology data in Python
License:    BSD
URL:        http://neuralensemble.org/elephant
Source0:    %{pypi_source elephant}
# All changes are here
# https://github.com/sanjayankur31/elephant/tree/fedora-0.11.1
Patch0:     0001-use-fedora-build-flags.patch

# Includes a modified copy of fim, so we cannot use the system copy of pyfim.
# https://github.com/NeuralEnsemble/elephant/issues/471#issuecomment-1098908479

BuildRequires:  git-core
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%description
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%package -n     python3-elephant
Summary:        %{summary}


%description -n python3-elephant
Elephant - Electrophysiology Analysis Toolkit Elephant is a package for the
analysis of neurophysiology data, based on Neo.

%prep
%autosetup -n elephant-%{version} -S git

# Loosen scipy version cap
# https://github.com/NeuralEnsemble/elephant/issues/47
sed -i 's/scipy.*/scipy/' requirements/requirements.txt

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# collect all test requirements in one file
echo >> requirements/requirements-tests.txt
cat requirements/requirements-extras.txt >> requirements/requirements-tests.txt

%generate_buildrequires
%pyproject_buildrequires -r requirements/requirements-tests.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files elephant

%check
# One test fails generally: reported upstream
# https://github.com/NeuralEnsemble/elephant/issues/410
# Fixed upstream (but Fedora dropped armv7hl support in F37)
# https://github.com/NeuralEnsemble/elephant/pull/500
#k="not test__UE_surrogate"

# fails on aarch64
# reported upstream: https://github.com/NeuralEnsemble/elephant/issues/479
%ifarch %{arm64}
k="${k:-}${k:+ and }not test_welch_psd_multidim_input and not test_welch_cohere_multidim_input"
%endif

%if %{without net_tests}
# Disable tests that download bits
k="${k:-}${k:+ and }not test_repr and not test__UE_surrogate and not test_spike_contrast_with_Izhikevich_network_auto and not test_Riehle_et_al_97_UE and not test_multitaper_psd_against_nitime"
%endif

# serial
# MPI tests hang in mock and builders, not sure why, so we skip them for the moment
%pytest -v -k "${k} and not test_parallel"

%files -n python3-elephant -f %{pyproject_files}
%license LICENSE.txt elephant/spade_src/LICENSE

%changelog
%autochangelog
