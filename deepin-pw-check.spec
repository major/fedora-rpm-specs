# broken Makefile
%global _smp_mflags -j1

%global __provides_exclude_from ^%{_libdir}/security/.*\.so$

Name:           deepin-pw-check
Version:        5.1.18
Release:        %autorelease
Summary:        Tool used to check password and manager the configuration for password
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-pw-check
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-Adapt-to-Fedora-cracklib-API.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  compiler(go-compiler)
BuildRequires:  golang(github.com/godbus/dbus)
BuildRequires:  golang(github.com/linuxdeepin/go-dbus-factory/org.freedesktop.policykit1)
BuildRequires:  golang(github.com/linuxdeepin/go-lib/dbusutil)
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  deepin-gettext-tools
BuildRequires:  cracklib-devel
BuildRequires:  iniparser-devel
BuildRequires:  deepin-gir-generator

%description
In order to unify the authentication interface, this interface is designed to
adapt to fingerprint, face and other authentication methods.

%package devel
Summary: Header files and libraries used to build deepin-pw-check
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cracklib-devel%{?_isa}
Requires: iniparser-devel%{?_isa}

%description devel
In order to unify the authentication interface, this interface is designed to
adapt to fingerprint, face and other authentication methods.

%prep
%autosetup -p1

sed -i -e 's|\${PREFIX}/lib$|\${PREFIX}/%{_lib}|; s|cp |cp -a |' Makefile
sed -i -e 's|/usr/lib|%{_libdir}|' misc/pkgconfig/libdeepin_pw_check.pc
sed -i 's|sprintf(outbuf, err_to_string|sprintf(outbuf, "%s", err_to_string|' pam/pam.c

# expand build_ldflags at %%build section, RHBZ#2044028
sed -i 's|gcc |gcc %{build_cflags} %{build_ldflags} |' Makefile

%build
# manually build the deepin-pw-check command since it is hard to override
# Makefile with %%gobuild
make prepare
touch prepare
export GOPATH=%{gopath}
%gobuild -o out/bin/%{name} service/*.go

%make_build

%install
export GOPATH=%{gopath}
export PKG_FILE_DIR=%{_libdir}/pkgconfig
%make_install PKG_FILE_DIR=%{_libdir}/pkgconfig PAM_MODULE_DIR=%{_libdir}/security
# don't install static library
rm -v %{buildroot}%{_libdir}/*.a

%find_lang deepin-pw-check

%files -f deepin-pw-check.lang
%doc README.md
%license LICENSE
%{_bindir}/pwd-conf-update
%{_prefix}/lib/deepin-pw-check/
%{_libdir}/libdeepin_pw_check.so.1*
%{_libdir}/security/pam_deepin_pw_check.so
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/polkit-1/actions/*.policy

%files devel
%{_libdir}/libdeepin_pw_check.so
%{_libdir}/pkgconfig/libdeepin_pw_check.pc
%{_includedir}/deepin_pw_check.h

%changelog
%autochangelog
