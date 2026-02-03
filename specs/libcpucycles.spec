Name:           libcpucycles
Version:        20260105
Release:        %autorelease
Summary:        Library for counting CPU cycles
License:        LicenseRef-Fedora-Public-Domain OR 0BSD OR MIT-0 OR MIT
URL:            https://cpucycles.cr.yp.to/
Source:         https://cpucycles.cr.yp.to/libcpucycles-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3


%description
libcpucycles support several machine-level cycle counters and OS-level
mechanisms on many CPU architectures and auto-selects the best performing one
when it's initialized.


%package devel
Summary:        Development files for libcpucycles
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
libcpucycles headers and other development files.


%package static
Summary:        Static version of the libcpucycles library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description static
Statically linkable version of the libcpucycles library.


%prep
%autosetup


%build
cat compilers/default
# at of 2026-01: gcc -Wall -fPIC -fwrapv -O -fvisibility=hidden
echo '%{__cc} %{build_cflags} %{build_ldflags} -fPIC -fwrapv -fvisibility=hidden' > compilers/default
./configure --prefix=%{_prefix}
%make_build

# rebuild static library with PIE instead of PIC ...
echo '%{__cc} %{build_cflags} %{build_ldflags} -fPIE -fwrapv -fvisibility=hidden' > compilers/default
rm build/0/cpucycles/*.o
rm build/0/package/lib/libcpucycles.a
make -C build/0 package/lib/libcpucycles.a %{?_smp_mflags}


%install
%make_install
if [ %{buildroot}%{_prefix}/lib != %{buildroot}%{_libdir} ]; then
    mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
fi
chmod 755 %{buildroot}%{_libdir}/*.so.*
mkdir -p %{buildroot}%{_prefix}/share
mv %{buildroot}%{_prefix}/man %{buildroot}%{_prefix}/share


%check
LD_LIBRARY_PATH=$PWD/build/0/package/lib ./build/0/package/bin/cpucycles-info


%files
%{_libdir}/libcpucycles.so.1{,.*}
%{_bindir}/cpucycles-{info,open}
%{_mandir}/man1/cpucycles*.1*
%doc doc/counters.md doc/readme.md doc/security.md doc/selection.md
%license  doc/license.md


%files devel
%{_includedir}/cpucycles.h
%{_libdir}/libcpucycles.so
%{_mandir}/man3/cpucycles.3*


%files static
%{_libdir}/libcpucycles.a


%changelog
%autochangelog
