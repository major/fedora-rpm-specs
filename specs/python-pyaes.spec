%global pypi_name pyaes
%global common_description %{expand:
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).}

%bcond_without check

Name:       python-%{pypi_name}
Version:    1.6.1
Release:    %autorelease
Summary:    Pure-Python implementation of AES block-cipher and common modes of operation
License:    MIT
URL:        https://github.com/ricmoo/%{pypi_name}
VCS:        git:%{url}.git
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:     python-pyaes-0001-Use-relative-imports-during-tests.patch
Patch2:     51.patch

BuildArch:  noarch
BuildRequires: python3-devel

%if %{with check}
# https://bugzilla.redhat.com/show_bug.cgi?id=2339093
BuildRequires: python3dist(pycryptodomex)
Patch3:     python-pyaes-0002-replace-pycrypto-with-cryptodome.patch
%endif

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:  %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%if %{with check}
%{__python3} tests/test-aes.py
%{__python3} tests/test-blockfeeder.py
%{__python3} tests/test-util.py
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
