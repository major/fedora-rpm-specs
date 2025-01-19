# Because of the LuaJIT requirements:
%ifarch %{arm} %{ix86} x86_64 %{mips} aarch64
%global luadep luajit
%else
%global luadep lua
%endif

Name:           love
Version:        11.5
Release:        5%{?dist}
Summary:        A free 2D game engine which enables easy game creation in Lua

License:        Zlib
URL:            http://love2d.org
Source0:        https://github.com/love2d/love/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  mesa-libGL
BuildRequires:  mpg123-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  %{luadep}-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires: make
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

#The following is bundled.
#Upstream will not unbundle this code as the
#code has been modified to work better with love
#As well, it's not clear if it would be worth unbundling
#See below for the correspondence:
#https://bitbucket.org/rude/love/issues/870/allow-for-shared-version-of-libraries
Provides: bundled(Box2D) = 2.3.0
Provides: bundled(enet) = 1.3.13
#Luasocket 3.0 rc1:
Provides: bundled(luasocket) = 3.0
Provides: bundled(lz4) = 1.8.0
Provides: bundled(physfs) = 3.0.1

#Big endian systems are not yet supported by love 11+
ExcludeArch:    ppc ppc64 s390x

%description
LOVE is an open source, cross platform 2D game engine which uses the
Lua scripting language. LOVE can be used to make games of any license
allowing it to be used for both free and non-free projects.

%package -n lib%{name}
Summary:        Library for Love, A free 2D game engine

%description -n lib%{name}
This package includes the library files for LOVE.
LOVE is an open source, cross platform 2D game engine which uses the
Lua scripting language. LOVE can be used to make games of any license
allowing it to be used for both free and non-free projects.

%prep
%autosetup -p1
#Fixing line encoding:
sed -i 's/\r//' license.txt
#Fixing permissions:
chmod a-x src/libraries/*/*/*/*.* src/libraries/*/*.*

%build
platform/unix/automagic
%configure  --prefix=/usr --with-lua=%{luadep} --enable-static=no
%make_build

%install
%make_install
#Check Desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
#This seems to be built, despite disabling static libraries
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%ldconfig_scriptlets

%ldconfig_scriptlets -n lib%{name}

%files
%doc changes.txt readme.md
%license license.txt
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-%{name}-game.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.*

%files -n lib%{name}
%doc changes.txt readme.md
%license license.txt
#Note that liblove.so is just a symlink, so a devel package is useless
%{_libdir}/lib%{name}*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 4 2023 Jeremy Newton <alexjnewt AT hotmail DOT com> - 11.5-1
- Update to 11.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Jeremy Newton <alexjnewt AT hotmail DOT com> - 11.4-1
- Update to 11.4
- PPC64le doesn't appear to have a luajit anymore, switch to lua

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> - 11.3-1
- Update to 11.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> - 11.2-1
- Update to 11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Jeremy Newton <alexjnewt AT hotmail DOT com> - 11.1-1
- Update to 11.1

* Thu May 03 2018 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.2-12
- Update bundle info
- Cleanup build requires

* Sat Mar 17 2018 Jeremy Newton <alexjnewt AT hotmail DOT com>
- Disable PPC64le for builds prior to f28

* Thu Mar 15 2018 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.2-11
- Enable PPC64le

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.2-9
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.2-6
- Cherry-pick upstream luajit patch

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.2-3
- Bump and build

* Sat Nov 12 2016 Jeremy Newton <alexjnewt AT hotmail DOT com>
- Enable mp3 support

* Tue Nov 8 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.2-2
- Add mips and aarch64 as supported by luajit
- Excluding ppc64le as it's broken for now

* Mon Nov 7 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.2-1
- Update to new version
- Use lua instead lua-git on unsupported platforms

* Fri Sep 16 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.10.1-3
- LuaJIT on aarch64 for 2.1.0 and later

* Mon Aug 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.10.1-2
- Rebuild for LuaJIT 2.1.0

* Sun Aug 21 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.1-1
- Update to new version

* Sat Aug 20 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.10.0-3
- Make exclusive arch to those supported by LuaJIT

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 1 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.10.0-1
- Update to new version
- Update provides to include bundling

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.9.2-1
- Update to 0.9.2

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 12 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.9.1-1
- Update to 0.9.1

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-5
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 5 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.9.0-2
- Use repo version, fixes opengl issue

* Wed Jan 1 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.9.0-1
- New upstream 0.9.0
- Removed all patches/sources (all fixed in 0.9.0)
- Add disable-mpg123 flag and enable-static=no
- Split into 2 packages, love and liblove

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 3 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.8.0-2
- Fixed a typo in the manpage
- Fixed minor typo in files

* Tue Apr 3 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.8.0-1
- Updated spec for new upstream version

* Wed Mar 28 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.7.2-3
- Added man page
- Made more use of the name macro
- Removed unnecessary build flags
- Fixed typo in changelog

* Tue Mar 27 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.7.2-2
- Added missing build dependencies

* Tue Mar 6 2012 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.7.2-1
- Initial Package
