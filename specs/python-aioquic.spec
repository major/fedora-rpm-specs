%if 0%{?fedora} || 0%{?rhel}
%bcond_without pyproject
%else
%bcond_with pyproject
%global __python3 /usr/bin/python3.11
%global python3_version 3.11
%endif

%global pypi_name aioquic

# as_needed flag breaks links to Python  
%undefine _ld_as_needed

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        %autorelease
Summary:        %{pypi_name} is a library for the QUIC network protocol in Python
License:        BSD-3-Clause
URL:            https://github.com/aiortc/%{pypi_name}
Source0:        %{pypi_source}
# https://cryptography.io/en/latest/objects.inv
Source1:        cryptography.inv
# https://docs.python.org/3/objects.inv
Source2:        python.inv
# Use local copies of documentation links
Patch:          doc-links.patch

%description
It features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.

QUIC was standardised in RFC 9000 and HTTP/3 in RFC 9114.
%{pypi_name} is regularly tested for interoperability against other
QUIC implementations.

It provides Python Decoder and Encoder objects
to read or write HTTP/3 headers compressed with QPACK.


%package -n python3-%{pypi_name}
Summary: %{pypi_name} is a library for the QUIC network protocol in Python
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
%if %{with pyproject}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinxcontrib-trio
%else
BuildRequires:  python%{python3_version}-certifi
BuildRequires:  python%{python3_version}-cryptography
BuildRequires:  python%{python3_version}-devel
BuildRequires:  python%{python3_version}-setuptools
BuildRequires:  python%{python3_version}-wheel
BuildRequires:  python%{python3_version}-pylsqpack
BuildRequires:  python%{python3_version}-pytest
BuildRequires:  python%{python3_version}-service-identity
Recommends:     python%{python3_version}-uvloop
%py_provides    python%{python3_version}-%{pypi_name}
%endif


%description -n python3-%{pypi_name}
It features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.

QUIC was standardised in RFC 9000 and HTTP/3 in RFC 9114.
%{pypi_name} is regularly tested for interoperability against other
QUIC implementations.

It provides Python Decoder and Encoder objects
to read or write HTTP/3 headers compressed with QPACK.


%prep
%autosetup -n %{pypi_name}-%{version} -p1

cp %{SOURCE1} docs/
cp %{SOURCE2} docs/

rm -rf %{pypi_name}.egg-info
%if %{with pyproject}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
# Be sure Python lib is linked
export LDFLAGS="%{__global_ldflags} %(pkg-config --libs python3-embed)"
%if %{with pyproject}
%pyproject_wheel
%else
%py3_build
%endif

%check
%pyproject_check_import
# SHA1 not supported, so disable test
%pytest -k "not test_handshake_with_rsa_pkcs1_sha1_signature"


%install
%if %{with pyproject}
%pyproject_install
%pyproject_save_files %{pypi_name} -l
mkdir -p %{buildroot}%{_mandir}/man1
# Build and install documentation
# Package needs to be installed
pushd docs
%{py3_test_envvars} make man
install -m 644 _build/man/aioquic.1 %{buildroot}%{_mandir}/man1
popd
%else
%py3_install
# Documentation dependencies not available
%endif


%if %{with pyproject}
%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_mandir}/man1/aioquic.1*
%else
%files -n python3-%{pypi_name}
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}*.egg-info/
%license LICENSE
%endif
%doc README.rst


%changelog
%autochangelog
