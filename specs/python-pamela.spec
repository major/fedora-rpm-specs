%global srcname pamela

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Python PAM interface

License:        MIT
URL:            https://github.com/jupyterhub/%{srcname}
Source0:        https://github.com/jupyterhub/%{srcname}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
Yet another Python wrapper for PAM.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
Yet another Python wrapper for PAM.


%prep
%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%pytest -k "not test_environment"


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
