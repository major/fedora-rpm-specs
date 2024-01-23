%global pypi_name QtAwesome
%global simple_name qtawesome

Name:		python-%{pypi_name}
Version:	1.3.0
Release:	3%{?dist}

Summary:	FontAwesome icons in PyQt and PySide applications
# MIT: QtAwesome code and the bundled phosphor and remixicon fonts
# CC-BY-4.0: the bundled codicon font
# Apache-2.0: the bundled material design icons fonts
# OFL-1.1: the bundled elusive icons font
# OFL-1.1-RFN: the bundled fontawesome icon fonts
%if 0%{?fedora} > 38
License:	MIT AND CC-BY-4.0 AND Apache-2.0 AND OFL-1.1
%else
License:	MIT AND CC-BY-4.0 AND Apache-2.0 AND OFL-1.1 AND OFL-1.1-RFN
%endif
URL:		https://github.com/spyder-ide/%{simple_name}

Source0:	%pypi_source

BuildArch:	noarch

BuildRequires:	python3-devel

%description
QtAwesome enables iconic fonts such as Font Awesome and Elusive.

It is a port to Python - PyQt / PySide of the QtAwesome C++ library by 
Rick Blommers.

%package -n     python3-%{pypi_name}
Summary:	FontAwesome icons in PyQt and PySide applications
%{?python_provide:%python_provide python3-%{pypi_name}}

#provides font files
#./qtawesome/fonts/codicon.ttf
Provides:	bundled(codicon-fonts) = 1.10
#./qtawesome/fonts/elusiveicons-webfont.ttf
Provides:	bundled(elusiveicons-fonts) = 001.000
#./qtawesome/fonts/materialdesignicons5-webfont.ttf
Provides:	bundled(materialdesignicons5-fonts) = 5.9.55
#./qtawesome/fonts/materialdesignicons6-webfont.ttf
Provides:	bundled(materialdesignicons6-fonts) = 1.0
#./qtawesome/fonts/phosphor.ttf
Provides:	bundled(phosphor-fonts) = 1.3
#./qtawesome/fonts/remixicon.ttf
Provides:	bundled(remixicon-fonts) = 2.5
%if 0%{?fedora} > 38
Requires:	fontawesome4-fonts-web
Requires:	fontawesome-fonts-web
%else
#./qtawesome/fonts/fontawesome4.7-webfont.ttf
Provides:	bundled(fontawesome-fonts-web) = 4.7.0
#./qtawesome/fonts/fontawesome5-brands-webfont.ttf
#./qtawesome/fonts/fontawesome5-regular-webfont.ttf
#./qtawesome/fonts/fontawesome5-solid-webfont.ttf
Provides:	bundled(fontawesome5-fonts-web) = 5.15.4
%endif

%description -n python3-%{pypi_name}

QtAwesome enables iconic fonts such as Font Awesome and Elusive.

It is a port to Python - PyQt / PySide of the QtAwesome C++ library by 
Rick Blommers.

%prep
%autosetup -n %{pypi_name}-%{version}

# Fix end of line encoding
sed -i 's/\r//' README.md

# Don't use the bundled fonts.
# This disables verifying the checksum of font files.
%if 0%{?fedora} > 38
sed -i '/^SYSTEM_FONTS = /s/False/True/' qtawesome/iconic_font.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l qtawesome

%if 0%{?fedora} > 38
# Unbundle the fontawesome 4.x font
rm %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome4.7-webfont.ttf
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome4.7-webfont.ttf
# Unbundle the fontawesome 5.x fonts
# Version 6 is backwards compatible with version 5
rm %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-*.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-brands-400.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-brands-webfont.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-regular-400.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-regular-webfont.ttf
ln -s %{_datadir}/fontawesome/webfonts/fa-solid-900.ttf \
      %{buildroot}%{python3_sitelib}/qtawesome/fonts/fontawesome5-solid-webfont.ttf
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/qta-browser

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.0-2
- Assert a license file is automatically handled; don’t package a duplicate

* Thu Dec 14 2023 Jonathan Wright <jonathan@almalinux.org> - 1.3.0-1
- Update to 1.3.0 rhbz#2254511

* Tue Oct 03 2023 Alessandro Astone <ales.astone@gmail.com> - 1.2.3-4
- Fix using the system fontawesome fonts rhbz#2241351

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.3-2
- Rebuilt for Python 3.12

* Thu Apr 13 2023 Jonathan Wright <jonathan@almalinux.org> - 1.2.3-1
- Update to 1.2.3 rhbz#2136710

* Thu Mar 30 2023 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- Update to 1.2.2
- Unbundle the FontAwesome fonts
- Update python macro usage
- Convert License tag to SPDX
- Move Provides for bundled fonts to python3-qtawesome

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Sat Dec 11 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Tue Sep 22 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2
- Use pypi_source macro in specfile

* Sat May 02 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Mon Feb 17 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.7-1
- Update to 0.5.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.4-7
- Drop python2 package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.4-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-6
- Rebuild for Python 3.6

* Sun Oct 02 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-5
- Fixed typo on dependency

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-4
- Added license tag
- Added doc file 
- Added provides

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-3
- Fix source url

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-2
- Fix license file installation

* Thu Aug 11 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-1
- Initial package.
