%global pypi_name opensearch-py

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Python low-level client for OpenSearch

License:        Apache-2.0
URL:            https://github.com/opensearch-project/%{pypi_name}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
opensearch-py is a community-driven, open source OpenSearch client
licensed under the Apache v2.0 License. 
For more information, see opensearch.org.}

%description %_description

%pyproject_extras_subpkg -n python3-opensearch-py async kerberos

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x async -x kerberos


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files opensearchpy


%check
%pyproject_check_import -e opensearchpy.helpers.test


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
* Fri May 12 2023 Steve Traylen <steve.traylen@cern.ch> - 2.2.0-1
- Update to 2.2.0
- Enable python extra packages
- Update license to SPDX string.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 30 2022 Steve Traylen <steve.traylen@cern.ch> - 2.0.0-1
- Upgrade to version 2.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.11

* Wed Feb 9 2022 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-3
- Migrate to pyproject macros

* Thu Dec 9 2021 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-2
- Review corrections rhbz#2016597

* Fri Oct 22 2021 Steve Traylen <steve.traylen@cern.ch> - 1.0.0-1
- Initial package.
