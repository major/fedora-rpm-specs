%bcond autoreconf 1

Name:           eot-utils
Version:        1.1
Release:        %autorelease
Summary:        Create or examine EOT font format files

# SPDX
#
# The entire source is W3C, except for certain build system files, the licenses
# of which do not contribute to the license of the binary RPM:
#   - aclocal.m4 is FSFULLR
#   - configure is FSFUL, or more likely (W3C AND FSFUL)
#   - depcomp and missing are GPL-2.0-or-later
#   - install-sh is X11
License:        W3C
URL:            https://www.w3.org/Tools/eot-utils/
Source:         %{url}/eot-utilities-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

%description
The eot-utils are the two programs mkeot and eotinfo. The former creates an EOT
(Embedded OpenType) file from an OpenType or TrueType font and the URLs of one
or more Web pages, respecting the TrueType embedding bits. The eotinfo program
displays EOT metadata in a human-readable way.


%prep
%autosetup -n eot-utilities-%{version}


%build
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc README

%{_bindir}/mkeot
%{_bindir}/eotinfo

%{_mandir}/man1/mkeot.1*
%{_mandir}/man1/eotinfo.1*


%changelog
%autochangelog
