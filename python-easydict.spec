%global         pypi_name       easydict
Version:        1.10
%global         forgeurl        https://github.com/makinacorpus/easydict
%global         tag             %{version}
%forgemeta

Name:           python-%{pypi_name}
Release:        1%{?dist}
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
* Mon Jul 03 2023 Benson Muite <benson_muite@emailplus.org> - 1.10-1
- Initial packaging
