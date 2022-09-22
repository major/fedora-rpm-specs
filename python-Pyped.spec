%global srcname Pyped
%global sum Replace sed/grep/cut/awk by letting you execute Python one-liners

Name:           python-%{srcname}
Version:        1.4
Release:        25%{?dist}
Summary:        %{sum}

License:        GPLv2
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        http://pypi.python.org/packages/source/P/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         Pyped-1.4-encoding.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pyped is a command-line tool that let you process another command
output with a Python one-liner like Perl or AWK.

%package -n python3-%{srcname}
Requires:       python3-minibelt
Requires:       python3-arrow
Requires:       python3-requests
Requires:       python3-path
Requires:       python3-six
Summary:        %{sum}

%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
Pyped is a command-line tool that let you process another command
output with a Python one-liner like Perl or AWK.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf Pyped.egg-info
# Change shebang according to Python version
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' pyped.py

%build
%py3_build

%install
%py3_install
chmod a+x %{buildroot}%{python3_sitelib}/pyped.py
mv %{buildroot}%{_bindir}/pyp %{buildroot}%{_bindir}/pyp-%{python3_version}
ln -s %{_bindir}/pyp-%{python3_version} %{buildroot}%{_bindir}/pyp-3
ln -s %{_bindir}/pyp-%{python3_version} %{buildroot}%{_bindir}/pyp

%check

%files -n python3-%{srcname}
%license licence.txt
%doc README.md
%{python3_sitelib}/pyped*
%{python3_sitelib}/Pyped*
%{python3_sitelib}/__pycache__/pyped.*
%{_bindir}/pyp-%{python3_version}
%{_bindir}/pyp-3
%{_bindir}/pyp

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4-24
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4-21
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-16
- Subpackage python2-Pyped has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 28 2019 René Ribaud <rene.ribaud@free.fr> - 1.4-13
- Fix of python3-Pyped requires both Python 2 and Python 3 (rhbz #1546790)
  Thanks goes to Jan Beran <jberan@redhat.com> who submited the fix.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 9 2015 René Ribaud <rene.ribaud@free.fr> - 1.4-2
- Fix according to Julien's feedbacks (bug 1262644).
* Sun Sep 13 2015 René Ribaud <rene.ribaud@free.fr> - 1.4-1
- Initial rpm
