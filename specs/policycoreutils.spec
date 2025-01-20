%global libauditver     3.0
%global libsepolver     3.8-0.rc3
%global libsemanagever  3.8-0.rc3
%global libselinuxver   3.8-0.rc3

%global generatorsdir %{_prefix}/lib/systemd/system-generators

# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0

Summary: SELinux policy core utilities
Name:    policycoreutils
Version: 3.8
Release: 0.rc3.1%{?dist}.2
License: GPL-2.0-or-later
# https://github.com/SELinuxProject/selinux/wiki/Releases
Source0: https://github.com/SELinuxProject/selinux/releases/download/%{version}-rc3/selinux-%{version}-rc3.tar.gz
Source1: https://github.com/SELinuxProject/selinux/releases/download/%{version}-rc3/selinux-%{version}-rc3.tar.gz.asc
Source2: https://github.com/bachradsusi.gpg
URL:     https://github.com/SELinuxProject/selinux
Source13: system-config-selinux.png
Source14: sepolicy-icons.tgz
Source15: selinux-autorelabel
Source16: selinux-autorelabel.service
Source17: selinux-autorelabel-mark.service
Source18: selinux-autorelabel.target
Source19: selinux-autorelabel-generator.sh
# Drop this when upstream updates translations and the package is rebased
# wlc --key <apikey> --url https://translate.fedoraproject.org/api/ download selinux/policycoreutils --output ./
Source20: selinux-policycoreutils.zip
# wlc --key <apikey> --url https://translate.fedoraproject.org/api/ download selinux/python --output ./
Source21: selinux-python.zip
# wlc --key <apikey> --url https://translate.fedoraproject.org/api/ download selinux/gui --output ./
Source22: selinux-gui.zip
# wlc --key <apikey> --url https://translate.fedoraproject.org/api/ download selinux/sandbox --output ./
Source23: selinux-sandbox.zip
# https://github.com/fedora-selinux/selinux
# $ git format-patch -N 3.8 -- policycoreutils python gui sandbox dbus semodule-utils restorecond
# $ for j in [0-9]*.patch; do printf "Patch%s: %s\n" ${j/-*/} $j; done
# Patch list start
Patch0001: 0001-Don-t-be-verbose-if-you-are-not-on-a-tty.patch
Patch0002: 0002-sepolicy-generate-Handle-more-reserved-port-types.patch
Patch0003: 0003-sandbox-Use-matchbox-window-manager-instead-of-openb.patch
Patch0004: 0004-Use-SHA-2-instead-of-SHA-1.patch
Patch0005: 0005-python-sepolicy-Fix-spec-file-dependencies.patch
# Patch list end

Obsoletes: policycoreutils < 2.0.61-2
Conflicts: filesystem < 3, selinux-policy-base < 3.13.1-138
# initscripts < 9.66 shipped fedora-autorelabel services which are renamed to selinux-relabel
Conflicts: initscripts < 9.66
Provides: /sbin/fixfiles
Provides: /sbin/restorecon

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/restorecon
Provides: /usr/sbin/fixfiles
Provides: /usr/sbin/setfiles
Provides: /usr/sbin/setsebool
Provides: /usr/sbin/semodule
%endif

BuildRequires: gcc make
BuildRequires: pam-devel libsepol-static >= %{libsepolver} libsemanage-devel >= %{libsemanagever} libselinux-devel >= %{libselinuxver}  libcap-devel audit-libs-devel >=  %{libauditver} gettext
BuildRequires: desktop-file-utils dbus-devel glib2-devel
BuildRequires: python3-devel python3-setuptools python3-wheel python3-pip
BuildRequires: systemd
BuildRequires: git-core
BuildRequires: gnupg2
Requires: util-linux grep gawk diffutils rpm sed
Requires: libsepol >= %{libsepolver} coreutils libselinux-utils >=  %{libselinuxver}

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

policycoreutils contains the policy core utilities that are required
for basic operation of a SELinux system.  These utilities include
load_policy to load policies, setfiles to label filesystems, newrole
to switch roles.

%prep -p /usr/bin/bash
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1 -n selinux-%{version}-rc3

cp %{SOURCE13} gui/
tar -xvf %{SOURCE14} -C python/sepolicy/

# Temporary disabled since upstream updated translations in this release
# Since patches containing translation changes were too big, translations were moved to separate tarballs
# For more information see README.translations
# First remove old translation files
# rm -f policycoreutils/po/*.po python/po/*.po gui/po/*.po sandbox/po/*.po
# unzip %{SOURCE20}
# cp -r selinux/policycoreutils/po policycoreutils
# unzip %{SOURCE21}
# cp -r selinux/python/po python
# unzip %{SOURCE22}
# cp -r selinux/gui/po gui
# unzip %{SOURCE23}
# cp -r selinux/sandbox/po sandbox

%build
%set_build_flags
export PYTHON=%{__python3}

make -C policycoreutils SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" SEMODULE_PATH="/usr/sbin" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C python SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C gui SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C sandbox SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C dbus SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C semodule-utils SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C restorecond SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
%{__mkdir} -p %{buildroot}/%{_usr}/share/doc/%{name}/

%make_install -C policycoreutils LSPP_PRIV=y SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" SEMODULE_PATH="/usr/sbin" LIBSEPOLA="%{_libdir}/libsepol.a"

%make_install -C python PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"

%make_install -C gui PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"

%make_install -C sandbox PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"

%make_install -C dbus PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"

%make_install -C semodule-utils PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"

%make_install -C restorecond PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"

# Fix perms on newrole so that objcopy can process it
chmod 0755 %{buildroot}%{_bindir}/newrole

# Systemd
rm -rf %{buildroot}/%{_sysconfdir}/rc.d/init.d/restorecond

rm -f %{buildroot}/usr/share/man/man8/open_init_pty.8
rm -f %{buildroot}%{_sbindir}/open_init_pty
rm -f %{buildroot}%{_sbindir}/run_init
rm -f %{buildroot}/usr/share/man/man8/run_init.8*
rm -f %{buildroot}/etc/pam.d/run_init*

mkdir   -m 755 -p %{buildroot}/%{generatorsdir}
install -m 644 -p %{SOURCE16} %{buildroot}/%{_unitdir}/
install -m 644 -p %{SOURCE17} %{buildroot}/%{_unitdir}/
install -m 644 -p %{SOURCE18} %{buildroot}/%{_unitdir}/
install -m 755 -p %{SOURCE19} %{buildroot}/%{generatorsdir}/
install -m 755 -p %{SOURCE15} %{buildroot}/%{_libexecdir}/selinux/

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/system-config-selinux

%find_lang policycoreutils
%find_lang selinux-python
%find_lang selinux-gui
%find_lang selinux-sandbox

%package python-utils
Summary:    SELinux policy core python utilities
Requires:   python3-policycoreutils = %{version}-%{release}
Obsoletes:  policycoreutils-python <= 2.4-4
BuildArch:  noarch

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/semanage
%endif

%description python-utils
The policycoreutils-python-utils package contains the management tools use to manage
an SELinux environment.

%files python-utils
%{_sbindir}/semanage
%{_bindir}/chcat
%{_bindir}/audit2allow
%{_bindir}/audit2why
%{_mandir}/man1/audit2allow.1*
%{_mandir}/man1/audit2why.1*
%{_sysconfdir}/dbus-1/system.d/org.selinux.conf
%{_mandir}/man8/chcat.8*
%{_mandir}/man8/semanage*.8*
%{_datadir}/bash-completion/completions/semanage

%package dbus
Summary:    SELinux policy core DBUS api
Requires:   python3-policycoreutils = %{version}-%{release}
Requires:   python3-gobject-base
Requires:   polkit
BuildArch:  noarch

%description dbus
The policycoreutils-dbus package contains the management DBUS API use to manage
an SELinux environment.

%files dbus
%{_sysconfdir}/dbus-1/system.d/org.selinux.conf
%{_datadir}/dbus-1/system-services/org.selinux.service
%{_datadir}/polkit-1/actions/org.selinux.policy
%{_datadir}/polkit-1/actions/org.selinux.config.policy
%{_datadir}/system-config-selinux/selinux_server.py
%dir %{_datadir}/system-config-selinux/__pycache__
%{_datadir}/system-config-selinux/__pycache__/selinux_server.*

%package -n python3-policycoreutils
%{?python_provide:%python_provide python3-policycoreutils}
# Remove before F31
Provides: %{name}-python3 = %{version}-%{release}
Provides: %{name}-python3 = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
Summary: SELinux policy core python3 interfaces
Requires:policycoreutils = %{version}-%{release}
Requires:python3-libsemanage >= %{libsemanagever} python3-libselinux
# no python3-audit-libs yet
Requires:audit-libs-python3 >=  %{libauditver}
Requires: checkpolicy
Requires: python3-setools >= 4.4.0
Requires: python3-distro
BuildArch: noarch

%description -n python3-policycoreutils
The python3-policycoreutils package contains the interfaces that can be used
by python 3 in an SELinux environment.

%files -f selinux-python.lang -n python3-policycoreutils
%{python3_sitelib}/seobject.py*
%{python3_sitelib}/__pycache__
%{python3_sitelib}/sepolgen
%dir %{python3_sitelib}/sepolicy
%{python3_sitelib}/sepolicy/templates
%dir %{python3_sitelib}/sepolicy/help
%{python3_sitelib}/sepolicy/help/*
%{python3_sitelib}/sepolicy/__init__.py*
%{python3_sitelib}/sepolicy/booleans.py*
%{python3_sitelib}/sepolicy/communicate.py*
%{python3_sitelib}/sepolicy/generate.py*
%{python3_sitelib}/sepolicy/interface.py*
%{python3_sitelib}/sepolicy/manpage.py*
%{python3_sitelib}/sepolicy/network.py*
%{python3_sitelib}/sepolicy/transition.py*
%{python3_sitelib}/sepolicy/sedbus.py*
%{python3_sitelib}/sepolicy*.dist-info/
%{python3_sitelib}/sepolicy/__pycache__

%package devel
Summary: SELinux policy core policy devel utilities
Requires: policycoreutils-python-utils = %{version}-%{release}
Requires: /usr/bin/make python3-dnf
Requires: (selinux-policy-devel if selinux-policy)

%description devel
The policycoreutils-devel package contains the management tools use to develop policy in an SELinux environment.

%files devel
%{_bindir}/sepolgen
%{_bindir}/sepolgen-ifgen
%{_bindir}/sepolgen-ifgen-attr-helper
%dir  /var/lib/sepolgen
/var/lib/sepolgen/perm_map
%{_bindir}/sepolicy
%{_mandir}/man8/sepolgen.8*
%{_mandir}/man8/sepolicy-booleans.8*
%{_mandir}/man8/sepolicy-generate.8*
%{_mandir}/man8/sepolicy-interface.8*
%{_mandir}/man8/sepolicy-network.8*
%{_mandir}/man8/sepolicy.8*
%{_mandir}/man8/sepolicy-communicate.8*
%{_mandir}/man8/sepolicy-manpage.8*
%{_mandir}/man8/sepolicy-transition.8*
%{_usr}/share/bash-completion/completions/sepolicy


%package sandbox
Summary: SELinux sandbox utilities
Requires: python3-policycoreutils = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} <= 9
Requires: xorg-x11-server-Xephyr >= 1.14.1-2
Requires: xmodmap
Requires: matchbox-window-manager
%endif
Requires: rsync
BuildRequires: libcap-ng-devel

%description sandbox
The policycoreutils-sandbox package contains the scripts to create graphical
sandboxes

%files -f selinux-sandbox.lang sandbox
%config(noreplace) %{_sysconfdir}/sysconfig/sandbox
%{_datadir}/sandbox/sandboxX.sh
%{_datadir}/sandbox/start
%caps(cap_setpcap,cap_setuid,cap_fowner,cap_dac_override,cap_sys_admin,cap_sys_nice=pe) %{_sbindir}/seunshare
%{_mandir}/man8/seunshare.8*
%{_bindir}/sandbox
%{_mandir}/man5/sandbox.5*
%{_mandir}/man8/sandbox.8*

%package newrole
Summary: The newrole application for RBAC/MLS
Requires: policycoreutils = %{version}-%{release}

%description newrole
RBAC/MLS policy machines require newrole as a way of changing the role
or level of a logged in user.

%files newrole
%attr(0755,root,root) %caps(cap_dac_read_search,cap_setpcap,cap_audit_write,cap_sys_admin,cap_fowner,cap_chown,cap_dac_override=pe) %{_bindir}/newrole
%{_mandir}/man1/newrole.1.gz
%config(noreplace) %{_sysconfdir}/pam.d/newrole

%package gui
Summary: SELinux configuration GUI
Requires: policycoreutils-devel = %{version}-%{release}, python3-policycoreutils = %{version}-%{release}
Requires: policycoreutils-dbus = %{version}-%{release}
Requires: gtk3, python3-gobject
BuildRequires: desktop-file-utils
BuildArch: noarch

%description gui
system-config-selinux is a utility for managing the SELinux environment

%files -f selinux-gui.lang gui
%{_bindir}/system-config-selinux
%{_bindir}/selinux-polgengui
%{_datadir}/applications/sepolicy.desktop
%{_datadir}/applications/system-config-selinux.desktop
%{_datadir}/applications/selinux-polgengui.desktop
%{_datadir}/icons/hicolor/24x24/apps/system-config-selinux.png
%{_datadir}/pixmaps/system-config-selinux.png
%dir %{_datadir}/system-config-selinux
%dir %{_datadir}/system-config-selinux/__pycache__
%{_datadir}/system-config-selinux/system-config-selinux.png
%{_datadir}/system-config-selinux/*Page.py
%{_datadir}/system-config-selinux/__pycache__/*Page.*
%{_datadir}/system-config-selinux/system-config-selinux.py
%{_datadir}/system-config-selinux/__pycache__/system-config-selinux.*
%{_datadir}/system-config-selinux/*.ui
%{python3_sitelib}/sepolicy/gui.py*
%{python3_sitelib}/sepolicy/sepolicy.glade
%{_datadir}/icons/hicolor/*/apps/sepolicy.png
%{_datadir}/pixmaps/sepolicy.png
%{_mandir}/man8/system-config-selinux.8*
%{_mandir}/man8/selinux-polgengui.8*
%{_mandir}/man8/sepolicy-gui.8*

%files -f %{name}.lang
%{_sbindir}/restorecon
%{_sbindir}/restorecon_xattr
%{_sbindir}/fixfiles
%{_sbindir}/setfiles
%{_sbindir}/load_policy
%{_sbindir}/genhomedircon
%{_sbindir}/setsebool
%{_sbindir}/semodule
%{_sbindir}/unsetfiles
%if "%{_sbindir}" != "%{_bindir}"
# symlink to %%{_bindir}/sestatus
%{_sbindir}/sestatus
%endif
%{_bindir}/secon
%{_bindir}/semodule_expand
%{_bindir}/semodule_link
%{_bindir}/semodule_package
%{_bindir}/semodule_unpackage
%{_bindir}/sestatus
%{_libexecdir}/selinux/hll
%{_libexecdir}/selinux/selinux-autorelabel
%{_unitdir}/selinux-autorelabel-mark.service
%{_unitdir}/selinux-autorelabel.service
%{_unitdir}/selinux-autorelabel.target
%{generatorsdir}/selinux-autorelabel-generator.sh
%config(noreplace) %{_sysconfdir}/sestatus.conf
%{_mandir}/man5/selinux_config.5.gz
%{_mandir}/man5/sestatus.conf.5.gz
%{_mandir}/man8/fixfiles.8*
%{_mandir}/man8/load_policy.8*
%{_mandir}/man8/restorecon.8*
%{_mandir}/man8/restorecon_xattr.8*
%{_mandir}/man8/semodule.8*
%{_mandir}/man8/sestatus.8*
%{_mandir}/man8/setfiles.8*
%{_mandir}/man8/setsebool.8*
%{_mandir}/man1/secon.1*
%{_mandir}/man1/unsetfiles.1*
%{_mandir}/man8/genhomedircon.8*
%{_mandir}/man8/semodule_expand.8*
%{_mandir}/man8/semodule_link.8*
%{_mandir}/man8/semodule_unpackage.8*
%{_mandir}/man8/semodule_package.8*
%dir %{_datadir}/bash-completion
%{_datadir}/bash-completion/completions/setsebool
%{!?_licensedir:%global license %%doc}
%license policycoreutils/LICENSE
%doc %{_usr}/share/doc/%{name}

%package restorecond
Summary: SELinux restorecond utilities
BuildRequires: systemd-units

%description restorecond
The policycoreutils-restorecond package contains the restorecond service.

%files restorecond
%{_sbindir}/restorecond
%{_unitdir}/restorecond.service
%{_userunitdir}/restorecond_user.service
%config(noreplace) %{_sysconfdir}/selinux/restorecond.conf
%config(noreplace) %{_sysconfdir}/selinux/restorecond_user.conf
%{_sysconfdir}/xdg/autostart/restorecond.desktop
%{_datadir}/dbus-1/services/org.selinux.Restorecond.service
%{_mandir}/man8/restorecond.8*

%{!?_licensedir:%global license %%doc}
%license policycoreutils/LICENSE

%post
%systemd_post selinux-autorelabel-mark.service

%preun
%systemd_preun selinux-autorelabel-mark.service

%post restorecond
%systemd_post restorecond.service

%preun restorecond
%systemd_preun restorecond.service

%postun restorecond
%systemd_postun_with_restart restorecond.service

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-0.rc3.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.8-0.rc3.1.1
- Rebuilt for the bin-sbin merge (2nd attempt)

%autochangelog
