%global is_alpha 0

Summary:	Extensible editor for structured binary data
Name:		poke
Version:	4.3
Release:	%autorelease

# Documentation under GFDL
License:	GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later
URL:		https://www.jemarch.net/poke
%if 0%is_alpha
Source0:	https://alpha.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	https://alpha.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
%else
Source0:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
%endif
# the url also contains html -> manually stripped away
Source2:	https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf951cd18180e20b7dbd9359d54583674549e7e3a#./mnabipoor-keyring.asc

BuildRequires:	emacs
BuildRequires:	gcc
BuildRequires:	gc-devel
BuildRequires:	libnbd-devel
BuildRequires:	nbdkit
BuildRequires:	nbdkit-data-plugin
BuildRequires:	nbdkit-memory-plugin
BuildRequires:	make
BuildRequires:	readline-devel
BuildRequires:	vim-common
# for gpg verification
BuildRequires:	gnupg2
# for check
BuildRequires:	dejagnu

Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

# bundles gnulib commit de9671e9cae1dd9b6d1c41a377726aff9dcbdba1
Provides:	bundled(gnulib) = 20250308
# bundles jitter, should be packaged independently in the future
Provides:	bundled(jitter) = 0.7.312

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
%{_bindir}/pokefmt
%{_bindir}/pk-bin2poke
%{_bindir}/pk-jojopatch
%{_bindir}/pk-strings
%{_infodir}/poke.info*.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/poked.1*
%{_mandir}/man1/pokefmt.1*
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
%{_libdir}/libpoke.so.1*
%license COPYING

%files vim
%{vimfiles_root}/ftdetect/%{name}.vim
%{vimfiles_root}/syntax/%{name}.vim

%changelog
%autochangelog
