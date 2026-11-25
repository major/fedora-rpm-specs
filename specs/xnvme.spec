Name:           xnvme
Version:        0.8.1
Release:        1%{?dist}
Summary:        Unified API and tools for traditional and emerging I/O interfaces

License:        BSD-3-Clause
URL:            https://github.com/xnvme/xnvme
Source:         %{url}/releases/download/v%{version}/xnvme-%{version}.tar.gz

# Upstream builds and tests only x86_64 and aarch64; the uPCIe backend has
# memory barriers for those alone, and xnvme cmd-admin assumes little-endian
# These exclusions are permanent:
# ppc64le: https://bugzilla.redhat.com/2583445 (WONTFIX)
# s390x:   https://bugzilla.redhat.com/2583444 (WONTFIX)
ExclusiveArch:  x86_64 aarch64

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  liburing-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

%description
%{summary}.
Minimal-overhead libraries and tools for cross-platform storage I/O and
NVMe-native development. A unified API encapsulating traditional block-I/O via
psync, libaio, and io_uring as well as user-space NVMe drivers.

%package devel
Summary:        Development library and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This contains the headers and libraries for developing against %{name}.

%package static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
%{summary}.

%package tools
Summary:        Command-line tools for storage I/O and NVMe-native development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
%{summary}.

%prep
%autosetup -p1

%build
%meson -Dforce_completions=true -Dwith-libvfn=disabled -Dwith-isal=disabled -Dwith-spdk=disabled -Dwith-cuda=disabled -Dwith-hip=disabled -Dwith-cuse=enabled -Dsystemd=enabled -Dexamples=false -Dtests=false
%meson_build

%install
%meson_install

%check
%meson_test --num-processes 1

%post tools
%systemd_post xnvme-homi@.service xnvme-qublk@.service

%preun tools
%systemd_preun xnvme-homi@.service xnvme-qublk@.service

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/lib%{name}*.h

%files static
%{_libdir}/lib%{name}.a

%files tools
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-*.1*
%{bash_completions_dir}/%{name}
%{_unitdir}/%{name}-homi@.service
%{_unitdir}/%{name}-qublk@.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/homi.conf.example
%config(noreplace) %{_sysconfdir}/%{name}/qublk.conf.example

%changelog
* Tue Nov 24 2026 Karl B. Torp <k.torp@samsung.com> - 0.8.1-1
- Bump to v0.8.1
- Drop the rpath patch; upstream omits the rpath for a /usr prefix
- Package the xnvme front-end, its libexec programs and the homi/qublk systemd units
- Build only for x86_64 and aarch64, the architectures upstream supports

* Fri Jul 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 11 2024 Karl B. Torp <k.torp@samsung.com> - 0.7.5-1
- Bump to v0.7.5

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 25 2024 Richard W.M. Jones <rjones@redhat.com> - 0.7.4-3
- Use %%{bash_completions_dir} macro

* Mon Feb 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.7.4-2
- Initial version
