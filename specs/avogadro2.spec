# Qt6 builds for testing
%bcond qt6 1

# Package language files
%bcond lang 1

%global app_id org.openchemistry.Avogadro2

Name:           avogadro2
Version:        1.100.0
Release:        %autorelease
Summary:        Advanced molecular editor
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://avogadro.openmolecules.net/
Source0:        https://github.com/OpenChemistry/avogadroapp/archive/%{version}/avogadroapp-%{version}.tar.gz
Source2:        https://github.com/OpenChemistry/avogadro-i18n/archive/%{version}/avogadro-i18n-%{version}.tar.gz

Patch0:         %{name}-avoid_i18n_download.patch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  cmake3
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  avogadro2-libs-devel >= 0:%{version}
BuildRequires:  spglib-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  hdf5-devel
BuildRequires:  glew-devel
%if %{with qt6}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
%else
BuildRequires:  molequeue-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
%endif
BuildRequires:  make
BuildRequires:  libappstream-glib

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
%{_datadir}/%{name}/i18n/avogadroapp-%{1}.qm \
%{_datadir}/%{name}/i18n/avogadrolibs-%{1}.qm

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
%lang_subpkg ka Georgian
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
 -DQT_VERSION:STRING=%{?with_qt6:6}%{!?with_qt6:5} \
 %{?with_qt6:-DAvogadro_ENABLE_RPC=OFF} \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DCMAKE_INSTALL_LOCALEDIR:PATH=%{_datadir}/%{name}/i18n
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc

chrpath -d %{buildroot}%{_bindir}/%{name}

desktop-file-edit --set-key=Exec --set-value='env QT_QPA_PLATFORM=wayland LD_LIBRARY_PATH=%{_libdir}/avogadro2 %{name} %f' \
 %{buildroot}%{_datadir}/applications/%{app_id}.desktop

mkdir -p %{buildroot}%{_datadir}/icons/%{name}
cp -a avogadro/icons/* %{buildroot}%{_datadir}/icons/%{name}/

%if %{with lang}
mkdir -p %{buildroot}%{_datadir}/%{name}/i18n
install -pm 644 avogadro-i18n-%{version}/avogadroapp/* %{buildroot}%{_datadir}/%{name}/i18n/
install -pm 644 avogadro-i18n-%{version}/avogadrolibs/* %{buildroot}%{_datadir}/%{name}/i18n/
%endif

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{app_id}.*
%{_datadir}/icons/%{name}
%if %{with lang}
%dir %{_datadir}/%{name}
%exclude %{_datadir}/%{name}/i18n
%endif

%changelog
%autochangelog
