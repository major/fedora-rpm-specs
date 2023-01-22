Name:           pyutil
Version:        3.1.0
Release:        14%{?dist}
Summary:        A collection of mature utilities for Python programmers

License:        GPLv2+
URL:            https://github.com/tpltnt/pyutil
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

Patch1:         package-data.patch
# https://github.com/tpltnt/pyutil/pull/3
Patch2:         py3.patch

BuildArch:      noarch


%global _description\
These are a few data structures, classes and functions which we've needed \
over many years of Python programming and which seem to be of general use \
to other Python programmers. Many of the modules that have existed in pyutil \
over the years have subsequently been obsoleted by new features added to \
the Python language or its standard library, thus showing that we're not \
alone in wanting tools like these.

%description %_description

%package -n python3-%{name}
Summary:        %summary
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-zbase32
BuildRequires:  python3-twisted
BuildRequires:  net-tools
BuildRequires:  python3-simplejson
BuildRequires:  python3-mock
Requires:       python3-twisted
Requires:       python3-zbase32
Requires:       python3-simplejson

%description -n python3-%{name} %_description

%prep
%setup -q
find . -name "*~" -delete
%patch1 -p1
%patch2 -p1

%build
%py3_build

%install
%py3_install

# rename the utilities to something less generic
mv %{buildroot}%{_bindir}/lines %{buildroot}%{_bindir}/%{name}_lines
mv %{buildroot}%{_bindir}/randcookie %{buildroot}%{_bindir}/%{name}_randcookie
mv %{buildroot}%{_bindir}/randfile %{buildroot}%{_bindir}/%{name}_randfile
mv %{buildroot}%{_bindir}/tailx %{buildroot}%{_bindir}/%{name}_tailx
mv %{buildroot}%{_bindir}/try_decoding %{buildroot}%{_bindir}/%{name}_try_decoding
mv %{buildroot}%{_bindir}/unsort %{buildroot}%{_bindir}/%{name}_unsort
mv %{buildroot}%{_bindir}/verinfo %{buildroot}%{_bindir}/%{name}_verinfo
mv %{buildroot}%{_bindir}/passphrase %{buildroot}%{_bindir}/%{name}_passphrase

rm -rf %{buildroot}%{_docdir}/%{name}

# remove shebang
find %{buildroot}%{python3_sitelib}/%{name} \
        -type f -name \*.py -o -name test_template | \
	xargs sed -i '/^#!\/usr\/bin\/env/d'
 
%check
%{__python3} setup.py test

%files -n python3-%{name}
%doc README.rst COPYING.GPL COPYING.SPL.txt COPYING.TGPPL.rst CREDITS
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-*.egg-info
%{_bindir}/%{name}_lines
%{_bindir}/%{name}_randcookie
%{_bindir}/%{name}_randfile
%{_bindir}/%{name}_tailx
%{_bindir}/%{name}_try_decoding
%{_bindir}/%{name}_unsort
%{_bindir}/%{name}_verinfo
%{_bindir}/%{name}_passphrase

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Remove Python 2 subpackage

* Sun Aug 26 2018 Dan Callaghan <dcallagh@redhat.com> - 3.1.0-1
- New upstream release 3.1.0
- Added Python 3 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.7-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.9.7-2
- Don't ship editor backup files

* Fri Jan 17 2014 Anish Patil <apatil@apatil@redhat.com> 1.9.7-1
- Added passphrase utility 

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 01 2012 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.9.1-1
- Upstream released new version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.8.4-1
- Upstream released new version
- Drop patches which are merged upstream

* Fri Feb 11 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.8.1-2
- Rebuild

* Wed Feb 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.8.1-1
- Upstream released new version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.7.9-3
- Fix broken tests

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.7.9-1
- Upstream released new version

* Sat Feb 13 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.6.1-4
- Review fixes (#560457)

* Sat Feb 13 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.6.1-3
- Rename utilities to something less generic
- BR Twisted for testsuite

* Fri Feb 12 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.6.1-2
- Remove dependency on darcs

* Sun Jan 31 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.6.1-1
- Initial import

