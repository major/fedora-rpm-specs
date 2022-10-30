%global cmapdir %(echo `rpm -qls ghostscript | grep CMap | awk '{print $2}'`)
%global pypi_name reportlab

%bcond_without tests

Name:           python-%{pypi_name}
Version:        3.6.12
Release:        1%{?dist}
Summary:        Library for generating PDFs and graphics
License:        BSD and GPLv2+
URL:            https://www.reportlab.com/opensource/
Source0:        %pypi_source

BuildRequires:  gcc
BuildRequires:  freetype-devel
BuildRequires:  ghostscript
BuildRequires:  libart_lgpl-devel

Buildrequires:  fontpackages-devel
%global fonts font(dejavusans)
BuildRequires:  %{fonts}

Obsoletes:      %{name}-doc < 0:3.5.21-1

%description
This is the ReportLab PDF Toolkit. It allows rapid creation of rich PDF
documents, and also creation of charts in a variety of bitmap and vector
formats.

%package -n     python3-%{pypi_name}
Summary:        Library for generating PDFs and graphics
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pillow
Requires:       %{fonts}
%py_provides python3-%{pypi_name}
Obsoletes: python2-reportlab < 0:%{version}-%{release}

%description -n python3-%{pypi_name}
This is the ReportLab PDF Toolkit. It allows rapid creation of rich PDF 
documents, and also creation of charts in a variety of bitmap and vector 
formats.

%prep
%autosetup -n %{pypi_name}-%{version}

# clean up hashbangs from libraries
find src -name '*.py' | xargs sed -i -e '/^#!\//d'
# patch the CMap path by adding Fedora ghostscript path before the match
sed -i '/\~\/\.local\/share\/fonts\/CMap/i''\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ '\'%{cmapdir}\''\,' src/reportlab/rl_settings.py

# Remove Upstream Egg
rm -rf src/reportlab.egg-info

# Remove bundled libart
rm -rf src/rl_addons/renderPM/libart_lgpl

%build
CFLAGS="%{build_cflags} -Isrc/rl_addons/renderPM `pkg-config --cflags libart-2.0`" \
 %py3_build -- --use-system-libart --no-download-t1-files

%install
CFLAGS="%{build_cflags} -Isrc/rl_addons/renderPM `pkg-config --cflags libart-2.0`" \
 %py3_install -- --use-system-libart --no-download-t1-files

# Unbundled fonts
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Regular") %{buildroot}%{python3_sitearch}/reportlab/fonts/Vera.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold Oblique") %{buildroot}%{python3_sitearch}/reportlab/fonts/VeraBI.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold") %{buildroot}%{python3_sitearch}/reportlab/fonts/VeraBd.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Condensed Oblique") %{buildroot}%{python3_sitearch}/reportlab/fonts/VeraIt.ttf

rm -f %{buildroot}%{python3_sitearch}/reportlab/fonts/bitstream-vera-license.txt

cp -a demos %{buildroot}%{python3_sitearch}/reportlab/
cp -a tools %{buildroot}%{python3_sitearch}/reportlab/

# Fix shebang in individual files
pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/reportlab/demos/tests/testdemos.py
pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/reportlab/tools/docco/docpy.py
pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/reportlab/tools/docco/graphdocpy.py
pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/reportlab/tools/docco/rl_doc_utils.py
pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/reportlab/tools/pythonpoint/pythonpoint.py

chmod 0755 %{buildroot}%{python3_sitearch}/reportlab/demos/tests/testdemos.py
chmod 0755 %{buildroot}%{python3_sitearch}/reportlab/tools/docco/docpy.py
chmod 0755 %{buildroot}%{python3_sitearch}/reportlab/tools/docco/graphdocpy.py
chmod 0755 %{buildroot}%{python3_sitearch}/reportlab/tools/docco/rl_doc_utils.py
chmod 0755 %{buildroot}%{python3_sitearch}/reportlab/tools/pythonpoint/pythonpoint.py

%if %{with tests}
%check
# Tests need in-build compiled Python modules to be executed
# Tests pre-generate userguide PDF
cp -a build/lib.%{python3_platform}-cpython-%{python3_version_nodots}/reportlab tests/
cp -a build/lib.%{python3_platform}-cpython-%{python3_version_nodots}/reportlab docs/
cp -a build/lib.%{python3_platform}-cpython-%{python3_version_nodots}/reportlab docs/userguide/
%{__python3} setup.py tests
%endif

%files -n python3-%{pypi_name}
%doc README.txt CHANGES.md docs/reportlab-userguide.pdf
%license LICENSE.txt
%{python3_sitearch}/reportlab/
%{python3_sitearch}/reportlab-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Oct 28 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.6.12-1
- Release 3.6.12

* Sat Aug 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.6.11-1
- Release 3.6.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.6.10-2
- Rebuilt for Python 3.11

* Tue Jun 07 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.6.10-1
- Release 3.6.10

* Fri Mar 11 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.6.8-1
- Release 3.6.8

* Sun Feb 20 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.6.7-1
- Release 3.6.7

* Sat Feb 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.6.6-1
- Release 3.6.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.6.5-1
- Release 3.6.5

* Sat Dec 04 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.6.3-1
- Release 3.6.3

* Wed Nov 10 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.6.2-2
- Use DejaVuSans fonts (rhbz#1852520)

* Sat Oct 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.6.2-1
- Release 3.6.2

* Fri Aug 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-1
- Release 3.6.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.68-1
- Release 3.5.68

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5.66-2
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.66-1
- Release 3.5.66

* Tue Mar 09 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.64-1
- Release 3.5.64

* Fri Mar 05 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.63-1
- Release 3.5.63

* Thu Mar 04 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.62-1
- Release 3.5.62

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.60-1
- Release 3.5.60

* Wed Jan 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.59-1
- Release 3.5.59

* Fri Jan 01 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.5.57-1
- Release 3.5.57

* Sat Dec 12 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.56-1
- Release 3.5.56

* Fri Nov 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.55-1
- Release 3.5.55

* Mon Oct 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.54-1
- Release 3.5.54

* Mon Oct 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.53-1
- Release 3.5.53

* Fri Sep 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.51-1
- Release 3.5.51

* Fri Sep 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.50-1
- Release 3.5.50

* Fri Sep 04 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.49-1
- Release 3.5.49

* Wed Aug 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.48-1
- Release 3.5.48

* Fri Aug 07 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.47-1
- Release 3.5.47

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.46-1
- Release 3.5.46

* Mon Jul 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.45-1
- Release 3.5.45

* Tue Jun 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.44-2
- Fix symlinks to the font files

* Sat Jun 27 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.44-1
- Release 3.5.44

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.42-4
- BuildRequires python3-setuptools explicitly
- Remove automagic Python bytecompilation_extra

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5.42-3
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.42-2
- Drop patch for Python 3.9

* Wed Mar 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.42-1
- Release 3.5.42

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.34-4
- Patched for Python-3.9 (rhbz#1808508)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.34-2
- Fix permissions

* Tue Jan 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.5.34-1
- Release 3.5.34

* Thu Oct 31 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.5.32-1
- Release 3.5.32

* Thu Oct 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.5.28-1
- Release 3.5.28 (rhbz#1757766)

* Thu Sep 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.5.26-1
- Release 3.5.26 (rhbz#1752842)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.23-5
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.5.23-4
- Rebuild for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.5.23-2
- Reintroduce python2-reportlab on Fedora 31 (rhbz#1723034)

* Wed Jun 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.5.23-1
- Release 3.5.23 (rhbz#1713011)
- Unbundle libart (rhbz#1435836)

* Wed May 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.5.21-1
- Release 3.5.21 (rhbz#1600316)
- Obsolete Python2 on Fedora 31+

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 3.4.0-9
- Update url
  See: https://bugzilla.redhat.com/show_bug.cgi?id=1622664

* Thu Aug 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.0-8
- Correct egg-info dependency information

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 williamjmorenor@gmail.com - 3.4.0-4
- Adjust requirements

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 William Moreno <williamjmorenor@gmail.com> - 3.4.0-1
- Update to 3.4.0 upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 09 2016 William Moreno <williamjmorenor@gmail.com> - 3.3.0-1
- Update to v3.3.0
- Update python macros
- Enable %%test
- Use license macro
- Provide python2 subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 26 2015 Peter Gordon <peter@thecodergeek.com> - 3.2.0-1
- Update to new upstream release (3.2.0)
- Drop font locations patches (fixed upstream):
  - 3.1.8-font-locations.patch
  - 2.5-font-locations.patch
- Resolves: #1175228 (python-reportlab-3.2.0 is available).
- Resolves: #1277162 (Wrong dependency version number for pillow.)
- Resolves: #1267446 (Missing Requires: on pillow)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Apr 22 2014 Christopher Meng <rpm@cicku.me> - 3.1.8-1
- Update to 3.1.8
- Documentation package should be -doc instead of -docs.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.5-6
- Add a dep on python-imaging to process images

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.5-2
- Update to version 2.5 of reportlab.
- Remove tabs in specfile.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Nov 23 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.3-2
- Do not bundle fonts
- Point the config to Fedora's font locations

* Thu Nov 12 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.3-1
- Updated to 2.3
- New version is no longer noarch.

* Fri Apr 17 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 2.1-6
- Rebuild for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.1-4
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.1-3
- Rebuild for Python 2.6

* Mon Jan  7 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.1-2
- Remove luxi font. (#427845)
- Add patch to not search for the luxi font.

* Sat May 26 2007 Brian Pepple <bpepple@fedoraproject.org> - 2.1-1
- Update to 2.1.

* Wed Dec 27 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0-2
- Make docs subpackage.

* Wed Dec 27 2006 Brian Pepple <bpepple@fedoraproject.org> - 2.0-1
- Update to 2.0.

* Fri Dec  8 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.21.1-2
- Rebuild against new python.

* Thu Sep  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.21.1-1
- Update to 1.20.1.

* Tue Feb 14 2006 Brian Pepple <bdpepple@ameritech.net> - 1.20-5
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 26 2005 Brian Pepple <bdpepple@ameritech.net> - 1.20-4
- Add dist tag. (#176479)

* Mon May  9 2005 Brian Pepple <bdpepple@ameritech.net> - 1.20-3.fc4
- Switchback to sitelib patch.
- Make package noarch.

* Thu Apr  7 2005 Brian Pepple <bdpepple@ameritech.net> - 1.20-2.fc4
- Use python_sitearch to fix x86_64 build.

* Wed Mar 30 2005 Brian Pepple <bdpepple@ameritech.net> - 1.20-1.fc4
- Rebuild for Python 2.4.
- Update to 1.20.
- Switch to the new python macros for python-abi
- Add dist tag.

* Sat Apr 24 2004 Brian Pepple <bdpepple@ameritech.net> 0:1.19-0.fdr.2
- Removed ghosts.

* Sat Mar 20 2004 Brian Pepple <bdpepple@ameritech.net> 0:1.19-0.fdr.1
- Initial Fedora RPM build
