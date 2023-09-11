%bcond_without tests

%global forgeurl  https://github.com/BlueBrain/eFEL
# Use github commit tar instead of pypi which does not include tests
%global commit d7a7e70daf905489d1cd0d91c3f158e7bae56828


%global desc %{expand: \
The Electrophys Feature Extraction Library (eFEL) allows neuroscientists to
automatically extract features from time series data recorded from neurons
(both in vitro and in silico). Examples are the action potential width and
amplitude in voltage traces recorded during whole-cell patch clamp experiments.
The user of the library provides a set of traces and selects the features to be
calculated. The library will then extract the requested features and return the
values to the user.

The core of the library is written in C++, and a Python wrapper is included. At
the moment we provide a way to automatically compile and install the library as
a Python module.}

Name:           python-efel
Version:        5.0.5
Release:        %autorelease
Summary:        Electrophys Feature Extraction Library
%forgemeta

# python-pyedflib does not support s390x$
# https://src.fedoraproject.org/rpms/python-pyedflib/blob/rawhide/f/python-pyedflib.spec$
ExcludeArch:    s390x

License:        LGPLv3
URL:            http://efel.readthedocs.io/
Source0:        %{forgesource}
# Use the _version.py from pypi
Source1:        _version.py

BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-efel
Summary:        %{summary}
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
# from extras, but neo in Fedora doesn't provide extras yet, so we can't use
# the -x neo flag in pyproject_buildrequires
BuildRequires:  python3-neo
BuildRequires:  python3-scipy

%description -n python3-efel
%{desc}

%prep
%forgesetup
%autopatch -p1
rm -rf efel.egg-info

# Install the version file
cp %{SOURCE1} efel/_version.py -v

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
# Remove headers. We won't provide them here.
rm -rf %{buildroot}/%{python3_sitearch}/efel/cppcore/
%pyproject_install
%pyproject_save_files efel


%check
%pyproject_check_import
%if %{with tests}
# https://github.com/BlueBrain/eFEL/blob/master/Makefile#L36: is obsolete
%pytest
%endif

%files -n python3-efel -f %{pyproject_files}
%exclude %{python3_sitearch}/efel/cppcore/
%doc README.md

%changelog
%autochangelog
