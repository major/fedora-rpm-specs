# Initially created by pyp2rpm-3.3.2
%global pypi_name webscrapbook

Name:           python-%{pypi_name}
Version:        1.16.0
Release:        4%{?dist}
Summary:        A backend toolkit for management of WebScrapBook collection

License:        MIT
URL:            https://github.com/danny0838/PyWebScrapBook
Source0:        https://github.com/danny0838/PyWebScrapBook/archive/%{version}.tar.gz#/PyWebScrapBook-%{version}.tar.gz

# Downstream Fedora patch to comply with packaging guidelines
Patch100:       python-webscrapbook-1.15-disable-linters.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# For mime.types
BuildRequires:  mailcap


%global _description %{expand:
PyWebScrapBook is a command line toolkit and backend server for the
WebScrapBook browser extension.

Features: Host any directory as a website; HTZ or MAFF archive file viewing;
Markdown file rendering; Directory listing; Create, view, edit, and/or delete
files via the web page or API; HTTP(S) authorization.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3-%{pypi_name}+adhoc_ssl
 
%description -n python3-%{pypi_name} %_description

%pyproject_extras_subpkg -n python3-%{pypi_name} adhoc_ssl


%prep
%autosetup -p1 -n PyWebScrapBook-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files webscrapbook

%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/webscrapbook
%{_bindir}/wsb
%{_bindir}/wsbview

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1.16.0-1
- New upstream release
- Add mailcap as build requirement (for mime.types, needed by tests)

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.15.0-2
- Rebuilt for Python 3.12

* Wed May 31 2023 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1.15.0-1
- New upstream release
- Convert spec file to pyproject_* RPM macros
- Actually use automatic build dependency generator
- Enable tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
