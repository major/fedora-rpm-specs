%global commit 8f37f07a1ac425ed8769da65f7a0a2d26b1392a7
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20231220
%global commit_release .%{commit_date}git%{short_commit}

# To make rpmdev-bumpspec and similar tools happy
%global baserelease 8

Name:           libvmi
Version:        0.14.0
Release:        %{baserelease}%{commit_release}%{?dist}
Summary:        A library for performing virtual-machine introspection

License:        LGPLv3+
URL:            http://libvmi.com/
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

# disable '-Werror'
Patch0001:      libvmi-no_werror.patch

# Cannot presently build on other architectures.
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc bison flex xen-devel fuse-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libvirt)

%description
LibVMI is a C library with Python bindings that makes it easy to monitor
the low-level details of a running virtual machine by viewing its memory,
trapping on hardware events, and accessing the vCPU registers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities which make use of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains a number of programs which make
use of %{name}.

%prep
%autosetup -n libvmi-%{commit} -p1

%build
%cmake -DCMAKE_BUILD_TYPE="Release"
%cmake_build

%install
%cmake_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print
find %{buildroot}%{_libdir} -name '*.a' -delete -print

%ldconfig_scriptlets

%files
%license COPYING.LESSER
%doc README
%{_libdir}/libvmi.so.*

%files devel
%doc examples/*.c
%{_includedir}/%{name}/
%{_libdir}/libvmi.so
%{_libdir}/pkgconfig/libvmi.pc

%files utils
%{_bindir}/*

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-8.20231220git8f37f07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%autochangelog
