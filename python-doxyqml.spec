%global srcname doxyqml
%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        0.5.1
Release:        3%{?dist}
License:        BSD
Summary:        Doxygen to document your QML classes
Url:            https://invent.kde.org/sdk/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Doxyqml lets you use Doxygen to document your QML classes,
It integrates as a Doxygen input filter to turn .qml files into pseudo-C++
which Doxygen can then use to generate documentation.}

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
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.5.1-1
- Initial version of package
