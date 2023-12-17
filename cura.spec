%global         major_minor_version 5.4
%global         patch_version 0

Name:           cura
Epoch:          1
Version:        %{major_minor_version}.%{patch_version}
Release:        %autorelease
Summary:        3D printer / slicing GUI

# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/MOUNX6I3POCDMYWBNJ7JPLLIKVYWVRBJ/
License:        LGPL-3.0-or-later

URL:            https://ultimaker.com/en/products/cura-software
Source0:        https://github.com/Ultimaker/Cura/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2:        mod_bundled_packages_json.py
Source3:        CuraPluginInstall.cmake
Source4:        CuraTests.cmake
Source5:        com.ultimaker.cura.desktop.in
Source6:        CMakeLists.txt
Source7:        CuraVersion.py.in
Source8:        com.ultimaker.cura.appdata.xml

# Skip forced loading SentryLogger to avoid an error on startup
Patch:          028e7f7.patch

# Fix asserts for called once in Python 3.12
Patch:          https://github.com/Ultimaker/Cura/pull/16103.patch

# Avoid "KeyError: material_name" crash
Patch:          https://github.com/Ultimaker/Cura/pull/17642.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-keyring
BuildRequires:  python3-pyserial
BuildRequires:  python3-pynest2d
BuildRequires:  python3-requests
BuildRequires:  python3-savitar >= 5.3.0
BuildRequires:  python3-uranium >= 5.4.0
BuildRequires:  python3-zeroconf

Requires:       open-sans-fonts
Requires:       python3-certifi
Requires:       python3-keyring
Requires:       python3-numpy-stl
Requires:       python3-pyserial
Requires:       python3-pynest2d
Requires:       python3-requests
Requires:       python3-savitar >= 5.3.0
Requires:       python3-trimesh
Requires:       python3-uranium >= 5.4.0
Requires:       python3-zeroconf
# Requires:       qt5-qtquickcontrols
# Requires:       qt5-qtquickcontrols2
Requires:       CuraEngine == %{epoch}:%{version}
Requires:       cura-fdm-materials >= %{major_minor_version}

# Workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1494278
Requires:       libglvnd-devel

# So that it just works
Requires:       3dprinter-udev-rules

# For various plugins
Recommends:     python3-trimesh
Recommends:     python3-certifi

%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura prepares your model for 3D printing. For novices, it makes it easy to get
great results. For experts, there are over 200 settings to adjust to your
needs. As it's open source, our community helps enrich it even more.

# see: https://github.com/Ultimaker/Cura/issues/5142
%define cura_cloud_api_root https://api.ultimaker.com
%define cura_cloud_api_version 1
%define cura_cloud_account_api_root https://account.ultimaker.com

%define reverse_dns_name com.ultimaker.%{name}

%prep
%autosetup -p1 -S git -n Cura-%{version}

mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE4} cmake
rm -rf CMakeLists.txt
cp -a %{SOURCE5} %{SOURCE6} %{SOURCE8} .
cp -a %{SOURCE7} cura

# Wrong end of line encoding
dos2unix docs/How_to_use_the_flame_graph_profiler.md

# Wrong shebang
sed -i '1s=^#!/usr/bin/\(python\|env python\)3*=#!%{python3}=' cura_app.py

%build
%cmake \
  -DCURA_VERSION:STRING=%{version} \
  -DCURA_BUILDTYPE="RPM %{version}"\
  -DCURA_CLOUD_API_ROOT:STRING=%{cura_cloud_api_root} \
  -DCURA_CLOUD_API_VERSION:STRING=%{cura_cloud_api_version} \
  -DCURA_CLOUD_ACCOUNT_API_ROOT:STRING=%{cura_cloud_account_api_root} \
  -DLIB_SUFFIX:STR=
%cmake_build

# rebuild locales
cd resources/i18n
rm *.pot
for DIR in *; do
  pushd $DIR
  for FILE in *.po; do
    msgfmt $FILE.po -o LC_MESSAGES/${FILE%po}mo || :
  done
  popd
done
cd -


%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/%{name}/resources/images/whats_new
mkdir -p %{buildroot}%{_datadir}/%{name}/resources/texts/whats_new
mkdir -p %{buildroot}%{_datadir}/%{name}/resources/scripts

# Sanitize the location of locale files
pushd %{buildroot}%{_datadir}
mv cura/resources/i18n locale
ln -s ../../locale cura/resources/i18n
rm locale/*/*.po
popd

# Unbundle fonts
rm -rf %{buildroot}%{_datadir}/%{name}/resources/themes/cura-light/fonts/
ln -s %{_datadir}/fonts/open-sans/ %{buildroot}%{_datadir}/%{name}/resources/themes/cura-light/fonts

# Remove failing plugins
rm -r %{buildroot}%{_prefix}/lib/cura/plugins/{SentryLogger,UFPReader,UFPWriter}

# Bytecompile the plugins
%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/cura

# Use the default flags in the shebang
%py3_shebang_fix %{buildroot}%{_bindir}/*

%find_lang cura
%find_lang fdmextruder.def.json
%find_lang fdmprinter.def.json


%check
%{python3} -m pip freeze
%{python3} -m pytest -v

desktop-file-validate %{buildroot}%{_datadir}/applications/%{reverse_dns_name}.desktop


%files -f cura.lang -f fdmextruder.def.json.lang -f fdmprinter.def.json.lang
%license LICENSE
%doc README.md
# CHANGES is not updated since 15.x
# things in docs are developer oriented
%{python3_sitelib}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{reverse_dns_name}.desktop
%{_datadir}/metainfo/%{reverse_dns_name}.appdata.xml
%{_datadir}/icons/hicolor/128x128/apps/%{name}-icon.png
%{_datadir}/mime/packages/%{name}.xml
%{_bindir}/%{name}
%{_prefix}/lib/%{name}

%changelog
%autochangelog
