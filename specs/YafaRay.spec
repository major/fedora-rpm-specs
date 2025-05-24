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
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
Summary:	A free open-source ray-tracing render engine
Version:	3.5.1
URL:		https://www.yafaray.org/
Release:	%autorelease

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
# Note: Cannot use ninja with swig apparently
# ninja: error: build.ninja:4216: multiple rules generate src/bindings/yafaray_v3_interface.py
%global _cmake_generator "Unix Makefiles"
BuildRequires:	make
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
# TODO: Remove in the next release
export CMAKE_POLICY_VERSION_MINIMUM=3.5
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
mkdir -p %{buildroot}%{blender_extensions}/%{yname}

%if %{snapshot}
cp -pR %{name}-Blender-%{commit1}/* \
  %{buildroot}%{blender_extensions}/%{yname}
%else
cp -pR %{name}-Blender-%{version}/* \
  %{buildroot}%{blender_extensions}/%{yname}
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
%{blender_extensions}/%{yname}/*

%files -n python3-%{name}
%{python3_sitearch}/*.{py,so}

%changelog
%autochangelog
