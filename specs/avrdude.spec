%global udev_rules_old 70-avrdude-devices.rules
%global udev_rules_gen 71-avrdude-devices.rules

# Allow skipping doc builds for faster mockbuilds without the
# literally hundreds of extra packages required for building docs.
%bcond_without docs

Name:           avrdude
Version:        8.2
Release:        %autorelease
Summary:        Software for programming Atmel AVR Microcontroller

License:        GPL-2.0-or-later AND GPL-3.0-only AND (WTFPL OR MIT)
URL:            https://github.com/avrdudes/avrdude

# Upstream avrdude have no 4big endian support planned.
# https://bugzilla.redhat.com/show_bug.cgi?id=2308947
# https://github.com/avrdudes/avrdude/issues/1917
ExcludeArch:    s390x

Source0:        https://github.com/avrdudes/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Debian have a more comprehensive list of programmer devices in their
# avrdude.dev file. We do cannot use this unchanged, though, as we do
# not want to grant blanket access to all ttyUSB and ttyACM devices.
# Source1:        https://salsa.debian.org/debian/avrdude/-/raw/master/debian/avrdude.udev
Source1:        avrdude.udev

# Remarks on the Fedora package for the users
Source2:        README.fedora

# Quick fix elf2tag man page
Source5:        elf2tag.1

# Stop granting blanket access to all /dev/tty{ACM,USB}* devices
Patch:          avrdude-udev-no-blanket-access.patch

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  elfutils-libelf-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  hidapi-devel
BuildRequires:  libftdi-devel
%if ((0%{?fedora} >= 1) || (0%{?rhel} >= 8))
BuildRequires:  libgpiod-devel
%endif
# EL does not have libhid-devel
%if 0%{?fedora} >= 28
BuildRequires:  libhid-devel
%endif
%if ((0%{?fedora} >= 1) || (0%{?rhel} >= 9))
BuildRequires:  libserialport-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
%if %{with docs}
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
%endif


%description
AVRDUDE is a program for programming Atmel's AVR CPU's. It can program the
Flash and EEPROM, and where supported by the serial programming protocol, it
can program fuse and lock bits. AVRDUDE also supplies a direct instruction
mode allowing one to issue any programming instruction to the AVR chip
regardless of whether AVRDUDE implements that specific feature of a
particular chip.


%prep
%autosetup -N
cp -p %{SOURCE1} avrdude.udev
%autopatch -v -p1
if test -d atmel-docs; then
  echo "Directory 'atmel-docs' still exists, aborting."
  exit 2
fi


%build
%cmake \
       -D CMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
       -D CMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
%if %{with docs}
       -D BUILD_DOC:BOOL=ON \
%else
       -D BUILD_DOC:BOOL=OFF \
%endif
       -D HAVE_LINUXSPI:BOOL=ON \
       -D HAVE_LINUXGPIO:BOOL=ON \
       -D HAVE_PARPORT:BOOL=ON \
       -D FETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
       -D FETCHCONTENT_QUIET:BOOL=OFF \
       -D FORCE_DISABLE_PYTHON_SUPPORT:BOOL=ON \
       -D BUILD_SHARED_LIBS:BOOL=NO \
       -D USE_STATIC_LIBS:BOOL=YES

if test -d _deps; then
  echo "cmake appears to have fetched some dependency despite our precautions:"
  ls -l _deps
  exit 2
fi

%cmake_build

# generate set of udev rules from avrdude.conf
%{__cmake_builddir}/src/avrdude -C %{__cmake_builddir}/src/avrdude.conf -c '*/u' \
  | sed -n '/ACTION!=/,$p' \
  | sed 's|, MODE="0660"||' \
  > genset.rules
test -s genset.rules


%install
%cmake_install

rm -f %{buildroot}%{_infodir}/dir

rm -f %{buildroot}%{_includedir}/libavrdude-avrintel.h
rm -f %{buildroot}%{_includedir}/libavrdude.h
rm -f %{buildroot}%{_libdir}/libavrdude.a

install -d -m 755              %{buildroot}%{_udevrulesdir}
install -p -m 644 avrdude.udev %{buildroot}%{_udevrulesdir}/%{udev_rules_old}
install -p -m 644 genset.rules %{buildroot}%{_udevrulesdir}/%{udev_rules_gen}

install -d -m 755            %{buildroot}%{_pkgdocdir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_pkgdocdir}/README.fedora
install -p -m 644         -t %{buildroot}%{_pkgdocdir} AUTHORS NEWS README.md

install -d -m 755            %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE5} %{buildroot}%{_mandir}/man1/elf2tag.1


%check
%ctest


%files
%license COPYING
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/README.fedora
%if %{with docs}
%doc %{_pkgdocdir}/avrdude-html/
%doc %{_pkgdocdir}/avrdude.pdf
%endif
%config(noreplace) %{_sysconfdir}/avrdude.conf
%{_udevrulesdir}/%{udev_rules_old}
%{_udevrulesdir}/%{udev_rules_gen}
%{_bindir}/avrdude
%{_bindir}/elf2tag
%{_mandir}/man1/avrdude.1*
%{_mandir}/man1/elf2tag.1*
%if %{with docs}
%{_infodir}/avrdude.info*
%endif


%changelog
%autochangelog
