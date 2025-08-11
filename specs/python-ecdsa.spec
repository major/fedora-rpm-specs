%global srcname ecdsa

Name:           python-%{srcname}
Version:        0.19.1
Release:        %autorelease
Summary:        ECDSA cryptographic signature library

License:        MIT
URL:            https://pypi.python.org/pypi/ecdsa
Source0:        %{pypi_source ecdsa}

BuildArch:      noarch

BuildRequires:  python3-devel
# For tests
BuildRequires:  openssl
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
%if 0%{!?rhel}
# for better performance
BuildRequires:  python3-gmpy2
%endif

%description
This is an easy-to-use implementation of ECDSA cryptography (Elliptic Curve
Digital Signature Algorithm), implemented purely in Python, released under
the MIT license. With this library, you can quickly create keypairs (signing
key and verifying key), sign messages, and verify the signatures. The keys
and signatures are very short, making them easy to handle and incorporate
into other protocols.

%package -n python3-%{srcname}
Summary:        ECDSA cryptographic signature library

%description -n python3-%{srcname}
This is an easy-to-use implementation of ECDSA cryptography (Elliptic Curve
Digital Signature Algorithm), implemented purely in Python, released under
the MIT license. With this library, you can quickly create keypairs (signing
key and verifying key), sign messages, and verify the signatures. The keys
and signatures are very short, making them easy to handle and incorporate
into other protocols.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove extraneous #!
find src/ecdsa -name \*.py | xargs sed -ie '/\/usr\/bin\/env/d'

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc NEWS README.md


%changelog
%autochangelog
