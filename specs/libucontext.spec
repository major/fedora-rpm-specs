%global somajor 1

Name:           libucontext
Version:        1.3.3
Release:        1%{?dist}
Summary:        ucontext implementation featuring glibc-compatible ABI

License:        ISC
URL:            https://github.com/kaniini/libucontext
Source:         https://distfiles.ariadne.space/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc

%description
libucontext is a library which provides the ucontext.h C API.
Unlike other implementations, it faithfully follows the Linux
kernel process ABI when doing context swaps.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%meson -Ddefault_library=shared -Dexport_unprefixed=false
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}*.so.%{somajor}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Nov 18 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.3.3-1
- Initial package
