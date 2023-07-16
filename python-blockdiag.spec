%global srcname blockdiag
%global srcdesc \
blockdiag and its family generate diagram images from simply text file.\
\
Features:\
- Generates beautiful diagram images from simple text format (similar to\
  graphviz’s DOT format)\
- Layouts diagram elements automatically\
- Embeds to many documentations; Sphinx, Trac, Redmine and some wikis\
\
- Supports many types of diagrams\
  - block diagram (with this package)\
  - sequence diagram (with the seqdiag package)\
  - activity diagram (with the actdiag package)\
  - logical network diagram (with the nwdiag package)\
\
Enjoy documentation with blockdiag !

Name:           python-%{srcname}
Version:        3.0.0
Release:        7%{?dist}
Summary:        Generate block-diagram images from text

License:        ASL 2.0
URL:            https://blockdiag.com/
Source:         %pypi_source
Patch0:         https://patch-diff.githubusercontent.com/raw/blockdiag/blockdiag/pull/159.patch

BuildArch:      noarch
# upstream uses ipagp.ttf as its default font
BuildRequires:  ipa-pgothic-fonts
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist flake8}
BuildRequires:  %{py3_dist funcparserlib}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist reportlab}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist tox-current-env}
BuildRequires:  %{py3_dist webcolors}


%description %{srcdesc}


%package -n %{srcname}
Summary:        %{summary}
Requires:       python3-%{srcname} = %{version}-%{release}


%description -n %{srcname} %{srcdesc}


%package -n python3-%{srcname}
Summary:        Python 3 module for %{srcname}
Requires:       ipa-pgothic-fonts
Provides:       python3-%{srcname}-devel = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# collateral from patch0:
touch src/blockdiag/tests/diagrams/invalid.txt


%build
%py3_build


%install
%py3_install
install -pm 644 -D %{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1


%check
ALL_TESTS=1 %tox


%files -n %{srcname}
%license LICENSE
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1*


%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}*


%changelog
* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 3.0.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Dridi Boukelmoune <dridi@fedoraproject.com> - 3.0.0-2
- Patch the test suite to skip networked tests

* Tue Dec 07 2021 Dridi Boukelmoune <dridi@fedoraproject.com> - 3.0.0-1
- Bump version to 3.0.0
- Run the test suite with tox

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Dridi Boukelmoune <dridi@fedoraproject.com> - 2.0.1-1
- Fold the devel subpackage in the python3 subpackage
- Bump version to 2.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Dridi Boukelmoune <dridi@fedoraproject.com> - 2.0.0-1
- Bump version to 2.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.4-7
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.5.4-6
- Drop pep8 dependency

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.5.4-4
- Fix obsolete/provides for python 2

* Sat Apr 20 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.5.4-3
- Fix devel requires

* Sat Apr 20 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.5.4-2
- Move the blockdiag command to its own package

* Tue Feb 05 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.5.4-1
- Bump to 1.5.4
- Drop downstream patches (upstreamed)
- Catch up with packaging guidelines
- In general, use recommended RPM macros
- Drop the Python 2 package
- Inline package description

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Dridi Boukelmoune <dridi@fedoraproject.org> 1.5.3-14
- Amended patch for Python 3.7

* Tue Jul 03 2018 Dridi Boukelmoune <dridi@fedoraproject.org> 1.5.3-13
- Patched for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.3-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Aug 29 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 1.5.3-9
- Rename also -devel package

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.3-8
- Python 2 binary package renamed to python2-blockdiag
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 20 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.5.3-1
- Upstream 1.5.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 03 2014 Dridi Boukelmoune <dridi@fedoraproject.org> 1.3.2-4
- Switched to the source tarball from bitbucket
- Added missing dependencies

* Sun Feb 16 2014 Dridi Boukelmoune <dridi@fedoraproject.org> 1.3.2-3
- Added devel packages needed by other *diag packages

* Tue Dec 31 2013 Dridi Boukelmoune <dridi@fedoraproject.org> 1.3.2-2
- Fixed python => python2 where relevant
- New slightly different summary

* Sat Dec 28 2013 Dridi Boukelmoune <dridi@fedoraproject.org> 1.3.2-1
- Initial spec
