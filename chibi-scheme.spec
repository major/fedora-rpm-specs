%global _description %{expand:
Chibi-Scheme is a very small library intended for use as an extension
and scripting language in C programs. In addition to support for
lightweight VM-based threads, each VM itself runs in an isolated
heap allowing multiple VMs to run simultaneously in different OS threads.

The default language is R7RS Scheme, with support for all libraries.
Support for additional languages such as JavaScript, Go, Lua and Bash
are planned for future releases. Scheme is chosen as a substrate because
its first class continuations and guaranteed tail-call optimization
makes implementing other languages easy.

Chibi-Scheme is known to work on 32 and 64-bit Linux, FreeBSD and OS X,
Plan9, Windows (using Cygwin), iOS, and Emscripten.
}

Name:           chibi-scheme
Version:        0.10.0
Release:        %autorelease
Summary:        Minimal Scheme implementation for use as an extension language

# Most of the project is licensed under BSD-3-Clause, while certain SRFIs
# like SRFI 101 and 135 are imported from elsewhere and have the MIT license.
License:        BSD-3-Clause AND MIT
URL:            http://synthcode.com/wiki/chibi-scheme
Source0:        http://synthcode.com/scheme/chibi/%{name}-%{version}.tgz

BuildRequires:  make
BuildRequires:  gcc

%description %_description

%package devel
Summary:        Development files for chibi-scheme
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %name-devel %_description

This package contains the development files alongside the tool `chibi-ffi`.

%prep
%autosetup

%build
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} SOLIBDIR=%{_libdir} SNOWPREFIX=%{_prefix} SNOWLIBDIR=%{_libdir} doc all

%install
# Disable generating Chibi images at build time, since it'd attempt to reference the buildroot paths.
# Instead generate at install time on user's machine.
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} SOLIBDIR=%{_libdir} SNOWPREFIX=%{_prefix} SNOWLIBDIR=%{_libdir} IMAGE_FILES=""

%post
# Always generate images when installing (upgrade or not)
# This is needed, because as explained in the %%install -section,
# this needs to be done at install time because otherwise the referred paths
# would point to the buildroot instead of the user's filesystem
%{_bindir}/chibi-scheme -mchibi.repl -d %{_datadir}/chibi/chibi.img
%{_bindir}/chibi-scheme -xscheme.red -mchibi.repl -d %{_datadir}/chibi/red.img
%{_bindir}/chibi-scheme -mchibi.snow.commands -mchibi.snow.interface -mchibi.snow.package -mchibi.snow.utils -d %{_datadir}/chibi/snow.img

%preun
# Remove generated Chibi images if uninstalling totally
if [ $1 -lt 1 ]; then
    rm -f %{_datadir}/chibi/chibi.img
    rm -f %{_datadir}/chibi/red.img
    rm -f %{_datadir}/chibi/snow.img
fi

%files
%license COPYING
%doc doc/lib/chibi/*.html
%{_bindir}/chibi-doc
%{_bindir}/%{name}
%{_bindir}/snow-chibi
%{_bindir}/snow-chibi.scm

%{_libdir}/libchibi-scheme.so.0*
%{_libdir}/chibi

%{_datadir}/chibi/

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/chibi-doc.1*

%files devel
%{_bindir}/chibi-ffi
%{_includedir}/chibi
%{_libdir}/libchibi-scheme.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/chibi-ffi.1*

%changelog
%autochangelog
