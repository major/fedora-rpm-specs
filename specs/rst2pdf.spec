
Name: rst2pdf
Version: 0.102
Release: 4%{?dist}
Summary: Tool for transforming reStructuredText to PDF
License: MIT

URL: https://rst2pdf.org/
Source0: %{pypi_source}

BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildArch: noarch

%description
Tool for transforming reStructuredText to PDF using ReportLab

%prep
%autosetup -n %{name}-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files rst2pdf

%files -n %{name} -f %{pyproject_files}
%doc CHANGES.rst Contributors.txt README.rst
%license LICENSE.txt
%{_bindir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Sergio Pascual <sergiopr at fedoraproject.org> - 0.102-3
- Updated to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Sergio Pascual <sergiopr at fedoraproject.org> - 0.102-1
- New upstream source (0.102)

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.101-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 28 2023 Sergio Pascual <sergiopr at fedoraproject.org> - 0.101-1
- New upstream version 0.101

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.97-13
- Adjust to py 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.97-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.97-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.97-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.97-3
- Rebuilt for Python 3.9

* Thu May 21 2020 Sergio Pascual <sergiopr at fedoraproject.org> - 0.97-2
- New upstream source (0.97)
- Add distag macro

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-0.2.20190902gitf7adb4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Sergio Pascual <sergiopr at fedoraproject.org> - 0.95-0.1.20190902gitf7adb4a.fc32
- Using prerelease from repository, works with python 3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Sergio Pascual <sergiopr at fedoraproject.org> - 0.93-14
- Use python2 macros for build and install

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.93-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 0.93-3
- Added a requires: python-pdfrw (fixes #957835)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.93-1
- New upstream version 0.93

* Fri Dec 07 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.92-4
- Fix wrong URL

* Fri Jul 27 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.92-3
- Fix for bz #842800

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.92-1
- New upstream source, compatible with docutils 9

* Mon Mar 26 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.91-2
- Adding sources

* Mon Mar 26 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.91-1
- New upstream source, fixes bz #709119

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 08 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.16-4
- Updated fix for bz #709119

* Tue May 31 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.16-3
- Fix for bz #709119

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.16-1
- New upstream source

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 06 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.14.2-1
- New upstream source

* Thu Mar 18 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.13.1-1
- New upstream source

* Mon Mar 15 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.13-1
- New upstream source

* Tue Feb 02 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 0.12.3-2
- Missing python-docutils dependency (bz #561050)

* Wed Dec 23 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.12.3-1
- New upstream source

* Fri Nov 13 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 0.12.2-2
- URL changed
- Requires pygments
- Preserving timestamps during install

* Thu Nov 05 2009 Sergio Pascual <spr@astrax.fis.ucm.es> - 0.12.2-1
- New upstream source

* Wed Jun 24 2009 Sergio Pascual <spr@astrax.fis.ucm.es> - 0.11-1
- New upstream source

* Sun Jun 21 2009 Sergio Pascual <spr@astrax.fis.ucm.es> - 0.10.1-2
- Requires simplejson

* Wed Jun 17 2009 Sergio Pascual <spr@astrax.fis.ucm.es> - 0.10.1-1
- Initial spec file
