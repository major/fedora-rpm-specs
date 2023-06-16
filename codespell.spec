Name:           codespell
Version:        2.2.5
Release:        1%{?dist}
Summary:        Fix common misspellings in text files

License:        GPLv2 and CC-BY-SA
URL:            https://github.com/codespell-project/codespell/
Source0:        https://pypi.io/packages/source/c/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-setuptools_scm
BuildRequires:  python3-pytest

%description
codespell fixes common misspellings in text files. It's designed primarily for
checking misspelled words in source code, but it can be used with other files
as well.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install

%files
%doc README.rst
%{_bindir}/codespell
%{python3_sitelib}/codespell_lib
%{python3_sitelib}/%{name}-%{version}.dist-info

%changelog
* Wed Jun 14 2023 Bastien Nocera <bnocera@redhat.com> - 2.2.5-1
- Update to 2.2.5

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.4-2
- Rebuilt for Python 3.12

* Wed Mar 08 2023 Bastien Nocera <bnocera@redhat.com> - 2.2.4-1
- Update to 2.2.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.2-2
- Re-add egg-info

* Mon Oct 17 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Thu Aug 18 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.1-1
+ codespell-2.2.1-1
- Update to 2.2.1

* Thu Aug 18 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.0-1
+ codespell-2.2.0-1
- Update to 2.2.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Bastien Nocera <bnocera@redhat.com> - 2.1.0-3
+ codespell-2.1.0-3
- Fix CC-BY-SA shortname (#2036037)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Bastien Nocera <bnocera@redhat.com> - 2.1.0-1
+ codespell-2.1.0-1
- Update to 2.1.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Bastien Nocera <bnocera@redhat.com> - 2.0.0-1
+ codespell-2.0.0-1
- Update to 2.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-5
+ codespell-1.17.1-5
- Replace Python version globs with macros to support 3.10

* Fri Jun 19 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-4
+ codespell-1.17.1-4
- Bump version to match f32 branch

* Fri Jun 19 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-3
+ codespell-1.17.1-3
- Fix usage dictionary not being distributed

* Mon Jun 15 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-2
+ codespell-1.17.1-2
- Add usage dictionary

* Wed Jun 10 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-1
+ codespell-1.17.1-1
- Update to 1.17.1
- Fix Python 3.8 warning (#1840693)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.16.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Wolfgang Stöggl <c72578@yahoo.de> - 1.16.0-1
- New upstream version 1.16.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Bastien Nocera <bnocera@redhat.com> - 1.15.0-2
+ codespell-1.15.0-2
- Fix some review comments

* Tue Jun 18 2019 hadess <bnocera@redhat.com> - 1.15.0-1
- Initial package.
