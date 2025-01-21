# vosk-api-devel primarily consists of header and shared lib 
# with no significant executable content requiring debugging.
%global debug_package %{nil}
%global kaldi_commit 93ef0019b847272a239fbb485ef97f29feb1d587 
Name:           vosk-api
Version:        0.3.45
Release:        2%{?dist}
Summary:        Offline speech recognition toolkit
# vosk-api depends on Kaldi, which itself relies on OpenFST that uses 
# floating-point optimizations specific to 64-bit systems
ExclusiveArch:  x86_64 aarch64 ppc64le
License:        Apache-2.0
URL:            https://alphacephei.com/vosk
Source0:        https://github.com/alphacep/vosk-api/archive/v%{version}/vosk-api-%{version}.tar.gz
Source1:        https://github.com/alphacep/kaldi/archive/%{kaldi_commit}.tar.gz

# These patches improve Kaldi's OpenFST, OpenBLAS, and LAPACK compatibility.
Patch0: kaldi-fst.patch
Patch1: kaldi-lapack.patch
Patch2: kaldi-openblas.patch
Patch3: vosk-lapack.patch
Patch4: vosk-lib_fst.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  blas-static
BuildRequires:  lapack-static
BuildRequires:  openblas-static
BuildRequires:  openfst-tools
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
BuildRequires:  openblas-devel
BuildRequires:  openfst-devel
BuildRequires:  unzip

%description
Vosk is an offline open source speech recognition toolkit.

%package devel
Summary: Development libraries of vosk-api
 
%description devel
The vosk-api-devel package contains the header and shared library 

%prep
%setup -q -a1
tar -xzf %{SOURCE1}

# Move and setup Kaldi
mv kaldi-%{kaldi_commit} kaldi

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

cd kaldi/tools
mkdir -p OpenBLAS/install/lib
ln -sf %{_includedir}/openblas OpenBLAS/install/include
ln -sf %{_libdir}/* OpenBLAS/install/lib
mkdir -p openfst/include openfst/lib
ln -sf %{_includedir}/fst openfst/include
ln -sf %{_libdir}/* openfst/lib

%build
cd kaldi/src
./configure --mathlib=OPENBLAS_NO_F2C --shared --use-cuda=no
%make_build online2 lm rnnlm

cd %{_builddir}/vosk-api-%{version}/src
%make_build KALDI_ROOT=../kaldi HAVE_OPENBLAS_NO_F2C=1 HAVE_OPENBLAS_CLAPACK=0

%install
# Install vosk-api headers and library
install -Dpm 644 %{_builddir}/vosk-api-%{version}/src/vosk_api.h %{buildroot}%{_includedir}/vosk_api.h
install -Dpm 755 %{_builddir}/vosk-api-%{version}/src/libvosk.so %{buildroot}%{_libdir}/libvosk.so

%files devel
%license COPYING
%doc README.md
%{_includedir}/vosk_api.h
%{_libdir}/libvosk.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Manish Tiwari <matiwari@redhat.com> - 0.3.45-1
- Initial package release
