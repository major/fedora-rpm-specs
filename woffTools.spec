%global commit0 67030d47ccb97993eb683e23bbce0f79d9577cf5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           woffTools
Version:        0.1
Release:        0.36.20160211git%{?dist}
Summary:        Tool for manipulating and examining WOFF files

License:        MIT
URL:            https://github.com/typesupply/woffTools
Source0:        https://github.com/typesupply/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-fonttools
Requires:       python3-fonttools
Requires:       python3-woffTools

%description
woffTools is a collection of command line tools for verifying and
examining WOFF files. This is also a Python package that can be used
to manipulate and examine WOFF files just as you can examine SFNT files
with FontTools.

%package -n python3-%{name}
Summary:        Tool for manipulating and examining WOFF files
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
An python module which provides a convenient example.

%prep
%setup -q -n %{name}-%{commit0}

# Remove shebang
sed -i -e '/^#! \//, 1d' Lib/woffTools/tools/validate.py

2to3 -w .

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/woff*

%files -n python3-%{name}
%doc README.txt
%license License.txt
%{python3_sitelib}/*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.36.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.1-0.35.20160211git
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.34.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.33.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1-0.32.20160211git
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.31.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.30.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.29.20160211git
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.28.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.27.20160211git
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.26.20160211git
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.25.20160211git
- Drop python2-woffTools (#1634872)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.21.20160211git
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.1-0.20.20160211git
- rebuilt to fix FTBFS on rawhide

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.20160211git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.16.20160211git
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.15.20160211git
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 11 2016 Parag Nemade <pnemade AT redhat DOT com>- 0.1-0.14.20160211git
- Update to latest snapshot 20160211

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.13.20151005git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.12.20151005git
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 05 2015 Parag Nemade <pnemade@redhat.com>- 0.1-0.11.20151005git
- Update to new upstream github URL
- Follow git hosting source guidelines
- remove optional group tag, buildroot, defattr, %%clean
- removal of buildroot from %%install
- follow newer python packaging guidelines

* Fri Sep 11 2015 Sandeep Shedmake <sshedmak@redhat.com> - 0.1-0.10.684svn
- Patch0 added, Release bumped

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.684svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.8.684svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.684svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.6.684svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.684svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.684svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.3.684svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-0.2.684svn
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Nov 27 2009 Parag Nemade <pnemade@redhat.com>- 0.1-0.1.684svn
- Initial specfile for Fedora


