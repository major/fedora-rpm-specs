Name:           venus-protocol
Version:        1.1.3
Release:        %autorelease
Summary:        Venus Vulkan protocol headers for VirtIO GPU

License:        MIT AND (Apache-2.0 OR MIT)
URL:            https://gitlab.freedesktop.org/virgl/venus-protocol
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        %{name}.rpmlintrc

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  meson >= 0.54.0
BuildRequires:  python3-mako

%description
Venus protocol defines the Vulkan protocol used by the Venus Vulkan driver
for VirtIO GPU. It provides generated C header files for encoding and decoding
Vulkan commands between the guest Venus driver and the host virglrenderer.

%package        devel
Summary:        Development files for venus-protocol
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Venus protocol defines the Vulkan protocol used by the Venus Vulkan driver
for VirtIO GPU.

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

# Move the .pc file to /usr/share/pkgconfig/, which is arch-independent and the
# correct path for a header-only package
mkdir -p %{buildroot}%{_datadir}/pkgconfig
mv %{buildroot}%{_libdir}/pkgconfig/%{name}.pc %{buildroot}%{_datadir}/pkgconfig/

%files devel
%doc README
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
