%global pypi_name pynacl
%bcond_without check

%global modname pynacl

Name:           python-%{modname}
Version:        1.6.2
Release:        %autorelease
Summary:        Python binding to the Networking and Cryptography (NaCl) library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/pyca/pynacl
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  libsodium-devel

%global _description %{expand:
PyNaCl is a Python binding to the Networking and Cryptography library,
a crypto library with the stated goal of improving usability, security
and speed.}

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled libsodium, to be sure
rm -vrf src/libsodium/

# ARM and s390x is too slow for upstream tests
# See https://bugzilla.redhat.com/show_bug.cgi?id=1594901
# And https://github.com/pyca/pynacl/issues/370
%ifarch s390x %{arm}
sed -i 's/@settings(deadline=1500, max_examples=5)/@settings(deadline=4000, max_examples=5)/' tests/test_pwhash.py
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_check:-x tests}

%build
export SODIUM_INSTALL=system
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nacl

%check
%if %{with check}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
