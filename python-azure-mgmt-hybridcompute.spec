%global         srcname     azure-mgmt-hybridcompute

Name:           python-%{srcname}
Version:        7.0.0
Release:        7%{?dist}
Summary:        Microsoft Azure Hybrid Compute Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch


BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%global _description %{expand:
Microsoft Azure Hybrid Compute Management Client Library for Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 7.0.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 7.0.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Major Hayden <major@mhtx.net> - 7.0.0-2
- Move obsoletes into subpackage

* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - 7.0.0-1
- First package.
