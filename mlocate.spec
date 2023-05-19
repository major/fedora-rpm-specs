%global _hardened_build 1

Summary: An utility for finding files by name
Name: mlocate
Version: 0.26
Release: %autorelease -b 253
License: GPL-2.0-only
URL: https://fedorahosted.org/mlocate/
Source0: https://fedorahosted.org/releases/m/l/mlocate/mlocate-%{version}.tar.xz
Source1: updatedb.conf
Source2: mlocate-run-updatedb
Source3: mlocate-updatedb.service
Source4: mlocate-updatedb.timer
Requires(pre): shadow-utils
Requires(post): grep, sed
BuildRequires: make
BuildRequires: systemd-rpm-macros
BuildRequires: gcc
Provides: bundled(gnulib)
Provides: locate
Conflicts: plocate
Obsoletes: slocate <= 2.7-30

%description
mlocate is a locate/updatedb implementation.  It keeps a database of
all existing files and allows you to lookup files by name.

The 'm' stands for "merging": updatedb reuses the existing database to avoid
rereading most of the file system, which makes updatedb faster and does not
trash the system caches as much as traditional locate implementations.

%prep
%setup -q

%build
%configure --localstatedir=%{_localstatedir}/lib
make %{?_smp_mflags} groupname=slocate

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' groupname=slocate

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},/etc/cron.daily}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/updatedb.conf
install -D -p -m 750 %{SOURCE2} $RPM_BUILD_ROOT%{_libexecdir}/mlocate-run-updatedb
install -D -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/mlocate-updatedb.service
install -D -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/mlocate-updatedb.timer

# %%ghost semantics is so stupid
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/mlocate/mlocate.db

%find_lang mlocate

%pre
getent group slocate >/dev/null || groupadd -g 21 -r -f slocate
exit 0

%post
if /bin/grep -q '^[^#]*DAILY_UPDATE' %{_sysconfdir}/updatedb.conf; then
    /bin/sed -i.rpmsave -e '/DAILY_UPDATE/s/^/#/' %{_sysconfdir}/updatedb.conf
fi
# Bind mounts shouldn't be pruned on ostree based systems so locate works
# properly on HOME and other directories. We can't use the ostree-booted file
# to identy Silverblue - see
# https://github.com/fedora-silverblue/issue-tracker/issues/76#issuecomment-714562564
. /etc/os-release || exit
if [ "$VARIANT_ID" = "silverblue" ] || [ -f /run/ostree-booted ]; then
  if /bin/grep -q '^[^#]*PRUNE_BIND_MOUNTS' %{_sysconfdir}/updatedb.conf; then
      /bin/sed -i.rpmsave -e '/PRUNE_BIND_MOUNTS/s/^/#/' %{_sysconfdir}/updatedb.conf
  fi
fi

%systemd_post mlocate-updatedb.timer
if [ -x /usr/bin/systemctl ]; then
    /usr/bin/systemctl start mlocate-updatedb.timer
fi

%preun
%systemd_preun mlocate-updatedb.timer

%postun
%systemd_postun_with_restart mlocate-updatedb.timer

%triggerin -- %{name} < 0.26-11
if [ -x /usr/bin/systemctl ]; then
    /usr/bin/systemctl start mlocate-updatedb.timer
fi

%files -f mlocate.lang
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/updatedb.conf
%attr(2711,root,slocate) %{_bindir}/locate
%{_unitdir}/mlocate-updatedb.service
%{_unitdir}/mlocate-updatedb.timer
%{_libexecdir}/mlocate-run-updatedb
%{_bindir}/updatedb
%{_mandir}/man*/*
%dir %attr(0750,root,slocate) %{_localstatedir}/lib/mlocate
%ghost %attr(0640,root,slocate) %{_localstatedir}/lib/mlocate/mlocate.db

%changelog
%autochangelog
