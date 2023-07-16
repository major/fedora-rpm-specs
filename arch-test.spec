# This package installs binaries of different ISA's at the same time.
# Follow the Debian package to set it noarch and bypass binaries-in-noarch check.
%global _binaries_in_noarch_packages_terminate_build   0

Name:           arch-test
Version:        0.21
Release:        %autorelease
Summary:        Tools to detect architectures runnable by your machine+kernel

License:        MIT
URL:            https://github.com/kilobyte/arch-test
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
# different variants of binutils ustilised by arch-test
BuildRequires:  %{_bindir}/aarch64-linux-gnu-as
BuildRequires:  %{_bindir}/aarch64-linux-gnu-ld
BuildRequires:  %{_bindir}/alpha-linux-gnu-as
BuildRequires:  %{_bindir}/alpha-linux-gnu-ld
BuildRequires:  %{_bindir}/arm-linux-gnu-as
BuildRequires:  %{_bindir}/arm-linux-gnu-ld
BuildRequires:  %{_bindir}/hppa-linux-gnu-as
BuildRequires:  %{_bindir}/hppa-linux-gnu-ld
BuildRequires:  %{_bindir}/i686-w64-mingw32-as
BuildRequires:  %{_bindir}/i686-w64-mingw32-ld
BuildRequires:  %{_bindir}/ia64-linux-gnu-as
BuildRequires:  %{_bindir}/ia64-linux-gnu-ld
BuildRequires:  %{_bindir}/loongarch64-linux-gnu-as
BuildRequires:  %{_bindir}/loongarch64-linux-gnu-ld
BuildRequires:  %{_bindir}/arc-linux-gnu-as
BuildRequires:  %{_bindir}/arc-linux-gnu-ld
BuildRequires:  %{_bindir}/m68k-linux-gnu-as
BuildRequires:  %{_bindir}/m68k-linux-gnu-ld
BuildRequires:  %{_bindir}/mips64-linux-gnu-as
BuildRequires:  %{_bindir}/mips64-linux-gnu-ld
BuildRequires:  %{_bindir}/powerpc64le-linux-gnu-as
BuildRequires:  %{_bindir}/powerpc64le-linux-gnu-ld
BuildRequires:  %{_bindir}/powerpc64-linux-gnu-as
BuildRequires:  %{_bindir}/powerpc64-linux-gnu-ld
BuildRequires:  %{_bindir}/riscv64-linux-gnu-as
BuildRequires:  %{_bindir}/riscv64-linux-gnu-ld
BuildRequires:  %{_bindir}/s390x-linux-gnu-as
BuildRequires:  %{_bindir}/s390x-linux-gnu-ld
BuildRequires:  %{_bindir}/sh-linux-gnu-as
BuildRequires:  %{_bindir}/sh-linux-gnu-ld
BuildRequires:  %{_bindir}/sparc64-linux-gnu-as
BuildRequires:  %{_bindir}/sparc64-linux-gnu-ld
BuildRequires:  %{_bindir}/x86_64-linux-gnu-as
BuildRequires:  %{_bindir}/x86_64-linux-gnu-ld
BuildRequires:  %{_bindir}/x86_64-w64-mingw32-as
BuildRequires:  %{_bindir}/x86_64-w64-mingw32-ld
# needed but not pulled in by mingw*-binutils
BuildRequires:  mingw64-crt
BuildRequires:  mingw32-crt
BuildArch:      noarch

%description
This tool will tell you "can your machine+kernel run architecture X?".

The check is for the ability to run machine code and supporting appropriate
syscall ABI, not for the presence of userland libraries.  IE, a positive
answer means you can use a chroot or container of that architecture, add it
to your multiarch set, etc, but doesn't mean you can currently run non-static
binaries without installing required libraries.

%prep
%autosetup
# add search path to find '-lkernel32'
sed -i 's:-s win32.o:-s win32.o -L%{mingw32_libdir}:' Makefile
sed -i 's:-s win64.o:-s win64.o -L%{mingw64_libdir}:' Makefile

# risc32 cross-build binutils is not available in Fedora
sed -i '0,/riscv32/ {s/riscv32//}' Makefile

# use triplets of cross-build binutils of Fedora
sed -i 's/sh4-linux-gnu/sh-linux-gnu/' Makefile
cat << "EOF" >config
VERSION=%{version}
MIPS=mips64-linux-gnu
POWERPC=powerpc64-linux-gnu
ARM=arm-linux-gnu
EOF


%build
%make_build


%install
%make_install PREFIX=%{_prefix}
chmod 644 %{buildroot}%{_mandir}/man1/*

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_bindir}/elf-arch
%{_prefix}/lib/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/elf-arch.1*


%changelog
%autochangelog
