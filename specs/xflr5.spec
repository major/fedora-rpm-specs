Name:           xflr5
Version:        6.47
Release:        16%{?dist}
Summary:        Analysis tool for airfoils, wings and planes

License:        GPL-3.0-or-later
URL:            http://www.xflr5.com/
Source0:        https://sourceforge.net/projects/xflr5/files/%{version}/%{name}_v%{version}_src.tar.gz
Source1:        %{name}.desktop

# Read library installation directory from env-var
Patch0:         xflr5_libdir.patch

BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  texlive-scheme-basic
BuildRequires:  texlive-cm-super
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(babel.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(keystroke.sty)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(rotating.sty)
BuildRequires:  tex(ecrm1200.tfm)

Requires:       hicolor-icon-theme


%description
XFLR5 is an analysis tool for airfoils, wings and planes operating at low
Reynolds Numbers. It includes:
1. XFoil's Direct and Inverse analysis capabilities
2. Wing design and analysis capabilities based on the Lifiting Line Theory, on
   the Vortex Lattice Method, and on a 3D Panel Method


%prep
%autosetup -p1 -n %{name}

# Fix FSF addresses
find . -type f -print0 | xargs -0 sed -i 's|59 Temple Place, Suite 330, Boston, MA  02111-1307|51 Franklin Street, Fifth Floor, Boston, MA  02110-1301|'

# Fix line endings
find . -type f -exec dos2unix {} \;

# Build only english documentation
rm -f doc/xflr5-guidelines_latex/guidelines_fr.tex


%build
LIBDIR=%{_lib} %qmake_qt5 PREFIX=%{_prefix} %{name}.pro
# Parallel build broken on s390x...
%ifarch s390x
LIBDIR=%{_lib} make
%else
LIBDIR=%{_lib} %make_build
%endif
make -C doc/xflr5-guidelines_latex
lrelease-qt5 translations/*.ts

# Delete the translations template
rm translations/xflr5v6.qm


%install
make INSTALL_ROOT=%{buildroot} install
install -d %{buildroot}%{_datadir}/%{name}/translations
install -pm 0644 translations/*.qm %{buildroot}%{_datadir}/%{name}/translations
cp -a qss %{buildroot}%{_datadir}/%{name}/qss
install -Dpm 0644 xflr5-gui/images/xflr5_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}


%files
%doc doc/ReleaseNotes.txt
%doc doc/xflr5-guidelines_latex/guidelines_en.pdf
%license License.txt
%{_bindir}/%{name}
%{_libdir}/libXFoil.so*
%{_libdir}/libxflr5-engine.so*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Sandro Mani <manisandro@gmail.com> - 6.47-1
- Update to 6.47

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Sandro Mani <manisandro@gmail.com> - 6.41-1
- Update to 6.41

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 6.40-4
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.40-3
- Escape macros in %%changelog

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.40-2
- Remove obsolete scriptlets

* Mon Jan 08 2018 Sandro Mani <manisandro@gmail.com> - 6.40-1
- Update to 6.40

* Thu Sep 21 2017 Sandro Mani <manisandro@gmail.com> - 6.39-1
- Update to 6.39

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 6.38-1
- Update to 6.38

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Sandro Mani <manisandro@gmail.com> - 6.30-1
- Update to 6.30

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Sandro Mani <manisandro@gmail.com> - 6.12-1
- Update to 6.12

* Thu Nov 19 2015 Sandro Mani <manisandro@gmail.com> - 6.11-1
- Update to 6.11

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.10.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Sandro Mani <manisandro@gmail.com> - 6.10.04-1
- Update to 6.10.04

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.10.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.10.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Ville Skyttä <ville.skytta@iki.fi> - 6.10.02-2
- Don't ship .svn files

* Mon Mar 24 2014 Sandro Mani <manisandro@gmail.com> - 6.10.02-1
- Update to 6.10.02

* Mon Jan 27 2014 Sandro Mani <manisandro@gmail.com> - 6.09.06-1
- Update to 6.09.06

* Mon Nov 18 2013 Sandro Mani <manisandro@gmail.com> - 6.09.05-6
- Add pretrans scriptlet to handle replacement of %%{_datadir}/applications/%%{name}.desktop directory with file

* Sat Nov 16 2013 Sandro Mani <manisandro@gmail.com> - 6.09.05-5
- Fix desktop-file-install syntax

* Fri Sep 13 2013 Sandro Mani <manisandro@gmail.com> - 6.09.05-4
- Add fix for translations and guidelines path
- Build guidelines

* Fri Sep 13 2013 Sandro Mani <manisandro@gmail.com> - 6.09.05-3
- Use desktop-file-install
- Preserve timestamps

* Fri Sep 13 2013 Sandro Mani <manisandro@gmail.com> - 6.09.05-2
- Fix line endings
- Add patch to fix fsf addresses

* Fri Sep 13 2013 Sandro Mani <manisandro@gmail.com> - 6.09.05-1
- Initial package for review
