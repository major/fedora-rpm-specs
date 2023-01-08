# Required for the plugin directory name, see https://github.com/OpenImageIO/oiio/issues/2583
%global oiio_major_minor_ver %(rpm -q --queryformat='%%{version}' OpenImageIO-devel | cut -d . -f 1-2)
#%%global prerelease -RC1
%bcond_without  qt5

Name:           openshadinglanguage
Version:        1.12.8.0
Release:        %autorelease
Summary:        Advanced shading language for production GI renderers
License:        BSD-3-Clause
URL:            https://github.com/AcademySoftwareFoundation/OpenShadingLanguage
Source:        %{url}/archive/v%{version}/OpenShadingLanguage-%{version}%{?prerelease}.tar.gz

# Required for %%autosetup -S git, which in turn is required to use a patch
# from git containing a binary diff.
BuildRequires:  git-core

BuildRequires:  bison >= 2.7
BuildRequires:  boost-devel >= 1.55
BuildRequires:  clang-devel >= 3.4
BuildRequires:  cmake >= 3.12
BuildRequires:  flex >= 2.5.35
BuildRequires:  gcc-c++ >= 6.1
BuildRequires:  llvm-devel >= 9
# Needed for OSL pointclound functions
BuildRequires:  partio-devel
BuildRequires:  pkgconfig(Imath) >= 2.3
BuildRequires:  pkgconfig(OpenImageIO) >= 2.3
BuildRequires:  pkgconfig(pugixml)

# For osltoy
BuildRequires:  pkgconfig(Qt5) >= 5.6
BuildRequires:  pkgconfig(zlib)

# 64 bit only
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

%description
Open Shading Language (OSL) is a small but rich language for programmable
shading in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package doc
Summary:        Documentation for OpenShadingLanguage
License:        CC-BY
BuildArch:      noarch
Requires:       %{name} = %{version}

%description doc
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.
This package contains documentation.

%package example-shaders-source
Summary:        OSL shader examples
License:        BSD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-common-headers

%description example-shaders-source
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains some OSL example shaders.

%package common-headers
Summary:        OSL standard library and auxiliary headers
License:        BSD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description common-headers
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the OSL standard library headers, as well
as some additional headers useful for writing shaders.

%package -n OpenImageIO-plugin-osl
Summary:        OpenImageIO input plugin
License:        BSD

%description -n OpenImageIO-plugin-osl
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This is a plugin to access OSL from OpenImageIO.

%package        libs
Summary:        OpenShadingLanguage's libraries
License:        BSD

%description    libs
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.


%package        devel
Summary:        Development files for %{name}
License:        BSD
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python3-%{name}
Summary:        %{summary}
License:        BSD
BuildRequires:  cmake(pybind11)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)

%description    -n python3-%{name}
%{description}

%prep
%autosetup -p1 -n OpenShadingLanguage-%{version}%{?prerelease} -S git
# Use python3 binary instead of unversioned python
sed -i -e "s/COMMAND python/COMMAND python3/" $(find . -iname CMakeLists.txt)

%build
%cmake \
   -DCMAKE_CXX_STANDARD=17 \
   -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
   -DCMAKE_SKIP_RPATH=TRUE \
   -DCMAKE_SKIP_INSTALL_RPATH=YES \
   -DLLVM_STATIC=0 \
   -DOSL_SHADER_INSTALL_DIR:PATH=%{_datadir}/%{name}/shaders/ \
   -Dpartio_DIR=%{_prefix} \
   -DPARTIO_INCLUDE_DIR=%{_includedir} \
   -DPARTIO_LIBRARIES=%{_libdir}/libpartio.so \
   -DPYTHON_VERSION=%{python3_version} \
   -DSTOP_ON_WARNING=OFF 
%cmake_build

%install
%cmake_install

# Move the OpenImageIO plugin into its default search path
mkdir %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}
mv %{buildroot}%{_libdir}/osl.imageio.so %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/

%files
%license LICENSE.md
%doc CHANGES.md CONTRIBUTING.md README.md
%{_bindir}/oslc
%{_bindir}/oslinfo
%if %{with qt5}
%{_bindir}/osltoy
%endif
%{_bindir}/testrender
%{_bindir}/testshade
%{_bindir}/testshade_dso

%files doc
%doc %{_docdir}/%{name}/

%files example-shaders-source
%{_datadir}/%{name}/shaders/*.osl
%{_datadir}/%{name}/shaders/*.oso

%files common-headers
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shaders
%{_datadir}/%{name}/shaders/*.h

%files -n OpenImageIO-plugin-osl
%license LICENSE.md
%dir %{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/
%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/osl.imageio.so
   
%files libs
%license LICENSE.md
%{_libdir}/libosl*.so.1*
%{_libdir}/libtestshade.so.1*

%files devel
%{_includedir}/OSL/
%{_libdir}/libosl*.so
%{_libdir}/libtestshade.so
%{_libdir}/cmake/
%{_libdir}/pkgconfig/

%files -n python3-%{name}
%{python3_sitearch}/oslquery.so

%changelog
%autochangelog
