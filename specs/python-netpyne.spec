# No tests, they run examples for tests.
# https://github.com/Neurosim-lab/netpyne/blob/development/.travis.yml

# Some tests require optional pyneuroml, which cannot be packaged in Fedora.
# Refer to https://docs.fedoraproject.org/en-US/neurofedora/copr/ for more information.

# So these tests are disabled
# We add + enable the NeuroFedora COPR for pyneuroml in mock and run tests
# manually
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enablerepo=neurofedora-copr --with=pyneuroml

%bcond pyneuroml 0

# disable debuginfo
# sub package is noarch, but keep the main package archful to run tests on all arches.
%global debug_package  %{nil}

%global _description %{expand:
NetPyNE is a Python package to facilitate the development, simulation,
parallelization, analysis, and optimization of biological neuronal networks
using the NEURON simulator.

For more details, installation instructions, documentation, tutorials, forums,
videos and more, please visit: www.netpyne.org

This package is developed and maintained by the Neurosim lab
(www.neurosimlab.org) }

Name:           python-netpyne
Version:        1.0.7
Release:        %autorelease
Summary:        Develop, simulate and analyse biological neuronal networks in NEURON

%global forgeurl https://github.com/Neurosim-lab/netpyne/
%forgemeta

# netpyne/support/stackedBarGraph.py is GPLv3+
# netpyne/support/filter.py is GPLv3
# netpyne/analysis/filter.py is GPLv3
# everything else is MIT
# spdx
License:        MIT AND GPL-3.0-only AND GPL-3.0-or-later
URL:            %forgeurl
Source0:        %forgesource

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# https://github.com/suny-downstate-medical-center/netpyne/pull/767
# merged but not released
Patch:          https://github.com/suny-downstate-medical-center/netpyne/pull/767.patch

# fix mod files to work with c23
Patch:          0001-fix-verbatim-function-defs-in-mod-files.patch

%description %_description

%package -n python3-netpyne
Summary:        %{summary}
# Main package is not noarch so that tests can be run on all platforms
# but the sub-package can be noarch
BuildArch:      noarch

BuildRequires:  gcc-g++
BuildRequires:  neuron-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-neuron
# skipped in setup.py
BuildRequires:  python3-dill

%if %{with pyneuroml}
BuildRequires:  %{py3_dist pyneuroml}
%endif

# Not mentioned in setup.py etc.
Requires:  %{py3_dist neuron}

# Optional dep in COPR, users will have to install it manually if they want to use its features
# Requires:  %%{py3_dist pyneuroml}

%description -n python3-netpyne %_description

%prep
%forgeautosetup -p1

sed -e 's/"future",//' \
    -i setup.py

# None executable script
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l netpyne

%check
# Do not test optional modules that have requirements not yet packaged in Fedora
# sbi: requires pytorch
# batchtools: requires ray batchtk + ray
%pyproject_check_import -e *optuna* -e *sbi* -e *batchtools*

export %{py3_test_envvars}
pushd doc/source/code
nrnivmodl mod
%{python3} tut2.py --nogui || true
%{python3} tut3.py --nogui || true
%{python3} tut4.py --nogui || true
%{python3} tut5.py --nogui || true
%{python3} tut6.py --nogui || true
%{python3} tut7.py --nogui || true
popd

# some of these are currently broken upstream
pushd examples/HHTut/src
%{python3} init.py -nogui || true
popd

pushd examples/HybridTut/src/
nrnivmodl ../mod/
%{python3} init.py -nogui || true
popd

pushd examples/M1/src
nrnivmodl ../mod
%{python3} init.py -nogui || true
popd

# this one failes, there's no init.py file in the main directory
pushd examples/PTcell/src
nrnivmodl ../mod/
%{python3} init.py -nogui || true
popd

pushd examples/LFPrecording
nrnivmodl mod
%{python3} cell_lfp.py -nogui || true
popd

pushd examples/saving
%{python3} init.py -nogui || true
popd

pushd examples/rxd_buffering
%{python3} buffering.py -nogui || true
popd

pushd examples/rxd_net/
nrnivmodl mod
%{python3} src/init.py -nogui || true
popd

%if %{with pyneuroml}
pushd examples/NeuroMLImport/
nrnivmodl .
%{python3} SimpleNet_import.py -nogui || true
popd
%endif

%files -n python3-netpyne -f %{pyproject_files}
%doc README.md CHANGES.md

%changelog
%autochangelog
