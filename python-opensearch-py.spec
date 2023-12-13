%global pypi_name opensearch-py

Name:           python-%{pypi_name}
Version:        2.4.2
Release:        %autorelease
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
%autochangelog
