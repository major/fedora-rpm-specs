Name:           python-jwcrypto
Version:        1.5.8
Release:        %autorelease
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography

License:        LGPL-3.0-or-later
URL:            https://github.com/latchset/jwcrypto
Source0:        https://github.com/latchset/jwcrypto/releases/download/v%{version}/jwcrypto-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-pytest
BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires


%description
Implements JWK, JWS, JWE specifications using python-cryptography


%package -n python3-jwcrypto
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography
Requires:       python3-cryptography >= 2.3
%{?python_provide:%python_provide python3-jwcrypto}

%description -n python3-jwcrypto
Implements JWK, JWS, JWE specifications using python-cryptography


%prep
%setup -q -n jwcrypto-%{version}


%build
%pyproject_wheel


%check
%{__python3} -bb -m pytest jwcrypto/test*.py


%install
%pyproject_install

rm -rf %{buildroot}%{_docdir}/jwcrypto
rm -rf %{buildroot}%{python3_sitelib}/jwcrypto/tests{,-cookbook}.py*
rm -rf %{buildroot}%{python3_sitelib}/jwcrypto/__pycache__/tests{,-cookbook}.*.py*


%files -n python3-jwcrypto
%doc README.md
%license LICENSE
%{python3_sitelib}/jwcrypto
%{python3_sitelib}/jwcrypto-%{version}.dist-info


%changelog
%autochangelog
