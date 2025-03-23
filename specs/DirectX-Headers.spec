# Disable debug as this package only provides a static archive (and no shared object).
# debuginfo will be made available via consumer (mesa) instead.
%global debug_package %{nil}
%global __strip /bin/true

# There is no LTO in mesa, so drop that in stub archives also
# see mesa comment:
# We've gotten a report that enabling LTO for mesa breaks some games. See
# https://bugzilla.redhat.com/show_bug.cgi?id=1862771 for details.
# Disable LTO for now
%define _lto_cflags %{nil}

Name:           DirectX-Headers
Version:        1.615.0
Release:        %autorelease
Summary:        Official Direct3D 12 headers

License:        MIT
URL:            https://github.com/microsoft/DirectX-Headers
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
# Test assumes the build is under WSL, which is unlikely
%{?_with_test:BuildRequires: gtest-devel}


%description
Official Direct3D 12 headers

%package        devel
Summary:        Development files for %{name}
# This only provides -static files, so only
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
# Change EOL encoding
for i in LICENSE README.md ; do
  sed -i -e 's/\r$//' ${i}
  touch -r SECURITY.md ${i}
done


%build
%meson \
 %{?!_with_test:-Dbuild-test=false}

%meson_build


%install
%meson_install


%check
%{?_with_test:
%meson_test
}


%files devel
%license LICENSE
%doc README.md SECURITY.md
%{_includedir}/directx
%{_includedir}/dxguids
%{_includedir}/wsl
%{_libdir}/libDirectX-Guids.a
%{_libdir}/libd3dx12-format-properties.a
%{_libdir}/pkgconfig/DirectX-Headers.pc


%changelog
%autochangelog
