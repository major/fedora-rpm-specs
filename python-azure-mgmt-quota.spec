%global         srcname azure-mgmt-quota
%global         upstream_version 1.0.0b2

Name:           python-%{srcname}
Version:        1.0.0~b2
Release:        2%{?dist}
Summary:        Microsoft Azure Quota Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{upstream_version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Quota Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{upstream_version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Fri Oct 28 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0~b2-2
- Fix release by adding disttag

* Wed Oct 26 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0~b2-1
- Initial package
