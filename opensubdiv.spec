# Force out of source build
%undefine __cmake_in_source_build

%global		upstream_version 3_4_4
#%%global       prerelease RC1

Name:           opensubdiv
Version:        3.4.4
Release:        4%{?prerelease}%{?dist}
Summary:        High performance subdivision surface libraries

License:        ASL 2.0
#URL:            http://graphics.pixar.com/%%{name}
Url:		https://github.com/PixarAnimationStudios/OpenSubdiv
Source:	        https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v%{upstream_version}%{?prerelease}/%{name}-%{version}%{?prerelease}.tar.gz

# fix linking against libdl (see https://github.com/PixarAnimationStudios/OpenSubdiv/issues/1196)
Patch:         	%{name}-rpath.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:	pkgconfig(OpenCL)
BuildRequires:	pkgconfig(Ptex)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	python3dist(docutils)
BuildRequires:	python3dist(pygments)

%description
OpenSubdiv is a set of open source libraries that implement high performance
subdivision surface (subdiv) evaluation on massively parallel CPU and
GPU architectures. 
This codepath is optimized for drawing deforming subdivs with static topology
at interactive framerates.

%package        libs
Summary:        Core OpenSubdiv libraries
Requires:       %{name}%{?_isa} = %{version}-%{release} 
%description    libs
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:	High performance subdivision surface libraries
BuildArch:	noarch

%description doc
OpenSubdiv is a set of open source libraries that implement high
performance subdivision surface (subdiv) evaluation on massively
parallel CPU and GPU architectures. 
This code path is optimized for
drawing deforming surfaces with static topology at interactive
frame rates.

This package includes the documentation of OpenSubdiv.

%prep
%autosetup -p1 -n OpenSubdiv-%{upstream_version}%{?prerelease}

# work around linking glitch
# https://github.com/PixarAnimationStudios/OpenSubdiv/issues/1196
sed -i 's|${PLATFORM_GPU_LIBRARIES}|${PLATFORM_GPU_LIBRARIES} ${CMAKE_DL_LIBS}|' opensubdiv/CMakeLists.txt
	
%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_LIBDIR_BASE=%{_libdir} \
       -DGLEW_LOCATION=%{_libdir} \
       -DGLFW_LOCATION=%{_libdir} \
       -DNO_CLEW=1 \
       -DNO_CUDA=1 \
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

# Remove static files
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

%files
%%license LICENSE.txt
%{_bindir}/stringify

%files libs
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.%{version}

%files devel
%doc NOTICE.txt README.md
%{_includedir}/*
%{_libdir}/*.so

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.4-1
- Update to 3.4.4
- Rebuild for ptex 2.4.0

* Fri Feb 05 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.4-0.1.RC1
- Update to 3.4.4 RC1
- Enable ptex support

* Mon Sep 21 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.3-1
- Update to 3.4.3
- Port Mageia patch for building with Python 3 dependency
- Add doc subpackage
- Disable OpenCL due to upstream bug

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.0-3
- Remove rpath
- Remove unneeded ldconfig_scriptlets macro
- Improve spec file upon review (rhbz #1762155)

* Mon Oct 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.0-2
- Adjust maximum line limit on description

* Mon Oct 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.0-1
- Initial package
