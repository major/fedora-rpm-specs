Summary: Linux kernel and C library user-space interface documentation
Name: man-pages
Version: 6.13
Release: %autorelease
# List of all licenses - each with an example of a man-page that uses it
# (complete list of all man-pages per license would be too long)
# BSD-2-Clause: man5/elf.5
# BSD-3-Clause: man3/list.3
# BSD-4.3TAHOE: man5/resolv.conf.5
# BSD-4-Clause-UC: man2/accept.2
# GPL-1.0-or-later: man1/ldd.1
# GPL-2.0-only: man2/fallocate.2
# GPL-2.0-or-later: man1/getent.1
# LicenseRef-Fedora-Public-Domain: man2/nfsservctl.2
# LicenseRef-Fedora-UltraPermissive: man2/futex.2
# Linux-man-pages-1-para: man2/getcpu.2
# Linux-man-pages-copyleft: man2/chdir.2
# Linux-man-pages-copyleft-2-para: man2/move_pages.2
# Linux-man-pages-copyleft-var: man2/get_mempolicy.2
# MIT: man3/program_invocation_name.3
# Spencer-94: man7/regex.7
License: BSD-2-Clause AND BSD-3-Clause AND BSD-4.3TAHOE AND BSD-4-Clause-UC AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive AND Linux-man-pages-1-para AND Linux-man-pages-copyleft AND Linux-man-pages-copyleft-2-para AND Linux-man-pages-copyleft-var AND MIT AND Spencer-94
URL: http://www.kernel.org/doc/man-pages/
# Verify signature:
# wget http://www.kernel.org/pub/linux/docs/man-pages/man-pages-%%{version}.tar.xz
# wget http://www.kernel.org/pub/linux/docs/man-pages/man-pages-%%{version}.tar.sign
# gpg --armour \
# 	--no-default-keyring \
#	--keyring ./man-pages.gpg --import ./man-pages.keyring
# gpg --no-default-keyring --keyring ./man-pages.gpg \
# 	--verify man-pages-%%{version}.tar.sign man-pages-%%{version}.tar.xz
# Verify "Good signature from" for the stored key.
Source0: http://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz
Source1: http://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.sign

BuildRequires: make
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

# attr.5 man page was moved from attr to man-pages in attr-2.4.47-11
Conflicts: attr < 2.4.47-11

# keyrings.7, persistent-keyring.7, process-keyring.7, session-keyring.7,
# thread-keyring.7, user-keyring.7 and user-session-keyring.7 man pages
# were moved from keyutils-libs to man-pages in keyutils-libs-1.5.10
Conflicts: keyutils-libs < 1.5.10

Autoreq: false
BuildArch: noarch

## Patches ##

# Regular man pages
# resolves: #650985
# https://bugzilla.kernel.org/show_bug.cgi?id=53781
Patch21: man-pages-3.42-close.patch

# Add rtas.2, swapcontext.2 and cons.saver.8 man pages
Patch28: additional-man-pages.patch

%description
A large collection of manual pages from the Linux Documentation Project (LDP).

%prep
%setup -q -a 0

%patch -P 21 -p1
%patch -P 28 -p1

## Remove man pages we are not going to use ##

# deprecated
rm man2/pciconfig_{write,read,iobase}.2

# problem with db x db4 (#198597) - man pages are obsolete
rm man3/{db,btree,dbopen,hash,mpool,recno}.3

# we are not using SystemV anymore
rm man7/boot.7

# remove man pages deprecated by libxcrypt (#1610307)
rm man3/crypt{,_r}.3

%build
# nothing to build

%install
make -R install prefix=/usr DESTDIR=$RPM_BUILD_ROOT

# The man.7 manual page is empty and references groff_man.7, but we
# don't want to explicitly require installing groff to make the set
# of man pages complete.
#
# rename files for alternative usage
mv %{buildroot}%{_mandir}/man7/man.7 %{buildroot}%{_mandir}/man7/man.%{name}.7
touch %{buildroot}%{_mandir}/man7/man.7

# Remove binaries we don't use and their man pages.
rm %{buildroot}%{_bindir}/diffman-git
rm %{buildroot}%{_bindir}/mansect
rm %{buildroot}%{_bindir}/pdfman
rm %{buildroot}%{_bindir}/sortman
rm %{buildroot}%{_mandir}/man1/mansect.1
rm %{buildroot}%{_mandir}/man1/diffman-git.1
rm %{buildroot}%{_mandir}/man1/pdfman.1
rm %{buildroot}%{_mandir}/man1/sortman.1

%pre
# remove alternativized files if they are not symlinks
[ -L %{_mandir}/man7/man.7.gz ] || rm -f %{_mandir}/man7/man.7.gz >/dev/null 2>&1 || :

%post
# set up the alternatives files
%{_sbindir}/update-alternatives --install %{_mandir}/man7/man.7.gz man.7.gz %{_mandir}/man7/man.%{name}.7.gz 300 \
    >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove man.7.gz %{_mandir}/man7/man.%{name}.7.gz >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ]; then
    if [ "$(readlink %{_sysconfdir}/alternatives/man.7.gz)" == "%{_mandir}/man7/man.%{name}.7.gz" ]; then
        %{_sbindir}/update-alternatives --set man.7.gz %{_mandir}/man7/man.%{name}.7.gz >/dev/null 2>&1 || :
    fi
fi

%files
%doc README Changes
%ghost %{_mandir}/man7/man.7.gz
%{_mandir}/man*/*

%changelog
%autochangelog
