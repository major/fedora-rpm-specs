%bcond_without qt6

Name:           contour-terminal
Version:        0.3.11.258
Release:        %autorelease
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        %{url}/archive/v%{version}/contour-%{version}.tar.gz

ExcludeArch:    s390x i686 ppc64le

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  fmt-devel
BuildRequires:  guidelines-support-library-devel
BuildRequires:  range-v3-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  libxcb-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libunicode-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
%if %{?fedora} <= 38
BuildRequires:  catch-devel
%else
BuildRequires:  catch2-devel
%endif

%if %{with qt6}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtmultimedia-devel
%else
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtmultimedia-devel
%endif

Requires:       hicolor-icon-theme
Requires:       kf5-kservice
Requires:       kf5-filesystem
Requires:       ncurses-base

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
%autosetup -n contour-%{version}

%build
%cmake \
    -GNinja \
%if %{with qt6}
    -DCONTOUR_BUILD_WITH_QT6=ON
%else
    -DCONTOUR_BUILD_WITH_QT6=OFF
%endif
%ninja_build -C %{_vpath_builddir}

%install
%ninja_install -C %{_vpath_builddir}

rm %{buildroot}%{_datadir}/terminfo/c/contour-latest
ln -s contour %{buildroot}%{_datadir}/terminfo/c/contour-latest
rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md

%check
./%{_vpath_builddir}/src/crispy/crispy_test
./%{_vpath_builddir}/src/vtbackend/vtbackend_test

desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/contour
%{_datadir}/applications/*.desktop
%{_datadir}/kservices5/ServiceMenus/*.desktop
%dir %{_datadir}/contour
%dir %{_datadir}/contour/shell-integration
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/terminfo/c/contour*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.xml

%changelog
%autochangelog
