%global srcname ytmusicapi
%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        0.22.0
Release:        1%{?dist}
License:        MIT
Summary:        Unofficial API for YouTube Music
Url:            https://github.com/sigma67/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
ytmusicapi is a Python 3 library to send requests to the YouTube Music API. 
It emulates YouTube Music web client requests using the userâ€™s 
cookie data for authentication.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build

%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Thu Aug 25 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.22.0-1
- v0.22.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.20.0-2
- Rebuilt for Python 3.11

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.20.0-1
- Initial version of package