%global _description %{expand:
pybv is a lightweight exporter to the BrainVision data format. The BrainVision
data format is a recommended data format for use in the Brain Imaging Data
Structure. BrainVision is the name of a file format commonly used for storing
electrophysiology data. Originally, it was put forward by the company Brain
Products, however the simplicity of the format has allowed for a diversity
of tools reading from and writing to the format.

The format consists of three separate files:

* A text header file (.vhdr) containing meta data
* A text marker file (.vmrk) containing information about events in the data
* A binary data file (.eeg) containing the voltage values of the EEG}

Name:           python-pybv
Version:        0.6.0
Release:        %autorelease
Summary:        A lightweight I/O utility for the BrainVision data format

License:        BSD
URL:            https://pybv.readthedocs.io/en/stable/
Source0:        https://github.com/bids-standard/pybv/archive/v%{version}/pybv-%{version}.tar.gz

BuildArch:      noarch
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-pybv
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist mne}

%description -n python3-pybv %_description

%prep
%autosetup -n pybv-%{version}
rm -rf pybv.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# Remove linters etc from requirements
sed -i -e '/check-manifest/ d' -e '/pytest-/ d' -e '/flake8/ d' -e '/pycodestyle/ d' -e '/sphinx/ d' -e '/numpydoc/ d' requirements-dev.txt

%generate_buildrequires
%pyproject_buildrequires -r requirements-dev.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pybv

%check
%{pytest}

%files -n python3-pybv -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
