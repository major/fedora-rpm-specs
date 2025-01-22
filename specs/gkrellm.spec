Name:           gkrellm
Version:        2.4.0
Release:        %autorelease
Summary:        Multiple stacked system monitors in one process
License:        GPL-3.0-or-later
URL:            https://gkrellm.srcbox.net/
Source0:        https://gkrellm.srcbox.net/releases/%{name}-%{version}.tar.bz2
Source5:        make-git-snapshot.sh
Patch1:         gkrellm-2.4.0-config.patch
Patch3:         gkrellm-2.4.0-width.patch
BuildRequires:  gcc
BuildRequires:  gtk2-devel openssl-devel libSM-devel desktop-file-utils gettext
BuildRequires:  lm_sensors-devel libntlm-devel libappstream-glib
Requires:       gdk-pixbuf2-modules-extra%{?_isa}

%description
GKrellM charts CPU, load, Disk, and all active net interfaces
automatically.  An on/off button and online timer for the PPP
interface is provided, as well as monitors for memory and swap usage,
file system, internet connections, APM laptop battery, mbox style
mailboxes, and temperature sensors on supported systems.  Also
included is an uptime monitor, a hostname label, and a clock/calendar.
Additional features are:

  * Autoscaling grid lines with configurable grid line resolution.
  * LED indicators for the net interfaces.
  * A gui popup for configuration of chart sizes and resolutions.


%package daemon
Summary:        The GNU Krell Monitors Server
# systemd >= 186 for scriptlet macros
BuildRequires:  systemd >= 186
BuildRequires: make
Requires(pre):  shadow-utils systemd
Requires(post,preun,postun): systemd


%description daemon
gkrellmd listens for connections from gkrellm clients. When a gkrellm
client connects to a gkrellmd server all builtin monitors collect their
data from the server.


%package        devel
Summary:        Development files for the GNU Krell Monitors
Requires:       gtk2-devel%{?_isa}

%description devel
Development files for the GNU Krell Monitors.


%prep
%autosetup -p1

for i in gkrellmd.1 gkrellm.1 README Changelog.OLD Changelog-plugins.html \
    src/gkrellm.h server/gkrellmd.h; do
   sed -i -e "s@/usr/lib/gkrellm2*/plugins@%{_libdir}/gkrellm2/plugins@" $i
   sed -i -e "s@/usr/local/lib/gkrellm2*/plugins@/usr/local/%{_lib}/gkrellm2/plugins@" $i
done


%build
make %{?_smp_mflags} PREFIX=%{_prefix} \
    PKGCONFIGDIR=%{_libdir}/pkgconfig \
    INCLUDEDIR=%{_includedir} \
    SINSTALLDIR=%{_sbindir} \
    CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -Wno-error=incompatible-pointer-types" \
    LDFLAGS="$RPM_LD_FLAGS"


%install
mkdir -p %{buildroot}%{_datadir}/gkrellm2/themes
mkdir -p %{buildroot}%{_libdir}/gkrellm2/plugins

make install DESTDIR=%{buildroot} PREFIX=%{_prefix} \
    LOCALEDIR=%{buildroot}%{_datadir}/locale \
    INSTALLDIR=%{buildroot}%{_bindir} \
    SINSTALLDIR=%{buildroot}%{_sbindir} \
    MANDIR=%{buildroot}%{_mandir}/man1 \
    PKGCONFIGDIR=%{buildroot}%{_libdir}/pkgconfig \
    INCLUDEDIR=%{buildroot}%{_includedir} \
    CFGDIR=%{buildroot}%{_sysconfdir}
%find_lang %name

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%pre daemon
getent group gkrellmd >/dev/null || groupadd -r gkrellmd
getent passwd gkrellmd >/dev/null || \
useradd -r -g gkrellmd -M -d / -s /sbin/nologin -c "GNU Krell daemon" gkrellmd
:

%post daemon
%systemd_post gkrellmd.service

%preun daemon
%systemd_preun gkrellmd.service

%postun daemon
%systemd_postun_with_restart gkrellmd.service


%files -f %{name}.lang
%license COPYRIGHT
%doc CHANGELOG.md Changelog.OLD README Themes.html
%{_bindir}/%{name}
%{_libdir}/gkrellm2
%{_datadir}/gkrellm2
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/*.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files devel
%license %{_licensedir}/%{name}*
%{_includedir}/gkrellm2
%{_libdir}/pkgconfig/%{name}.pc

%files daemon
%license %{_licensedir}/%{name}*
%{_unitdir}/gkrellmd.service
%{_sbindir}/gkrellmd
%{_mandir}/man1/gkrellmd.*
%config(noreplace) %{_sysconfdir}/gkrellmd.conf


%changelog
%autochangelog
