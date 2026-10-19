%global enable_fulltest %{!?enable_fulltest:0}%{?enable_fulltest:%enable_fulltest}
Name:           lib25519
Version:        20260614
Release:        %autorelease
Summary:        Fast X25519 encryption and Ed25519 signature microlibrary and CLI
License:        LicenseRef-Fedora-Public-Domain OR 0BSD OR MIT-0 OR MIT
URL:            https://lib25519.cr.yp.to/
Source:         https://lib25519.cr.yp.to/lib25519-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libcpucycles-devel
BuildRequires:  librandombytes-devel
BuildRequires:  python3
BuildRequires:  python3-capstone
BuildRequires:  valgrind-devel


%description

lib25519 provides stateless API and command line utilities for performing
Curve25519 elliptic curve encryption and signature operations.
Where available, lib25519 uses vector instructions for better performance.
It's implemented to protect against timing attacks and parts of its
implementation are formally verified.


%package devel
Summary:        Development files for lib25519
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
lib25519 headers and other development files.


%package static
Summary:        Static version of the 25519 library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description static
Statically linkable version of the 25519 library.


%prep
%autosetup -p1 -n lib25519-%{version}


%build
for i in $(find compilers -maxdepth 1 -type f -not -name '*.c'); do
    echo $i from $(cat $i)
    grep '^gcc ' $i | sed -e 's@-Wall\|-O[^ ]\+@@g' -e 's@^gcc @%{__cc} %{build_cflags} %{build_ldflags} @' > t
    mv t $i
    echo $i to $(cat $i)
done

./configure --prefix=%{_prefix}
%make_build
cp -a build build-shared
sed 's/-fPIC/-fPIE/' build/0/command/link -i
sed 's/-fPIC/-fPIE -pie/' build/0/scripts/cdcompile -i
rm build/0/package/bin/*
rm build/0/command/*.o
%make_build -C build/0 commands
mv build build-exe

# rebuild static library and executable with PIE instead of PIC ...
sed -i 's/-fPIC/-fPIE/' compilers/*
./configure --prefix=%{_prefix}
%make_build -C build/0 package/lib/lib25519.a
mv build build-static

%install
install -d %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} build-exe/0/package/bin/ed25519-{keypair,open,sign}
install -t %{buildroot}%{_bindir} build-exe/0/package/bin/lib25519-{fulltest,speed,test}
install -t %{buildroot}%{_bindir} build-exe/0/package/bin/x25519-{dh,keypair}
install -d %{buildroot}%{_includedir}
install -m 644 -t %{buildroot}%{_includedir} build-shared/0/package/include/lib25519.h
install -d %{buildroot}%{_libdir}
install -t %{buildroot}%{_libdir}  build-shared/0/package/lib/lib25519.so.1
ln -s lib25519.so.1 %{buildroot}%{_libdir}/lib25519.so
install -m 644 -t %{buildroot}%{_libdir} build-static/0/package/lib/lib25519.a
install -d %{buildroot}%{_mandir}/man1
install -m 644 -t %{buildroot}%{_mandir}/man1 build-shared/0/package/man/man1/ed25519.1
for i in cli keypair open sign ; do
    echo ".so man1/ed25519.1" > %{buildroot}%{_mandir}/man1/ed25519-$i.1
    chmod 644 %{buildroot}%{_mandir}/man1/ed25519-$i.1
done
install -m 644 -t %{buildroot}%{_mandir}/man1 build-shared/0/package/man/man1/lib25519-{fulltest,speed,test}.1
install -m 644 -t %{buildroot}%{_mandir}/man1 build-shared/0/package/man/man1/x25519.1
for i in cli dh keypair ; do
    echo ".so man1/x25519.1" > %{buildroot}%{_mandir}/man1/x25519-$i.1
    chmod 644 %{buildroot}%{_mandir}/man1/x25519-$i.1
done
install -d %{buildroot}%{_mandir}/man3
install -m 644 -t %{buildroot}%{_mandir}/man3 build-shared/0/package/man/man3/lib25519.3
for i in dh dh_keypair sign sign_keypair sign_open ; do
    echo ".so man3/lib25519.3" > %{buildroot}%{_mandir}/man3/lib25519_$i.3
    chmod 644 %{buildroot}%{_mandir}/man3/lib25519_$i.3
done


%check
find %{buildroot} -ls

for i in ed25519-{keypair,open,sign} lib25519-{speed,test} x25519-{dh,keypair} ; do
    echo Checking $i for PIE ...
    readelf -h %{buildroot}%{_bindir}/$i | grep '^ *Type: *DYN'  -q
done

LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/lib25519-speed
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/lib25519-test
# disabled since it make take up to an hour on medium build machines
%if %enable_fulltest
LD_LIBRARY_PATH=%{buildroot}%{_libdir} PATH=%{buildroot}%{_bindir}:$PATH %{buildroot}%{_bindir}/lib25519-fulltest
%endif

LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/ed25519-keypair 5>alice.edpub 9>alice.edpriv
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/ed25519-keypair 5>bob.edpub 9>bob.edpriv
echo 'Hello World!' > msg
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/ed25519-sign 8<alice.edpriv <msg >msg.signed
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/ed25519-open 4<alice.edpub <msg.signed >msg2
cmp msg msg2
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/x25519-keypair 5>alice.xpub 9>alice.xpriv
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/x25519-keypair 5>bob.xpub 9>bob.xpriv
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/x25519-dh 8<alice.xpriv 4<bob.xpub 7>alice-bob.sec
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/x25519-dh 8<bob.xpriv 4<alice.xpub 7>bob-alice.sec
cmp alice-bob.sec bob-alice.sec

set +e
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/ed25519-open 4<bob.edpub <msg.signed >msg3
if [ "$?" -eq 0 ]; then
    echo "ed25519-open didn't detect invalid signature: $?" >&2
    exit 1
fi
set -e


%files
%{_bindir}/ed25519-{keypair,open,sign}
%{_bindir}/lib25519-{fulltest,speed,test}
%{_bindir}/x25519-{dh,keypair}
%{_libdir}/lib25519.so.1
%{_mandir}/man1/ed25519{-{cli,keypair,open,sign},}.1*
%{_mandir}/man1/lib25519-{fulltest,speed,test}.1*
%{_mandir}/man1/x25519{-{cli,dh,keypair},}.1*
%doc doc/readme.md doc/security.md
%license doc/license.md
%license LICENSES/0BSD.txt
%license LICENSES/MIT-0.txt
%license LICENSES/MIT.txt


%files devel
%{_includedir}/lib25519.h
%{_libdir}/lib25519.so
%{_mandir}/man3/lib25519{_{,dh,dh_keypair,sign,sign_keypair,sign_open},}.3*


%files static
%{_libdir}/lib25519.a


%changelog
%autochangelog
