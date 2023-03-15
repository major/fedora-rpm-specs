# AV1 decode since libva 2.7
%if 0%{?fedora} || 0%{?rhel} >= 9
%global av1_decode ON
%else
%global av1_decode OFF
%endif

# AV1 encode since libva 2.14
%if 0%{?fedora} >= 36
%global av1_encode ON
%else
%global av1_encode OFF
%endif

Name:           oneVPL-intel-gpu
Version:        23.1.3
Release:        1%{?dist}
Summary:        Intel oneVPL GPU Runtime
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/oneapi-src/%{name}/archive/refs/tags/intel-onevpl-%{version}.tar.gz
Patch0:         %{name}-fix-build.patch

# Every other component has the 2022.x.x format:
Requires:       oneVPL%{?_isa}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  oneVPL-devel
BuildRequires:  pkgconfig(libdrm) >= 2.4
# Should be >= 1.9 but fails with libva < 2.12 (VAProcFilterCap3DLUT):
# https://github.com/oneapi-src/oneVPL-intel-gpu/issues/198
# Once fixed, can be built on epel9 as well.
BuildRequires:  pkgconfig(libva) >= 1.12

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
export VPL_BUILD_DEPENDENCIES="%{_prefix}"
%cmake \
    -DBUILD_TESTS:BOOL='OFF' \
    -DCMAKE_BUILD_TYPE:STRING="Fedora" \
    -DMFX_ENABLE_AV1_VIDEO_DECODE:BOOL='%{av1_decode}' \
    -DMFX_ENABLE_AV1_VIDEO_ENCODE:BOOL='%{av1_encode}'
%cmake_build

%install
%cmake_install

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_docdir}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmfx-gen.so.1.2
%{_libdir}/libmfx-gen.so.1.2.8
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc

%changelog
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
