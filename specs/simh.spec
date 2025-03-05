Name:           simh
Version:        3.12.5
Release:        %autorelease
Summary:        Highly portable, multi-system emulator

# The licensing is mostly MIT, but there is also some GPL+ (literally, v1+) code
# in there, notably in AltairZ80/.
# (each target is compiled into its own binary, so only AltairZ80 is GPL+)
License:        MIT AND GPL-1.0-or-later

URL:            http://simh.trailing-edge.com/
Source0:        simh-%{version}-noroms.tar.gz
# we use
# this script to remove the roms binary and patented code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./simh-generate-tarball.sh 3.8.1
Source1:        simh-generate-tarball.sh
Patch:          https://gitlab.archlinux.org/archlinux/packaging/packages/simh/-/raw/3.12.5-1/build-fix.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  libpcap-devel

%description
SIMH is a historical computer simulation system. It consists of simulators
for many different computers, all written around a common user
interface package and set of supporting libraries.
SIMH can be used to simulate any computer system for which sufficient detail
is available, but the focus to date has been on simulating computer systems
of historic interest.

SIMH implements simulators for:

* Data General Nova, Eclipse
* Digital Equipment Corporation PDP-1, PDP-4, PDP-7, PDP-8, PDP-9, PDP-10,
  PDP-11, PDP-15, VAX
* GRI Corporation GRI-909, GRI-99
* IBM 1401, 1620, 7090/7094, System 3
* Interdata (Perkin-Elmer) 16b and 32b systems
* Hewlett-Packard 2114, 2115, 2116, 2100, 21MX, 1000
* Honeywell H316/H516
* MITS Altair 8800, with both 8080 and Z80
* Royal-Mcbee LGP-30, LGP-21
* Scientific Data Systems SDS 940

%prep
%autosetup -n %{name}-%{version}/sim -p1

# Convert docs to UNIX line endings
sed -i 's/\r$//' */*.txt

%build
CC="$CC -I . -fPIE -g -D_LARGEFILE64_SOURCE"
LDFLAGS="$LDFLAGS -lm -lpcap"
%make_build -e ROMS_OPT="%{optflags}" USE_NETWORK=1 LIBPATH="${_libdir}"

%install
for i in BIN/*; do
  [ -f "$i" ] && install -Dpm0755 "$i" "%{buildroot}%{_bindir}/simh-$(basename "$i")"
done

%files
%{_bindir}/simh-altair
%{_bindir}/simh-eclipse
%{_bindir}/simh-gri
%{_bindir}/simh-h316
%{_bindir}/simh-i1401
%{_bindir}/simh-i1620
%{_bindir}/simh-i7094
%{_bindir}/simh-id16
%{_bindir}/simh-id32
%{_bindir}/simh-lgp
%{_bindir}/simh-nova
%{_bindir}/simh-pdp1
%{_bindir}/simh-pdp10
%{_bindir}/simh-pdp11
%{_bindir}/simh-pdp15
%{_bindir}/simh-pdp4
%{_bindir}/simh-pdp7
%{_bindir}/simh-pdp8
%{_bindir}/simh-pdp9
%{_bindir}/simh-sds
%{_bindir}/simh-sigma
%{_bindir}/simh-uc15
%{_bindir}/simh-vax
%{_bindir}/simh-vax780
%doc ALTAIR/altair.txt NOVA/eclipse.txt
%doc I7094/i7094_bug_history.txt Interdata/id_diag.txt
%doc PDP1/pdp1_diag.txt PDP10/pdp10_bug_history.txt PDP18B/pdp18b_diag.txt
%doc S3/haltguide.txt S3/readme_s3.txt S3/system3.txt SDS/sds_diag.txt
%doc VAX/vax780_bug_history.txt

%changelog
%autochangelog
