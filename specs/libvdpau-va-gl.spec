Name:           libvdpau-va-gl
Version:        0.4.2
Release:        29%{?dist}
Summary:        VDPAU driver with OpenGL/VAAPI back-end

License:        MIT
URL:            https://github.com/i-rinat/libvdpau-va-gl
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(gl)

#As per https://fedorahosted.org/council/ticket/61
#libva-intel-driver can use supplement/enhance
#Requires: libva-intel-driver%%{?_isa}



%description
VDPAU driver with OpenGL/VAAPI back-end.


%prep
%autosetup


%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DLIB_INSTALL_DIR=%{_libdir}/vdpau \

%cmake_build


%install
%cmake_install


%files
%doc ChangeLog README.md
%license LICENSE
%{_libdir}/vdpau/libvdpau_va_gl.so.1
#VDPAU only dlopen the versioned so
%exclude %{_libdir}/vdpau/libvdpau_va_gl.so



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-24
- rebuilt

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-18
- rebuilt

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-15
- Rebuilt for libva-2.7.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-13
- Rebuilt for libva-2.6.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-10
- Rebuilt for libva-2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-7
- Rebuilt for libva-2.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-4
- Rebuild for vaapi 0.40

* Tue Jan 17 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-3
- Drop ExclusiveArch
- Add comment about why to drop un-versioned symlink
- Add missing BR

* Tue Nov 08 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-2
- Fixup License and libtool deletion

* Wed Oct 12 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-1
- Update to 0.4.2
- Add %%{?_isa} to Requires libva-intel-driver
- Use %%make_build macro

* Tue Aug 30 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-1
- Update to 0.4.0
- Drop compat symlink

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.3.6-2
- Rebuilt for ffmpeg-3.1.1

* Sun May 22 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.3.6-1
- Update to 0.3.6

* Sun Jan 04 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-6
- Fix asserts in release package - rfbz#3419

* Tue Nov 04 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-5
- Rebuilt for vaapi 0.36

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.3.4-4
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-3
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.3.4-2
- Rebuilt for ffmpeg-2.3

* Sat Apr 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-1
- Update to 0.3.4

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 0.3.2-2
- Rebuilt for ffmpeg-2.2

* Sun Jan 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Tue Nov 19 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Thu Jul 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-1
- Initial spec file

