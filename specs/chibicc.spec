%global commit 90d1f7f199cc55b13c7fdb5839d1409806633fdb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20201207
Name:           chibicc
Version:        0.0^%{date}.%{shortcommit}
Release:        %{autorelease}
Summary:        A small C compiler

License:        MIT
URL:            https://github.com/rui314/chibicc
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  glibc-static
BuildRequires:  make
# Other architectures are not supported
ExclusiveArch:  x86_64

%description
chibicc is yet another small C compiler that implements most C11 features.
Even though it still probably falls into the "toy compilers" category just
like other small compilers do, chibicc can compile several real-world
programs, including Git, SQLite, libpng and chibicc itself, without making
modifications to the compiled programs. Generated executables of these
programs pass their corresponding test suites. So, chibicc actually supports
a wide variety of C11 features and is able to compile hundreds of thousands
of lines of real-world C code correctly.

If you like this project, please consider purchasing a copy of the book when
it becomes available! I publish the source code here to give people early
access to it, because I was planing to do that anyway with a permissive
open-source license after publishing the book. If I don't charge for the source
code, it doesn't make much sense to me to keep it private.

%prep
%autosetup -n %{name}-%{commit}
sed -i 's/CFLAGS=-std=c11/CFLAGS+=-std=c11/g' Makefile

%build
%make_build


%install
install -D -p -m 755 chibicc %{buildroot}%{_bindir}/chibicc
mkdir -p %{buildroot}%{_includedir}/chibicc
install -p -m 644 include/*.h %{buildroot}%{_includedir}/chibicc/
install -p -m 644 chibicc.h %{buildroot}%{_includedir}/

%check
make test-all

%files
%license LICENSE
%doc README.md
%{_bindir}/chibicc
%{_includedir}/chibicc.h
%dir %{_includedir}/chibicc
%{_includedir}/chibicc/*.h

%changelog
%autochangelog
