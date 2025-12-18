Name:           python-google-crc32c
Version:        1.8.0
Release:        %autorelease
Summary:        A python wrapper of the C library ‘Google CRC32C’

License:        Apache-2.0
URL:            https://github.com/googleapis/python-crc32c
Source:         %{url}/archive/v%{version}/python-crc32c-%{version}.tar.gz

# chore: Migrate extras config to pyproject.toml
# https://github.com/googleapis/python-crc32c/pull/325
#
# Partially fixes (the extra part of):
#
# 1.8.0 missing testing extra, ships unnecessary C source
# https://github.com/googleapis/python-crc32c/issues/324
Patch:          %{url}/pull/325.patch

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


%install -a
# 1.8.0 missing testing extra, ships unnecessary C source
# https://github.com/googleapis/python-crc32c/issues/324
rm -v '%{buildroot}%{python3_sitearch}/google_crc32c/_crc32c.c'
sed -r -i 's@.*/_crc32c\.c$@# &@' %{pyproject_files}


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
