%global	commit0 0a182c13556bc46424e32083559e2ff6784c17ac
%global	commit1 943be3f2a3f26a6b1bbde944347921c85a98af3d
#%%global	shortcommit0 %%(c=%%{commit0}; echo ${c:0:7})
#%%global	shortcommit1 %%(c=%%{commit1}; echo ${c:0:7})
%global	snapshot 0
#%%global	date 20190819
%global	yname yafaray
#%%global	prerelease beta

# [Fedora] Turn off the brp-python-bytecompile script 
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		YafaRay
License:	LGPLv2+
Summary:	A free open-source ray-tracing render engine
Version:	3.5.1
URL:		https://www.yafaray.org/
Release:	24%{?prerelease}%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}

%{?shortcommit0:
Source0:	https://github.com/%{name}/lib%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz}
%{!?shortcommit0:
Source0:	https://github.com/%{name}/lib%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz}

%{?shortcommit1:
Source1:	https://github.com/%{name}/%{name}-Blender/archive/%{commit1}.tar.gz#/YafaRay-blender-%{shortcommit1}.tar.gz}
%{!?shortcommit1:
Source1:	https://github.com/%{name}/%{name}-Blender/archive/v%{version}.tar.gz#/%{name}-blender-%{version}.tar.gz}

Source2:	yafaray-blender.metainfo.xml

Patch0:         YafaRay-gcc11.patch
# As of OpenEXR 3 upstream has significantly reorganized the libraries
# including splitting out imath as a standalone library (which this project may
# or may not need). Please see
# https://github.com/AcademySoftwareFoundation/Imath/blob/master/docs/PortingGuide2-3.md
# for porting details and encourage upstream to support it.
# Minimal patch to port to OpenEXR 3.
Patch1:         YafaRay-openexr3.patch
# Add missing includes needed by gcc 13
Patch2:         YafaRay-include.patch

BuildRequires:	blender-rpm-macros
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	gcc-c++
#BuildRequires:	git
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(OpenEXR) >= 1.2 
BuildRequires:	pkgconfig(Qt5)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	swig


Requires:	%{name}%{?_isa} = %{version}-%{release}
# Set exclusive arch
# https://koji.fedoraproject.org/koji/taskinfo?taskID=17920427
ExclusiveArch:	%{ix86} x86_64

%description
YafaRay is a free open-source ray-tracing render engine. Ray-tracing is a
rendering technique for generating realistic images by tracing the path of
light through a 3D scene. A render engine consists of a "faceless" computer
program that interacts with a host 3D application to provide very specific
ray-tracing capabilities "on demand". Blender 3D is the host application of
YafaRay.

%package	lib
Summary:	Libraries for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	lib
%{name} is a free open-source ray-tracing render engine. Ray-tracing is a
rendering technique for generating realistic images by tracing the path of
light through a 3D scene. A render engine consists of a "faceless" computer
program that interacts with a host 3D application to provide very specific
ray-tracing capabilities "on demand". Blender 3D is the host application of
%{name}.

This package contains the program libraries.

%package	blender
Summary:	Blender integration scripts for %{name}
Requires:	blender
Obsoletes:	%{yname}-blender < 0.1.1-4
Provides:	%{yname}-blender = %{version}-%{release}

%description	blender
%{name} is a free open-source ray-tracing render engine. Ray-tracing is a
rendering technique for generating realistic images by tracing the path of
light through a 3D scene. A render engine consists of a "faceless" computer
program that interacts with a host 3D application to provide very specific
ray-tracing capabilities "on demand". Blender 3D is the host application of
%{name}.

%{name} uses a python-coded settings interface to set lighting and rendering
parameters. This settings interface is launched by an entry automatically
added to the Blender Render menu.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}-lib%{?_isa} = %{version}-%{release}

%description    devel
%{name} is a free open-source ray-tracing render engine. Ray-tracing is a
rendering technique for generating realistic images by tracing the path of
light through a 3D scene. A render engine consists of a "faceless" computer
program that interacts with a host 3D application to provide very specific
ray-tracing capabilities "on demand". Blender 3D is the host application of
%{name}.

The %{name}-devel package contains libraries and header files for applications
that use %{name}.

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name} 
The python3-%{name} package contains Python 3 bindings for %{name}.

%prep
%if %{?snapshot}
%autosetup -D -n lib%{name}-%{commit0}
%autosetup -D -T -a 1 -n lib%{name}-%{commit0}

#Fix syntax for python 3.5+ declaration
sed -i 's|metaclass=RNAMeta|metaclass.RNAMeta|' %{name}-Blender-%{commit1}/ot/%{yname}_presets.py
%else
%autosetup -p1 -D -n lib%{name}-%{version}
%autosetup -N -D -T -a 1 -n lib%{name}-%{version}

#Fix syntax for python 3.5+ declaration
sed -i 's|metaclass=RNAMeta|metaclass.RNAMeta|' %{name}-Blender-%{version}/ot/%{yname}_presets.py

%endif


sed -i -e 's|set(YAF_LIB_DIR lib)|set(YAF_LIB_DIR %{_lib})|g' CMakeLists.txt
sed -i -e 's|set(YAF_TARGET_TYPE ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/lib RUNTIME)|\
    set(YAF_TARGET_TYPE ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}%{_lib} RUNTIME)|g' CMakeLists.txt

# Set proper permission per packaging guideline
find . -name "*.h" -exec chmod 644 {} \;
find . -name "*.c" -exec chmod 644 {} \;
find . -name "*.cc" -exec chmod 644 {} \;

%build
%cmake \
	-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=true \
	-DCMAKE_SKIP_RPATH:BOOL=true \
	-DDEBUG_BUILD=ON \
	-DWITH_QT=ON \
	-DUSER_DBGFLAGS="%{optflags}" \
	-DYAF_PY_VERSION="%{python3_version}" \
	-DYAF_BINDINGS_PY_DIR="%{python3_sitearch}" \
	%{nil}

%cmake_build


%install
%cmake_install


# Let RPM pick docs in the file section
rm -fr %{buildroot}%{_docdir}/%{yname}

# Install add-on on Blender directory
mkdir -p %{buildroot}%{blender_addons}/%{yname}

%if %{snapshot}
cp -pR %{name}-Blender-%{commit1}/* \
  %{buildroot}%{blender_addons}/%{yname}
%else
cp -pR %{name}-Blender-%{version}/* \
  %{buildroot}%{blender_addons}/%{yname}
%endif


# AppData
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_metainfodir}/%{yname}-blender.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{yname}-blender.metainfo.xml


%files
%license LICENSES
%doc AUTHORS.md CHANGELOG.md README.md
%{_bindir}/%{yname}-xml
%{_datadir}/%{yname}/*

%files lib
%{_libdir}/%{yname}-plugins
%{_libdir}/*.so
%{_libdir}/libyafarayqt.so

%files devel
%{_includedir}/%{yname}/

%files blender
%license LICENSES
%{_metainfodir}/%{yname}-blender.metainfo.xml
%{blender_addons}/%{yname}/*

%files -n python3-%{name}
%{python3_sitearch}/*.{py,so}

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Python Maint <python-maint@redhat.com> - 3.5.1-23
- Rebuilt for Python 3.12

* Mon Feb 13 2023 Orion Poplawski <orion@nwra.com> - 3.5.1-22
- Add patch to add needed include for gcc 13

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 3.5.1-20
- Rebuild for opencv 4.7.0

* Mon Sep 12 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-19
- Rebuild for blender 3.3.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 3.5.1-17
- Rebuilt for opencv 4.6.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.5.1-16
- Rebuilt for Python 3.11

* Thu Jun 9 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-15
- Rebuild for blender 3.2.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 Richard Shaw <hobbes1069@gmail.com> - 3.5.1-13
- Add patch for OpenEXR 3.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Michael J Gruber <mjg@fedoraproject.org> - 3.5.1-11
- fix spec description

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5.1-10
- Rebuilt for Python 3.10

* Thu Jun 3 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-9
- Rebuild for blender 2.93.0

* Fri Feb 26 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-8
- Rebuild for blender 2.92.0

* Sun Feb 07 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-7
- Update url for upstream new github repository
- Update renamed sources from upstream

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-5
- Rebuild for Blender 2.91.2

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-4.2
- rebuild against New OpenEXR properly

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.5.1-4.1
- Rebuild for OpenEXR 2.5.3.

* Sat Nov 28 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-4
- Rebuild for Blender 2.91

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.5.1-3.1
- Rebuilt for OpenCV

* Mon Oct 12 2020 Jeff Law <law@redhat.com> - 3.5.1-3
- Add missing #include for gcc-11

* Sat Sep 05 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-2
- Rebuild for Blender 2.90

* Sat Aug 29 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1 (#1855915)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0 (#1855915)

* Fri Jun 26 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.4-3
- Rebuild for Blender 2.83.1

* Mon Jun 08 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.4-2
- Rebuilt for Blender 2.83.0

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.4.4-1.3
- Rebuilt for OpenCV 4.3

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 3.4.4-1.2
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.4-1.1
- Rebuilt for Python 3.9

* Sat May 09 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.4-1
- Update to 3.4.4 (#1822412)

* Sat Apr 11 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1 (#1822412)

* Sat Mar 28 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Sun Mar 15 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-33.20190819git0a182c1
- Rebuild for blender 2.82a

* Fri Feb 21 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-32.20190819git0a182c1
- Rebuilt for blender 2.8.2

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.3.0-31.20190819git0a182c1
- Rebuild for OpenCV 4.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-30.20190819git0a182c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 3.3.0-29.20190819git0a182c1
- Rebuilt for opencv4

* Thu Dec 12 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-28.20190819git0a182c1
- Rebuilt for openvdb 7.0.0

* Fri Dec 06 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-27.20190819git0a182c1
- Rebuild for blender 2.81a

* Sat Nov 23 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-26.20190819git0a182c1
- Rebuild for blender 2.81

* Sun Nov 03 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-25.20190819git0a182c1
- Rebuilt for alembic 1.7.12 on blender

* Sat Aug 24 2019 Simone Caronni <negativo17@gmail.com> - 3.3.0-24.20190819git0a182c1
- Use packaging guidelines format for package release.

* Sat Aug 24 2019 Simone Caronni <negativo17@gmail.com> - 3.3.0-23.20190819git
- Update to latest Core snapshot.
- Add devel subpackage.
- Fix descriptions.
- Use _metainfodir macro.
- Move license in the libraries subpackage, as this is always installed.
- Fix build flags, debug package so binaries are stripped.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-22.20190223git
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-21
- Rebuild for blender 2.80
- Rebuild for embree 3.6.0 beta

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-19.20190223git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-18
- Append Python3 declaration on cmake invocation

* Fri Apr 12 2019 Richard Shaw <hobbes1069@gmail.com> - 3.3.0-17
- Rebuild for OpenEXR 2.3.0.

* Thu Mar 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-16
- Rebuild for updated blender

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 3.3.0-15
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 3.3.0-14
- Append curdir to CMake invokation. (#1668512)

* Fri Nov 02 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-13
- Rebuilt for blender

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-11
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-10
- Actually rebuild for blender 2.78b

* Thu Mar 29 2018 Luya Tshimbalanaga <luya@fedoraproject.org> - 3.3.0-9
- Rebuild for blender-2.79b

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 3.3.0-8
- Rebuild for opencv soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-6
- Rebuild for embree-3.0.0-beta.0

* Fri Jan 19 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-5
- Rebuilt for embree 2.12.2

* Thu Dec 28 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-4
- Rebuild for OpenCV

* Thu Sep 14 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-3
- bump

* Wed Sep 13 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 3.3.0-2
- Rebuild for Blender 2.79

* Wed Aug 23 2017 Luya Tshimbalanga <releng@fedoraproject.org> - 3.3.0-4
- Update to 3.3.0
- Set enabled blender addon

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 3.2.0-2
- Rebuilt for Boost 1.64

* Fri May 26 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.2.0-1
- Upstream update

* Fri Apr 28 2017 Simone Caronni <negativo17@gmail.com> - 3.2.0-0.7.20170221git
- Rebuild for OpenCV 3.2.0 update.

* Sat Feb 25 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.2.0-0.6.20170221git
- Enable preset
- Change upstream url

* Wed Feb 22 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.2.0-0.5.20170221git
- Latest git snapshot

* Fri Feb 17 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.2.0-0.4.20170217git
- Latest git snapshot
- Fix spelling to adhere US spelling guideine
- Fix license
- Fix mixed use of spaces and tab errors
- Set source files non executables

* Mon Feb 13 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.2.0-0.3.20170212git
- Add conditional statement for release line
- Align description to 80 columns as possible
- Disable rpath per Fedora packaging guideline
- Let RPM pick docs in the file section
- Add missing requirement libappstream-glib
- Temporarily disable preset in yafaray-blender

* Sun Feb 12 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.2.0-0.2.20170212git
- Latest git snapshot
- Add libtiff dependency
- Use versioning from Fedora packaging guideline
- Define sources url

* Wed Feb 08 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.2.0-0.1.20170131git
- Move appdata to its own file
- Latest git snapshot
- Use POSITION_INDEPENDENT_CODE to prevent compilation error
- Fix library path

* Thu Jan 12 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 3.1.1-0.2.beta
- Fixed changelog by including missing upstream update info
- Fixed url for the sources
- Added requirement for base package
- Fix lib sharing, relic for legacy method
- Further cleaned up spec

* Thu Sep 22 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 3.0.0-0.1.beta
- Update to 3.1.1-beta

* Sat Jul 16 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 3.0.0-0.1.beta
- Update to 3.0.0-beta
- Cleaned up spec file
- Dropped scons as dependency

* Tue Mar 08 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.1.1-14
- Fix FTBFS with GCC 6 (#1307303)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-10
- rebuild (openexr)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-8
- rebuild (OpenEXR)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
