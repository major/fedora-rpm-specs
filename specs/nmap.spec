Name: nmap
Epoch: 4
Version: 7.92
#global prerelease TEST5
Release: %autorelease
Summary: Network exploration tool and security scanner
URL: http://nmap.org/
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/Q67UGCHSCKCLJOVOHSLYU4AERAHBS5YE/
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/543
License: LicenseRef-Nmap

Source0: http://nmap.org/dist/%{name}-%{version}%{?prerelease}.tar.bz2
Source1: https://nmap.org/dist/sigs/%{name}-%{version}.tar.bz2.asc
Source2: https://svn.nmap.org/nmap/docs/nmap_gpgkeys.txt

#prevent possible race condition for shtool, rhbz#158996
Patch1: nmap-4.03-mktemp.patch
#don't suggest to scan microsoft
Patch2: nmap-4.52-noms.patch
# upstream provided patch for rhbz#845005, not yet in upstream repository
Patch3: ncat_reg_stdin.diff
# TODO: review after GUI gets enabled again
#Patch4: nmap-6.25-displayerror.patch
# https://github.com/nmap/nmap/pull/2247
Patch7: nmap_resolve_config.patch
# backport of upstream pcre2 migration, rhbz#2128336
Patch8: nmap-pcre2.patch
# https://github.com/nmap/nmap/pull/2724
Patch9: nmap-ems-ssl-enum-ciphers.patch
# Fix build with libpcap 1.10.5
Patch10: nmap-libpcap.patch

BuildRequires: automake make
BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: libpcap-devel
%if 0%{?fedora} 
BuildRequires: libssh2-devel
%endif
BuildRequires: libtool
BuildRequires: lua-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: zlib-devel
BuildRequires: gnupg2
Requires: %{name}-ncat = %{epoch}:%{version}-%{release}

Obsoletes: nmap-frontend < 7.70-1
Obsoletes: nmap-ndiff < 7.70-1

%define pixmap_srcdir zenmap/share/pixmaps

%description
Nmap is a utility for network exploration or security auditing.  It supports
ping scanning (determine which hosts are up), many port scanning techniques
(determine what services the hosts are offering), and TCP/IP fingerprinting
(remote host operating system identification). Nmap also offers flexible target
and port specification, decoy scanning, determination of TCP sequence
predictability characteristics, reverse-identd scanning, and more. In addition
to the classic command-line nmap executable, the Nmap suite includes a flexible
data transfer, redirection, and debugging tool (netcat utility ncat), a utility
for comparing scan results (ndiff), and a packet generation and response
analysis tool (nping). 

%package ncat
Summary: Nmap's Netcat replacement
Requires(post): %{_sbindir}/alternatives
Requires(preun): %{_sbindir}/alternatives
Obsoletes: nc < 1.109.20120711-2
Obsoletes: nc6 < 1.00-22
Provides: nc = %{epoch}:%{version}-%{release}
Provides: nc6 = %{epoch}:%{version}-%{release}
Provides: ncat = %{epoch}:%{version}-%{release}

%description ncat
Ncat is a feature packed networking utility which will read and
write data across a network from the command line.  It uses both
TCP and UDP for communication and is designed to be a reliable
back-end tool to instantly provide network connectivity to other
applications and users. Ncat will not only work with IPv4 and IPv6
but provides the user with a virtually limitless number of potential
uses.


%prep
%{gpgverify} --keyring=%{SOURCE2} --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoconf -f

#TODO: stop using local copy of libdnet, once system distributed version
#supports sctp (grep sctp /usr/include/dnet.h)
#be sure we're not using tarballed copies of some libraries
#rm -rf liblua libpcap libpcre macosx mswin32 ###TODO###
rm -rf libpcap libpcre macosx mswin32 libssh2 libz

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
### TODO ## configure  --with-libpcap=/usr ###TODO###
%configure  --with-libpcap=yes --with-liblua=included \
  --without-zenmap --without-ndiff \
%if 0%{?fedora} 
  --with-libssh2=yes  \
%else
  --with-libssh2=no  \
%endif
  --enable-dbus 

%make_build

#fix man page (rhbz#813734)
sed -i 's/-md/-mf/' nping/docs/nping.1

%install
#prevent stripping - replace strip command with 'true'
make DESTDIR=%{buildroot} STRIP=true install

#do not include certificate bundle (#734389)
rm -f %{buildroot}%{_datadir}/ncat/ca-bundle.crt
rmdir %{buildroot}%{_datadir}/ncat

#we provide 'nc' replacement (#1653119)
touch %{buildroot}%{_mandir}/man1/nc.1.gz
touch %{buildroot}%{_bindir}/nc

%find_lang nmap --with-man

%post ncat
%{_sbindir}/alternatives --install %{_bindir}/nc nc %{_bindir}/ncat 10 \
  --slave %{_mandir}/man1/nc.1.gz nc-man %{_mandir}/man1/ncat.1.gz

%preun ncat
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove nc %{_bindir}/ncat
fi

%files -f nmap.lang
%license LICENSE
%doc docs/README
%doc docs/nmap.usage.txt
%{_bindir}/nmap
%{_bindir}/nping
%{_mandir}/man1/nmap.1.gz
%{_mandir}/man1/nping.1.gz
%{_datadir}/nmap

%files ncat 
%license LICENSE
%doc ncat/docs/AUTHORS ncat/docs/README ncat/docs/THANKS ncat/docs/examples
%ghost %{_bindir}/nc
%{_bindir}/ncat
%ghost %{_mandir}/man1/nc.1.gz
%{_mandir}/man1/ncat.1.gz

%changelog
%autochangelog
