%global srcname doxypypy
%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        0.8.8.6
Release:        1%{?dist}
License:        GPLv2
Summary:        A more Pythonic version of doxypy, a Doxygen filter for Python
Url:            https://github.com/Feneric/%{srcname}
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
A more Pythonic version of doxypy, a Doxygen filter for Python.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     python3-%{srcname}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}


# Remove shebangs
find . -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' '{}' \;
find . -name \*.py -exec sed -i '/#!\/usr\/bin\/python/d' '{}' \;

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%attr(644, -, -) %{python3_sitelib}/%{srcname}/*.py
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}

%changelog
* Mon Dec 19 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.8.8.6-1
- Initial version of package
