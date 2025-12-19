%global git_commit 96bbdb53ed6b5bdf2e940f6068016a78afcc7852
%global git_date 20240704

Name:		libyuv
Summary:	YUV conversion and scaling functionality library
Version:	0
Release:	%autorelease -p -s %{git_date}git%{sub %git_commit 0 7}
License:	BSD-3-Clause
Url:		https://chromium.googlesource.com/libyuv/libyuv
VCS:		git:%{url}
Source0:	%{url}/+archive/%{git_commit}.tar.gz
# Fedora-specific. Upstream isn't interested in these patches.
Patch1:		libyuv-0001-Move-Linux-variables-to-the-top.patch
Patch2:		libyuv-0002-Use-a-proper-so-version.patch
Patch3:		libyuv-0003-Link-against-shared-library.patch
Patch4:		libyuv-0004-Disable-static-library.patch
Patch5:		libyuv-0005-Use-library-suffix-during-installation.patch
Patch6:		libyuv-0006-Link-against-math-library-for-roundf.patch
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gtest-devel
BuildRequires:	libjpeg-devel


%description
This is an open source project that includes YUV conversion and scaling
functionality. Converts all webcam formats to YUV (I420). Convert YUV to
formats for rendering/effects. Rotate by 90 degrees to adjust for mobile
devices in portrait mode. Scale YUV to prepare content for compression,
with point, bilinear or box filter.


%package devel
Summary: The development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
Additional header files for development with %{name}.


%prep
%autosetup -p1 -c %{name}-%{version}

cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -lyuv
EOF


%build
# TODO: Please submit an issue to upstream (rhbz#2380770)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake} -DUNIT_TEST=TRUE
%{cmake_build}


%install
%{cmake_install}

mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -a %{name}.pc %{buildroot}%{_libdir}/pkgconfig/

# FIXME
rm -f %{buildroot}%{_bindir}/yuvconvert


%check
# FIXME fails again on s390 - we should use CTest via %%{ctest} macro
# ./libyuv_unittest || true


%files
%license LICENSE
%doc AUTHORS PATENTS README.md
%{_libdir}/%{name}.so.*


%files devel
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
