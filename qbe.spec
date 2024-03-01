
Name:           qbe
Version:        1.2
Release:        %autorelease
Summary:        A pure C embeddable compiler backend

License:        MIT
URL:            https://c9x.me/compile/
Source0:        %{url}/release/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make

ExclusiveArch: x86_64 aarch64 riscv64

%description
QBE is a compiler backend that aims to provide 70% of the performance of
industrial optimizing compilers in 10% of the code. QBE fosters language
innovation by offering a compact user-friendly and performant backend. The size
limit constrains QBE to focus on the essential and prevents embarking on a
never-ending path of diminishing returns.


%prep
%autosetup -n %{name}-%{version} -p 1


%build
%{!?_auto_set_build_flags:%{set_build_flags}}
%make_build CFLAGS="${CFLAGS} -fPIE -std=c17 -Wall -Wextra -Wpedantic"


%install
%make_install PREFIX=%{_prefix}


%check
%{!?_auto_set_build_flags:%{set_build_flags}}
make check


%files
%license LICENSE
%doc README doc/*
%{_bindir}/%{name}


%changelog
%autochangelog
