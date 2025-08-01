# Do not terminate build if language files are empty.
%define _empty_manifest_terminate_build 0

Name:           authselect
Version:        1.6.1
Release:        %autorelease
Summary:        Configures authentication and identity sources from supported profiles
URL:            https://github.com/authselect/authselect

License:        GPL-3.0-or-later
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%global makedir %{_builddir}/%{name}-%{version}

# Disable NIS profile on RHEL
%if 0%{?rhel}
%global with_nis_profile 0
%else
%global with_nis_profile 1
%endif

# Set the default profile
%{?fedora:%global default_profile local with-silent-lastlog}
%{?rhel:%global default_profile local}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(popt)
BuildRequires:  gettext-devel
BuildRequires:  po4a
BuildRequires:  %{_bindir}/a2x
BuildRequires:  libcmocka-devel >= 1.0.0
BuildRequires:  libselinux-devel
Requires: authselect-libs%{?_isa} = %{version}-%{release}

# RHEL does not have meta flag yet
%if 0%{?rhel} <= 10
Suggests: sssd
Suggests: samba-winbind
Suggests: fprintd-pam
Suggests: oddjob-mkhomedir
%else
Suggests(meta): sssd
Suggests(meta): samba-winbind
Suggests(meta): fprintd-pam
Suggests(meta): oddjob-mkhomedir
%endif

# Properly obsolete removed authselect-compat package.
Obsoletes: authselect-compat < 1.3

%description
Authselect is designed to be a replacement for authconfig but it takes
a different approach to configure the system. Instead of letting
the administrator build the PAM stack with a tool (which may potentially
end up with a broken configuration), it would ship several tested stacks
(profiles) that solve a use-case and are well tested and supported.
At the same time, some obsolete features of authconfig are not
supported by authselect.

%package libs
Summary: Utility library used by the authselect tool
# Required by scriptlets
Requires: coreutils
Requires: sed
Suggests: systemd

%description libs
Common library files for authselect. This package is used by the authselect
command line tool and any other potential front-ends.

%package devel
Summary: Development libraries and headers for authselect
Requires: authselect-libs%{?_isa} = %{version}-%{release}

%description devel
System header files and development libraries for authselect. Useful if
you develop a front-end for the authselect library.

%prep
%setup -q

for p in %patches ; do
    %__patch -p1 -i $p
done

%build
autoreconf -if
%configure \
%if %{with_nis_profile}
    --with-nis-profile \
%endif
    %{nil}
%make_build

%check
%make_build check

%install
%make_install

# Find translations
%find_lang %{name}
%find_lang %{name} %{name}.8.lang --with-man
%find_lang %{name}-migration %{name}-migration.7.lang --with-man
%find_lang %{name}-profiles %{name}-profiles.5.lang --with-man

# We want this file to contain only manual page translations
%__sed -i '/LC_MESSAGES/d' %{name}.8.lang

# Remove .la and .a files created by libtool
find $RPM_BUILD_ROOT -name "*.la" -exec %__rm -f {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec %__rm -f {} \;

%ldconfig_scriptlets libs

%files libs -f %{name}.lang -f %{name}-profiles.5.lang
%dir %{_sysconfdir}/authselect
%dir %{_sysconfdir}/authselect/custom
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/authselect.conf
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/dconf-db
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/dconf-locks
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/fingerprint-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/nsswitch.conf
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/password-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/postlogin
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/smartcard-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/authselect/system-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/nsswitch.conf
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/fingerprint-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/password-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/postlogin
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/smartcard-auth
%ghost %attr(0644,root,root) %{_sysconfdir}/pam.d/system-auth
%dir %{_localstatedir}/lib/authselect
%ghost %attr(0755,root,root) %{_localstatedir}/lib/authselect/backups/
%dir %{_datadir}/authselect
%dir %{_datadir}/authselect/vendor
%dir %{_datadir}/authselect/default
%dir %{_datadir}/authselect/default/local/
%dir %{_datadir}/authselect/default/sssd/
%dir %{_datadir}/authselect/default/winbind/
%{_datadir}/authselect/default/local/dconf-db
%{_datadir}/authselect/default/local/dconf-locks
%{_datadir}/authselect/default/local/fingerprint-auth
%{_datadir}/authselect/default/local/nsswitch.conf
%{_datadir}/authselect/default/local/password-auth
%{_datadir}/authselect/default/local/postlogin
%{_datadir}/authselect/default/local/README
%{_datadir}/authselect/default/local/REQUIREMENTS
%{_datadir}/authselect/default/local/smartcard-auth
%{_datadir}/authselect/default/local/system-auth
%{_datadir}/authselect/default/sssd/dconf-db
%{_datadir}/authselect/default/sssd/dconf-locks
%{_datadir}/authselect/default/sssd/fingerprint-auth
%{_datadir}/authselect/default/sssd/nsswitch.conf
%{_datadir}/authselect/default/sssd/password-auth
%{_datadir}/authselect/default/sssd/postlogin
%{_datadir}/authselect/default/sssd/README
%{_datadir}/authselect/default/sssd/REQUIREMENTS
%{_datadir}/authselect/default/sssd/smartcard-auth
%{_datadir}/authselect/default/sssd/system-auth
%{_datadir}/authselect/default/winbind/dconf-db
%{_datadir}/authselect/default/winbind/dconf-locks
%{_datadir}/authselect/default/winbind/fingerprint-auth
%{_datadir}/authselect/default/winbind/nsswitch.conf
%{_datadir}/authselect/default/winbind/password-auth
%{_datadir}/authselect/default/winbind/postlogin
%{_datadir}/authselect/default/winbind/README
%{_datadir}/authselect/default/winbind/REQUIREMENTS
%{_datadir}/authselect/default/winbind/smartcard-auth
%{_datadir}/authselect/default/winbind/system-auth
%if %{with_nis_profile}
%dir %{_datadir}/authselect/default/nis/
%{_datadir}/authselect/default/nis/dconf-db
%{_datadir}/authselect/default/nis/dconf-locks
%{_datadir}/authselect/default/nis/fingerprint-auth
%{_datadir}/authselect/default/nis/nsswitch.conf
%{_datadir}/authselect/default/nis/password-auth
%{_datadir}/authselect/default/nis/postlogin
%{_datadir}/authselect/default/nis/README
%{_datadir}/authselect/default/nis/REQUIREMENTS
%{_datadir}/authselect/default/nis/smartcard-auth
%{_datadir}/authselect/default/nis/system-auth
%endif
%{_libdir}/libauthselect.so.*
%{_mandir}/man5/authselect-profiles.5*
%dir %{_datadir}/doc/authselect
%{_datadir}/doc/authselect/COPYING
%{_datadir}/doc/authselect/README.md
%license COPYING
%doc README.md

%files devel
%{_includedir}/authselect.h
%{_libdir}/libauthselect.so
%{_libdir}/pkgconfig/authselect.pc

%files  -f %{name}.8.lang  -f %{name}-migration.7.lang
%{_bindir}/authselect
%{_mandir}/man8/authselect.8*
%{_mandir}/man7/authselect-migration.7*
%{_sysconfdir}/bash_completion.d/authselect-completion.sh

%preun
if [ $1 == 0 ] ; then
    # Remove authselect symbolic links so all authselect files can be
    # deleted safely. If this fail, the uninstallation must fail to avoid
    # breaking the system by removing PAM files. However, the command can
    # only fail if it can not write to the file system.
    %{_bindir}/authselect opt-out
fi

%posttrans libs
# Keep nss-altfiles for all rpm-ostree based systems.
# See https://github.com/authselect/authselect/issues/48
if test -e /run/ostree-booted; then
    for PROFILE in `ls %{_datadir}/authselect/default`; do
        %{_bindir}/authselect create-profile $PROFILE --vendor --base-on $PROFILE --symlink-pam --symlink-dconf --symlink=REQUIREMENTS --symlink=README &> /dev/null
        %__sed -i -e 's/{if "with-altfiles":\([^}]\+\)}/\1/g' %{_datadir}/authselect/vendor/$PROFILE/nsswitch.conf &> /dev/null
    done
fi

# If this is a new installation select the default configuration.
if [ $1 == 1 ] ; then
    %{_bindir}/authselect select %{default_profile} --force --nobackup &> /dev/null
    exit 0
fi

# Minimal profile was removed. Switch to local during upgrade.
%__sed -i '1 s/^minimal$/local/'  %{_sysconfdir}/authselect/authselect.conf
for file in  %{_sysconfdir}/authselect/custom/*/*; do
    link=`%{_bindir}/readlink "$file"`
    if [[ "$link" == %{_datadir}/authselect/default/minimal/* ]]; then
        target=`%{_bindir}/basename "$link"`
        %{_bindir}/ln -sfn "%{_datadir}/authselect/default/local/$target" "$file"
    fi
done

# Apply any changes to profiles (validates configuration first internally)
%{_bindir}/authselect apply-changes &> /dev/null

exit 0

%autochangelog
