%global         pypi_name       easydict
Version:        1.10
%global         forgeurl        https://github.com/makinacorpus/easydict
%global         tag             %{version}
%forgemeta

Name:           python-%{pypi_name}
Release:        6%{?dist}
Summary:        Access dict values as attributes (works recursively) 

License:        LGPL-3.0-only
URL:            %{forgeurl}
Source0:        %{forgesource} 


BuildRequires:  python3-devel
BuildArch: noarch

%global _description %{expand:
EasyDict allows to access dict values as attributes (works recursively).
A Javascript-like properties dot notation for python dicts.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import
# No tests available

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%doc CHANGES

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.10-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 03 2023 Benson Muite <benson_muite@emailplus.org> - 1.10-1
- Initial packaging
