%global pypi_name python-xmp-toolkit
%global srcname xmp-toolkit

Name:           python-%{srcname}
Version:        2.0.2
Release:        %autorelease
Summary:        Python XMP Toolkit for working with metadata

License:        BSD-3-Clause
URL:            https://github.com/python-xmp-toolkit/python-xmp-toolkit
# Can't use pypi_source due to https://github.com/python-xmp-toolkit/python-xmp-toolkit/issues/91
Source0:        https://github.com/python-xmp-toolkit/python-xmp-toolkit/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# https://github.com/python-xmp-toolkit/python-xmp-toolkit/pull/84
Source1:        https://github.com/python-xmp-toolkit/python-xmp-toolkit/raw/e0f42af4a731ac1eea2977895f2c8dd0264304c3/test/samples/BlueSquare.gif
Patch:          https://github.com/python-xmp-toolkit/python-xmp-toolkit/commit/0cbdae107d9b8e825511c6a6833d47923208ed7d.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  exempi
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)

%description
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.

%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       exempi

%description -n python3-%{srcname}
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.


%package -n python-%{srcname}-doc
Summary:        python-xmp-toolkit documentation

%description -n python-%{srcname}-doc
Documentation for python-xmp-toolkit


%prep
%autosetup -n %{pypi_name}-%{version} -p1
cp %SOURCE1 test/samples/

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH="$PWD/build/lib" sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l libxmp


%check
%{python3} setup.py test


%files -n python3-%{srcname} -f %{pyproject_files}
#license LICENSE
%doc README.rst

%files -n python-%{srcname}-doc
%doc html
%license LICENSE


%changelog
%autochangelog
