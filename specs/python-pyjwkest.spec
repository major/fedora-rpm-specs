Name:           python-pyjwkest
Version:        1.4.2
Release:        11%{?dist}
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
# The project does not need future anymore
# https://github.com/IdentityPython/pyjwkest/issues/102
sed -i 's/, "future"//' setup.py


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
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.4.2-11
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.4.2-10
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.4.2-8
- Rebuilt for Python 3.14

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Python Maint <python-maint@redhat.com> - 1.4.2-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.12

* Sun Jan 15 2023 lcrpkking <pkwarcraft@gmail.com> - 1.4.2-1
- Initial package
