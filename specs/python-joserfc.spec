%bcond_without tests

Name:           python-joserfc
Version:        1.7.5
Release:        %autorelease
Summary:        The ultimate Python library for JOSE RFCs, including JWS, JWE, JWK, JWA, JWT

License:        BSD-3-Clause
URL:            https://github.com/authlib/joserfc
Source:         %{pypi_source joserfc}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
An RFC-compliant Python library for JSON Object Signing and Encryption (JOSE),
providing support for JSON Web Signature (JWS), JSON Web Encryption (JWE), 
JSON Web Key (JWK), and JSON Web Token (JWT).}

%description %_description

%package -n     python3-joserfc
Summary:        %{summary}

%description -n python3-joserfc %_description


%prep
%autosetup -p1 -n joserfc-%{version}


%generate_buildrequires
%pyproject_buildrequires
%if %{with tests}
echo "python3dist(pytest)"
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l joserfc


%check
%pyproject_check_import -e "joserfc.drafts*"
%if %{with tests}
%pytest --ignore-glob="*chacha20*"
%endif


%files -n python3-joserfc -f %{pyproject_files}


%changelog
%autochangelog
