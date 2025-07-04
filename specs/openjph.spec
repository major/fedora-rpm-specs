%global real_name OpenJPH

Name:           openjph
Version:        0.21.3
Release:        %autorelease
Summary:        Open-source implementation of JPEG2000 Part-15 (or JPH or HTJ2K)
License:        BSD-2-Clause
URL:            https://openjph.org/
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
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/ojph_compress
%{_bindir}/ojph_expand

%files -n lib%{name}
%license LICENSE
%{_libdir}/lib%{name}.so.0.21
%{_libdir}/lib%{name}.so.%{version}

%files -n lib%{name}-devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
