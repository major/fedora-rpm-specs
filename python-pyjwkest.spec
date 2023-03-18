Name:           python-pyjwkest
Version:        1.4.2
Release:        1%{?dist}
Summary:        Python implementation of JWT, JWE, JWS and JWK

# pyjwkest: Apache-2.0
# src/jwkest/aes_gcm.py: MIT
# src/jwkest/PBKDF2.py: MIT
License:        Apache-2.0 AND MIT
URL:            https://github.com/IdentityPython/pyjwkest
Source:         %{pypi_source pyjwkest}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand: 
Python implementation of JWT, JWE, JWS and JWK, which is used by pyoidc.}

%description %_description

%package -n     python3-pyjwkest
Summary:        %{summary}

%description -n python3-pyjwkest %_description


%prep
%autosetup -p1 -n pyjwkest-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'jwkest' +auto


%check
%pyproject_check_import -t


%files -n python3-pyjwkest -f %{pyproject_files}


%changelog
* Sun Jan 15 2023 lcrpkking <pkwarcraft@gmail.com> - 1.4.2-1
- Initial package
