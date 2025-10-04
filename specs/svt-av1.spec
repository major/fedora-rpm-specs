%global _description %{expand:
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.}

Name:           svt-av1
Version:        3.1.2
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
# third_party/fastfeat : BSD-3-Clause
# third_party/safestringlib : MIT
License:        LicenseRef-BSD-3-Clause-Clear-WITH-AdditionRef-AOMPL-1.0 AND MIT AND ISC AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause
URL:            https://gitlab.com/AOMediaCodec/SVT-AV1
Source:         %url/-/archive/v%{version}/SVT-AV1-v%{version}.tar.bz2

BuildRequires:  cmake >= 3.28
BuildRequires:  gcc >= 5.4.0
BuildRequires:  gcc-c++ >= 5.4.0
BuildRequires:  help2man
BuildRequires:  nasm >= 2.14
BuildRequires:  ninja-build

Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description %_description

%package    libs
Summary:    SVT-AV1 
Obsoletes:  gstreamer1-%{name} < %{?epoch:%{epoch}:}%{version}-%{release}

Provides: bundled(fastfeat) = 0^20191113git391d5e9-1
Provides: bundled(safestringlib) = 1.0.0^20250325gite399109-1

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

%prep
%autosetup -p1 -n SVT-AV1-v%{version}

# Mitigate name collisions
mv third_party/fastfeat/LICENSE LICENSE.fastfeat
mv third_party/safestringlib/LICENSE LICENSE.safestringlib

# Sanitize third_party
rm -rfv third_party/googletest

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_CPUINFO=AUTO \
       -DREPRODUCIBLE_BUILDS=1 \
       -DSVT_AV1_LTO=ON \
       -DSVT_AV1_PGO=ON \
       -G Ninja
%cmake_build

%install
%cmake_install
rm -rfv %{buildroot}%{_libdir}/*.{a,la}

install -dm0755 %{buildroot}/%{_mandir}/man1
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
help2man -N --help-option=--help --no-discard-stderr --version-string=%{version} %{buildroot}%{_bindir}/SvtAv1EncApp > %{buildroot}%{_mandir}/man1/SvtAv1EncApp.1

%files
%{_bindir}/SvtAv1EncApp
%{_mandir}/man1/SvtAv1EncApp.1*

%files libs
%license LICENSE.md PATENTS.md LICENSE.fastfeat LICENSE.safestringlib
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_libdir}/libSvtAv1Enc.so.3*

%files devel
%{_includedir}/svt-av1
%{_libdir}/libSvtAv1Enc.so
%{_libdir}/pkgconfig/SvtAv1Enc.pc

%files devel-docs
%license LICENSE.md PATENTS.md LICENSE.fastfeat LICENSE.safestringlib
%doc Docs

%changelog
%autochangelog
