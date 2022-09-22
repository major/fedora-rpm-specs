Summary: The GNU line editor
Name: ed
Version: 1.18
Release: %autorelease

# The entire source is GPLv2 except doc/ed.info and doc/ed.texi, which are GFDL
License: GPLv2 and GFDL
URL:     https://www.gnu.org/software/ed/
Source0: https://download.savannah.gnu.org/releases/ed/%{name}-%{version}.tar.lz
Source1: https://download.savannah.gnu.org/releases/ed/%{name}-%{version}.tar.lz.sig
Source2: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x8FE99503132D7742#./antoniodiazdiaz-keyring.asc

BuildRequires: gcc
BuildRequires: make
BuildRequires: lzip
# for gpg verification
BuildRequires: gnupg2

%description
ed is a line-oriented text editor, used to create, display, and modify text
files (both interactively and via shell scripts). For most purposes, ed has been
replaced in normal usage by full-screen editors (emacs and vi, for example).

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup

%build
%set_build_flags
# Custom configure script; not Autoconf, so we do not use %%configure macro
./configure \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --datarootdir=%{_datadir} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --program-prefix=%{?_program_prefix} \
    CC="${CC-gcc}" \
    CPPFLAGS="${CPPFLAGS}" \
    CFLAGS="${CFLAGS}" \
    LDFLAGS="${LDFLAGS}"
%make_build

%install
%make_install
rm -vrf %{buildroot}%{_infodir}/dir

%check
%make_build check

%files
%license COPYING doc/fdl.texi
%doc ChangeLog NEWS README AUTHORS
%{_bindir}/ed
%{_bindir}/red
%{_mandir}/man1/ed.1*
%{_mandir}/man1/red.1*
%{_infodir}/ed.info*

%changelog
%autochangelog
