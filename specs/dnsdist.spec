%ifarch %{nodejs_arches}
# el-7 does not have uglifyjs
%if "0%{?el7}" == "0"
%global uglify 1
%endif
%endif

Name: dnsdist
Version: 1.9.8
Release: %autorelease
Summary: Highly DNS-, DoS- and abuse-aware loadbalancer
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://dnsdist.org
Source0: https://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2

ExcludeArch: %{ix86} #1994125
ExcludeArch: armv7hl #1994125
BuildRequires: boost-devel
BuildRequires: fstrm-devel
BuildRequires: gcc-c++
#ppc64 buildroot doesn't have libatomic, so require it
#https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/FSMMBCD2C2SPO4D66O35EGUTF7YXEPBA/
BuildRequires: libatomic
BuildRequires: libcap-devel
BuildRequires: libedit-devel
BuildRequires: libnghttp2-devel
BuildRequires: libsodium-devel
BuildRequires: lmdb-devel
%ifarch %{ix86} x86_64 %{mips} aarch64
BuildRequires: luajit-devel
%else
BuildRequires: lua-devel
%endif
BuildRequires: openssl-devel
BuildRequires: protobuf-devel
BuildRequires: re2-devel
BuildRequires: readline-devel
BuildRequires: systemd-devel
BuildRequires: systemd-units
BuildRequires: tinycdb-devel
%if 0%{?uglify}
BuildRequires: uglify-js
%endif
BuildRequires: make
Requires(post): systemd
Requires(preun): shadow-utils
Requires(preun): systemd
Requires(postun): systemd

%description
dnsdist is a highly DNS-, DoS- and abuse-aware loadbalancer. Its goal in life
is to route traffic to the best server, delivering top performance to
legitimate users while shunting or blocking abusive traffic.


%prep
%autosetup -p2

# run as dnsdist user
sed -i '/^ExecStart/ s/dnsdist/dnsdist -u dnsdist -g dnsdist/' dnsdist.service.in

# Create a sysusers.d config file
cat >dnsdist.sysusers.conf <<EOF
u dnsdist - 'dnsdist user' - -
EOF

%build
%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --disable-static \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --enable-dnscrypt \
    --enable-dns-over-https \
    --enable-dns-over-tls \
%if 0%{?fedora} >= 41
    --enable-tls-providers \
%endif
    --enable-unit-tests \
    --with-cdb \
    --with-lmdb \
    --with-nghttp2 \
    --with-re2

rm html/js/*
%if 0%{?uglify}
make min_js
%else
cp src_js/*.js html/js
rename .js .min.js html/js/*.js
%endif

make %{?_smp_mflags}
%{__cp} dnsdist.conf-dist dnsdist.conf.sample

%install
make install DESTDIR=%{buildroot}

# install systemd unit file
install -D -p -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sysconfdir}/%{name}/
%{__mv} %{buildroot}%{_sysconfdir}/%{name}/dnsdist.conf-dist %{buildroot}%{_sysconfdir}/%{name}/dnsdist.conf
chmod 0640 %{buildroot}/%{_sysconfdir}/%{name}/dnsdist.conf

install -m0644 -D dnsdist.sysusers.conf %{buildroot}%{_sysusersdir}/dnsdist.conf


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc dnsdist.conf.sample
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/dnsdist.conf
%{_sysusersdir}/dnsdist.conf

%changelog
%autochangelog
