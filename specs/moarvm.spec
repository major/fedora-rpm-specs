Name:           moarvm
Version:        2025.10
Release:        %autorelease
Summary:        Metamodel On A Runtime Virtual Machine
License:        Artistic-2.0
URL:            https://github.com/MoarVM/MoarVM
Source:         %{url}/releases/download/%{version}/MoarVM-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  libffi-devel
BuildRequires:  libtommath-devel
BuildRequires:  libuv-devel
BuildRequires:  libzstd-devel
BuildRequires:  mimalloc-devel

%description
MoarVM (short for Metamodel On A Runtime Virtual Machine) is a runtime built
for the 6model object system. It is primarily aimed at running NQP and Rakudo,
but should be able to serve as a backend for any compilers built using the NQP
compiler toolchain.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libuv-devel
Requires:       mimalloc-devel
Requires:       libffi-devel
Requires:       libtommath-devel
Requires:       libzstd-devel

%description devel
This package contains development files for developing applications that use
%{name}.

%prep
%autosetup -p1 -n MoarVM-%{version}

# remove bundled libraries
rm -rf 3rdparty/{libuv,libatomicops,dyncall,libtommath,mimalloc}/

%build
%{__perl} Configure.pl --prefix=%{_prefix} --libdir=%{_libdir} \
  --has-libuv \
  --has-libffi \
  --c11-atomics \
  --has-libtommath \
  --has-mimalloc

%make_build

%install
%make_install

chmod 755 %{buildroot}%{_libdir}/libmoar.so

%files
%license LICENSE
%doc CREDITS docs
%{_bindir}/moar
%{_libdir}/libmoar.so
%{_datadir}/nqp/
%{_libdir}/libmoar.so-gdb.py

%files devel
%{_includedir}/moar/
%{_datadir}/pkgconfig/moar.pc

%changelog
%autochangelog
