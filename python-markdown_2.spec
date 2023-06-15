%global pypi_name Markdown
%global modname markdown

Name:           python-%{modname}_2
Version:        2.6.11
Release:        11%{?dist}
Summary:        Python implementation of Markdown

License:        BSD
URL:            https://github.com/Python-Markdown/markdown
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{modname}_2
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Conflicts:      python%{python3_version}dist(%{modname})

%description -n python3-%{modname}_2 %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -vr *.egg-info
sed -i -e '/markdown.__main__/d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}_2
%license LICENSE.md
%doc README.md
%{python3_sitelib}/markdown/
%{python3_sitelib}/Markdown-*.egg-info/

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.6.11-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.6.11-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.11-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.11-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.6.11-1
- Initial package
