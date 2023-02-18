Name:           moarvm
Version:        2022.12
Release:        %autorelease
Summary:        Metamodel On A Runtime Virtual Machine
License:        Artistic-2.0
URL:            https://moarvm.org/
Source:         https://github.com/MoarVM/MoarVM/releases/download/%{version}/MoarVM-%{version}.tar.gz
# Add --has-mimalloc option to use system mimalloc
# https://github.com/MoarVM/MoarVM/pull/1742
Patch0:         use-system-mimalloc.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  libffi-devel
BuildRequires:  libatomic_ops-devel
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
Summary:        Header files for MoarVM development

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libffi-devel
Requires:       libatomic_ops-devel
Requires:       libtommath-devel
Requires:       libuv-devel
Requires:       libzstd-devel
Requires:       mimalloc-devel

%description devel
This package contains header files for developing applications that use
moarvm (Metamodel On A Runtime).

%prep
%autosetup -p1 -n MoarVM-%{version}

# make sure to not bundle this
rm -rf 3rdparty/libuv
rm -rf 3rdparty/libatomicops
rm -rf 3rdparty/dyncall
rm -rf 3rdparty/libtommath
rm -rf 3rdparty/mimalloc

%build
%{__perl} Configure.pl --prefix=%{_prefix} --libdir=%{_libdir} \
  --has-libuv \
  --has-libffi \
  --has-libatomic_ops \
  --has-libtommath \
  --has-mimalloc
%{make_build}

%install
%{make_install}

chmod 755 %{buildroot}%{_libdir}/libmoar.so

%files
%license LICENSE
%doc CREDITS docs
%{_bindir}/moar
%{_libdir}/libmoar.so
%{_datadir}/nqp

%files devel
%{_includedir}/moar
%{_datadir}/pkgconfig/moar.pc

%changelog
%autochangelog
