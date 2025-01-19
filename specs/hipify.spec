%global upstreamname HIPIFY

%global rocm_release 6.3
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

# This is a clang tool so best to build with clang
%global toolchain clang

Name:           hipify
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        Convert CUDA to HIP

Url:            https://github.com/ROCm
License:        MIT
Source0:        %{url}/%{upstreamname}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-prepare-hipify-cmake-for-fedora.patch

BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  cmake
BuildRequires:  perl
BuildRequires:  zlib-devel

Requires:       perl

# ROCm is really only on x86_64
ExclusiveArch:  x86_64

%description
HIPIFY is a set of tools to translate CUDA source code into portable
HIP C++ automatically.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build

%cmake 
%cmake_build

%check
echo "void f(int *a, const cudaDeviceProp *b) { cudaChooseDevice(a,b); }" > b.cu
echo "void f(int *a, const hipDeviceProp_t *b) { hipChooseDevice(a,b); }" > e.hip
./bin/hipify-perl b.cu -o t.hip
diff e.hip t.hip

%install
%cmake_install
rm -rf %{buildroot}/usr/hip
# Fix executable perm:
chmod a+x %{buildroot}%{_bindir}/*
# Fix script shebang (Fedora doesn't allow using "env"):
sed -i 's|\(/usr/bin/\)env perl|\1perl|' %{buildroot}%{_bindir}//hipify-perl

if [ -d %{buildroot}%{_includedir} ]; then
    rm -rf %{buildroot}%{_includedir}
fi

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/hipconvertinplace-perl.sh
%{_bindir}/hipconvertinplace.sh
%{_bindir}/hipexamine-perl.sh
%{_bindir}/hipexamine.sh
%{_bindir}/hipify-clang
%{_bindir}/hipify-perl
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-2
- Build with system clang

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3
