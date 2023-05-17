Summary:	Extensible editor for structured binary data
Name:		poke
Version:	3.2
Release:	%autorelease

# Documentation under GFDL
License:	GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later
URL:		https://www.jemarch.net/poke
Source0:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
# the url also contains html -> manually stripped away
Source2:	http://keys.gnupg.net/pks/lookup?op=get&search=0x3EF90523B304AF08#./jemarch-keyring.asc

BuildRequires:	emacs
BuildRequires:	gcc
BuildRequires:	gc-devel
BuildRequires:	libnbd-devel
BuildRequires:	make
BuildRequires:	readline-devel
BuildRequires:	vim-common
# for gpg verification
BuildRequires:	gnupg2
# for check
BuildRequires:	dejagnu

Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

# bundles gnulib commit 738dcb549287cf29ed74a6d741d2a0723259b57e
Provides:	bundled(gnulib) = 20230125
# bundles jitter, should be packaged independently in the future
Provides:	bundled(jitter) = 0.9.294

%description
GNU poke is an interactive, extensible editor for binary data. Not
limited to editing basic entities such as bits and bytes, it provides
a full-fledged procedural, interactive programming language designed
to describe data structures and to operate on them.

%package	data
Summary:	Data files for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
%description	data
Data files for %{name}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	emacs
Summary:	Emacs support for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
%description	emacs
Emacs support for %{name}.

%package	libs
Summary:	Library files for %{name}
%description	libs
Libraries for %{name}.

%package	vim
Summary:	vim support for %{name}
%description	vim
vim support for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
# Confirmed by upstream, Jitter is sensible to LTO and pvm-vm2.c requires no LTO.
# Until a fix exists, remove LTO flags.
%define _lto_cflags %{nil}
%configure
%make_build

%check
make check

%install
%{make_install}
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/libpoke.a
rm -f %{buildroot}%{_libdir}/libpoke.la

# Byte compile the Emacs files
cd %{buildroot}%{_emacs_sitelispdir}
%_emacs_bytecompile poke-map-mode.el poke-ras-mode.el
cd -

%files
%{_bindir}/%{name}
%{_bindir}/poked
%{_bindir}/pk-bin2poke
%{_bindir}/pk-elfextractor
%{_bindir}/pk-strings
%{_infodir}/poke.info*.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/poked.1*
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING

%files data
%{_datadir}/%{name}/

%files devel
%{_includedir}/libpoke.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libpoke.so
%{_datadir}/aclocal/%{name}.m4


%files emacs
%{_emacs_sitelispdir}/poke-*

%files libs
%{_libdir}/libpoke.so.0*
%license COPYING

%files vim
%{vimfiles_root}/ftdetect/%{name}.vim
%{vimfiles_root}/syntax/%{name}.vim

%changelog
%autochangelog
