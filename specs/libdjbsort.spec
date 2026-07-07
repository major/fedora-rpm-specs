Name:           libdjbsort
Version:        20260621
Release:        %autorelease
Summary:        Fast in-place numeric sorting library
License:        LicenseRef-Fedora-Public-Domain OR 0BSD OR MIT-0 OR MIT
URL:            https://sorting.cr.yp.to/
Source:         https://sorting.cr.yp.to/djbsort-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libcpucycles-devel
BuildRequires:  python3
BuildRequires:  python3-capstone
BuildRequires:  valgrind-devel


%description
djbsort sorts arrays of integers or floats in-place using sorting networks.
Sorting networks scale O(n log^2 n), but help to protect against
timing attacks.
Where available, djbsort uses vector instructions for better performance.
djbsort performs well in sorting benchmarks and thus is well-suited
in cryptographic and non-cryptographic contexts.


%package devel
Summary:        Development files for djbsort
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
djbsort headers and other development files.


%package static
Summary:        Static version of the djbsort library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description static
Statically linkable version of the djbsort library.


%prep
%autosetup -p1 -n djbsort-%{version}


%build
grep -r . compilers
echo '%{__cc} %{build_cflags} %{build_ldflags} -fPIC -fwrapv' > compilers/default
# library uses ifunc mechanism to runtime dispatch into vector optimized function versions
echo '%{__cc} %{build_cflags} %{build_ldflags} -mmmx -msse -msse2 -msse3 -mssse3 -msse4.1 -msse4.2 -mavx -mbmi -mbmi2 -mpopcnt -mavx2 -mtune=haswell -fPIC -fwrapv' > compilers/amd64+sse3+ssse3+sse41+sse42+popcnt+avx+bmi1+bmi2+avx2

./configure --prefix=%{_prefix}
%make_build
mv build build-shared

# rebuild static library with PIE instead of PIC ...
sed -i 's/-fPIC/-fPIE/' compilers/*
./configure --prefix=%{_prefix}
%make_build -C build/0 package/lib/libdjbsort.a
mv build build-static

# also rebuild executables
mkdir build-exe
%{__cc} %{build_cflags} %{build_ldflags} -fPIE -fwrapv -Ibuild-shared/0/package/include command/djbsort-speed.c -o build-exe/djbsort-speed -Lbuild-shared/0/package/lib -ldjbsort -lcpucycles
%{__cc} %{build_cflags} %{build_ldflags} -fPIE -fwrapv -Ibuild-shared/0/package/include -Ibuild-shared/0/include-build command/djbsort-test.c -o build-exe/djbsort-test -Lbuild-shared/0/package/lib -ldjbsort


%install
install -d %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} build-shared/0/package/bin/djbsort-fulltest
install -t %{buildroot}%{_bindir} build-exe/djbsort-{speed,test}
install -d %{buildroot}%{_includedir}
install -m 644 -t %{buildroot}%{_includedir} build-shared/0/package/include/djbsort.h
install -d %{buildroot}%{_libdir}
install -t %{buildroot}%{_libdir}  build-shared/0/package/lib/libdjbsort.so.1
ln -s libdjbsort.so.1 %{buildroot}%{_libdir}/libdjbsort.so
install -m 644 -t %{buildroot}%{_libdir} build-static/0/package/lib/libdjbsort.a
install -d %{buildroot}%{_mandir}/man1
install -m 644 -t %{buildroot}%{_mandir}/man1 build-shared/0/package/man/man1/djbsort-{speed,test,fulltest}.1
install -d %{buildroot}%{_mandir}/man3
install -m 644 -t %{buildroot}%{_mandir}/man3 build-shared/0/package/man/man3/djbsort.3
for i in {float,{,u}int}{32,64}{,down} ; do
    echo ".so man3/djbsort.3" > %{buildroot}%{_mandir}/man3/djbsort_$i.3
    chmod 644 %{buildroot}%{_mandir}/man3/djbsort_$i.3
done


%check
find %{buildroot} -ls
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/djbsort-speed
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/djbsort-test
# disabled since it make take up to an hour on medium build machines
#LD_LIBRARY_PATH=$PWD/build/0/package/lib PATH=$PWD/build/0/package/bin:$PATH build/0/package/bin/djbsort-fulltest


%files
%{_bindir}/djbsort-{speed,test,fulltest}
%{_libdir}/libdjbsort.so.1
%{_mandir}/man1/djbsort-{speed,test,fulltest}.1*
%doc doc/readme.md doc/security.md
%license doc/license.md


%files devel
%{_includedir}/djbsort.h
%{_libdir}/libdjbsort.so
%{_mandir}/man3/djbsort.3*
%{_mandir}/man3/djbsort_{float,{,u}int}{32,64}{,down}.3*


%files static
%{_libdir}/libdjbsort.a


%changelog
%autochangelog
