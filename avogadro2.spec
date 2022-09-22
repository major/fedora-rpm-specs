# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

# Qt6 builds for testing
%bcond_with qt6

# Package language files
%bcond_without lang

Name:           avogadro2
Version:        1.97.0
Release:        2%{?dist}
Summary:        Advanced molecular editor
License:        BSD
URL:            http://avogadro.openmolecules.net/
Source0:        https://github.com/OpenChemistry/avogadroapp/archive/%{version}/avogadroapp-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Source2:        https://github.com/OpenChemistry/avogadro-i18n/archive/refs/tags/avogadro-i18n-%{version}.tar.gz

Patch0:         %{name}-avoid_i18n_download.patch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  cmake3
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  avogadro2-libs-devel >= 0:%{version}
BuildRequires:  molequeue-devel
BuildRequires:  spglib-devel
BuildRequires:  %{?dts}gcc
BuildRequires:  %{?dts}gcc-c++
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  hdf5-devel
BuildRequires:  glew-devel
%if %{with qt6}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
%else
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
%endif
BuildRequires:  make
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif

Requires: python%{python3_pkgversion}
Requires: openbabel%{?_isa} >= 3.1.1
Requires: xtb%{?_isa}
Requires: avogadro2-libs%{?_isa} >= 0:%{version}

# Avogadro-1.2.0 requires openbabel2,
# openababel2 is no longer available in Fedora 36+
Obsoletes: avogadro < 0:1.95.1
Provides: avogadro = 0:%{version}-%{release}

%description
Avogadro is an advanced molecular editor designed for cross-platform use in
computational chemistry, molecular modeling, bioinformatics, materials science,
and related areas. It offers flexible rendering and a powerful plugin
architecture. The code in this repository is a rewrite of Avogadro with source
code split across a libraries repository and an application repository. Core
features and goals of the Avogadro project:

* Open source distributed under the liberal 3-clause BSD license
* Cross platform with nightly builds on Linux, Mac OS X and Windows
* Intuitive interface designed to be useful to whole community
* Fast and efficient embracing the latest technologies
* Extensible, making extensive use of a plugin architecture
* Flexible supporting a range of chemical data formats and packages

%if %{with lang}
%define         lang_subpkg() \
%package        langpack-%{1}\
Summary:        %{2} language data for %{name}\
BuildArch:      noarch \
Requires:       %{name} = %{version}-%{release}\
Supplements:    (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description    langpack-%{1}\
%{2} language data for %{name}.\
\
%files          langpack-%{1}\
/usr/share/%{name}/i18n/avogadroapp-%{1}.qm \
/usr/share/%{name}/i18n/avogadrolibs-%{1}.qm

%lang_subpkg af Afrikaans
%lang_subpkg ar Arabic
%lang_subpkg bg Bulgarian
%lang_subpkg bs Bosnian
%lang_subpkg ca Catalan
%lang_subpkg ca_VA "Catalan Valencia"
%lang_subpkg cs Czech
%lang_subpkg da Danish
%lang_subpkg de German
%lang_subpkg el Greek
%lang_subpkg en_AU "English (Australia)"
%lang_subpkg en_CA "English (Canadian)"
%lang_subpkg en_GB "English (United Kingdom)"
%lang_subpkg eo Esperando
%lang_subpkg es Spanish
%lang_subpkg et Estonian
%lang_subpkg eu Basque
%lang_subpkg fa Persian
%lang_subpkg fi Finnish
%lang_subpkg fr French
%lang_subpkg fr_CA "French (Canadian)"
%lang_subpkg gl Galician
%lang_subpkg he Hebrew
%lang_subpkg hi Hindi
%lang_subpkg hr Croatian
%lang_subpkg hu Hungarian
%lang_subpkg id Indonesian
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg kn Kannada
%lang_subpkg ko Korean
%lang_subpkg ms "Malay (Malaysia)"
%lang_subpkg nb Norwegian
%lang_subpkg nl Dutch
%lang_subpkg oc Occitan
%lang_subpkg pl Polish
%lang_subpkg pt Portuguese
%lang_subpkg pt_BR Brazil
%lang_subpkg ro Romanian
%lang_subpkg ru Russian
%lang_subpkg sa Sanskrit
%lang_subpkg sk Slovakian
%lang_subpkg sl Slovenian
%lang_subpkg sq Albanian
%lang_subpkg sr "Serbian (Cyrillic and Latin)"
%lang_subpkg sv Swedish
%lang_subpkg ta Tamil
%lang_subpkg te Telugu
%lang_subpkg th Thai
%lang_subpkg tr Turkish
%lang_subpkg ug Uyghur
%lang_subpkg uk Ukrainian
%lang_subpkg vi Vietnamese
%lang_subpkg zh_CN "Simplified Chinese"
%lang_subpkg zh_TW Taiwan
%endif

%prep
%setup -n avogadroapp-%{version} -a 2 -q
%autopatch -p1

%if %{with lang}
cd avogadro-i18n-%{version}
mv avogadroapp/avogadroapp-ca@valencia.qm avogadroapp/avogadroapp-ca_VA.qm
mv avogadrolibs/avogadrolibs-ca@valencia.qm avogadrolibs/avogadrolibs-ca_VA.qm
%endif

%build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
export CFLAGS="%{optflags} -I%{_includedir}/%{name}"
export CXXFLAGS="%{optflags} -I%{_includedir}/%{name}"
# RHBZ #1996330
%ifarch %{power64}
export CXXFLAGS="%{optflags} -DEIGEN_ALTIVEC_DISABLE_MMA"
%endif
%cmake3 -DCMAKE_BUILD_TYPE:STRING=Release \
 -Wno-dev \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DENABLE_RPATH:BOOL=ON \
 -DENABLE_TESTING:BOOL=OFF \
 -DAvogadroLibs_DIR:PATH=%{_libdir} \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DCMAKE_INSTALL_LOCALEDIR:PATH=%{_datadir}/%{name}/i18n
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc

chrpath -d %{buildroot}%{_bindir}/%{name}

desktop-file-edit --set-key=Exec --set-value='env QT_QPA_PLATFORM=wayland LD_LIBRARY_PATH=%{_libdir}/avogadro2 %{name} %f' \
 --set-key=Icon --set-value=%{_datadir}/icons/%{name}/avogadro2_128.png \
 %{buildroot}%{_datadir}/applications/%{name}.desktop

cp -p %{buildroot}%{_datadir}/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}-x11.desktop
 desktop-file-edit --set-key=Exec --set-value='env QT_QPA_PLATFORM=xcb LD_LIBRARY_PATH=%{_libdir}/avogadro2 %{name} %f' \
  --set-name='Avogadro2 for X11' \
 %{buildroot}%{_datadir}/applications/%{name}-x11.desktop

mkdir -p %{buildroot}%{_datadir}/icons/%{name}
cp -a avogadro/icons/* %{buildroot}%{_datadir}/icons/%{name}/

%if %{with lang}
mkdir -p %{buildroot}%{_datadir}/%{name}/i18n
install -pm 644 avogadro-i18n-%{version}/avogadroapp/* %{buildroot}%{_datadir}/%{name}/i18n/
install -pm 644 avogadro-i18n-%{version}/avogadrolibs/* %{buildroot}%{_datadir}/%{name}/i18n/
%endif

%if 0%{?fedora}
## Install appdata file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/
%endif

%if 0%{?rhel}
%post
/bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
%endif

%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-x11.desktop
%if 0%{?fedora}
%{_metainfodir}/*.appdata.xml
%endif
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/%{name}
%if %{with lang}
%dir %{_datadir}/%{name}
%exclude %{_datadir}/%{name}/i18n
%endif

%changelog
* Tue Jul 26 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.97.0-2
- Fix QT_QPA_PLATFORM env variables (rhbz#2056155)

* Fri Jul 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.97.0-1
- Release 1.97.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.96.0-1
- Release 1.96.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.95.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 12 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-4
- Built on EPEL8

* Sat Nov 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-3
- Prepare Qt6 builds for testing
- Rebuild against openbabel3

* Mon Sep 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-2
- Manage locale files

* Tue Aug 31 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-1
- Release 1.95.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.94.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.94.0-1
- Release 1.94.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-4
- New rebuild

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-3
- Add avogadro2-libs runtime dependency

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-2
- New rebuild

* Sun Feb 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-1
- Release 1.93.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-5
- Rebuild for spglib-1.14.1
- Use devtools-8 on EPEL7
- Use CMake3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.91.0-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-1
- Release 1.91.0

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.90.0-14.20180713git74e1ede
- Rebuilt for glew 2.1.0

* Sun Jul 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-13.20180713git74e1ede
- Update to commit #74e1ede

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-10
- Rebuild for moloqueue-0.9.0
- Rebuild for GCC-8

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.90.0-9
- Remove obsolete scriptlets

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-8
- Appdata file moved into metainfo data directory

* Thu Dec 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-7
- Rebuild for spglib-1.10.2

* Fri Sep 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-6
- Require OpenBabel (bz#1489749)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-3
- Modified for epel7 builds

* Tue Apr 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-2
- Add appdata file

* Sat Mar 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-1
- Initial package
