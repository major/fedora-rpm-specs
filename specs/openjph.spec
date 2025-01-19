%global real_name OpenJPH

Name:           openjph
Version:        0.18.2
Release:        2%{?dist}
Summary:        Open-source implementation of JPEG2000 Part-15 (or JPH or HTJ2K)
License:        BSD-2-Clause
URL:            https://openjph.org/
ExcludeArch:    %{ix86}
Source:         https://github.com/aous72/%{real_name}/archive/refs/tags/%{version}/%{real_name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libtiff-4)

%description
Open source implementation of High-throughput JPEG2000 (HTJ2K), also known as
JPH, JPEG2000 Part 15, ISO/IEC 15444-15, and ITU-T T.814. Here, we are
interested in implementing the HTJ2K only, supporting features that are defined
in JPEG2000 Part 1. For example, for wavelet transform, only reversible 5/3 and
irreversible 9/7 are supported.

%package -n lib%{name}
Summary:        JPEG-2000 Part-15 library

%description -n lib%{name}
This package contains libopenjph, a library implementing the JPEG-2000
standard Part 15.

%package -n lib%{name}-devel
Summary:        Development files for libopenjph, a JPEG-2000 library
Requires:       pkgconfig(libjpeg)
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains libopenjph, a library implementing the JPEG-2000
standard Part 15.

%prep
%autosetup -n %{real_name}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/ojph_compress
%{_bindir}/ojph_expand

%files -n lib%{name}
%{_libdir}/lib%{name}*.so.0.18
%{_libdir}/lib%{name}*.so.%{version}

%files -n lib%{name}-devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 12 2024 Simone Caronni <negativo17@gmail.com> - 0.18.2-1
- Update to 0.18.2.

* Mon Nov 11 2024 Simone Caronni <negativo17@gmail.com> - 0.18.0-1
- Update to 0.18.0.

* Mon Sep 16 2024 Simone Caronni <negativo17@gmail.com> - 0.16.0-1
- Update to 0.16.0.

* Wed Sep 04 2024 Simone Caronni <negativo17@gmail.com> - 0.15.0-6
- Leave autodetection of hardware extensions as per developer's comment at
  https://bugzilla.redhat.com/show_bug.cgi?id=2307795#c16

* Wed Sep 04 2024 Simone Caronni <negativo17@gmail.com> - 0.15.0-5
- Adjust SIMD selection again.

* Fri Aug 30 2024 Simone Caronni <negativo17@gmail.com> - 0.15.0-4
- Switch on SIMD and drop AVX for old processors.

* Fri Aug 30 2024 Simone Caronni <negativo17@gmail.com> - 0.15.0-3
- Fix instructions set typo.

* Sun Aug 25 2024 Simone Caronni <negativo17@gmail.com> - 0.15.0-2
- Do not build on i686 (#2307782).

* Sat Aug 24 2024 Simone Caronni <negativo17@gmail.com> - 0.15.0-1
- First build.
