# Required for the plugin directory name, see https://github.com/OpenImageIO/oiio/issues/2583
%global oiio_major_minor_ver %(rpm -q --queryformat='%%{version}' OpenImageIO-devel | cut -d . -f 1-2)
#%%global prerelease -RC1
%bcond_without	materialx
%bcond_without  qt5

Name:           openshadinglanguage
Version:        1.11.17.0
Release:        %autorelease
Summary:        Advanced shading language for production GI renderers
License:        BSD
URL:            https://github.com/imageworks/OpenShadingLanguage
Source0:        %{url}/archive/Release-%{version}%{?prerelease}.tar.gz

# Backport upstream commit 9cfca9397b974f00bcc0915a4661be19e2e6e820:
#
#   Support for LLVM 14 (#1492)
#
#   API changes we had to take into account:
#   * TargetRegistry.h location
#   * No more DisableTailCalls field in PassManagerBuilder.
#
#   Needed to update the ref image for render-microfacet test, some sparklies
#   changed.  Looks like the new LLVM probably JITs to ever so slightly
#   different math code, tickling some LSB differences that at 1 sample per
#   pixel, results in some different sampling directions leading to fireflies.
#   We decided to just commit a new ref image and move on.
#
#   Signed-off-by: Larry Gritz <lg@larrygritz.com>
Patch:          0001-Support-for-LLVM-14-1492.patch

# Required for %%autosetup -S git, which in turn is required to use a patch
# from git containing a binary diff.
BuildRequires:  git-core

BuildRequires:  bison
BuildRequires:  boost-devel >= 1.55
BuildRequires:  clang-devel > 7
BuildRequires:  cmake >= 3.12
BuildRequires:  flex
BuildRequires:  gcc-c++ >= 6.1
BuildRequires:  llvm-devel > 7
# Needed for OSL pointclound functions
BuildRequires:  partio-devel
%if 0%{?fedora} < 35
BuildRequires:  pkgconfig(IlmBase) >= 2.0
%else
BuildRequires:  pkgconfig(Imath) >= 2.0
%endif
BuildRequires:  pkgconfig(OpenImageIO) >= 2.1
BuildRequires:  pkgconfig(pugixml)

# For osltoy
%if %{with qt5}
# Broken in Fedora 34
# /usr/bin/ld: /usr/lib64/libLLVM-12.so: error adding symbols: DSO missing from command line
# https://bugzilla.redhat.com/show_bug.cgi?id=2001177
%if 0%{?fedora} != 34
BuildRequires:  pkgconfig(Qt5) >= 5.6
%endif
%endif
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

%if %{with materialx}
%package MaterialX-shaders-source
Summary:        MaterialX shader nodes
License:        BSD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-common-headers

%description MaterialX-shaders-source
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the code for the MaterialX shader nodes.
%endif

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
%autosetup -p1 -n OpenShadingLanguage-Release-%{version}%{?prerelease} -S git
# Use python3 binary instead of unversioned python
sed -i -e "s/COMMAND python/COMMAND python3/" $(find . -iname CMakeLists.txt)

%build
%cmake \
   -DCMAKE_CXX_STANDARD=17 \
   -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
   -DCMAKE_SKIP_RPATH=TRUE \
   -DCMAKE_SKIP_INSTALL_RPATH=YES \
%if %{with materialx}
   -DOSL_BUILD_MATERIALX:BOOL=ON \
%endif
   -DOSL_SHADER_INSTALL_DIR:PATH=%{_datadir}/%{name}/shaders/ \
   -Dpartio_DIR=%{_prefix} \
   -DPARTIO_INCLUDE_DIR=%{_includedir} \
   -DPARTIO_LIBRARIES=%{_libdir} \
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
%if 0%{?fedora} != 34
%{_bindir}/osltoy
%endif
%endif
%{_bindir}/testrender
%{_bindir}/testshade
%{_bindir}/testshade_dso

%files doc
%doc %{_docdir}/%{name}/

%if %{with materialx}
%files MaterialX-shaders-source
%{_datadir}/%{name}/shaders/MaterialX
%endif

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
%if 0%{?fedora} < 32
%{_libdir}/osl*.so.1*
%endif
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
