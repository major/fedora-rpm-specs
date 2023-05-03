# No tests, they run examples for tests.
# https://github.com/Neurosim-lab/netpyne/blob/development/.travis.yml

# Some tests require optional pyneuroml, which cannot be packaged in Fedora.
# Refer to https://docs.fedoraproject.org/en-US/neurofedora/copr/ for more information.

# So these tests are disabled
# We add + enable the NeuroFedora COPR for pyneuroml in mock and run tests
# manually
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enablerepo=neurofedora-copr --with=pyneuroml

%bcond_with pyneuroml

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
Version:        1.0.4.1
Release:        %autorelease
Summary:        Develop, simulate and analyse biological neuronal networks in NEURON

# netpyne/support/stackedBarGraph.py is GPLv3+
# everything else is MIT
License:        MIT and GPLv3+
URL:            https://github.com/Neurosim-lab/netpyne/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
%autosetup -n netpyne-%{version}

sed -i 's/matplotlib<=3.5.1/matplotlib/' setup.py

# None executable script
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files netpyne

%check
# Do not test optional modules that have requirements not yet packaged in Fedora
# sbi: requires pytorch
%pyproject_check_import -e *optuna* -e *sbi*

export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
pushd doc/source/code
nrnivmodl mod
%{python3} tut2.py --nogui || true
%{python3} tut3.py --nogui || true
%{python3} tut4.py --nogui || true
%{python3} tut5.py --nogui || true
%{python3} tut6.py --nogui || true
%{python3} tut7.py --nogui || true
popd

pushd examples/HHTut
%{python3} HHTut_run.py -nogui || true
%if %{with pyneuroml}
%{python3} HHTut_export.py -nogui || true
%endif
popd

pushd examples/HybridTut
nrnivmodl .
%{python3} HybridTut_run.py -nogui || true
%if %{with pyneuroml}
%{python3} HybridTut_export.py -nogui || true
%endif
popd

pushd examples/M1
nrnivmodl .
%{python3} M1_run.py -nogui || true
%if %{with pyneuroml}
%{python3} M1_export.py -nogui || true
%endif
popd

pushd examples/PTcell
nrnivmodl mod
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
