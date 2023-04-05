%global additional_version 20140218
%global additional_name man-pages-additional-%{additional_version}

Summary: Linux kernel and C library user-space interface documentation
Name: man-pages
Version: 6.04
Release: %autorelease
License: GPL+ and GPLv2+ and BSD and MIT and Copyright only
URL: http://www.kernel.org/doc/man-pages/
Source: http://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz
# additional man-pages, the source tarball is fedora/rhel only
Source1: %{additional_name}.tar.xz

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

%description
A large collection of manual pages from the Linux Documentation Project (LDP).

%prep
%setup -q -a 1

%patch21 -p1

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
make install prefix=/usr DESTDIR=$RPM_BUILD_ROOT
pushd %{additional_name}
make install prefix=/usr DESTDIR=$RPM_BUILD_ROOT
popd

# rename files for alternative usage
mv %{buildroot}%{_mandir}/man7/man.7 %{buildroot}%{_mandir}/man7/man.%{name}.7
touch %{buildroot}%{_mandir}/man7/man.7

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
%ghost %{_mandir}/man7/man.7*
%{_mandir}/man*/*

%changelog
%autochangelog
