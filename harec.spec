%global srcver  0.24.0
%global srcpre  rc2
%global pkgsrc  %{srcver}%{?srcpre:-%{srcpre}}

Name:           harec
Version:        %{srcver}%{?srcpre:~%{srcpre}}
Release:        %autorelease
Summary:        Hare bootstrap compiler

License:        GPL-3.0-only
URL:            https://git.sr.ht/~sircmpwn/harec
Source0:        %{url}/archive/%{pkgsrc}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  qbe
Requires:       qbe

ExclusiveArch: x86_64 aarch64 riscv64

%description
This is a Hare compiler written in C11 for POSIX-compatible systems.
It is intended as a bootstrap compiler and using the Hare standard
library is recommended for production use.


%prep
%autosetup -n %{name}-%{pkgsrc}


%build
%{!?_auto_set_build_flags:%{set_build_flags}}
export CFLAGS="${CFLAGS} -std=c17"

cp configs/linux.mk config.mk
sed -i 's|^PREFIX.*|PREFIX = %{_prefix}|' config.mk
sed -i 's|^ARCH.*|ARCH = %{_arch}|' config.mk
sed -i 's|^VERSION.*|VERSION = %{version}|' config.mk
sed -i 's|^CFLAGS|UPSTREAMCFLAGS|' config.mk
echo 'CFLAGS := $(UPSTREAMCFLAGS) $(CFLAGS)' | tee -a config.mk
%make_build


%install
%make_install


%check
%{!?_auto_set_build_flags:%{set_build_flags}}
make check


%files
%license COPYING
%doc README.md docs/*.txt
%{_bindir}/harec


%changelog
%autochangelog
