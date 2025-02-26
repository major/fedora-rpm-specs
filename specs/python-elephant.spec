# Try to download data, so a few are disabled.
# We test these in mock using --with=net_tests --enable-network
%bcond net_tests 0

%global forgeurl  https://github.com/NeuralEnsemble/elephant/

Name:       python-elephant
Version:    1.1.1
Release:    %autorelease
Summary:    Analysis of electrophysiology data, using Neo data structures

%forgemeta

# SPDX
# elephant/spade_src is MIT licensed
License:    BSD-3-Clause AND MIT
URL:        http://neuralensemble.org/elephant
Source0:    %forgesource

# All changes are here
# https://github.com/sanjayankur31/elephant/tree/fedora-0.11.1
Patch0:     0001-use-fedora-build-flags.patch
# Fix for numpy 2
Patch:      https://patch-diff.githubusercontent.com/raw/NeuralEnsemble/elephant/pull/656.diff

# python-pyedflib does not support s390x, so the complete dep tree needs to also exclude it
# https://src.fedoraproject.org/rpms/python-pyedflib/blob/rawhide/f/python-pyedflib.spec
ExcludeArch: s390x

# Stop building for i686 (leaf package)
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Includes a modified copy of fim, so we cannot use the system copy of pyfim.
# https://github.com/NeuralEnsemble/elephant/issues/471#issuecomment-1098908479

BuildRequires:  git-core
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%global _description %{expand:
Elephant (Electrophysiology Analysis Toolkit) is an open-source,
community centered library for the analysis of electrophysiological
data in the Python programming language. The focus of Elephant is on
generic analysis functions for spike train data and time series
recordings from electrodes, such as the local field potentials (LFP) or
intracellular voltages. In addition to providing a common platform for
analysis code from different laboratories, the Elephant project aims to
provide a consistent and homogeneous analysis framework that is built
on a modular foundation. Elephant is the direct successor to Neurotools
and maintains ties to complementary projects such as OpenElectrophy and
spykeviewer.

Elephant was developed in part in the Human Brain Project, funded from
the European Union’s Horizon 2020 Framework Programme for Research and
Innovation under Specific Grant Agreements No. 720270, No. 785907 and
No. 945539 (Human Brain Project SGA1, SGA2, and SGA3).}

%description %_description


%package -n     python3-elephant
Summary:        %{summary}

%description -n python3-elephant %_description


%prep
%forgeautosetup -S git

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

# Drop `nixio` test requirement.
sed  -r -i '/nixio/d' requirements/requirements-tests.txt


%generate_buildrequires
%pyproject_buildrequires -r requirements/requirements-tests.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l elephant


%check
# One test fails generally: reported upstream
# https://github.com/NeuralEnsemble/elephant/issues/410
# Fixed upstream (but Fedora dropped armv7hl support in F37)

# fails on aarch64
# reported upstream: https://github.com/NeuralEnsemble/elephant/issues/479
%ifarch %{arm64}
k="${k:-}${k:+ and }not test_welch_psd_multidim_input"
k="${k:-}${k:+ and }not test_welch_cohere_multidim_input"
k="${k:-}${k:+ and }not test_multitaper_cohere_perfect_cohere"
%endif

# fails on ppc64le
%ifarch %{power64}
k="${k:-}${k:+ and }not test_multitaper_cohere_perfect_cohere"
%endif

%if %{without net_tests}
# Disable tests that download bits
k="${k:-}${k:+ and }not test_repr"
k="${k:-}${k:+ and }not test__UE_surrogate"
k="${k:-}${k:+ and }not test_spike_contrast_with_Izhikevich_network_auto"
k="${k:-}${k:+ and }not test_Riehle_et_al_97_UE"
k="${k:-}${k:+ and }not test_multitaper_psd_against_nitime"
k="${k:-}${k:+ and }not test_WPLI_"
k="${k:-}${k:+ and }not test_victor_purpura_matlab_comparison_"
k="${k:-}${k:+ and }not test_pairwise_spectral_granger"
k="${k:-}${k:+ and }not test_total_spiking_probability_edges"
%endif

# Requires `nixio` in addition to network.
k="${k:-}${k:+ and }not test_sttc_validation_test"

%pytest -v ${k+-k }"${k-}"


%files -n python3-elephant -f %{pyproject_files}
%license elephant/spade_src/LICENSE


%changelog
%autochangelog
