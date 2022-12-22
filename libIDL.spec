Name:           libIDL
Summary:        Library for parsing IDL (Interface Definition Language)
Version:        0.8.14
%global so_version 0
Release:        %autorelease

# The entire source is LGPL-2.0-or-later, except:
#   • The following are GPL-3.0-or-later:
#       - texinfo.tex
#       - libIDL2.info
#       - libIDL2.texi
#     The generated HTML documentation is also derived from texinfo.tex, and is
#     therefore also GPL-3.0-or-later. These files comprise the entire contents
#     of the -doc subpackage.
#
# Additionally, the following files do not contribute to the license of the
# binary RPMs because they belong to the build system or are otherwise not
# compiled and/or installed.
#   • The following are FSFULLR, or since they are derived from the corresponding
#     Makefile.am files, perhaps more properly (LGPL-2.0-or-later AND FSFULLR):
#       - Makefile.in and */Makefile.in
#   • The following are FSFUL, or since they are derived from the corresponding
#     configure.in file, perhaps more properly (LGPL-2.0-or-later AND FSFUL):
#       - configure
#   • The following are (clearly only) FSFULLR:
#       - aclocal.m4
#   • The following are GPL-2.0-or-later:
#       - config.guess
#       - config.sub
#       - depcomp
#       - ltmain.sh
#       - missing
License:        LGPL-2.0-or-later
%global minorversion %(echo '%{version}' | cut -d . -f 1-2)
URL:            https://download.gnome.org/sources/libIDL/%{minorversion}/
Source0:        %{url}/libIDL-%{version}.tar.bz2
# Hand-written man page:
Source1:        libIDL-config-2.1

# Note that upstream is dead; GNOME still offers just a download page, and the
# VCS was migrated to https://gitlab.gnome.org/Archive/libidl, but the project
# is archived and therefore no bug tracker is offered. An old email address for
# the ORBIT development mailing list is offered in the HACKING file, but the
# archived status of the project shows that nothing will be done with patches.
# Any patches below will therefore not be sent upstream, because there is
# nowhere for them to go.
#
# Normally this would be the time to re-evaluate whether the package still
# belongs in Fedora, but ORBit2 still requires it, and at least libgnome and
# libbonobo require that, so it is in the dependency chain of a great many
# packages.

# Fix paths reported by the libIDL-config-2 tool to conform with Fedora
# multilib installation paths:
Patch:          libIDL-0.8.6-multilib.patch
# Remove an unused parent-node variable in the primary_expr part of the parser,
# which caused a compiler warning.
Patch:          libIDL-0.8.14-parser-primary_expr-unused-parent-node.patch
# On platforms (such as 64-bit Linux), where long long int and long int are
# both 64-bit, we can have IDL_LL defined to ll (format with %%lld) while
# IDL_longlong_t, which is just gint64, may be ultimately defined to long int.
# This results in compiler warnings about the mismatch between the long long
# format and long parameter, even though the types are compatible. We can fix
# this with a cast to (long long) before formatting.
Patch:          libIDL-0.8.14-long-long-format-warnings.patch
# Instead of type-punning with sscanf, parse into a temporary with a type
# matching the format code and then memmove into the “integer” storage. This is
# no less platform-dependent, but does not invoke undefined behavior or produce
# a compiler warning.
Patch:          libIDL-0.8.14-lexer-sscanf-type-punning.patch
# Fix references to the old libIDL-config script by changing them to
# libIDL-config-2.
Patch:          libIDL-0.8.14-old-libIDL-config-script.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  flex
BuildRequires:  bison

BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)

%global common_description %{expand:
libIDL is a library for parsing IDL (Interface Definition Language). It can be
used for both COM-style and CORBA-style IDL.}

%description %{common_description}


%package devel
Summary:        Development libraries and header files for libIDL

Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}

%description devel %{common_description}

This package contains the header files and libraries needed to write or compile
programs that use libIDL.


%package doc
Summary:        Documentation for libIDL
License:        GPL-3.0-or-later

BuildArch:      noarch

%description doc %{common_description}

This page contains info pages and HTML and PDF documentation for libIDL.


%prep
%autosetup -p1


%build
%configure --disable-static
# We re-generate the info page, and also build PDF and HTML docs from the
# texinfo source.
rm libIDL2.info
%make_build all libIDL2.info libIDL2.html libIDL2.pdf


%install
%make_install
rm '%{buildroot}%{_libdir}/libIDL-2.la'
rm '%{buildroot}%{_infodir}/dir'
install -t '%{buildroot}%{_pkgdocdir}' -D -p -m 0644 \
    AUTHORS BUGS ChangeLog HACKING MAINTAINERS NEWS README libIDL2.pdf
cp -rp 'libIDL2.html' '%{buildroot}%{_pkgdocdir}/html'
install -t '%{buildroot}%{_datadir}/aclocal/libIDL.m4' -D -p -m 0644 \
    libIDL.m4
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%files
%license COPYING

%{_libdir}/libIDL-2.so.%{so_version}{,.*}


%files devel
%{_libdir}/libIDL-2.so

%{_includedir}/libIDL-2.0/

%{_libdir}/pkgconfig/libIDL-2.0.pc
# Note the aclocal directory is provided by the “filesystem” package
%{_datadir}/aclocal/libIDL.m4
%{_bindir}/libIDL-config-2
%{_mandir}/man1/libIDL-config-2.1*


%files doc
%{_infodir}/libIDL2.info*

%{_pkgdocdir}/


%changelog
%autochangelog
