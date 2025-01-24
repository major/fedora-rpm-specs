%global         srcname     pyopenssl

Name:           pyOpenSSL
Version:        25.0.0
Release:        %autorelease
Summary:        Python wrapper module around the OpenSSL library
License:        Apache-2.0
URL:            https://pyopenssl.readthedocs.org/
Source0:        %{pypi_source %{srcname} %{version}}

Patch:          0001-Limit-list-of-elliptic-curves-tested-to-those-in-Fed.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  python3-devel

%global _description %{expand:
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes}

%description %{_description}


%package -n python3-pyOpenSSL
Summary: Python 3 wrapper module around the OpenSSL library
Obsoletes: pyOpenSSL < 19.0.0-5
Provides: pyOpenSSL = %{version}-%{release}

%description -n python3-pyOpenSSL %{_description}

%package doc
Summary: Documentation for pyOpenSSL
BuildArch: noarch

%description doc
Documentation for pyOpenSSL

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x docs,test

%build
%pyproject_wheel

%{__make} -C doc html SPHINXBUILD=sphinx-build-3

%install
%pyproject_install
%pyproject_save_files OpenSSL

# Cleanup sphinx .buildinfo file before packaging
rm doc/_build/html/.buildinfo

%check
%pyproject_check_import
%pytest -k "not test_sign_verify_with_text" -k "not test_sign_verify"

%files -n python3-pyOpenSSL -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files doc
%license LICENSE
%doc CHANGELOG.rst doc/_build/html

%changelog
%autochangelog
