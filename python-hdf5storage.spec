# upstream has moved to pytest but not made a release yet.
# For the time being, it uses nose, so we disable tests by default
%bcond_with tests

%global forgeurl https://github.com/frejanordsiek/hdf5storage

%global _description %{expand:
This Python package provides high level utilities to read/write a variety of
Python types to/from HDF5 (Heirarchal Data Format) formatted files. This
package also provides support for MATLAB MAT v7.3 formatted files, which are
just HDF5 files with a different extension and some extra meta-data.

All of this is done without pickling data. Pickling is bad for security because
it allows arbitrary code to be executed in the interpreter. One wants to be
able to read possibly HDF5 and MAT files from untrusted sources, so pickling is
avoided in this package.

The package's documetation is found at http://pythonhosted.org/hdf5storage/

The package's source code is found at
https://github.com/frejanordsiek/hdf5storage}

Name:           python-hdf5storage
Version:        0.1.18
%global tag     %{version}
Release:        %{autorelease}
Summary:        Read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files
%forgemeta

License:        BSD
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-hdf5storage
Summary:        %{summary}
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist nose}
%endif

%description -n python3-hdf5storage %_description

%prep
%forgesetup

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hdf5storage

%check
%if %{with tests}
%{pytest}
%endif
%pyproject_check_import

%files -n python3-hdf5storage -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
