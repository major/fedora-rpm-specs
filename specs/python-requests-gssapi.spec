%global sname requests-gssapi
%global s_name requests_gssapi

Name:           python-%{sname}
Version:        1.4.0
Release:        %autorelease
Summary:        A GSSAPI/SPNEGO authentication handler for python-requests

License:        ISC
URL:            https://github.com/pythongssapi/%{sname}
Source0:        https://github.com/pythongssapi/%{sname}/archive/v%{version}/%{sname}-%{version}.tar.gz
BuildArch:      noarch

# Patches

BuildRequires:  git-core
BuildRequires:  python3dist(pytest)

%generate_buildrequires
%pyproject_buildrequires

%global _description %{expand:
Requests is an HTTP library, written in Python, for human beings. This
library adds optional GSSAPI authentication support and supports
mutual authentication. It includes a fully backward-compatible shim
for requests-kerberos.
}

%description %{_description}

%package -n python3-%{sname}
Summary:        %{summary}
Requires:       python3-gssapi
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{sname}}
%description -n python3-%{sname} %_description

%prep
%autosetup -S git_am -n %{sname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{s_name}

%check
%pyproject_check_import
%pytest

%files -n python%{python3_pkgversion}-%{sname} -f %{pyproject_files}
%doc README.rst AUTHORS HISTORY.rst
%license LICENSE

%changelog
%autochangelog
