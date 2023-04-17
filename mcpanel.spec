Name:           mcpanel
Version:        1.1
%global so_version 0
Release:        %autorelease
Summary:        C library providing multichannel scope interface

# The text of the file COPYING is version 3 of the GPL.
#
# The entire source is GPL-3.0-or-later based on the license statements in the
# source file headers, except:
#
#   - m4/ld-output-def.m4 is FSFULLR, but belongs to the Autotools build
#     scripts and does not contribute to the licenses of the binary RPMs
#   - meson.build has a License field of LGPL-3.0; we treat this as if it means
#     some unspecified portion of the library is LGPL-3.0-only for now, but we
#     have asked for clarification in
#     https://github.com/mmlabs-mindmaze/mcpanel/issues/9.
#   - src/led_{blue,gray,green,red}.png are CC0-1.0 as specified in
#     src/led.license, and contribute only to the -data subpackage; as image
#     resources, these should be considered content and therefore this is an
#     allowed license for them
License:        GPL-3.0-or-later AND LGPL-3.0-only
URL:            https://opensource.mindmaze.com/projects/mcpanel/
Source0:        https://github.com/mmlabs-mindmaze/mcpanel/archive/%{version}/mcpanel-%{version}.tar.gz

# Include <rtf_common.h> for a declaration of rtf_create_butterworth
# https://github.com/mmlabs-mindmaze/mcpanel/pull/10
Patch:          mcpanel-c99.patch

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  rtfilter-devel

Requires:       mcpanel-data = %{version}-%{release}

%description
This package provides a library written in C implementing a set of widgets
designed to view in realtime multichannels signals. While it has been initially
designed to view signals coming from a BIOSEMI Activetwo system, it is totally
system agnostic and any user of other systems might find it useful.

%package        devel
Summary:        Development files for mcpanel

Requires:       mcpanel%{?_isa} = %{version}-%{release}

%description    devel
The mcpanel-devel package contains libraries and header files for
developing applications that use mcpanel.

%package        data
Summary:        Data files for mcpanel
# See the license breakdown above the base package’s License field; the CC0-1.0
# PNG images appear *only* in this subpackage, but it also contains a .ui file
# that we must treat as having the same license as the base package.
License:        GPL-3.0-or-later AND LGPL-3.0-only AND CC0-1.0

BuildArch:      noarch

%description    data
The mcpanel-data package contains architecture-independent data files for
mcpanel.

%prep
%autosetup -p1

%build
# We could build the tests (after adding a BR on mmlib-devel), but we can’t
# usefully run them non-interactively (even with xvfb-run).
%meson -Dtests=false
%meson_build

%install
%meson_install

%files
%{_libdir}/libmcpanel.so.%{so_version}{,.*}

%files devel
%{_includedir}/mcpanel.h
%{_libdir}/libmcpanel.so
%{_libdir}/pkgconfig/mcpanel.pc

%files data
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/mcpanel/

%changelog
%autochangelog
