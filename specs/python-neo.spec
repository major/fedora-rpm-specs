# IO tests download LARGE amounts of test data so must be run with
# network enabled in mock:
# --with io_tests --enable-network
# Note: all tests pass, they just take a lot of bandwidth and time.
# Tests with unsatisfied dependencies will be skipped.
%bcond io_tests 0

# Run tests that do not require network or special dependencies.
%bcond tests 1

%global _description %{expand:
Neo is a package for representing electrophysiology data in Python, together
with support for reading a wide range of neurophysiology file formats,
including Spike2, NeuroExplorer, AlphaOmega, Axon, Blackrock, Plexon, Tdt, and
support for writing to a subset of these formats plus non-proprietary formats
including HDF5.

The goal of Neo is to improve interoperability between Python tools for
analyzing, visualizing and generating electrophysiology data (such as
OpenElectrophy, NeuroTools, G-node, Helmholtz, PyNN) by providing a common,
shared object model. In order to be as lightweight a dependency as possible,
Neo is deliberately limited to representation of data, with no functions for
data analysis or visualization.

Neo implements a hierarchical data model well adapted to intracellular and
extracellular electrophysiology and EEG data with support for multi-electrodes
(for example tetrodes). Neos data objects build on the quantities_ package,
which in turn builds on NumPy by adding support for physical dimensions. Thus
neo objects behave just like normal NumPy arrays, but with additional metadata,
checks for dimensional consistency and automatic unit conversion.

Read the documentation at http://neo.readthedocs.io/}

Name:       python-neo
Version:    0.14.2
Release:    %autorelease
Summary:    Represent electrophysiology data in Python

%global forgeurl https://github.com/NeuralEnsemble/python-neo
%global tag %{version}
%forgemeta

License:    BSD-3-Clause
URL:        %forgeurl
Source:     %forgesource

BuildArch:  noarch

# python-pyedflib does not support s390x
# https://src.fedoraproject.org/rpms/python-pyedflib/blob/rawhide/f/python-pyedflib.spec
ExcludeArch:  s390x

%description %{_description}

%package -n python3-neo
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests} || %{with io_tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist ipython}
%if %{with io_tests}
BuildRequires:  %{py3_dist datalad}
BuildRequires:  %{py3_dist pyedflib}
BuildRequires:  %{py3_dist h5py}
# Retired from Fedora. Dead upstream and didn't work with Python 3.12.
# However, there is igor2' on PyPI. But that's not available in Fedora.
%dnl BuildRequires:  %{py3_dist igor}
BuildRequires:  %{py3_dist klusta}
BuildRequires:  %{py3_dist nixio}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist probeinterface}
# Some tests require pynwb. However with the current version (2.8.3)
# a PermissionError is raised.
%dnl BuildRequires:  %{py3_dist pynwb}
%endif
%endif
# https://github.com/NeuralEnsemble/python-neo/issues/1471: neuroshare is dead

# Extra requires:
# Not in fedora yet, to be updated as these are added
# Recommends:  %%{py3_dist stfio}
Recommends:  %{py3_dist datalad}
Recommends:  %{py3_dist h5py}
# Retired from Fedora. Dead upstream and didn't work with Python 3.12.
# However, there is igor2' on PyPI. But that's not available in Fedora.
%dnl Recommends:  %{py3_dist igor}
Recommends:  %{py3_dist nixio}
Recommends:  %{py3_dist klusta}
Recommends:  %{py3_dist pillow}
Recommends:  %{py3_dist probeinterface}
Recommends:  %{py3_dist pynwb}
Recommends:  %{py3_dist scipy}

%description -n python3-neo %{_description}


%prep
%forgeautosetup
# remove rpm's SPECPARTS file
rm -rf SPECPARTS

# Remove upstream's pin to py<3.13
sed -i '/requires-python/ d' pyproject.toml

# Unpin setuptools
sed -r -i 's/(setuptools)[<=>]+[0-9.]+/\1/' pyproject.toml

%if %{with io_tests}
# datalad needs to know who we are later when it tries to download the data sets
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l neo


%check
%if 0%{with tests} || 0%{with io_tests}
%if %{with io_tests}
# Requires Maxwell H5 (HDF5) compression library, which needs to be
# and installed manually.
k="${k:-}${k:+ and }not TestMaxwell"
%endif
%pytest \
%if %{without io_tests}
  --ignore=neo/test/iotest/ \
  --ignore=neo/test/rawiotest/ \
  --deselect=neo/test/utils/test_datasets.py::TestDownloadDataset \
%endif
  -r fEs ${k:+-k "${k:-}"}
%else
  # do not export EPHY_TESTING_DATA_FOLDER, use ~
  # exclude one that requires "zugbruecke" to open windows dlls?
  # Also exclude tests from import check.
  %pyproject_check_import -e *pypl2.pypl2lib* -e neo.test*
%endif


%files -n python3-neo -f %{pyproject_files}
%doc README.rst examples doc/source/authors.rst CODE_OF_CONDUCT.md CITATION.txt


%changelog
%autochangelog
