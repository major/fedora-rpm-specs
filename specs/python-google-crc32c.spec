Name:           python-google-crc32c
Version:        1.7.1
Release:        %autorelease
Summary:        A python wrapper of the C library ‘Google CRC32C’

License:        Apache-2.0
URL:            https://github.com/googleapis/python-crc32c
Source:         %{url}/archive/v%{version}/python-crc32c-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x testing
BuildOption(install):   -l google_crc32c

BuildRequires:  gcc-c++
BuildRequires:  google-crc32c-devel >= 1.1.2

%global _description %{expand:
This package wraps the google/crc32c hardware-based implementation of the
CRC32C hashing algorithm.}

%description %{_description}


%package -n python3-google-crc32c
Summary:        %{summary}

%description -n python3-google-crc32c %{_description}


%prep -a
# This is a git submodule, so the bundled library isn’t included in the GitHub
# source archive, but it doesn’t hurt to be very certain.
rm -rv google_crc32c/


%check -a
# See BUILDING.md.
pushd scripts >/dev/null
# Check the package, try and load the native library
%{py3_test_envvars} %{python3} -m check_crc32c_extension
popd >/dev/null

%pytest


%files -n python3-google-crc32c -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%doc SECURITY.md


%changelog
%autochangelog
