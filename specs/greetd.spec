%global         doc_commit  1bbd4fec
%global         username    greetd
%global         selinuxtype targeted
%global         forgeurl    https://git.sr.ht/~kennylevinsen/greetd

%bcond_without  check
%bcond_without  selinux

Name:           greetd
Version:        0.10.3
Release:        %autorelease
Summary:        A generic greeter daemon

# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# GPL-3.0-only
# MIT
# MIT OR Apache-2.0
# Unlicense
License:        GPL-3.0-only AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND MIT AND Unlicense
URL:            https://kl.wtf/projects/greetd
Source0:        %{forgeurl}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Better offline documentation file
Source1:        %{forgeurl}-docs/blob/%{doc_commit}/index.md#/%{name}-docs-%{doc_commit}.md

# SELinux file labels
Source100:      %{name}.fc
# Pam configs for greeter and user sessions
Source101:      %{name}.pam
Source102:      %{name}-greeter.pam
# User definition
Source103:      %{name}.sysusers
# /var/lib/greetd contents and ownership
Source104:      %{name}.tmpfiles

Patch:          greetd-0.10.0-Unbundle-greetd_ipc.patch

Provides:       service(graphical-login) = greetd

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make
BuildRequires:  scdoc >= 1.10
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros

%if %{with selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif

%description
greetd is a minimal and flexible login manager daemon
that makes no assumptions about what you want to launch.


%package        fakegreet
Summary:        Test utility for greeter development

%description    fakegreet
fakegreet is a test utility that allows launching greeters
without greetd daemon.


%if %{with selinux}
# SELinux subpackage
%package        selinux
Summary:        SELinux policy for %{name}
BuildArch:      noarch
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description    selinux
Custom SELinux policy module for %{name}
%endif

%prep
%autosetup -p1
%cargo_prep
# patch greetd daemon user
sed -i 's/"greeter"/"%{username}"/' config.toml
# replace README with a better documentation file
cp %{SOURCE1} README.md


%generate_buildrequires
%cargo_generate_buildrequires


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%make_build -C man

%if %{with selinux}
# SELinux policy
mkdir selinux
pushd selinux
# generate the type enforcement file as it has no other content
echo 'policy_module(%{name},1.0)' >%{name}.te
cp %{SOURCE100} %{name}.fc
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
popd
%endif


%install
for name in greetd agreety fakegreet; do
    install -D -m755 -vp target/release/$name   %{buildroot}%{_bindir}/$name
done
%make_install PREFIX=%{_prefix} -C man
install -D -m644 -vp greetd.service     %{buildroot}%{_unitdir}/%{name}.service
install -D -m644 -vp config.toml        %{buildroot}%{_sysconfdir}/%{name}/config.toml
install -D -m644 -vp %{SOURCE101}       %{buildroot}%{_sysconfdir}/pam.d/%{name}
install -D -m644 -vp %{SOURCE102}       %{buildroot}%{_sysconfdir}/pam.d/%{name}-greeter
install -D -m644 -vp %{SOURCE103}       %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m644 -vp %{SOURCE104}       %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m750 -vp                    %{buildroot}%{_sharedstatedir}/%{name}

%if %{with selinux}
install -D -m 0644 -vp selinux/%{name}.pp.bz2 \
    %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%endif


%if %{with check}
%check
%cargo_test
%endif



%post
%systemd_post %{name}.service
# block unwanted systemd user services for greetd user
XDG_CONFIG_DIR=%{_sharedstatedir}/%{name}/.config
if [ ! -d $XDG_CONFIG_DIR/systemd ]; then
    mkdir -p $XDG_CONFIG_DIR/systemd/user
    ln -sf /dev/null $XDG_CONFIG_DIR/systemd/user/xdg-desktop-portal.service
    chown -R %{username}:%{username} $XDG_CONFIG_DIR
fi
exit 0

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%if %{with selinux}
%pre selinux
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif


%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%attr(-,%{username},%{username}) %dir %{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}-greeter
%{_bindir}/%{name}
%{_bindir}/agreety
%{_mandir}/man1/agreety.1*
%{_mandir}/man1/greetd.1*
%{_mandir}/man5/greetd.5*
%{_mandir}/man7/greetd-ipc.7*
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service

%files fakegreet
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/fakegreet

%if %{with selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.*
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%endif

%changelog
%autochangelog
