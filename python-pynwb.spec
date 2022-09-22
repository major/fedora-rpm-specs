%global desc %{expand:
PyNWB is a Python package for working with NWB files. It provides a high-level
API for efficiently working with Neurodata stored in the NWB format.
https://pynwb.readthedocs.io/en/latest/}

Name:           python-pynwb
Version:        2.1.0
Release:        %autorelease
Summary:        PyNWB is a Python package for working with NWB files
License:        BSD
URL:            https://github.com/NeurodataWithoutBorders/pynwb
# Use the pypi tar because GitHub tar does not include the required git-submodules
Source0:        %{pypi_source pynwb}
BuildArch:      noarch

%description %{desc}

%package -n python3-pynwb
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-pynwb %{desc}

%prep
%autosetup -n pynwb-%{version}
# test_validate uses python instead of python3
sed -i 's|python|python3|' tests/validation/test_validate.py

# unpin deps
for i in requirements*txt
do
    sed -i 's/==.*//' $i
done
sed -i -e "s/h5py>.*'/h5py'/" -e "s/numpy>.*'/numpy'/" -e "s/pandas>.*'/pandas'/" setup.py


%generate_buildrequires
%pyproject_buildrequires -r requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pynwb

%check
# do not run ros tests (--ros3)
export PYTHONPATH=".:%{buildroot}/%{python3_sitelib}:%{buildroot}/%{python3_sitearch}" 
# run unit tests using pytest so that we can exclude tests that fail etc., which is hard to do with the test.py script
# Disable test which fails on s390x on F34
%if 0%{?fedora} < 35 && "%{_host_cpu}" == "s390x" || "%{_host_cpu}" == "ppc64le"
%{pytest} tests/unit -k "not test_icephys_filtering_roundtrip"
%else
%{pytest} tests/unit
%endif
%{python3} test.py --example --validation --integration --backwards

%files -n python3-pynwb -f %{pyproject_files}
%license license.txt
%doc README.rst

%changelog
%autochangelog
