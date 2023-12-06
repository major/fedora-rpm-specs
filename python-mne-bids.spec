# The test require internet to download data and so cannot be run in koji
# Confirmed all tests pass in mock with network access:
# mock -r fedora-rawhide-x86_64 rebuild ./python-mne-bids-0.1-2.fc29.src.rpm
# --enable-network --rpmbuild-opts="--with tests"
# Test disable
%bcond_with tests

%global desc %{expand: \
MNE-BIDS: Organizing MEG, EEG, and iEEG data according to the BIDS
specification and facilitating their analysis with MNE-Python}

Name:           python-mne-bids
Version:        0.14
Release:        %autorelease
Summary:        Experimental code for BIDS using MNE
License:        BSD-3-Clause
URL:            https://github.com/mne-tools/mne-bids
Source0:        %{url}/archive/v%{version}/mne-bids-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch:    %{ix86}

%description
%{desc}

%package -n python3-mne-bids
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# not automatically generated
Requires:  python3-pandas
Requires:  python3-six
Requires:  python3-nose
Requires:  python3-pytest-shutil
Requires:  python3-matplotlib
Requires:  python3-tempita

%description -n python3-mne-bids
%{desc}

%prep
%autosetup -n mne-bids-%{version}

# Not required on the python versions Fedora uses
sed -i '/importlib-resources/ d' setup.cfg

sed -i 's/mne.externals.six/six/' mne_bids/utils.py
find -type f -name '*.py' -exec sed -i \
  -e "s/from mne.externals.tempita/from tempita/" \
  {} ';'

# remove she-bang lines in .py files.
find * -type f -name "*.py" -exec sed -i '/^#![ ]*\/usr\/bin\/.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mne_bids

%check
%if %{with tests}
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
%{pytest} mne_bids -W ignore::DeprecationWarning
%endif

# Run test require internet
# Example:
# mock -r fedora-rawhide-x86_64 rebuild ./python-mne-bids-0.1-2.fc29.src.rpm --enable-network --rpmbuild-opts="--with tests"

%files -n python3-mne-bids -f %{pyproject_files}
%doc README.md examples/README.rst
%{_bindir}/mne_bids

%changelog
%autochangelog
