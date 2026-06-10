%global build_type_safety_c 0

Name:             irsim
Version:          9.7.121
Release:          %autorelease
Summary:          Switch-level simulator used even for VLSI

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:          GPL-2.0-only
URL:              http://opencircuitdesign.com/%{name}
Source:           http://opencircuitdesign.com/%{name}/archive/%{name}-%{version}.tgz

Patch:            0000-missing-headers.patch

BuildRequires:    gcc
BuildRequires:    libXt-devel
BuildRequires:    m4
BuildRequires:    make
BuildRequires:    tcl-devel < 1:9
BuildRequires:    tk-devel < 1:9

%description
IRSIM is a tool for simulating digital circuits. It is a "switch-level"
simulator; that is, it treats transistors as ideal switches. Extracted
capacitance and lumped resistance values are used to make the switch a little
bit more realistic than the ideal, using the RC time constants to predict the
relative timing of events.

%prep
%autosetup -p1

%build
# The sources heavily rely on implicit ints and implicit function
# declarations and are not compatible with C99.
export CFLAGS="${CFLAGS} -std=gnu99"

# ./configure kills CFLAGS
# Invoke scripts/configure directly
(cd scripts && %configure)
%make_build

%install
%make_install INSTALL_BINDIR="%{_bindir}" INSTALL_LIBDIR="%{_libdir}"
rm -rf %{buildroot}%{_libdir}/%{name}/doc/

%files
%license COPYRIGHT
%doc README VERSION doc/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man3/%{name}-analyzer.3*
%{_mandir}/man5/netchange.5*

%changelog
%autochangelog
