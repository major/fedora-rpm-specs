Name:           librandombytes
Version:        20240318
Release:        %autorelease
Summary:        Library for portably obtaining cryptographically secure randomness
License:        LicenseRef-Fedora-Public-Domain OR 0BSD OR MIT-0 OR MIT
URL:            https://randombytes.cr.yp.to/
Source:         https://randombytes.cr.yp.to/librandombytes-%{version}.tar.gz
Patch:          librandombytes-soname.diff

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  openssl-devel

Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives


%description
librandombytes provides an abstraction over suitable syscalls such as
getrandom(), /dev/urandom and OpenSSL's RAND_bytes().


%package devel
Summary:        Development files for librandombytes
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
librandombytes headers and other development files.


%package static
Summary:        Static version of the librandombytes library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description static
Statically linkable version of the librandombytes library.


%prep
%autosetup -p1


%build
cat compilers/default
# as of 20240318: gcc -Wall -fPIC -fwrapv -O
# NB: -fvisibility=hidden is added via another wrapper
echo '%{__cc} %{build_cflags} %{build_ldflags} -fPIC -fwrapv' > compilers/default
./configure --prefix=%{_prefix}
%make_build

mv build build-shared

# rebuild static library with PIE instead of PIC ...
echo '%{__cc} %{build_cflags} %{build_ldflags} -fPIE -fwrapv' > compilers/default
./configure --prefix=%{_prefix}
%make_build


%install
install -d %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} build-shared/0/package/bin/randombytes-info
install -d %{buildroot}%{_includedir}
install -m 644 -t %{buildroot}%{_includedir} build-shared/0/package/include/randombytes.h
install -d %{buildroot}%{_libdir}/randombytes
install -T build-shared/0/package/lib/librandombytes-kernel.so.1 %{buildroot}%{_libdir}/randombytes/kernel.so.1
install -T build-shared/0/package/lib/librandombytes-openssl.so.1 %{buildroot}%{_libdir}/randombytes/openssl.so.1
ln -s librandombytes.so.1 %{buildroot}%{_libdir}/librandombytes.so
# librandombytes.so.1 is provided by alternatives mechanism
install -m 644 -t %{buildroot}%{_libdir} build/0/package/lib/librandombytes-{kernel,openssl}.a
ln -s librandombytes-kernel.a %{buildroot}%{_libdir}/librandombytes.a
install -d %{buildroot}%{_mandir}/man1
install -m 644 -t %{buildroot}%{_mandir}/man1 build-shared/0/package/man/man1/randombytes-info.1
install -d %{buildroot}%{_mandir}/man3
install -m 644 -t %{buildroot}%{_mandir}/man3 build-shared/0/package/man/man3/randombytes.3


%check
find %{buildroot} -ls
LD_LIBRARY_PATH=$PWD/build-shared/0/package/lib ./build-shared/0/package/bin/randombytes-info


%post
alternatives --install %{_libdir}/librandombytes.so.1 librandombytes %{_libdir}/randombytes/kernel.so.1  50
alternatives --install %{_libdir}/librandombytes.so.1 librandombytes %{_libdir}/randombytes/openssl.so.1 40

%preun
if [ $1 = 0 ]; then
  alternatives --remove-all librandombytes
fi


%files
%{_bindir}/randombytes-info
%dir %{_libdir}/randombytes
%{_libdir}/randombytes/{kernel,openssl}.so.1
%ghost %attr(0644,root,root) %{_libdir}/librandombytes.so.1
%{_mandir}/man1/randombytes-info.1*
%doc doc/readme.md doc/security.md
%license  doc/license.md


%files devel
%{_includedir}/randombytes.h
%{_libdir}/librandombytes.so
%{_mandir}/man3/randombytes.3*


%files static
%{_libdir}/librandombytes.a
%{_libdir}/librandombytes-{kernel,openssl}.a


%changelog
%autochangelog
