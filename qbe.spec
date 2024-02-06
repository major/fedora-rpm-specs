%bcond snapshot 1

%global srcver      1.1
%global commit      2d683e0c53907ebca9abde876dd87af70719e42d
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global commitdate  20240129
%global snapshotver %{commitdate}.%{shortcommit}

Name:           qbe
Version:        %{srcver}%{?with_snapshot:^%{snapshotver}}
Release:        %autorelease
Summary:        A pure C embeddable compiler backend

License:        MIT
URL:            https://c9x.me/compile/
Source0:        %{url}/release/%{name}-%{srcver}.tar.xz

%if %{with snapshot}
Patch:          0000-snapshot-%{srcver}-%{shortcommit}.patch
%endif

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
%autosetup -n %{name}-%{srcver} -p 1


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
