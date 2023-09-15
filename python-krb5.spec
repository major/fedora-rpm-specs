Name:           python-krb5
Version:        0.5.1
Release:        %autorelease
Summary:        Kerberos API bindings for Python
License:        MIT
URL:            https://github.com/jborean93/pykrb5
Source:         %{pypi_source krb5}
# https://github.com/jborean93/pykrb5/pull/32
Patch:          0001-Exclude-header-files-from-package-data.patch

BuildRequires:  gcc
BuildRequires:  krb5-devel

%global _description %{expand:
This library provides Python functions that wraps the Kerberos 5 C API.  Due to
the complex nature of this API it is highly recommended to use something like
python-gssapi which exposes the Kerberos authentication details through GSSAPI.}


%description %_description


%package -n python3-krb5
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-krb5 %_description


%prep
%autosetup -p 1 -n krb5-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files krb5


%check
# The upstream tests require k5test, which isn't packaged yet.  For now, just
# do an import check.
%pyproject_check_import


%files -n python3-krb5 -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
