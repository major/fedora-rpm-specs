# tutorial doctests require simplejson, not included in RHEL
%bcond doctests %{undefined rhel}

%global pypi_name jsonpatch

Name:           python-%{pypi_name}
Version:        1.47
Release:        %autorelease
Summary:        Applying JSON Patches in Python

License:        BSD-3-Clause
URL:            https://github.com/stefankoegl/python-json-patch
Source0:        https://pypi.io/packages/source/j/jsonpatch/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Library to apply JSON Patches according to RFC 6902 - Python 2 build.

%package -n python3-%{pypi_name}
Summary:        Applying JSON Patches in Python 3

BuildRequires:  python3-devel
# For tests
%if %{with doctests}
BuildRequires:  python3-simplejson
%endif


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

%pyproject_save_files jsonpatch jsonpatch_cli jsonpatch-stubs

# remove jsondiff binary conflicting with python-jsondiff
# https://bugzilla.redhat.com/show_bug.cgi?id=2029805
rm %{buildroot}%{_bindir}/jsondiff


%check
%if %{without doctests}
# doctests are skipped if file is missing
rm -f doc/tutorial.rst
%endif
%{__python3} tests.py


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jsonpatch


%changelog
%autochangelog
