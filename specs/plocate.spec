Name:           plocate
Version:        1.1.23
Release:        %autorelease
Summary:        Much faster locate

# Licensing information taken from README:
# * plocate (except updatedb) - GPL-2.0-or-later
# * updatedb                  - GPL-2.0-only
License:        GPL-2.0-or-later AND GPL-2.0-only
URL:            https://plocate.sesse.net/
Source0:        https://plocate.sesse.net/download/plocate-%{version}.tar.gz
Source1:        plocate.sysusers

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  libatomic

# The plan is to provide both mlocate and plocate for one or two
# Fedora releases, and then retire mlocate when the bugs in plocate
# have been ironed out. Thus, we only allow one or the other to be
# installed.
Conflicts:      mlocate
Provides:       locate

# https://bugzilla.redhat.com/show_bug.cgi?id=2052433
Obsoletes:      mlocate < 0.26-500

%description
plocate is a locate(1) based on posting lists, giving much faster
searches on a much smaller index. It is a drop-in replacement for
mlocate in nearly all aspects, and is fast on SSDs and non-SSDs alike.

%prep
%autosetup -p1

%build
%meson -Dsystemunitdir=%_unitdir -Dinstall_systemd=true
%meson_build

# Man page alias
cat >locate.1 <<EOF
.so man1/plocate.1
EOF

cat >updatedb.conf <<EOF
# https://bugzilla.redhat.com/show_bug.cgi?id=2033216
PRUNEFS = "9p afs autofs binfmt_misc ceph cgroup cgroup2 cifs coda configfs curlftpfs debugfs devfs devpts devtmpfs ecryptfs ftpfs fuse.ceph fuse.cryfs fuse.encfs fuse.glusterfs fuse.gvfsd-fuse fuse.mfs fuse.rclone fuse.rozofs fuse.sshfs fusec fusesmb gfs gfs2 gpfs hugetlbfs iso9660 lustre lustre_lite mfs mqueue ncpfs nfs nfs4 ocfs ocfs2 proc pstore ramfs pstorefs rootfs rpc_pipefs securityfs smbfs sysfs tmpfs tracefs udev udf usbfs"
# https://bugzilla.redhat.com/show_bug.cgi?id=2097889
PRUNEPATHS = "/tmp /media /dev /sys /proc /run /var/cache /var/spool"
EOF

%install
%meson_install

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/plocate.conf
ln -s plocate %{buildroot}%{_bindir}/locate
install -p -D -m 0644 -t %{buildroot}%{_mandir}/man1/ locate.1
install -p -D -m 0644 -t %{buildroot}%{_sysconfdir}/ updatedb.conf

# A state file to carry information from %%post to %%posttrans. See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_saving_state_between_scriptlets.
%global plocate_start_now %{_localstatedir}/lib/rpm-state/plocate_start_now


%post
%systemd_post plocate-updatedb.service plocate-updatedb.timer

if [ $1 == 1 ] && [ -d /run/systemd ]; then
     touch %{plocate_start_now} || :
fi

%preun
%systemd_preun plocate-updatedb.service plocate-updatedb.timer

%postun
%systemd_postun_with_restart plocate-updatedb.service plocate-updatedb.timer

%posttrans
# The timer runs once per day. On new installs, let's start both the
# timer and the service immediately in the background, so that the db
# becomes populated. When people install this package onto a running
# system, it's reasonable to assume that they want to use the database.
if [ -f %{plocate_start_now} ]; then
   rm %{plocate_start_now} || :
   if systemctl is-enabled plocate-updatedb.timer &>/dev/null; then
      systemctl start --no-block plocate-updatedb.timer plocate-updatedb.service || :
   fi
fi

%files
%license COPYING
%doc README
%attr(02755,-,plocate) %_bindir/plocate
%_bindir/locate
%_sbindir/plocate-build
%_sbindir/updatedb
%_unitdir/plocate-updatedb.service
%_unitdir/plocate-updatedb.timer
%_mandir/man1/plocate.1*
%_mandir/man1/locate.1*
%_mandir/man5/updatedb.conf.5*
%_mandir/man8/plocate-build.8*
%_mandir/man8/updatedb.8*
%_sysusersdir/plocate.conf
%config(noreplace) %{_sysconfdir}/updatedb.conf
%dir %{_sharedstatedir}/plocate
%{_sharedstatedir}/plocate/CACHEDIR.TAG
%ghost %attr(0640,-,plocate) %verify(not md5 mtime) %{_sharedstatedir}/plocate/plocate.db

%changelog
%autochangelog
