# Initially created by pyp2rpm-3.3.2
%global pypi_name webscrapbook

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        4%{?dist}
Summary:        A backend toolkit for management of WebScrapBook collection

License:        MIT
URL:            https://github.com/danny0838/PyWebScrapBook
Source0:        https://github.com/danny0838/PyWebScrapBook/archive/%{version}.tar.gz#/PyWebScrapBook-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(setuptools)

%global _description\
PyWebScrapBook is a command line toolkit and backend server for the\
WebScrapBook browser extension.\
\
Features: Host any directory as a website; HTZ or MAFF archive file viewing;\
Markdown file rendering; Directory listing; Create, view, edit, and/or delete\
files via the web page or API; HTTP(S) authorization.

%description %_description

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Recommends:     python%{python3_pkgversion}dist(%{pypi_name}[adhoc_ssl])
 
%description -n python%{python3_pkgversion}-%{pypi_name} %_description

%{?python_extras_subpkg:%python_extras_subpkg -n python%{python3_pkgversion}-%{pypi_name} -i %{python3_sitelib}/*.egg-info adhoc_ssl}

%prep
%autosetup -n PyWebScrapBook-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{_bindir}/webscrapbook
%{_bindir}/wsb
%{_bindir}/wsbview
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1.1.0-1
- New upstream release
- NOTE: As of release 1.0.0 support for legacy ScrapBook data is removed.
  ScrapBook-format data can be converted using the 'wsb convert sb2wsb'
  and 'wsb convert migrate' commands.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.33.4-2
- Rebuilt for Python 3.10

* Tue Feb 23 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.33.4-1
- New upstream release
- Main package Recommends adhoc_ssl extra

* Tue Feb 23 2021 Miro Hrončok <mhroncok@redhat.com> - 0.33.3-2
- Add python3-webscrapbook+adhoc_ssl extras metapackage

* Mon Feb 15 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.33.3-1
- New upstream release
- Drop sed command to remove shebangs (fixed upstream)
- Use auto-discovery for package dependencies

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.15.4-1
- New upstream release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.6.2-1
- Initial Fedora package.
