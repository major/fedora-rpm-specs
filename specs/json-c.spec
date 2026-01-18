%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# We don't want accidental SONAME bumps.
# When there is a SONAME bump in json-c, we need to request
# a side-tag for bootstrap purposes:
#
# 1. Build a bootstrap build of the systemd package, and wait
#    for it to be available inside the side-tag.
# 2. Re-build the following build-chain for bootstrap:
#    json-c : cryptsetup
# 3. Untag the systemd bootstrap build from the side-tag, and
#    disable bootstrapping in the systemd package.  Re-build
#    the systemd package into Rawhide.
# 4. Wait for the changes to populate and re-build the following
#    chain into the side-tag:
#    satyr : libdnf libreport
# 5. Merge the side-tag using Bodhi.
#
# After that procedure any other cosumers can be re-build
# in Rawhide as usual.
%global so_ver 5

# Releases are tagged with a date stamp.
%global reldate 20240915

%bcond_without mingw


Name:           json-c
Version:        0.18
Release:        8%{?dist}
Summary:        JSON implementation in C

License:        MIT
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/%{name}-%{version}-%{reldate}.tar.gz

# Add libver to mingw dll
Patch0:         json-c_mingw-libver.patch
Patch1:         json-c-0.18-utf8-validation.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif

%description
JSON-C implements a reference counting object model that allows you
to easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.  It aims to conform to RFC 7159.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Reference manual for json-c

#BuildArch:     noarch

BuildRequires:  doxygen
BuildRequires:  hardlink

%description    doc
This package contains the reference manual for %{name}.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc

%description -n mingw32-%{name}
%{summary}.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc

%description -n mingw64-%{name}
%{summary}.

%{?mingw_debug_package}
%endif


%prep
%autosetup -n %{name}-%{name}-%{version}-%{reldate} -p 1

# Remove pre-built html documentation.
rm -fr doc/html

# Update Doxyfile.
doxygen -s -u doc/Doxyfile.in


%build
cmake_opts="-DBUILD_STATIC_LIBS:BOOL=OFF       \
  -DCMAKE_BUILD_TYPE:STRING=RELEASE  \
  -DCMAKE_C_FLAGS_RELEASE:STRING=""  \
  -DDISABLE_BSYMBOLIC:BOOL=OFF       \
  -DDISABLE_WERROR:BOOL=ON           \
  -DENABLE_RDRAND:BOOL=ON            \
  -DENABLE_THREADING:BOOL=ON         \
  -DBUILD_APPS=OFF                   \
  -G Ninja"
%cmake $cmake_opts
%cmake_build --target all doc

%if %{with mingw}
%mingw_cmake $cmake_opts
%mingw_ninja
%endif


%install
%cmake_install

%if %{with mingw}
%mingw_ninja_install
%mingw_debug_install_post
%endif

# Documentation
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{__cmake_builddir}/doc/html ChangeLog README README.* \
  %{buildroot}%{_pkgdocdir}
hardlink -cfv %{buildroot}%{_pkgdocdir}


%check
export USE_VALGRIND=0
%ctest
%ifarch %{valgrind_arches}
export USE_VALGRIND=1
%ctest
%endif
unset USE_VALGRIND


%ldconfig_scriptlets


%files
%license AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.%{so_ver}*


%files devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/README*
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%if 0%{?fedora} || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%endif
%doc %{_pkgdocdir}

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_includedir}/%{name}
%{mingw32_bindir}/lib%{name}-%{so_ver}.dll
%{mingw32_libdir}/lib%{name}.dll.a
%{mingw32_libdir}/cmake/%{name}
%{mingw32_libdir}/pkgconfig/%{name}.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_includedir}/%{name}
%{mingw64_bindir}/lib%{name}-%{so_ver}.dll
%{mingw64_libdir}/lib%{name}.dll.a
%{mingw64_libdir}/cmake/%{name}
%{mingw64_libdir}/pkgconfig/%{name}.pc
%endif

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

%autochangelog
