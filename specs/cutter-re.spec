%global forgeurl https://github.com/rizinorg/cutter
Version:        2.5.0
%global tag     v%{version}
%forgemeta

Name:           cutter-re
Release:        %autorelease
Summary:        GUI for Rizin reverse engineering framework

# CC-BY-SA: src/img/icons/
# OFL-1.1: src/fonts/Anonymous Pro.ttf, src/fonts/Inconsolata-Regular.ttf
License:        GPL-3.0-only AND CC-BY-SA-3.0 AND OFL-1.1

URL:            https://cutter.re/
Source0:        %forgesource
Source1:        cutter-re.desktop
Source2:        cutter-re.appdata.xml

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  graphviz-devel
BuildRequires:  kf6-syntax-highlighting-devel
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-pyside6-devel
BuildRequires:  python3-shiboken6-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
%ifarch %{qt6_qtwebengine_arches}
BuildRequires:  qt6-qtwebengine-devel
%endif
BuildRequires:  rizin-devel >= 0.8.0
Requires:       hicolor-icon-theme
Requires:       python3-jupyter-client
Requires:       python3-notebook

%description
Cutter is a Qt and C++ GUI for Rizin. Its goal is making an advanced,
customizable and FOSS reverse-engineering platform while keeping the user
experience at mind. Cutter is created by reverse engineers for reverse
engineers.


%package devel
Summary:        Development files for the cutter-re package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the cutter-re package. See cutter-re package for more
information.


%prep
%autosetup -p1 -n cutter-%{version}
# Disable translations since they are in a git submodule not present in the release tarball
sed -i 's/include(Translations)/# include(Translations)/g' src/CMakeLists.txt


%build
%cmake -DCUTTER_USE_BUNDLED_RIZIN=OFF -DCMAKE_SKIP_RPATH=ON -DCMAKE_BUILD_TYPE=Release \
       -DCUTTER_ENABLE_PYTHON_BINDINGS=ON -DCUTTER_EXTRA_PLUGIN_DIRS=%{_libdir}/cutter \
       -DCUTTER_ENABLE_PYTHON=ON -DCUTTER_INCLUDE_GIT_HASH=OFF
%cmake_build


%install
%cmake_install
mv %{buildroot}%{_bindir}/cutter %{buildroot}%{_bindir}/cutter-re

# replace default .desktop file with our own, to use cutter-re name
mkdir -p %{buildroot}%{_datadir}/applications
rm %{buildroot}%{_datadir}/applications/re.rizin.cutter.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
        %{SOURCE1}

mkdir -p %{buildroot}%{_metainfodir}
install -pm644 %{SOURCE2} \
        %{buildroot}%{_metainfodir}

# rename cutter svg icon to cutter-re
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/{cutter,cutter-re}.svg
sed -i 's/bin\/cutter/bin\/cutter-re/g' %{buildroot}%{_libdir}/cmake/Cutter/CutterTargets-*.cmake

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%{_bindir}/cutter-re
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%license COPYING src/img/icons/Iconic-LICENSE
%doc README.md


%files devel
%{_includedir}/cutter
%{_libdir}/cmake/Cutter/*.cmake
%dir %{_libdir}/cmake/Cutter


%changelog
%autochangelog
