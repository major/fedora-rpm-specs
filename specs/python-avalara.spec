%global srcname AvaTax-REST-V2-Python-SDK
%global pkgname avalara

Name:           python-avalara
Version:        24.12.0
Release:        1%{?dist}
Summary:        AvaTax Python SDK


License:        Apache-2.0
URL:            https://github.com/avadev/%{srcname}
Source0:        https://github.com/avadev/%{srcname}/archive/refs/tags/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel



%global _description %{expand:
Sales Tax API SDK for Python and AvaTax REST.}

%description %_description

%package -n python3-%{pkgname}
Summary: %{summary}

%description -n python3-%{pkgname} %_description



%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pkgname}


%check
%pyproject_check_import
# Not running tests here as they require you to have an account and an internet connection.

%files -n python3-%{pkgname}
%{python3_sitelib}/Avalara-%{version}.dist-info
%{python3_sitelib}/avalara
%doc README.md
%license LICENSE.txt


%changelog
%autochangelog
