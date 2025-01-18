Name:           R2spec
Version:        5.0.0
Release:        19%{?dist}
Summary:        Python script to generate R spec file

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://fedorahosted.org/r2spec/
Source0:        https://fedorahosted.org/releases/r/2/r2spec/R2spec-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       R python3-jinja2 wget fedora-packager
Provides:       R2rpm >= 1.0.0

%description
R2spec is a small python tool that generates spec file for R libraries.
It can work from a URL or a tarball.
R2spec provides R2rpm which generates rpm for R libraries using the 
R2spec API.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install --root=%{buildroot}

## Only work localy, needs internet
#%check
#%%{__python3} tests.py

%files
#-f installed_files2
%doc README LICENSE CHANGELOG
%{python3_sitelib}/*
%config(noreplace) %{_sysconfdir}/%{name}/repos.cfg
%{_bindir}/%{name}
%{_bindir}/R2rpm
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/R2rpm.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.0-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.0.0-16
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.0.0-12
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.0.0-9
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.0-6
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 5.0.0-1
- Update to 5.0.0
- Port to py3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.2.1-13
- Bump release

* Wed Jul 18 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.2.1-12
- Use the py2 version of the macros

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.2.1-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.2.1-9
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.2-1-5
- Drop the dependency on python-argparse now that it's been in python's stdlib
  for so long

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.2.1-1
- Update to 4.2.1

* Thu Jun 04 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.2.0-1
- Update to 4.2.0
- Switch from '.format' invocations to '%%'; backward compatible (Allen S. Rout)
- Fix deps on EL5
- Document in the specfile the dependencies world according to R (Allen S. Rout)
- Accept package names with leading 'R-'.. (Allen S. Rout)
- Fail elegantly is the rpmbuild folder does not exist (RHBZ#901771)
- Do not mark DESCRIPTION R package file as doc (Castedo Ellerman)

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 11 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.1.0-1
- Update to 4.1.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.0.0-1
- Update to 4.0.0 which is an almost complete rewrite

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2010 pingou <pingou-at-pingoured.fr> 3.0.3-1
- Release 3.0.3

* Tue Jul 27 2010 pingou <pingou-at-pingoured.fr> 3.0.2-3
- Change python to %%{__python} (enables to specify 
   the python version at build time) Request from Olivier Lahaye

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 29 2010 pingou <pingou-at-pingoured.fr> 3.0.2-1
- Release 3.0.2

* Mon Jun 28 2010 pingou <pingou-at-pingoured.fr> 3.0.1-1
- Release version 3.0.1
- Update the description (R2spec is now more a tool than a script)

* Wed May 05 2010 pingou <pingou-at-pingoured.fr> 3.0.0-1
- Release version 3.0.0
- Update the description

* Wed May 05 2010 pingou <pingou-at-pingoured.fr> 3.0.0-0.9
- Prerelease 0.9
- Small bug fixes
- The argument to rpmbuild is configurable
- Fix typo in changelog
- Add fedora-packager as Requires

* Sat Mar 27 2010 ingou <pingou-at-pingoured.fr> 3.0.0-0.8
- Prerelease 0.8
- Enable to specify the command in the conf file

* Sat Mar 27 2010 ingou <pingou-at-pingoured.fr> 3.0.0-0.7
- Prerelease 0.7
- Fix the formatting of the description
- Option to use mock to build the RPMs

* Fri Mar 26 2010 ingou <pingou-at-pingoured.fr> 3.0.0-0.6
- Prerelease 0.6
- Fix R2rpm.py

* Thu Mar 25 2010 Pingou <pingou-at-pingoured.fr> 3.0.0-0.5
- Prerelease 0.5
- Do not print the todo while running R2rpm
- Fix summary if ends with a dot
- Refactor the function to read the rpm macro
- Change UTF-8 to utf-8 to make emacs happy

* Wed Mar 24 2010 Pingou <pingou-at-pingoured.fr> 3.0.0-0.4
- Prerelease 0.4
- Fix the description to fit in the length
- Add wget in the requires

* Wed Mar 24 2010 Pingou <pingou-at-pingoured.fr> 3.0.0-0.3
- Prerelease 0.3
- Add the -p option to build from a package name
- Output the rpm generated

* Tue Mar 23 2010 Pingou <pingou-at-pingoured.fr> 3.0.0-0.2
- Prerelease 0.2 
- Add the -p option to build from a package name
- Add the man page for R2rpm
- Fix release
- Fix changelog

* Sun Mar 07 2010 Pingou <pingou-at-pingoured.fr> 3.0.0-0.1
- Prerelease 0.1
- Add the R2rpm script

* Sun Aug 02 2009 Pingou <pingou-at-pingoured.fr> 2.5.3-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 22 2009 Pingou <pingou-at-pingoured.fr> 2.5.2-2
- Correct the source0

* Sun Mar 22 2009 Pingou <pingou-at-pingoured.fr> 2.5.2-1
- New upstream release

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 07 2008 Pingou <pingou-at-pingoured.fr> 2.5.1-6
- Correct the third sed 

* Sun Dec 07 2008 Pingou <pingou-at-pingoured.fr> 2.5.1-5
- Add the new sed to change the ~

* Sun Dec 07 2008 Pingou <pingou-at-pingoured.fr> 2.5.1-4
- Remove the Patch0

* Fri Dec 05 2008 Pingou <pingou-at-pingoured.fr> 2.5.1-3
- Apply patch for copy of the sources

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.5.1-2
- Rebuild for Python 2.6

* Tue Oct 07 2008 Pingou <pingou-at-pingoured.fr> 2.5.1-1
- New upstream release

* Sun Aug 31 2008 Pingou <pingou-at-pingoured.fr> 2.5.0-3
- Bring __init__.py back :)

* Sun Aug 31 2008 Pingou <pingou-at-pingoured.fr> 2.5.0-2
- Change Source0 to the correct one
- Correct a bug SOURCES != SOURCe
- Remove file __init__.py
- Change defattr(-,root,root) to defattr(-,root,root,-)

* Sun Aug 31 2008 Pingou <pingou-at-pingoured.fr> 2.5.0-1
- New upstream release

* Thu Aug 28 2008 Pingou <pingou-at-pingoured.fr> 2.4.2-1
- Update to version 2.4.2

* Wed Aug 20 2008 Pingou <pingou-at-pingoured.fr> 2.4.1-1
- Update to version 2.4.1

* Sun Aug 18 2008 Pingou <pingou-at-pingoured.fr> 2.4.0-1
- Update to version 2.4.0
- Addition of the spec into the sources

* Mon Aug 11 2008 Pingou <pingou-at-pingoured.fr> 2.3-2
- Change the source0 and url thanks to fedorahosted.org

* Sun Aug 10 2008 Pingou <pingou-at-pingoured.fr> 2.3-1
- Update to version 2.3

* Wed Jul 30 2008 Pingou <pingou-at-pingoured.fr> 2.2-1
- Update to version 2.2

* Wed Jul 30 2008 Pingou <pingou-at-pingoured.fr> 2.1-1
- Update to version 2.1

* Wed Jul 30 2008 Pingou <pingou-at-pingoured.fr> 2.0-1
- Update to version 2.0

* Tue Jul 29 2008 Pingou <pingou-at-pingoured.fr> 1.3-1
- First RPM for Fedora
