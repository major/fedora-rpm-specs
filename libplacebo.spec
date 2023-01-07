#global prerelease -rc1

Name:           libplacebo
Version:        5.229.2
Release:        1%{?dist}
Summary:        Reusable library for GPU-accelerated video/image rendering primitives

License:        LGPLv2+
URL:            https://github.com/haasn/libplacebo
Source0:        %{url}/archive/v%{version}%{?prerelease}/%{name}-%{version}%{?prerelease}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  glad2 >= 2.0.0
BuildRequires:  lcms2-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libunwind-devel
BuildRequires:  libshaderc-devel >= 2018.0-1
BuildRequires:  python3-mako
BuildRequires:  vulkan-devel
BuildRequires:  glslang-devel


%description
libplacebo is essentially the core rendering algorithms and ideas of
mpv turned into a library. This grew out of an interest to accomplish
the following goals:

- Clean up mpv's internal API and make it reusable for other projects.
- Provide a standard library of useful GPU-accelerated image processing
  primitives based on GLSL, so projects like VLC or Firefox can use them
  without incurring a heavy dependency on `libmpv`.
- Rewrite core parts of mpv's GPU-accelerated video renderer on top of
  redesigned abstractions. (Basically, I wanted to eliminate code smell
  like `shader_cache.c` and totally redesign `gpu/video.c`)


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}%{?prerelease}


%build
%meson \
 -Dd3d11=disabled \
 -Ddemos=False

%meson_build


%install
%meson_install


%ldconfig_scriptlets


%files
%license LICENSE
%doc README.md
%{_libdir}/libplacebo.so.229

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libplacebo.pc


%changelog
* Thu Jan 05 2023 Nicolas Chauvet <kwizart@gmail.com> - 5.229.2-1
- Update to 5.229.2

* Thu Nov 03 2022 Nicolas Chauvet <kwizart@gmail.com> - 5.229.1-1
- Update to 5.229.1

* Tue Oct 18 2022 Nicolas Chauvet <kwizart@gmail.com> - 5.228.0-1
- Update to 5.228.0

* Wed Aug 10 2022 Nicolas Chauvet <kwizart@gmail.com> - 4.208.0-1
- Update to 4.208.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.208.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Nicolas Chauvet <kwizart@gmail.com> - 4.208.0-0.1.rc1
- Update to 4.208.0-rc1

* Thu Feb 03 2022 Nicolas Chauvet <kwizart@gmail.com> - 4.192.1-1
- Update to 4.192.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.192.0-1.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Nicolas Chauvet <kwizart@gmail.com> - 4.192.0~rc1-1
- Update to 4.192.0-rc1

* Tue Oct 05 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.157.0-1
- Update to 4.157.0 (final)

* Thu Aug 19 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.157.0-0.1.rc1
- Update to 4.157.0-rc1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.120.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 08 2021 Nicolas Chauvet <kwizart@gmail.com> - 3.120.3-1
- Update to 3.120.3

* Mon Apr 19 2021 Nicolas Chauvet <kwizart@gmail.com> - 3.120.2-1
- Update to 3.120.2

* Tue Apr 06 2021 Nicolas Chauvet <kwizart@gmail.com> - 3.120.1-1
- Update to 3.120.1

* Thu Apr 01 2021 Nicolas Chauvet <kwizart@gmail.com> - 3.120.0-1
- Update to 3.120.0

* Tue Feb 09 2021 Nicolas Chauvet <kwizart@gmail.com> - 3.104.0-1
- Update to 3.104.0

* Thu Jan 28 2021 Leigh Scott <leigh123linux@gmail.com> - 2.72.2-1
- Update to 2.72.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.72.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Leigh Scott <leigh123linux@gmail.com> - 2.72.0-1
- Update to 2.72.0

* Sat Feb 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1.29.1-1
- Update to 1.29.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.21.0-1
- Update to 1.21.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.18.0-2
- Rebuild with Meson fix for #1699099

* Sat Apr 06 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.18.0-1
- Update to 1.18.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-2
- Drop WAR patch
- Enforce the shaderc version

* Mon Oct 01 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-2
- Fix build on EL7

* Mon Feb 12 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-1
- Initial spec file
