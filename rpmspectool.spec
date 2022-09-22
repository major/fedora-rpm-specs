Name:           rpmspectool
Version:        1.99.7
Release:        9%{?dist}
Summary:        Utility for handling RPM spec files

License:        GPLv3+
URL:            https://github.com/nphilipp/rpmspectool
Source0:        https://files.pythonhosted.org/packages/source/r/rpmspectool/rpmspectool-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-argcomplete
Requires:       python3-pycurl

%description
The rpmspectool utility lets users expand and download sources and patches in
RPM spec files.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files
%license COPYING
%doc README.md
%{_bindir}/rpmspectool
%{python3_sitelib}/rpmspectool
%{python3_sitelib}/rpmspectool*.egg-info
%{_datadir}/bash-completion/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.99.7-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.99.7-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.99.7-2
- Rebuilt for Python 3.9

* Fri Apr 03 2020 Nils Philippsen <nils@tiptoe.de> - 1.99.7-1
- version 1.99.7
- add bash completion

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.99.6-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.99.6-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.99.6-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jul 30 2017 Nils Philippsen <nils@tiptoe.de> - 1.99.6-1
- version 1.99.6
- distinguish --sources/--patches from --source/--patch options (#1325788)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.99.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Fri Apr 08 2016 Nils Philippsen <nils@redhat.com> - 1.99.5-1
- version 1.99.5
- use umask for downloaded files (#1323692, patch by Ville Skyttä)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Nils Philippsen <nils@redhat.com> - 1.99.4-1
- version 1.99.4
- don't trip over open conditional blocks (#1154596)
- catch errors from parsing intermediate spec file
- catch download errors
- implement --force

* Fri Nov 20 2015 Nils Philippsen <nils@redhat.com> - 1.99.3-1
- version 1.99.3
- initial release
