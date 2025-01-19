%global commit abcd277ea45e9098bed752cf9c6875b533c0892f

Name:		nanosvg
# This thing has no version so we'll use the last commit date
Version:	20221221
Release:	7%{?dist}
License:	Zlib
# Technically, this is a fork, but the upstream is unmaintained and this one has some fixes
URL:		https://github.com/fltk/nanosvg
Source0:	https://github.com/fltk/nanosvg/archive/%{commit}.tar.gz
# https://github.com/memononen/nanosvg/pull/246
Patch0:		nanosvg-sover.patch
# Idea taken from here, but their implementation didn't work
# https://github.com/memononen/nanosvg/pull/245
# using LIB_INSTALL_DIR seems to work better
Patch1:		nanosvg-lib64.patch
# Inspired by
# https://github.com/memononen/nanosvg/pull/216
# Modified slightly to work without an installed nanosvg instance
Patch2:		nanosvg-build-examples.patch
Summary:	Simple stupid SVG parser
BuildRequires:	cmake, gcc
# Needed for example1
BuildRequires:	libglvnd-devel, glfw-devel >= 3

%description
NanoSVG is a simple stupid single-header-file SVG parse. The output of the
parser is a list of cubic bezier shapes. The library suits well for
anything from rendering scalable icons in your editor application to
prototyping a game.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for nanosvg

%description devel
Development files for nanosvg.

%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1 -b .sover
%patch -P1 -p1 -b .lib64
%patch -P2 -p1 -b .build-examples

%build
%cmake
%cmake_build

%install
%cmake_install
# Note: We do not install the examples, they are not really useful outside of a testing context.

# Use example2 as a smoke test
%check
pushd example
../%{__cmake_builddir}/example/example2
popd

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libnanosvg.so.*
%{_libdir}/libnanosvgrast.so.*

%files devel
%{_includedir}/nanosvg/
%{_libdir}/cmake/NanoSVG
%{_libdir}/libnanosvg.so
%{_libdir}/libnanosvgrast.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20221221-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20221221-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20221221-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20221221-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 11 2023 Tom Callaway <spot@fedoraproject.org> - 20221221-3
- modified the build-examples patch to work without an install of nanosvg-devel

* Fri Aug 11 2023 Tom Callaway <spot@fedoraproject.org> - 20221221-2
- build examples
- add comments discussing upstream status of patches
- use example2 as a smoke test

* Thu Aug 10 2023 Tom Callaway <spot@fedoraproject.org> - 20221221-1
- initial package
