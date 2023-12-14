%global mfx_ver_major 2
%global mfx_ver_minor 10

Name:           oneVPL-intel-gpu
Version:        23.4.3
Release:        1%{?dist}
Summary:        Intel oneVPL GPU Runtime

License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
Source0:        https://github.com/oneapi-src/%{name}/archive/refs/tags/intel-onevpl-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  oneVPL-devel
BuildRequires:  pkgconfig(libdrm) >= 2.4
# Should be >= 1.9 but fails with libva < 2.12 (VAProcFilterCap3DLUT):
# https://github.com/oneapi-src/oneVPL-intel-gpu/issues/198
BuildRequires:  pkgconfig(libva) >= 1.12
# Every other component has the 2022.x.x format:
Requires:       oneVPL%{?_isa}

%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL API for Intel Gen
GPUs. Runtime provides access to hardware-accelerated video decode, encode and
filtering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-intel-onevpl-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}.%{mfx_ver_minor}
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc

%changelog
* Mon Dec 11 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 23.4.3-1
- Update to 23.4.3

* Wed Nov 01 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 23.4.0-1
- Update to 23.4.0 (RHBZ #2246790)

* Tue Oct 03 2023 Simone Caronni <negativo17@gmail.com> - 23.3.4-2
- Clean up SPEC file.

* Tue Oct 03 2023 Simone Caronni <negativo17@gmail.com> - 23.3.4-1
- Update to 23.3.4.
- Fixes #2231401.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 23.1.3-2
- Rebuilt for libva

* Mon Mar 13 2023 Adam Williamson <awilliam@redhat.com> - 23.1.3-1
- Update to 23.1.3.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Simone Caronni <negativo17@gmail.com> - 22.5.3-1
- Update to 22.5.3.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Simone Caronni <negativo17@gmail.com> - 22.4.4-1
- Update to 22.4.4.

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 22.4.2-1
- Update to 22.4.2.

* Tue Apr 26 2022 Simone Caronni <negativo17@gmail.com> - 22.4.0-1
- Update to 22.4.0.

* Wed Mar 30 2022 Simone Caronni <negativo17@gmail.com> - 22.3.1-2
- Disable AV1 encode/decode where not supported.
- Bump libva requirement (2.12+).

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 22.3.1-1
- Update to 22.3.1.

* Sun Mar 13 2022 Simone Caronni <negativo17@gmail.com> - 22.2.2-1
- Update to 22.2.2.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 22.2.1-1
- Update to 22.2.1.

* Tue Feb 08 2022 Simone Caronni <negativo17@gmail.com> - 22.2.0-1
- First build.
