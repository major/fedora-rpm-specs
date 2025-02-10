Name:      sile
Version:   0.14.17
Release:   %autorelease
Summary:   The SILE Typesetter
License:   MIT
URL:       https://sile-typesetter.org/
Source:    https://github.com/sile-typesetter/sile/releases/download/v%{version}/sile-%{version}.tar.xz

# Missing in the source tarball
# https://github.com/sile-typesetter/sile/issues/2100
Source1:   https://raw.githubusercontent.com/sile-typesetter/libtexpdf/736a5e7530c13582ea704a061a358d0caa774916/LICENSE#/LICENSE-libtexpdf

BuildRequires: lua
BuildRequires: lua-devel
BuildRequires: gcc
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: git
BuildRequires: jq
BuildRequires: /usr/bin/pdfinfo
BuildRequires: harfbuzz-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: lua-rpm-macros lua-srpm-macros

BuildRequires: lua-cassowary
BuildRequires: lua-cldr
BuildRequires: lua-cliargs
BuildRequires: lua-cosmo
BuildRequires: lua-expat
BuildRequires: lua-filesystem
BuildRequires: lua-fluent
BuildRequires: lua-linenoise
BuildRequires: lua-loadkit
BuildRequires: lua-lpeg
BuildRequires: lua-luarepl
BuildRequires: lua-penlight
BuildRequires: lua-sec
BuildRequires: lua-socket
BuildRequires: lua-luautf8
BuildRequires: lua-vstruct
BuildRequires: lua-zlib

BuildRequires: font(gentiumplus)

Requires: lua-cassowary
Requires: lua-cldr
Requires: lua-cliargs
Requires: lua-cosmo
Requires: lua-expat
Requires: lua-filesystem
Requires: lua-fluent
Requires: lua-linenoise
Requires: lua-loadkit
Requires: lua-lpeg
Requires: lua-luarepl
Requires: lua-penlight
Requires: lua-sec
Requires: lua-socket
Requires: lua-luautf8
Requires: lua-vstruct
Requires: lua-zlib
Requires: libtexpdf%{?_isa} = %{version}-%{release}


Recommends: font(gentiumplus)
Suggests:   font(libertinusmath)
Suggests:   font(libertinussans)
Suggests:   font(libertinusserif)
Suggests:   font(hack)

Provides: bundled(lua-lunamark)

%description
SILE is a typesetting system; its job is to produce beautiful printed documents.
Conceptually, SILE is similar to TeX—from which it borrows some concepts and
even syntax and algorithms—but the similarities end there.
Rather than being a derivative of the TeX family SILE is a new typesetting and
layout engine written from the ground up using modern technologies and borrowing
some ideas from graphical systems such as InDesign.

%package -n libtexpdf
Summary: A PDF library extracted from TeX's dvipdfmx
License: GPL-2.0-only

%description -n libtexpdf
%{summary}.

%package -n libtexpdf-devel
Summary:  Development files for libtexpdf
License:  GPL-2.0-only
Requires: libtexpdf%{?_isa} = %{version}-%{release}

%description -n libtexpdf-devel
%{summary}.

%prep
%autosetup
cp %{SOURCE1} LICENSE-libtexpdf

%build
%configure --disable-static --with-system-luarocks

%make_build all

%install
%make_install

%check
export SILE_PATH=$(pwd)
echo -n '\document{foo}' | ./sile - -o foo.pdf

%files
%license LICENSE
%license lua-libraries/LICENSE-lunamark

%doc README.md
%doc CHANGELOG.md
%{_bindir}/sile
%{_datadir}/sile
%{_libdir}/sile
%{_mandir}/man1/sile.1*

%files -n libtexpdf
%license LICENSE-libtexpdf
%doc libtexpdf/README.md
%{_libdir}/libtexpdf.so.0
%{_libdir}/libtexpdf.so.0.0.0

%files -n libtexpdf-devel
%license LICENSE-libtexpdf
%doc libtexpdf/README.md
%{_includedir}/libtexpdf
%{_libdir}/libtexpdf.so

%changelog
%autochangelog
