Name:           python-certifi
Version:        2026.01.04
Release:        %autorelease
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPL-2.0
URL:            https://certifi.io/
Source:         https://github.com/certifi/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          certifi-2025.07.09-use-system-cert.patch

BuildArch:      noarch

# Require the system certificate bundle (/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem)
BuildRequires:  ca-certificates

BuildRequires:  python3-devel

# Run upstream tests
BuildRequires:  python3-pytest

%description
Certifi is a carefully curated collection of Root Certificates for validating
the trustworthiness of SSL certificates while verifying the identity of TLS
hosts. It has been extracted from the Requests project.

Please note that this Fedora package does not actually include a certificate
collection at all. It reads the system shared certificate trust collection
instead. For more details on this system, see the ca-certificates package.

%package -n python3-certifi
Summary:        %{summary}
Requires:       ca-certificates

%description -n python3-certifi
Certifi is a carefully curated collection of Root Certificates for validating
the trustworthiness of SSL certificates while verifying the identity of TLS
hosts. It has been extracted from the Requests project.

Please note that this Fedora package does not actually include a certificate
collection at all. It reads the system shared certificate trust collection
instead. For more details on this system, see the ca-certificates package.

This package provides the Python 3 certifi library.


%prep
%autosetup -p1

# Remove bundled Root Certificates collection
rm -rf certifi/*.pem


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l certifi


%check
# sanity check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
test $(%{__python3} -m certifi) == /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
test $(%{__python3} -c 'import certifi; print(certifi.where())') == /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
%{__python3} -c 'import certifi; print(certifi.contents())' > contents
diff --ignore-blank-lines /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem contents
# upstream tests
%pytest -v


%files -n python3-certifi -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
