Summary: A set of system configuration and setup files
Name: setup
Version: 2.15.0
Release: %autorelease
License: LicenseRef-Fedora-Public-Domain
# This package is a downstream-only project
URL: https://src.fedoraproject.org/rpms/setup

Source0001: aliases
Source0002: bashrc
Source0003: csh.cshrc
Source0004: csh.login
Source0005: ethertypes
Source0006: filesystems
Source0007: host.conf
Source0008: hosts
Source0009: inputrc
Source0010: networks
Source0011: printcap
Source0012: profile
Source0013: protocols
Source0014: services
Source0015: shells

Source0021: lang.csh
Source0022: lang.sh

Source0031: COPYING
Source0032: uidgid
Source0033: setup.sysusers.conf
Source0034: uidgidlint
Source0035: serviceslint

BuildArch: noarch
BuildRequires: bash
BuildRequires: tcsh
BuildRequires: perl-interpreter
BuildRequires: /usr/bin/systemd-sysusers
#systemd-rpm-macros: required to use _sysusersdir and _tmpfilesdir macro
BuildRequires: systemd-rpm-macros
#require system release for saner dependency order
Requires: system-release

%description
The setup package contains a set of important system configuration and
setup files, such as passwd, group, and profile.

%prep
mkdir -p etc/profile.d
cp %{lua: for i=1,15 do print(sources[i]..' ') end} etc/
cp %SOURCE21 %SOURCE22 etc/profile.d/
touch etc/{exports,motd,subgid,subuid,environment,fstab}

mkdir -p docs
cp %SOURCE31 %SOURCE32 docs/

%build
# This produces ./etc/{passwd,group,shadow,gshadow}
systemd-sysusers --root=./ %SOURCE33
# Allow the user to copy the file
chmod 0400 ./etc/{shadow,gshadow}

%check
# Sanity checking selected files....
bash -n etc/bashrc
bash -n etc/profile
tcsh -f etc/csh.cshrc
tcsh -f etc/csh.login
bash %SOURCE34 docs/uidgid
(cd etc && perl %SOURCE35 ./services)

%install
mkdir -p %{buildroot}/etc
cp -ar etc/* %{buildroot}/etc/

install -D -m0644 %SOURCE33 %{buildroot}%{_sysusersdir}/setup.conf

mkdir -p %{buildroot}/var/log
touch %{buildroot}/etc/environment
touch %{buildroot}/etc/fstab
echo "#Add any required envvar overrides to this file, it is sourced from /etc/profile" >%{buildroot}/etc/profile.d/sh.local
echo "#Add any required envvar overrides to this file, it is sourced from /etc/csh.login" >%{buildroot}/etc/profile.d/csh.local
mkdir -p %{buildroot}/etc/motd.d
mkdir -p %{buildroot}/run/motd.d
mkdir -p %{buildroot}/usr/lib/motd.d
touch %{buildroot}/usr/lib/motd
#tmpfiles needed for files in /run
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "f /run/motd 0644 root root -" >%{buildroot}%{_tmpfilesdir}/%{name}.conf
echo "d /run/motd.d 0755 root root -" >>%{buildroot}%{_tmpfilesdir}/%{name}.conf
chmod 0644 %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Install yum protection config. Old location in /etc.
mkdir -p %{buildroot}/etc/dnf/protected.d/
echo "setup" >%{buildroot}/etc/dnf/protected.d/setup.conf
# Install dnf5 protection config. New location under /usr.
mkdir -p %{buildroot}/usr/share/dnf5/libdnf.conf.d/
cat >%{buildroot}/usr/share/dnf5/libdnf.conf.d/protect-setup.conf <<EOF
[main]
protected_packages = setup
EOF

%post -p <lua>
-- Throw away useless and dangerous update stuff until rpm will be able to
-- handle it.  See: http://rpm.org/ticket/6
for i, name in ipairs({"passwd", "shadow", "group", "gshadow"}) do
   os.remove("/etc/"..name..".rpmnew")
end
-- Use rpm.spawn() if available (in >= 4.20) but fallback to forking if not.
--
-- Initialize or update /etc/alias.db from /etc/aliases for sendmail, etc.
if posix.access("/usr/bin/newaliases", "x") then
  if rpm.spawn ~= nil then
    rpm.spawn({'/usr/bin/newaliases'}, {stdout='/dev/null'})
  else
    local pid = posix.fork()
    if pid == 0 then
      posix.redirect2null(1)
      posix.exec("/usr/bin/newaliases")
    elseif pid > 0 then
      posix.wait(pid)
    end
  end
end
-- Ensure pre-allocated tmpfiles are created immediately on upgrades.
if posix.access("/usr/bin/systemd-tmpfiles", "x") then
  if rpm.spawn ~= nil then
    rpm.spawn({"/usr/bin/systemd-tmpfiles", "--create"}, {stderr='/dev/null'})
  else
    local pid = posix.fork()
    if pid == 0 then
      posix.redirect2null(2)
      posix.exec("/usr/bin/systemd-tmpfiles", "--create")
    elseif pid > 0 then
      posix.wait(pid)
    end
  end
end

%files
%license docs/COPYING
%doc docs/uidgid
%verify(not md5 size mtime) %config(noreplace) /etc/passwd
%verify(not md5 size mtime) %config(noreplace) /etc/group
%verify(not md5 size mtime) %attr(0000,root,root) %config(noreplace,missingok) /etc/shadow
%verify(not md5 size mtime) %attr(0000,root,root) %config(noreplace,missingok) /etc/gshadow
%verify(not md5 size mtime) %config(noreplace) /etc/subuid
%verify(not md5 size mtime) %config(noreplace) /etc/subgid
%config(noreplace) /etc/services
%verify(not md5 size mtime) %config(noreplace) /etc/exports
%config(noreplace) /etc/aliases
%config(noreplace) /etc/environment
%config(noreplace) /etc/filesystems
%config(noreplace) /etc/host.conf
%verify(not md5 size mtime) %config(noreplace) /etc/hosts
%verify(not md5 size mtime) %config(noreplace) /etc/motd
%dir /etc/motd.d
%ghost %verify(not md5 size mtime) %attr(0644,root,root) /run/motd
%dir /run/motd.d
%verify(not md5 size mtime) %config(noreplace) /usr/lib/motd
%dir /usr/lib/motd.d
%config(noreplace) /etc/printcap
%verify(not md5 size mtime) %config(noreplace) /etc/inputrc
%config(noreplace) /etc/bashrc
%config(noreplace) /etc/profile
%config(noreplace) /etc/protocols
%config(noreplace) /etc/ethertypes
%config(noreplace) /etc/csh.login
%config(noreplace) /etc/csh.cshrc
%config(noreplace) /etc/networks
%dir /etc/profile.d
%config(noreplace) /etc/profile.d/sh.local
%config(noreplace) /etc/profile.d/csh.local
/etc/profile.d/lang.{sh,csh}
%config(noreplace) %verify(not md5 size mtime) /etc/shells
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) /etc/fstab
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/setup.conf
/etc/dnf/protected.d/%{name}.conf
%dir /usr/share/dnf5
%dir /usr/share/dnf5/libdnf.conf.d
/usr/share/dnf5/libdnf.conf.d/protect-setup.conf

%changelog
%autochangelog
