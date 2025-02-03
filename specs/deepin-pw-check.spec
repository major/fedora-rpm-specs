%global __provides_exclude_from ^%{_libdir}/security/.*\.so$

%global goipath         github.com/linuxdeepin/deepin-pw-check
Version:                6.0.2
%global tag             %{version}

%gometa -L

Name:           deepin-pw-check
Release:        %autorelease
Summary:        A tool to verify the validity of the password.
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}
# fix: Missing include stdlib.h
Patch0:         https://github.com/linuxdeepin/deepin-pw-check/pull/37.patch
Patch1:         0001-Adapt-to-Fedora-cracklib-API.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  deepin-gettext-tools
BuildRequires:  cracklib-devel
BuildRequires:  iniparser-devel
BuildRequires:  libxcrypt-devel

%description
In order to unify the authentication interface, this interface is designed to
adapt to fingerprint, face and other authentication methods.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cracklib-devel%{?_isa}
Requires:       iniparser-devel%{?_isa}

%description    devel
This package contains development files for %{name}.

%prep
%goprep -A
%autopatch -p1

sed -i 's|\${PREFIX}/lib$|\${PREFIX}/%{_lib}|; s|cp |cp -a |' Makefile
sed -i 's|/usr/lib|%{_libdir}|' misc/pkgconfig/libdeepin_pw_check.pc

# expand build_ldflags at %%build section, RHBZ#2044028
sed -i 's|gcc |gcc %{build_cflags} %{build_ldflags} |' Makefile

%generate_buildrequires
%go_generate_buildrequires

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
%dir %{_prefix}/lib/deepin-pw-check
%{_prefix}/lib/deepin-pw-check/deepin-pw-check
%{_libdir}/libdeepin_pw_check.so.1*
%{_libdir}/security/pam_deepin_pw_check.so
%{_datadir}/dbus-1/system-services/org.deepin.dde.PasswdConf1.service
%{_datadir}/dbus-1/system.d/org.deepin.dde.PasswdConf1.conf
%{_datadir}/polkit-1/actions/org.deepin.dde.passwdconf.policy

%files devel
%{_libdir}/libdeepin_pw_check.so
%{_libdir}/pkgconfig/libdeepin_pw_check.pc
%{_includedir}/deepin_pw_check.h

%changelog
%autochangelog
