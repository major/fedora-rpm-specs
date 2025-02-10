# See rhbz#2332382: gstreamer1-svt-av1 subpackage should not be built anymore
# as it is now directly maintained by the GStreamer project since  1.24.0.
%bcond gst_plugin %[0%{?rhel}]

# cpuinfo is only available for %%{x86_64} %%{arm64} on Fedora
%ifarch %{x86_64} %{arm64}
%bcond unbundled_cpuinfo 1
%endif

%global _description %{expand:
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.}

Name:           svt-av1
Version:        2.3.0
Release:        %autorelease
Summary:        Scalable Video Technology for AV1 Encoder

# Main library: BSD-3-Clause-Clear and AOMPL
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/383
# Source/Lib/Common/Codec/EbHmCode.c: BSD
# Source/App/EncApp/EbAppString.*
# Source/Lib/Common/Codec/EbString.*
# Source/Lib/Encoder/Codec/vector.*: MIT
# Source/Lib/Common/ASM_SSE2/x86inc.asm: ISC
# Source/App/DecApp/EbMD5Utility.*: PublicDomain
# third_party/cpuinfo : BSD-2-Clause
# third_party/fastfeat : BSD-3-Clause
# third_party/safestringlib : MIT
License:        LicenseRef-BSD-3-Clause-Clear-WITH-AdditionRef-AOMPL-1.0 AND MIT AND ISC AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause
URL:            https://gitlab.com/AOMediaCodec/SVT-AV1
Source:         %url/-/archive/v%{version}/SVT-AV1-v%{version}.tar.bz2

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc >= 5.4.0
BuildRequires:  gcc-c++ >= 5.4.0
BuildRequires:  help2man
BuildRequires:  nasm >= 2.14
BuildRequires:  ninja-build
%if %{with unbundled_cpuinfo}
BuildRequires:  pkgconfig(libcpuinfo)
%endif
%if %{with gst_plugin}
BuildRequires:  meson
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
%endif

Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description %_description

%package    libs
Summary:    SVT-AV1 libraries
%if ! %{with gst_plugin}
Obsoletes:  gstreamer1-%{name} < %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%if %{without unbundled_cpuinfo}
Provides: bundled(cpuinfo) = 0^20201129gita7e1076-1
%endif
Provides: bundled(fastfeat) = 0^20191113git391d5e9-1
Provides: bundled(safestringlib) = 1.0.0-1

%description libs %_description

This package contains SVT-AV1 libraries.

%package    devel
Summary:    Development files for SVT-AV1
Requires:   %{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends: %{name}-devel-docs = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel %_description.

This package contains the development files for SVT-AV1.

%package    devel-docs
Summary:    Development documentation for SVT-AV1
BuildArch:  noarch

%description devel-docs %_description.

This package contains the documentation for development of SVT-AV1.

%if %{with gst_plugin}
%package -n     gstreamer1-%{name}
Summary:        GStreamer 1.0 %{name}-based plug-in
Requires:       gstreamer1-plugins-base%{?_isa}

%description -n gstreamer1-%{name}
This package provides %{name}-based GStreamer plug-in.
%endif

%prep
%autosetup -p1 -n SVT-AV1-v%{version}

# Mitigate name collisions
mv third_party/cpuinfo/LICENSE LICENSE.cpuinfo
mv third_party/fastfeat/LICENSE LICENSE.fastfeat
mv third_party/safestringlib/LICENSE LICENSE.safestringlib

# Sanitize third_party
# cpuinfo is only available for %%{x86_64} %%{arm64} on Fedora
%if %{with unbundled_cpuinfo}
rm -rfv third_party/cpuinfo
%endif
rm -rfv third_party/aom*
rm -rfv third_party/googletest

%if %{with gst_plugin}
# Patch build gstreamer plugin
sed -e "s|install: true,|install: true, include_directories : [ include_directories('../Source/API') ], link_args : '-lSvtAv1Enc',|" \
-e "/svtav1enc_dep =/d" -e 's|, svtav1enc_dep||' -e "s|svtav1enc_dep.found()|true|" -i gstreamer-plugin/meson.build
%endif


%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{with unbundled_cpuinfo}
       -DUSE_EXTERNAL_CPUINFO=ON \
%else
       -DUSE_EXTERNAL_CPUINFO=OFF \
%endif
       -DSVT_AV1_LTO=ON \
       -DSVT_AV1_PGO=ON \
       -G Ninja
%cmake_build

%if %{with gst_plugin}
export LIBRARY_PATH="$LIBRARY_PATH:$(pwd)/Bin/RelWithDebInfo"
pushd gstreamer-plugin
%meson
%meson_build
popd
%endif


%install
%cmake_install
rm -rfv %{buildroot}%{_libdir}/*.{a,la}

install -dm0755 %{buildroot}/%{_mandir}/man1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
help2man -N --help-option=--help --no-discard-stderr --version-string=%{version} %{buildroot}%{_bindir}/SvtAv1EncApp > %{buildroot}%{_mandir}/man1/SvtAv1EncApp.1

%if %{with gst_plugin}
pushd gstreamer-plugin
%meson_install
popd
%endif


%files
%{_bindir}/SvtAv1EncApp
%{_mandir}/man1/SvtAv1EncApp.1*

%files libs
%license LICENSE.md PATENTS.md LICENSE.fastfeat LICENSE.safestringlib LICENSE.cpuinfo
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_libdir}/libSvtAv1Enc.so.2*

%files devel
%{_includedir}/svt-av1
%{_libdir}/libSvtAv1Enc.so
%{_libdir}/pkgconfig/SvtAv1Enc.pc

%files devel-docs
%license LICENSE.md PATENTS.md LICENSE.fastfeat LICENSE.safestringlib LICENSE.cpuinfo
%doc Docs

%if %{with gst_plugin}
%files -n gstreamer1-svt-av1
%license LICENSE.md PATENTS.md LICENSE.fastfeat LICENSE.safestringlib LICENSE.cpuinfo
%{_libdir}/gstreamer-1.0/libgstsvtav1enc.so
%endif

%changelog
%autochangelog
