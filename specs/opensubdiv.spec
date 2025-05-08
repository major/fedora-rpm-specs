# Force out of source build
%undefine __cmake_in_source_build

%global		upstream_version 3_6_0
#%%global       prerelease RC1

Name:           opensubdiv
Version:        3.6.0
Release:        %autorelease
Summary:        High performance subdivision surface libraries

# The entire source is Pixar except:
#
# MIT:
#   - glLoader/khrplatform.h
#   - documentation/tipuesearch/
License:        Pixar AND MIT
#URL:            http://graphics.pixar.com/%%{name}
Url:		https://github.com/PixarAnimationStudios/OpenSubdiv
Source:	        https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v%{upstream_version}%{?prerelease}/%{name}-%{version}%{?prerelease}.tar.gz

# fix linking against libdl (see https://github.com/PixarAnimationStudios/OpenSubdiv/issues/1196)
Patch:         	%{name}-rpath.patch

# make doxygen generated files consistent across builds & architectures
Patch:          opensubdiv-3.5.0-reproducible-docs.patch

# Downstream-only: do not compile static libraries
#
# When compiling shared libraries, do not compile static libraries. This
# patch suffices for Linux, but would have issues on some other platforms,
# and it’s not quite the behavior we would probably suggest upstream if we
# tried.
#
# We need to patch this rather than removing static libraries after the
# fact because the static libraries would still appear in the installed
# CMake files, causing problems for other packages like OpenUSD that want
# to link OpenSubdiv.
Patch:          0001-Downstream-only-do-not-compile-static-libraries.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:	pkgconfig(OpenCL)
BuildRequires:	pkgconfig(ptex)
BuildRequires:  pkgconfig(python3)
BuildRequires:  tbb2020.3-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:	python3dist(pygments)
# Drop libs subpackage
Obsoletes:	%{name}-libs < %{version}-%{release}
# Doxygen-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
Obsoletes:      %{name}-doc < 3.5.0-10

%description
OpenSubdiv is a set of open source libraries that implement high performance
subdivision surface (subdiv) evaluation on massively parallel CPU and
GPU architectures. 
This codepath is optimized for drawing deforming subdivs with static topology
at interactive framerates.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n OpenSubdiv-%{upstream_version}%{?prerelease}

# work around linking glitch
# https://github.com/PixarAnimationStudios/OpenSubdiv/issues/1196
sed -i 's|${PLATFORM_GPU_LIBRARIES}|${PLATFORM_GPU_LIBRARIES} ${CMAKE_DL_LIBS}|' opensubdiv/CMakeLists.txt

# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/#_compilationminification
find . -type f -name '*.min.js' -print -delete

%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_LIBDIR_BASE=%{_libdir} \
       -DGLEW_LOCATION=%{_libdir} \
       -DGLFW_LOCATION=%{_libdir} \
       -DNO_CLEW=1 \
       -DNO_CUDA=1 \
       -DNO_DOC=1\
       -DNO_EXAMPLES=1 \
       -DNO_GLFW_X11=1 \
       -DNO_OPENCL=1 \
       -DNO_METAL=1 \
       -DNO_REGRESSION=1 \
       -DNO_TUTORIALS=1 \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DTBB_LOCATION=%{_libdir}
%cmake_build

%{?_with_tests:
%check
make test V=1
}

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.%{version}

%files devel
%doc NOTICE.txt README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/OpenSubdiv/

%changelog
%autochangelog
