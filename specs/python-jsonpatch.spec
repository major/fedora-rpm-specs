%global pypi_name jsonpatch

Name:           python-%{pypi_name}
Version:        1.33
Release:        %autorelease
Summary:        Applying JSON Patches in Python

License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-patch
Source0:        https://pypi.io/packages/source/j/jsonpatch/%{pypi_name}-%{version}.tar.gz
# tarball from pypi does not include file tests.js required for a specific test.
# upstream issue https://github.com/stefankoegl/python-json-patch/issues/82
Patch0:         0001-Skip-unit-test-in-packaging.patch
# Avoid usage of unittest.makeSuite, removed from Python 3.13
Patch1:         https://github.com/stefankoegl/python-json-patch/pull/159.patch

BuildArch:      noarch

%description
Library to apply JSON Patches according to RFC 6902 - Python 2 build.

%package -n python3-%{pypi_name}
Summary:        Applying JSON Patches in Python 3

BuildRequires:  python3-devel


%description -n python3-%{pypi_name}
Library to apply JSON Patches according to RFC 6902 - Python 3 build.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%pyproject_wheel


%generate_buildrequires
%pyproject_buildrequires


%install
%pyproject_install

%pyproject_save_files jsonpatch

# remove jsondiff binary conflicting with python-jsondiff
# https://bugzilla.redhat.com/show_bug.cgi?id=2029805
rm %{buildroot}%{_bindir}/jsondiff


%check
%{__python3} tests.py


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jsonpatch


%changelog
%autochangelog
