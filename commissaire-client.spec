Name:           commissaire-client
Version:        0.0.6
Release:        19%{?dist}
Summary:        CLI for Commissaire
License:        LGPLv2+
URL:            http://github.com/projectatomic/commctl
Source0:        https://github.com/projectatomic/commctl/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# For tests
BuildRequires:  python3-coverage
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-flake8

Requires:       python3-setuptools
Requires:       python3-bcrypt
Requires:       python3-PyYAML

Provides:       commctl

%description
Command line tools for Commissaire.

%prep
%autosetup -n commctl-%{version}


%build
%py3_build

%install
%py3_install

%check
# XXX: Issue with the coverage module.
#%{__python3} setup.py nosetests


%files
%license COPYING
%doc README.md
%doc CONTRIBUTORS
%doc MAINTAINERS
%{_bindir}/commctl
%{python3_sitelib}/*


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.6-18
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.6-15
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.6-12
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.6-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.6-9
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.6-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.0.6-3
- Switch to python-bcrypt, BZ 1473018.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Matthew Barnes <mbarnes@redhat.com> - 0.0.6-1
- New upstream release 0.0.6

* Fri May 26 2017 Matthew Barnes <mbarnes@redhat.com> - 0.0.5-1
- New upstream release 0.0.5

* Wed Apr 26 2017 Matthew Barnes <mbarnes@redhat.com> - 0.0.4-1
- New upstream release 0.0.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-2
- Rebuild for Python 3.6

* Fri Aug 26 2016 Steve Milner <smilner@redhat.com> - 0.0.1
- Updated for 0.0.1.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.4.rc3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Matthew Barnes <mbarnes@redhat.com> - 0.0.1-0.3.rc3
- Switch to python3.
- Move pre-release indicator ('rc3') to Release tag for compliance with
  packaging guidelines.

* Thu Jun 02 2016 Matthew Barnes <mbarnes@redhat.com> - 0.0.1rc3-2
- Add Provides: commctl

* Wed Apr 20 2016 Matthew Barnes <mbarnes@redhat.com> - 0.0.1rc3-1
- Update for RC3.

* Wed Apr 20 2016 Matthew Barnes <mbarnes@redhat.com> - 0.0.1rc2-6
- commissaire-hashpass is now 'commctl create passhash'.

* Mon Apr  4 2016 Steve Milner <smilner@redhat.com> - 0.0.1rc2-5
- commctl and commissaire-hash-pass are now their own package.
