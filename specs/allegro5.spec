# Force out of source build
%undefine __cmake_in_source_build

Name:		allegro5
Version:	5.2.7
Release:	11%{?dist}
Summary:	A game programming library
License:	zlib
URL:		http://liballeg.org/
Source0:	https://github.com/liballeg/allegro5/releases/download/%{version}.0/allegro-%{version}.0.tar.gz
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel cmake dumb-devel flac-devel freetype-devel
BuildRequires:	gtk3-devel libICE-devel libjpeg-devel libpng-devel
BuildRequires:	libtheora-devel libvorbis-devel libXcursor-devel
BuildRequires:	libXext-devel libXxf86vm-devel libXrandr-devel
BuildRequires:	libXinerama-devel libXpm-devel mesa-libGL-devel
BuildRequires:	mesa-libGLU-devel openal-soft-devel physfs-devel
BuildRequires:	pulseaudio-libs-devel opus-devel opusfile-devel libwebp-devel
BuildRequires:	freeimage-devel

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. Allegro 5 is the latest major
revision of the library, designed to take advantage of modern hardware
(e.g. hardware acceleration using 3D cards) and operating systems.
Although it is not backwards compatible with earlier versions, it still
occupies the same niche and retains a familiar style.

%package devel
Summary:	Development files for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description devel
This package is needed to build programs using the Allegro 5 library.
Contains header files and man-page documentation.

%package addon-acodec
Summary:	Audio codec addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-acodec
This package provides the audio codec addon for the Allegro 5 library.
This addon allows you to load audio sample formats.

%package addon-acodec-devel
Summary:	Header files for the Allegro 5 audio codec addon
Requires:	%{name}-addon-acodec = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-acodec-devel
This package is required to build programs that use the Allegro 5 audio
codec addon.

%package addon-audio
Summary:	Audio addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-audio
This package provides the audio addon for the Allegro 5 library. This
addon allows you to play sounds in your Allegro 5 programs.

%package addon-audio-devel
Summary:	Header files for the Allegro 5 audio addon
Requires:	%{name}-addon-audio = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-audio-devel
This package is required to build programs that use the Allegro 5 audio
addon.

%package addon-dialog
Summary:	Dialog addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-dialog
This package provides the dialog addon for the Allegro 5 library. This
addon allows you to show dialog boxes.

%package addon-dialog-devel
Summary:	Header files for the Allegro 5 dialog addon
Requires:	%{name}-addon-dialog = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-dialog-devel
This package is required to build programs that use the Allegro 5 dialog
addon.

%package addon-image
Summary:	Image addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-image
This package provides the image addon for the Allegro 5 library. Provides
support for loading image file formats.

%package addon-image-devel
Summary:	Header files for the Allegro 5 image addon
Requires:	%{name}-addon-image = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-image-devel
This package is required to build programs that use the Allegro 5 image
addon.

%package addon-physfs
Summary:	Physfs addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-physfs
This package provides the physfs addon for the Allegro 5 library. This
addon provides an interface to the PhysicsFS library, allowing you to
mount virtual file-systems (e.g., archives) and access files as if they
were physically on the file-system.

%package addon-physfs-devel
Summary:	Header files for the Allegro 5 physfs addon
Requires:	%{name}-addon-physfs = %{version}-%{release}
%description addon-physfs-devel
This package is required to build programs that use the Allegro 5 physfs
addon.

%package addon-ttf
Summary:	TTF addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-ttf
This package provides the ttf addon for the Allegro 5 library. This addon
allows you to load and use TTF fonts in your Allegro 5 programs.

%package addon-ttf-devel
Summary:	Header files for the Allegro 5 TTF addon
Requires:	%{name}-addon-ttf = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-ttf-devel
This package is required to build programs that use the Allegro 5 ttf
addon.

%package addon-video
Summary:	Video addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-video
This package provides the video addon for the Allegro 5 library. This
addon allows you to play theora videos in your Allegro 5 programs.

%package addon-video-devel
Summary:	Header files for the Allegro 5 video addon
Requires:	%{name}-addon-video = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-video-devel
This package is required to build programs that use the Allegro 5 video
addon.


%prep
%autosetup -p1 -n allegro-%{version}.0


%build
%cmake -DWANT_DOCS=OFF
%cmake_build


%install
%cmake_install

mkdir %buildroot/%{_sysconfdir}
install -p -m 644 allegro5.cfg %buildroot/%{_sysconfdir}/allegro5rc
# install man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -p -m 644 docs/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3


%ldconfig_scriptlets

%ldconfig_scriptlets addon-acodec

%ldconfig_scriptlets addon-audio

%ldconfig_scriptlets addon-dialog

%ldconfig_scriptlets addon-image

%ldconfig_scriptlets addon-physfs

%ldconfig_scriptlets addon-ttf

%ldconfig_scriptlets addon-video


%files
%config(noreplace) %{_sysconfdir}/allegro5rc
%doc CHANGES-5.?.txt CONTRIBUTORS.txt README.txt
%license LICENSE.txt
%{_libdir}/liballegro.so.5.2
%{_libdir}/liballegro.so.%{version}
%{_libdir}/liballegro_color.so.5.2
%{_libdir}/liballegro_color.so.%{version}
%{_libdir}/liballegro_font.so.5.2
%{_libdir}/liballegro_font.so.%{version}
%{_libdir}/liballegro_main.so.5.2
%{_libdir}/liballegro_main.so.%{version}
%{_libdir}/liballegro_memfile.so.5.2
%{_libdir}/liballegro_memfile.so.%{version}
%{_libdir}/liballegro_primitives.so.5.2
%{_libdir}/liballegro_primitives.so.%{version}

%files devel
%doc docs/html/refman
%{_includedir}/allegro5
%exclude %{_includedir}/allegro5/allegro_acodec.h
%exclude %{_includedir}/allegro5/allegro_audio.h
%exclude %{_includedir}/allegro5/allegro_native_dialog.h
%exclude %{_includedir}/allegro5/allegro_image.h
%exclude %{_includedir}/allegro5/allegro_physfs.h
%exclude %{_includedir}/allegro5/allegro_ttf.h
%exclude %{_includedir}/allegro5/allegro_vidio.h
%{_libdir}/liballegro.so
%{_libdir}/liballegro_color.so
%{_libdir}/liballegro_font.so
%{_libdir}/liballegro_main.so
%{_libdir}/liballegro_memfile.so
%{_libdir}/liballegro_primitives.so
%{_libdir}/pkgconfig/allegro-5*.pc
%{_libdir}/pkgconfig/allegro_color-5*.pc
%{_libdir}/pkgconfig/allegro_font-5*.pc
%{_libdir}/pkgconfig/allegro_main-5*.pc
%{_libdir}/pkgconfig/allegro_memfile-5*.pc
%{_libdir}/pkgconfig/allegro_primitives-5*.pc
%{_mandir}/man3/ALLEGRO_*.3*
%{_mandir}/man3/al_*.3*

%files addon-acodec
%{_libdir}/liballegro_acodec.so.5.2
%{_libdir}/liballegro_acodec.so.%{version}

%files addon-acodec-devel
%{_includedir}/allegro5/allegro_acodec.h
%{_libdir}/liballegro_acodec.so
%{_libdir}/pkgconfig/allegro_acodec-5*.pc

%files addon-audio
%{_libdir}/liballegro_audio.so.5.2
%{_libdir}/liballegro_audio.so.%{version}

%files addon-audio-devel
%{_includedir}/allegro5/allegro_audio.h
%{_libdir}/liballegro_audio.so
%{_libdir}/pkgconfig/allegro_audio-5*.pc

%files addon-dialog
%{_libdir}/liballegro_dialog.so.5.2
%{_libdir}/liballegro_dialog.so.%{version}

%files addon-dialog-devel
%{_includedir}/allegro5/allegro_native_dialog.h
%{_libdir}/liballegro_dialog.so
%{_libdir}/pkgconfig/allegro_dialog-5*.pc

%files addon-image
%{_libdir}/liballegro_image.so.5.2
%{_libdir}/liballegro_image.so.%{version}

%files addon-image-devel
%{_includedir}/allegro5/allegro_image.h
%{_libdir}/liballegro_image.so
%{_libdir}/pkgconfig/allegro_image-5*.pc

%files addon-physfs
%{_libdir}/liballegro_physfs.so.5.2
%{_libdir}/liballegro_physfs.so.%{version}

%files addon-physfs-devel
%{_includedir}/allegro5/allegro_physfs.h
%{_libdir}/liballegro_physfs.so
%{_libdir}/pkgconfig/allegro_physfs-5*.pc

%files addon-ttf
%{_libdir}/liballegro_ttf.so.5.2
%{_libdir}/liballegro_ttf.so.%{version}

%files addon-ttf-devel
%{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/liballegro_ttf.so
%{_libdir}/pkgconfig/allegro_ttf-5*.pc

%files addon-video
%{_libdir}/liballegro_video.so.5.2
%{_libdir}/liballegro_video.so.%{version}

%files addon-video-devel
%{_includedir}/allegro5/allegro_video.h
%{_libdir}/liballegro_video.so
%{_libdir}/pkgconfig/allegro_video-5*.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.2.7-5
- Rebuilt for flac 1.4.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul  7 2021 Hans de Goede <hdegoede@redhat.com> - 5.2.7-1
- New upstream release 5.2.7
- Fixes rhbz#1979675

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Hans de Goede <hdegoede@redhat.com> - 5.2.4-2
- Switch to upstream's version of the FTBFS fix

* Sun Feb 17 2019 Hans de Goede <hdegoede@redhat.com> - 5.2.4-1
- New upstream release 5.2.4 (rhbz#1510456)
- Fix FTBFS (rhbz#1674642)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 21 2016 Hans de Goede <hdegoede@redhat.com> - 5.2.0-1
- New upstream release 5.2.0

* Mon Feb 29 2016 Hans de Goede <hdegoede@redhat.com> - 5.0.11-1
- New upstream release 5.0.11 (rhbz#1312588)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 5.0.3-7
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 5.0.3-6
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec  9 2011 Tom Callaway <spot@fedoraproject.org> - 5.0.3-3
- fix for png15

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 5.0.3-2
- Rebuild for new libpng

* Thu Jul 07 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.3-1
- Updating to 5.0.3.

* Mon May 09 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.0-4
- From Dan Horák to fix #703154.
- Explicitly disabled documentation generation.
- Use prebuilt man pages
- Added HTML reference manual.

* Wed Mar 09 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.0-3
- Adding file permissions to subpackages.
- Moving devel files (namely .so symlinks) to devel packages.
- Added %%doc section proper; readmes, changes, license, etc.
- Fixed SF.net URI.
- Modified BuildRequires.
- Added main devel dependency to subpackage devels.
- Replaced many al_*.3* manpage files with a glob.
- Replaced many header files with directory and %%exclude macros.
- Added allegro5.cfg file under /etc/allegro5rc.

* Fri Mar 04 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.0-2
- Merged primitives addon packages into core packages.
- Merged memfile addon packages into core packages.
- Merged "main" addon packages into core packages.
- Merged font packages into core packages.
- Merged color packages into core packages.
- Merged doc package into the devel package.
- Fixed spelling mistakes.
- Removed explicit library dependencies.

* Fri Feb 25 2011 Brandon McCaig <bamccaig@gmail.com> 5.0.0-1
- Initial version.

