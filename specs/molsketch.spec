Name:           molsketch
Version:        0.8.1
Release:        4%{?dist}
Summary:        Molecular Structures Editor
License:        GPL-2.0-or-later
URL:            http://molsketch.sourceforge.net
# Mask while using test builds
Source0:        https://downloads.sourceforge.net/molsketch/Molsketch-%{version}-src.tar.gz
# Mask for regular builds
#Source0:        https://downloads.sourceforge.net/molsketch/Molsketch-latest-src.tar.gz
# Alternative upstream repository for testing
# Source0:        https://github.com/hvennekate/Molsketch/archive/master/Molsketch-main.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  kdelibs-devel
BuildRequires:  openbabel-devel
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       openbabel%{?_isa}


%description
Molsketch is a 2D molecular editing tool. Its goal is to help you draw
molecules quickly and easily. Of course your creation can be exported
afterwards in high quality, in a number of vector and bitmap formats.



%package doc
Summary:        Documentation files for %{name}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
BuildArch:      noarch


%description doc
%{summary}.



%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qttools-devel


%description 	devel
2D molecular structures editor.

This package contains header files and libraries needed to develop
applications that use %{name}.



# Regular builds:
#%%setup -q -n Molsketch-%%{version}
# Test buids:
#%%setup -q -n Molsketch-latest (or Molsketch-master)
# "-c" needed in v0.7.3 because of missing top-level dir
%prep
%setup -q -n Molsketch-%{version}


%build
%cmake -DMSK_PREFIX=%{_prefix} -DMSK_QT6=true
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license COPYING
%doc CHANGELOG
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}*.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/*


%files doc
%license COPYING
%{_docdir}/%{name}


%files devel
%{_includedir}/lib%{name}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 25 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Mon Feb 19 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.8.0-6^20240218git66afe01
- 0.8.1 pre-release version
- Fix structure scaling bug

* Sun Feb 18 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.8.0-5^20240217git3cef8a2
- 0.8.1 pre-release version
- Switch to cmake

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 14 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.8.0-1
- New version with additional dark icons and a fix for upstream issue #37
- Switched to Qt6 
- Removed dos2unix invocation and BR

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.7.3-1
- Several bugfixes

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.7.2-3
- Rebuild for Open Babel 3.1.x 

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.7.2-1
- Fix problem with new library name
- Remove symbolic link to library (temporary workaround)

* Mon Mar 08 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.7.1-1
- Bugfix release
- Dropped Qt4 support

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.7.0-1
- New release
- Add qt5-linguist BR

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.6.0-1
- New release with overhauled drawing system and several bugfixes

* Sun Feb 03 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.2-3
- Bugfix release with some new features

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.2-1
- Code and license clean-up, version bump

* Mon Jul 16 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-13
- Refactored hovering and object selection mechanics
- Option to show/hide terminal methyl groups

* Tue Jun 19 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-12
- Interface improvements and more drawing functions

* Sun Jun 17 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-11
- Improvements in drawing functions

* Tue Jun 12 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-10
- UI and drawing improvements

* Sun Jun 10 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-9
- Incremental improvements over the previous version and bugfixes

* Mon May 21 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-8
- Pre-release version with new and improved scene and global drawing settings

* Sun Feb 11 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-7
- New release
- Remove headers patch
- Remove obsolete Group tag

* Fri Feb 09 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-6
- New bugfix release
- Patch by Antonio Trante to install all header files in devel subpackage
- Some more corrections

* Wed Feb 07 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-5
- New version with refactored installation
- Use ldconfig scriptlets

* Mon Jan 22 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-4
- More cleaning up 

* Mon Jan 22 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-3
- Clean up spec file according to remarks by Antonio Trande (rhbz#1536852)

* Sun Jan 21 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-2
- Remove obsolete scriptlets
- AppData changes merged upstream

* Fri Jan 05 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.1-1
- New version
- Remove conditional for AppData on F25

* Tue Dec 05 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-8
- Add conditional for AppData on F25

* Tue Dec 05 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-7
- New version with several improvements
- Add AppData XML file (submitted upstream)

* Wed Nov 01 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-6
- Fix post & postun scriptlets

* Wed Nov 01 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-5
- Fix for upstream bug #21
- Re-add xpm icon

* Tue Oct 31 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-4
- New release with modernized desktop file and mimetypes
- Move setup tasks from scriptlets to Qt project files 

* Fri Oct 13 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-3
- More bugfixes

* Wed Oct 11 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-2
- New bugfix release

* Tue Sep 26 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.5.0-1
- New version

* Wed Jun 28 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.4.1-1
- Update to newer version

* Sat Apr 02 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.3.1-1
- First release based on work by Huaren Zhong <huaren.zhong@gmail.com>
