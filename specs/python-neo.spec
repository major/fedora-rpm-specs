# downloads LARGE amounts of test data so must be run with network enabled in mock:
# --with=tests --enable-network
# Note: all tests pass, they just take a lot of bandwidth and time.
# 5 tests do not pass because we do not have sonpy in the repos yet.
%bcond_with tests

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

%global forgeurl  https://github.com/NeuralEnsemble/python-neo

Name:       python-neo
Version:    0.14.0
Release:    %autorelease
Summary:    Represent electrophysiology data in Python

%global tag %{version}
%forgemeta

License:    BSD-3-Clause
URL:        %forgeurl
Source0:    %forgesource
%if %{with tests}
# datalad clone of data obtained with these commands:
# datalad clone https://gin.g-node.org/NeuralEnsemble/ephy_testing_data
# tar -cvzf ephy_testing_data.tar.gz ephy_testing_data
Source1:    ephy_testing_data.tar.gz
%endif


BuildArch:  noarch

# python-pyedflib does not support s390x
# https://src.fedoraproject.org/rpms/python-pyedflib/blob/rawhide/f/python-pyedflib.spec
ExcludeArch:  s390x

%description %{_description}

%package -n python3-neo
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  datalad
BuildRequires:  python3-pillow
BuildRequires:  python3-pytest
# https://github.com/NeuralEnsemble/python-neo/issues/1471: neuroshare is dead

# Extra requires:
# Not in fedora yet, to be updated as these are added
# Recommends:  %%{py3_dist stfio}
Recommends:  %{py3_dist nixio}
Recommends:  %{py3_dist klusta}
Recommends:  %{py3_dist scipy}
Recommends:  %{py3_dist hypy}
Recommends:  %{py3_dist igor}

%description -n python3-neo %{_description}

%prep
%forgeautosetup
# remove rpm's SPECPARTS file
rm -rf SPECPARTS

# Remove upstream's pin to py<3.13
sed -i '/requires-python/ d' pyproject.toml

%if %{with tests}
# datalad needs to know who we are later when it tries to download the data sets
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Unpack test data tar in ~
pushd ~ && %{__tar} -xvf %{SOURCE1} && popd
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l neo

%check
# do not export EPHY_TESTING_DATA_FOLDER, use ~
# exclude one that requires "zugbruecke" to open windows dlls?
%pyproject_check_import -e *pypl2.pypl2lib*
%if %{with tests}
%pytest
%endif

%files -n python3-neo -f %{pyproject_files}
%doc README.rst examples doc/source/authors.rst CODE_OF_CONDUCT.md CITATION.txt

%changelog
%autochangelog
