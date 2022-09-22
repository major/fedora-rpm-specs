%global _description %{expand:
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.}

Name:           svt-av1
Version:        1.1.0
%global commit  6e87a1de98281840abebc030781780edd822bae5
Release:        %autorelease
Summary:        Scalable Video Technology for AV1 Encoder

# Main library: BSD-3
# Source/Lib/Common/Codec/EbHmCode.c: BSD
# Source/App/EncApp/EbAppString.*
# Source/Lib/Common/Codec/EbString.*
# Source/Lib/Common/Codec/vector.*: MIT
# Source/Lib/Common/ASM_SSE2/x86inc.asm: ISC
# Source/App/DecApp/EbMD5Utility.*: PublicDomain
License:        BSD and MIT and ISC and Public Domain
URL:            https://gitlab.com/AOMediaCodec/SVT-AV1
Source0:        %url/-/archive/v%{version}/%{name}-%{version}.tar.bz2

# 64Bits, 5th Generation Intel® Core™ processor only
ExclusiveArch:  x86_64

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  yasm
BuildRequires:  help2man
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description %_description

%package libs
Summary:    SVT-AV1 libraries

%description libs %_description

This package contains SVT-AV1 libraries.

%package devel
Summary:    Development files for SVT-AV1
Requires:   %{name}-libs = %{version}-%{release}
Recommends: %{name}-devel-docs = %{version}-%{release}

%description devel %_description.

This package contains the development files for SVT-AV1.

%package devel-docs
Summary:    Development documentation for SVT-AV1
BuildArch:  noarch

%description devel-docs %_description.

This package contains the documentation for development of SVT-AV1.

%package -n     gstreamer1-%{name}
Summary:        GStreamer 1.0 %{name}-based plug-in
Requires:       gstreamer1-plugins-base%{?_isa}

%description -n gstreamer1-%{name}
This package provides %{name}-based GStreamer plug-in.

%prep
%autosetup -p1 -n SVT-AV1-v%{version}-%{commit}
# Patch build gstreamer plugin
sed -e "s|install: true,|install: true, include_directories : [ include_directories('../Source/API') ], link_args : '-lSvtAv1Enc',|" \
-e "/svtav1enc_dep =/d" -e 's|, svtav1enc_dep||' -e "s|svtav1enc_dep.found()|true|" -i gstreamer-plugin/meson.build

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

export LIBRARY_PATH="$LIBRARY_PATH:$(pwd)/Bin/RelWithDebInfo"
pushd gstreamer-plugin
%meson
%meson_build
popd

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.{a,la}

install -d -m0755 %{buildroot}/%{_mandir}/man1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
help2man -N --help-option=-help --version-string=%{version} %{buildroot}%{_bindir}/SvtAv1DecApp > %{buildroot}%{_mandir}/man1/SvtAv1DecApp.1
help2man -N --help-option=-help --no-discard-stderr --version-string=%{version} %{buildroot}%{_bindir}/SvtAv1EncApp > %{buildroot}%{_mandir}/man1/SvtAv1EncApp.1

pushd gstreamer-plugin
%meson_install
popd

%files
%{_bindir}/SvtAv1DecApp
%{_bindir}/SvtAv1EncApp
%{_mandir}/man1/SvtAv1DecApp.1*
%{_mandir}/man1/SvtAv1EncApp.1*

%files libs
%license LICENSE.md PATENTS.md
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_libdir}/libSvtAv1Dec.so.0*
%{_libdir}/libSvtAv1Enc.so.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/libSvtAv1Dec.so
%{_libdir}/libSvtAv1Enc.so
%{_libdir}/pkgconfig/SvtAv1Dec.pc
%{_libdir}/pkgconfig/SvtAv1Enc.pc

%files devel-docs
%license LICENSE.md PATENTS.md
%doc Docs

%files -n gstreamer1-%{name}
%{_libdir}/gstreamer-1.0/libgstsvtav1enc.so

%changelog
%autochangelog
