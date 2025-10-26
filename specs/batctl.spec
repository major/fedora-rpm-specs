Name:           batctl
Version:        2025.4
Release:        %autorelease
Summary:        B.A.T.M.A.N. advanced control and management tool

License:        GPL-2.0-only AND MIT AND ISC
URL:            http://www.open-mesh.org/
Source0:        http://downloads.open-mesh.org/batman/stable/sources/batctl/%{name}-%{version}.tar.gz
Source1:        http://downloads.open-mesh.org/batman/stable/sources/batctl/%{name}-%{version}.tar.gz.asc
# Signing key of Simon Wunderlich <sw@simonwunderlich.de>
Source100:      https://keys.openpgp.org/pks/lookup?op=get&options=mr&search=0x2DE9541A85CC87D5D9836D5E0C8A47A2ABD72DF9#/sw.asc

# Require the batman-adv kernel module for convenience here
# It's not available on EL so make this conditional
# Also, Fedora < 21 doesn't support direct dependencies on kmods
%if 0%{?fedora} >= 21
Requires:       kmod(batman-adv.ko)
%endif
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  libnl3-devel

%description
batctl offers a convenient way to configure the batman-adv kernel module
as well as displaying debug information such as originator tables,
translation tables and the debug log. In combination with a bat-hosts
file batctl allows the use of host names instead of MAC addresses.

B.A.T.M.A.N. advanced operates on layer 2. Thus all hosts participating
in the virtual switched network are transparently connected together
for all protocols above layer 2. Therefore the common diagnosis tools
do not work as expected. To overcome these problems batctl contains the
commands ping, traceroute, tcpdump which provide similar functionality
to the normal ping(1), traceroute(1), tcpdump(1) commands, but modified
to layer 2 behavior or using the B.A.T.M.A.N. advanced protocol.


%prep
cat %{S:100} > %{_builddir}/%{name}.gpg
%{gpgverify} --keyring="%{_builddir}/%{name}.gpg" --signature="%{SOURCE1}" --data="%{SOURCE0}"
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags} -I%{_prefix}/include/libnl3" V=s


%install
%make_install PREFIX=%{_prefix} SBINDIR=%{_sbindir} install


%files
%doc CHANGELOG.rst README.rst bat-hosts.sample
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.gz


%changelog
%autochangelog
