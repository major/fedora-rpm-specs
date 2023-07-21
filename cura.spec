%global         major_minor_version 5.3
%global         patch_version 0

Name:           cura
Epoch:          1
Version:        %{major_minor_version}.%{patch_version}
Release:        3%{?dist}
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
Patch1:         028e7f7.patch

# Fix asserts for called once in Python 3.12
Patch2:         https://github.com/Ultimaker/Cura/pull/16103.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

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
BuildRequires:  python3-savitar >= 5.2.2
BuildRequires:  python3-uranium == %{version}
BuildRequires:  python3-zeroconf

Requires:       open-sans-fonts
Requires:       python3-certifi
Requires:       python3-keyring
Requires:       python3-numpy-stl
Requires:       python3-pyserial
Requires:       python3-pynest2d
Requires:       python3-requests
Requires:       python3-savitar >= 5.2.2
Requires:       python3-trimesh
Requires:       python3-uranium == %{version}
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

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

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
sed -i '1s=^#!/usr/bin/\(python\|env python\)3*=#!%{__python3}=' cura_app.py

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
%py_byte_compile %{__python3} %{buildroot}%{_prefix}/lib/cura

# Use the default flags in the shebang
%py3_shebang_fix %{buildroot}%{_bindir}/*

%find_lang cura
%find_lang fdmextruder.def.json
%find_lang fdmprinter.def.json


%check
%{__python3} -m pip freeze
%{__python3} -m pytest -v

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
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 09 2023 Python Maint <python-maint@redhat.com> - 1:5.3.0-2
- Rebuilt for Python 3.12

* Thu Mar  9 2023 Tom Callaway <spot@fedoraproject.org> - 1:5.3.0-1
- update to 5.3.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Miro Hrončok <mhroncok@redhat.com> - 1:4.13.1-5
- Use the default flags for Python in the shebang of /usr/bin/cura
- Fixes: rhbz#2117729

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1:4.13.1-3
- Rebuilt for Python 3.11

* Wed Feb 02 2022 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.13.1-2
- Fix error loading SentryLogger plugin

* Tue Feb 01 2022 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.13.1-1
- Update to 4.13.1

* Thu Jan 20 2022 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.13.0-1
- Update to 4.13.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.12.1-2
- Backport fix for Python 3.10

* Mon Dec 13 2021 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.12.1-1
- Update to 4.12.1

* Mon Aug 16 2021 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.10.0-1
- Update to 4.10.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.9.1-1
- Update to 4.9.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:4.9.0-2
- Rebuilt for Python 3.10

* Mon Apr 26 2021 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.9.0-1
- Update to 4.9.0

* Mon Mar 22 2021 Miro Hrončok <mhroncok@redhat.com> - 1:4.8.0-3
- Adapt to Python 3.9 API changes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Jan Pazdziora <jpazdziora@redhat.com> - 1:4.8.0-1
- Update to 4.8.0
- Recommend trimesh and certifi

* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 1:4.7.1-1
- Update to 4.7.1

* Mon Aug 31 2020 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.7.0-1
- Update to 4.7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:4.6.1-2
- Rebuilt for Python 3.9

* Tue May 5 2020 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.6.0-1
- Update to 4.6.1

* Tue Apr 21 2020 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.6.0-1
- Update to 4.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.4.0-1
- Update to 4.4.0
- Force X11 to workaround invisible window on Wayland

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:4.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:4.1.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.1.0-1
- Update to 4.1.0

* Thu Apr 04 2019 Gabriel Féron <feron.gabriel@gmail.com> - 1:4.0.0-1
- Update to 4.0.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Gabriel Féron <feron.gabriel@gmail.com> - 1:3.6.0-1
- Update to 3.6.0

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.5.1-1
- Update to 3.5.1 (#1644323)

* Tue Aug 28 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.4.1-1
- Update to 3.4.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.3.0-3
- Rebuilt for Python 3.7

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.3.0-2
- Bytecompile the plugins explicitly

* Wed May 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.3.0-1
- Update to 3.3.0
- Enable test_getPropertyFallThrough again

* Wed Mar 21 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.2.1-2
- Require qt5-qtquickcontrols2 in addition to qt5-qtquickcontrols

* Tue Mar 20 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.2.1-1
- Update to 3.2.1
- Force install to /usr/lib and keep this noarch
- Change the set of skipped tests

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.1.0-1
- Update to 3.1.0
- Disable most of the tests
- No longer needs to sed out dist-packages
- Move appdata to metainfo

* Mon Dec 04 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.3-5
- Mark the package with correct license

* Sun Dec 03 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.3-4
- Also apply the nvidia driver workaround on Fedora (#1520138)

* Tue Nov 21 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.3-3
- Require libglvnd-devel as a workaround for #1494278

* Fri Oct 27 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.3-2
- Add upstream commit to fix tests

* Mon Oct 23 2017 Miro Hrončok <mhroncok@redhat.com> - 1:3.0.3-1
- Update to 3.0.3
- Remove locale and desktop file changes (fixed upstream)

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.7.0-2
- Relocate Japanese locale to ja

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.7.0-1
- Update to 2.7.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.1-2
- Require cura-fdm-materials

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.1-1
- Updated to 2.6.1

* Wed May 10 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-2
- Require qt5-qtquickcontrols

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-1
- Update to modern Cura 2.x (introduce Epoch) (#1393176)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04.4-5
- Explicitly run cura on X11 GDK backend (#1388953)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 25 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04.4-3
- Require 3dprinter-udev-rules

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04.4-1
- New version

* Wed Jul 08 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-4
- No longer depend on pypy
- Simplify the launcher

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-3
- Patch for #1230281

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-2
- Require latest CuraEngine

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-1
- Update to 15.02.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-4
- Patch: Open directories with xdg-open (#1217961)

* Mon Apr 20 2015 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-3
- Handle files from the command line (#1213220)

* Mon Mar 30 2015 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-2
- Update the no firmware patch according to communication with Cura upstream

* Mon Dec 29 2014 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-1
- Updated to 14.12.1
- No longer depend on firmware

* Sat Oct 25 2014 Miro Hrončok <mhroncok@redhat.com> - 14.09-1
- New version 14.09

* Tue Jun 24 2014 Miro Hrončok <mhroncok@redhat.com> - 14.06-2
- Require at least the firmware version originally bundled in git

* Mon Jun 23 2014 Miro Hrončok <mhroncok@redhat.com> - 14.06-1
- New version 14.06

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Miro Hrončok <mhroncok@redhat.com> - 13.11.2-1
- New version 13.11.2

* Wed Oct 16 2013 Miro Hrončok <mhroncok@redhat.com> - 13.10-1
- New upstream release with CuraEngine

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Miro Hrončok <mhroncok@redhat.com> - 13.04-2
- Remove resources directory before trying to create a symlink there

* Sat May 04 2013 Miro Hrončok <mhroncok@redhat.com> - 13.04-1
- New upstream release
- Fixed missing slice module

* Sat Apr 20 2013 Miro Hrončok <mhroncok@redhat.com> - 13.03-1
- New upstream release

* Tue Feb 19 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-3
- chmod 755 cura-stripper.sh
- Use firmware from ultimaker-marlin-firmware package
- removed bundling note

* Sun Jan 20 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-2
- Launcher is in Python now

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-1
- First version

