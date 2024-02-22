%global _hardened_build 1

Summary: Bidirectional data relay between two data channels ('netcat++')
Name: socat
Version: 1.8.0.0
Release: %autorelease
License: GPL-2.0-only
Url:  http://www.dest-unreach.org/socat/
Source: http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires: openssl-devel readline-devel ncurses-devel
BuildRequires: autoconf kernel-headers > 2.6.18
# for make test
BuildRequires: iproute net-tools coreutils procps-ng openssl iputils

%description
Socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor (readline), a program, or a combination of two of these.


%prep
%setup -q
iconv -f iso8859-1 -t utf-8 CHANGES > CHANGES.utf8
mv CHANGES.utf8 CHANGES
%autopatch -p1

%build
# avoid warning on stderr disrupting tests
sed -i "s/FGREP=fgrep/FGREP='grep -F'/" configure
sed -i "s/fgrep/grep -F/" test.sh
sed -i "s/egrep/egrep -E/" test.sh
%configure  \
        --enable-help --enable-stdio \
        --enable-fdnum --enable-file --enable-creat \
        --enable-gopen --enable-pipe --enable-termios \
        --enable-unix --enable-ip4 --enable-ip6 \
        --enable-rawip --enable-tcp --enable-udp \
        --enable-listen --enable-proxy --enable-exec \
        --enable-system --enable-pty --enable-readline \
        --enable-openssl --enable-sycls --enable-filan \
        --enable-retry # --enable-fips

%make_build

%install
 %make_install
install -d %{buildroot}/%{_docdir}/socat
install -m 0644 *.sh %{buildroot}/%{_docdir}/socat/
echo ".so man1/socat.1" | gzip > %{buildroot}/%{_mandir}/man1/filan.1.gz
cp -a %{buildroot}/%{_mandir}/man1/filan.1.gz %{buildroot}/%{_mandir}/man1/procan.1.gz

%check
%ifarch x86_64
export TERM=ansi
export OD_C=/usr/bin/od
# intermittently, some tests fail and just hang
# FAILED on all arches:  146 478 528
# FAILED on i686: 311 313 513
# FAILED on 390s: 202 493
# FAILED:  146 (DSA algo disallowed?)
sed -i 's/NUMCOND=true/NUMCOND="test \\$N -ne 146 -a \\$N -ne 478 -a \\$N -ne 528"/' test.sh
make test
%endif

%files
%doc BUGREPORTS CHANGES DEVELOPMENT EXAMPLES FAQ PORTING
%doc COPYING* README SECURITY
%doc %{_docdir}/socat/*.sh
%{_bindir}/socat*
%{_bindir}/filan
%{_bindir}/procan
%doc %{_mandir}/man1/*

%autochangelog
