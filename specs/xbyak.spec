%global debug_package %{nil}

Summary:        A C++ JIT assembler for x86
Name:           xbyak
License:        BSD-3-Clause

Version:        7.23
Release:        %autorelease

URL:            https://github.com/herumi/xbyak
Source0:        %{url}/archive/v%{version}.tar.gz
# exception testing of allocator gets hung up on glibc double free check
Patch0:         xbyak-disable-noexecption-test3.patch

Group:          Development/Libraries
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sed

%bcond_with check
%if %{with check}
#  -m32
BuildRequires:  glibc-devel(x86-32), libstdc++(x86-32)
BuildRequires:  nasm, yasm
%endif

%description
Xbyak is a C++ header library that enables dynamically to
assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

The pronunciation of Xbyak is kəi-bja-k, かいびゃく.
It is named from a Japanese word 開闢, which means the beginning
of the world.

%package devel
Summary:        A C++ JIT assembler for x86
Provides:       xbyak-static = %{version}-%{release}

%description devel
Xbyak is a C++ header library that enables dynamically to
assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

The pronunciation of Xbyak is kəi-bja-k, かいびゃく.
It is named from a Japanese word 開闢, which means the beginning
of the world.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# Install samples
mkdir -p %{buildroot}%{_datadir}/xbyak/
cp -pr sample %{buildroot}%{_datadir}/xbyak/

%if %{with check}
%check
make test
%endif

%files devel
%license COPYRIGHT
%doc readme.md doc/changelog.md doc/usage.md
%doc %lang(jp) readme.txt
%{_datadir}/%{name}/
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
