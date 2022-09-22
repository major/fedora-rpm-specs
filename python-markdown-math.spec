%global pypi_name python-markdown-math
%global srcname markdown-math

Name:           python-%{srcname}
Version:        0.8
Release:        7%{?dist}
Summary:        Math extension for Python-Markdown

License:        BSD
URL:            https://github.com/mitya57/python-markdown-math
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(markdown)

%description
Extension for Python-Markdown: this extension adds math
formulas support to Python-Markdown.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Extension for Python-Markdown: this extension adds math
formulas support to Python-Markdown.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} test.py


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/mdx_math.py
%{python3_sitelib}/python_markdown_math-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 José Matos <jamatos@fedoraproject.org> - 0.8-1
- update to 0.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 José Matos <jamatos@fedoraproject.org> - 0.7-1
- update to 0.7
- remove requires python3dist(setuptools) since it used just during installation

* Sun May 03 2020 José Matos <jamatos@fedoraproject.org> - 0.6-1
- Initial package.
