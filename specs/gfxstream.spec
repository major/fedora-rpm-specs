%global gitdate 20240226
%global gitversion 23d05703

Name:           gfxstream
Version:        0.1.2^%{gitdate}git%{gitversion}
Release:        3%{?dist}

Summary:        Graphics Streaming Kit

# the project license declared in meson.build is "MIT OR Apache-2.0"
# but it also uses some MIT licensed headers and OpenGL headers are
# under the MIT-Khronos license, some files only have Apache-2.0
# license information.
#
# in the source package there are a number of other licenses
# that are (CC-BY-4.0) and not included in the
# software installed by the produced rpms,
# see the project LICENSE for a partial listing.
#
# See also licensecheck.txt for a full break down.
# (the project license will be clarified if/when it is accepted in mesa!27246)
License:        MIT AND Apache-2.0 AND MIT-Khronos-old

URL:            https://android.googlesource.com/platform/hardware/google/gfxstream

#VCS: https://android.googlesource.com/platform/hardware/google/gfxstream
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:        gfxstream-%{gitdate}.tar.xz
Source1:        make-git-snapshot.sh
Source2:        licensecheck.txt

Patch0000:      0001-meson-use-system-headers-if-possible.patch
Patch0001:      0001-meson-add-DGLM_ENABLE_EXPERIMENTAL.patch

BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(aemu_base)
BuildRequires:  pkgconfig(aemu_host_common)
BuildRequires:  pkgconfig(aemu_logging)
BuildRequires:  vulkan-headers
BuildRequires:  renderdoc-devel
BuildRequires:  glm-devel
BuildRequires:  libglvnd-devel
ExcludeArch:    %{ix86} %{power64} s390x


%description
Graphics Streaming Kit is a code generator that makes it easier to serialize and
forward graphics API calls from one place to another:
 - from a virtual machine guest to host for virtualized graphics
 - from one process to another for IPC graphics
 - from one computer to another via network sockets

%package devel
Summary: gfxstream development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
gfxstream development files, used by QEMU to build against.


%prep
%autosetup -n %{name}-%{gitdate} -p1

%build
%meson -Ddecoders=gles,vulkan,composer
%meson_build

%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libgfxstream_backend.so.0*

%files devel
%dir %{_includedir}/gfxstream/
%{_includedir}/gfxstream/*
%{_libdir}/libgfxstream_backend.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2^20240226git23d05703-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2^20240226git23d05703-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 16 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.1.2^20240226git23d05703-1
- Initial packaging (rhbz#2242058)
