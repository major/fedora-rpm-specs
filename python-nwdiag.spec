%global srcname nwdiag
%global srcdesc \
nwdiag and its family generate diagram images from simply text file.\
\
Features:\
- Generates beautiful diagram images from simple text format (similar to\
  graphviz’s DOT format)\
- Layouts diagram elements automatically\
- Embeds to many documentations; Sphinx, Trac, Redmine and some wikis\
\
- Supports many types of diagrams\
  - logical network diagram (with this package)\
  - block diagram (with the blockdiag package)\
  - sequence diagram (with the seqdiag package)\
  - activity diagram (with the actdiag package)\
\
Enjoy documentation with nwdiag !

Name:           python-%{srcname}
Version:        3.0.0
Release:        4%{?dist}
Summary:        Generate network-diagram images from text

License:        ASL 2.0
URL:            http://blockdiag.com/
Source:         %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist blockdiag}
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist flake8}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist reportlab}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist tox-current-env}


%description %{srcdesc}


%package -n %{srcname}
Summary:        %{summary}
Requires:       python3-%{srcname} = %{version}-%{release}


%description -n %{srcname} %{srcdesc}


%package -n python3-%{srcname}
Summary:        Python 3 module for %{srcname}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install
install -m 0644 -D %{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1
install -m 0644 -D packetdiag.1 %{buildroot}%{_mandir}/man1/packetdiag.1
install -m 0644 -D rackdiag.1   %{buildroot}%{_mandir}/man1/rackdiag.1


%check
ALL_TESTS=1 %tox


%files -n %{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/*
%{_mandir}/man1/*.1*


%files -n python3-%{srcname}
%license LICENSE
%doc PKG-INFO README.rst
%{python3_sitelib}/*diag*
%exclude %{python3_sitelib}/*/tests


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Dridi Boukelmoune <dridi@fedoraproject.com> - 3.0.0-1
- Bump version to 3.0.0
- Match blockdiag's summary
- Bring the test suite back
- Run the test suite with tox

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.0-1
- Bunp version to 2.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-17
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.4-16
- Drop pep8 dependency

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.4-14
- Move the nwdiag command to its own package
- Temporarilly disable the test suite

* Tue Feb 05 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.4-13
- Catch up with packaging guidelines
- In general, use recommended RPM macros
- Drop the Python 2 package
- Inline package description

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-10
- Explicit reference to /usr/bin/python2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.4-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.4-6
- Python 2 binary package renamed to python2-nwdiag
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.4-1
- Bumped to 1.0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Mar 04 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.0-2
- Fixed changelog format.
- Fixed man page permissions.
- Added missing man pages.
- Avoid co-ownership of %%{python3_sitelib}/__pycache__/.

* Sun Mar 02 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.0-1
- Initial version.
