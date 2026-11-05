Name:           4th
Version:        3.64.2
Release:        %autorelease
Summary:        A Forth compiler

License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://thebeez.home.xs4all.nl/4tH/
Source0:        https://downloads.sourceforge.net/project/forth-4th/%{name}-%{version}/%{name}-%{version}-unix.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
4tH is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low overhead.


%package devel
Summary:        Development files for 4th
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes headers for development with 4th, a Forth compiler
library.


%prep
%setup -q -n %{name}-%{version}
%ifarch aarch64 loongarch64 ppc64le riscv64 s390x x86_64
cp -p sources/include64/*.h sources/
%else
cp -p sources/include32/*.h sources/
%endif


%build
%set_build_flags
MYCFLAGS="-DUNIX -fsigned-char $CFLAGS $LDFLAGS -fPIC"
LD_LIBRARY_PATH="$PWD/sources/" \
%make_build -C sources \
        STATIC= SHARED=1 \
        CFLAGS="$MYCFLAGS"


%install
mkdir -p \
        %{buildroot}%{_libdir} \
        %{buildroot}%{_includedir}/%{name} \
        %{buildroot}%{_bindir} \
        %{buildroot}%{_mandir} \
        %{buildroot}%{_docdir}/%{name}

%set_build_flags
MYCFLAGS="-DUNIX -fsigned-char $CFLAGS $LDFLAGS -fPIC"
LD_LIBRARY_PATH="$PWD/sources/" \
%make_install -C sources \
        STATIC= SHARED=1 \
        CFLAGS="$MYCFLAGS" \
        LIBRARIES=%{buildroot}%{_libdir} \
        INCLUDES=%{buildroot}%{_includedir} \
        BINARIES=%{buildroot}%{_bindir} \
        MANDIR=%{buildroot}%{_mandir} \
        DOCDIR=%{buildroot}%{_docdir}
install -Dpm 0644 sources/4th.h %{buildroot}%{_includedir}/%{name}/4th.h


%check
LD_LIBRARY_PATH="$PWD/sources/" \
sources/4th cxq 4th/demo/hello.4th

# Run VM test
cd 4th
LD_LIBRARY_PATH="../sources/" \
../sources/4th cxq vm-test.4th


%files
%{_libdir}/lib4th.so.3*
%{_bindir}/4tsh
%{_bindir}/pp4th
%{_bindir}/4th
%{_mandir}/man1/4th.1*
%{_mandir}/man1/pp4th.1*
%doc %{_docdir}/%{name}/4tHmanual.pdf
%doc README
%license COPYING


%files devel
%{_libdir}/lib4th.so
%{_includedir}/%{name}


%changelog
%autochangelog
