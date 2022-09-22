Name:           nodepool
Version:        3.13.1
Release:        4%{?dist}
Summary:        Nodepool management for a distributed test infrastructure

License:        ASL 2.0
URL:            https://zuul-ci.org
Source0:        %pypi_source

Source1:        nodepool-launcher.service
Source2:        nodepool-builder.service
Source10:       nodepool.yaml
Source11:       secure.conf
Source12:       launcher-logging.yaml
Source13:       builder-logging.yaml
Source14:       sudoer

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  systemd


%description
Nodepool is a service used by the OpenStack CI team to deploy and manage a pool
of devstack images on a cloud server for use in OpenStack project testing.


%package launcher
Summary:        Nodepool launcher service
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description launcher
Nodepool launcher service.


%package builder
Summary:        Nodepool builder service
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       yum-utils
Requires:       sudo
Requires:       qemu-img
Requires:       diskimage-builder

%description builder
Nodepool builder service.


%package doc
Summary:        Nodepool documentation
BuildRequires:  python3-zuul-sphinx
BuildRequires:  python3-sphinx
BuildRequires:  python3-voluptuous
BuildRequires:  python3-kazoo
BuildRequires:  python3-zuul-sphinx
BuildRequires:  python3-snowballstemmer
BuildRequires:  python3-sphinxcontrib-programoutput
BuildRequires:  python3-sphinxcontrib-httpdomain
BuildRequires:  python3-reno

%description doc
Nodepool documentation.


%prep
%autosetup -n nodepool-%{version} -p1
sed -i "/^diskimage-builder>=2.36.0/d" requirements.txt
sed -i "s/^openshift<=0.8.9/openshift/" requirements.txt
rm -Rf nodepool/tests


%build
%py3_build
# Make the Nodepool directory a repo to satisfy python-reno
git init /builddir/build/BUILD/nodepool-%{version}
pushd /builddir/build/BUILD/nodepool-%{version}
git config user.email "you@example.com"
git config user.name "Your Name"
git add -A .
git commit -m"Initial commit"
popd
PBR_VERSION=%{version} SPHINX_DEBUG=1 sphinx-build-3 -b html doc/source build/html
rm -Rf /builddir/build/BUILD/nodepool-%{version}/.git


%install
%py3_install

# Copy non python modules over
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/nodepool-launcher.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/nodepool-builder.service
install -p -D -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/nodepool/nodepool.yaml
install -p -D -m 0640 %{SOURCE11} %{buildroot}%{_sysconfdir}/nodepool/secure.conf
install -p -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/nodepool/launcher-logging.yaml
install -p -D -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/nodepool/builder-logging.yaml
install -p -D -m 0644 %{SOURCE14} %{buildroot}%{_sysconfdir}/sudoers.d/nodepool
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/nodepool/scripts
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/nodepool/elements
install -p -d -m 0750 %{buildroot}%{_sharedstatedir}/nodepool
install -p -d -m 0750 %{buildroot}%{_sharedstatedir}/nodepool/dib
install -p -d -m 0750 %{buildroot}%{_sharedstatedir}/nodepool/.config/openstack
install -p -d -m 0750 %{buildroot}%{_localstatedir}/log/nodepool
install -p -d -m 0755 %{buildroot}%{_localstatedir}/cache/nodepool/dib_cache
install -p -d -m 0755 %{buildroot}%{_localstatedir}/cache/nodepool/dib_tmp


%pre
getent group nodepool >/dev/null || groupadd -r nodepool
if ! getent passwd nodepool >/dev/null; then
  useradd -r -g nodepool -G nodepool -d %{_sharedstatedir}/nodepool -s /sbin/nologin -c "Nodepool Daemon" nodepool
fi
exit 0


%post launcher
%systemd_post nodepool-launcher.service
%post builder
%systemd_post nodepool-builder.service

%preun launcher
%systemd_preun nodepool-launcher.service
%preun builder
%systemd_preun nodepool-builder.service

%postun launcher
%systemd_postun nodepool-launcher.service
%postun builder
%systemd_postun nodepool-builder.service


%files
%{_bindir}/nodepool
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/nodepool/nodepool.yaml
%config(noreplace) %attr(0644, root, nodepool) %{_sysconfdir}/nodepool/secure.conf
%dir %{_sysconfdir}/nodepool/scripts
%dir %{_sysconfdir}/nodepool/elements
%dir %attr(0755, nodepool, nodepool) %{_localstatedir}/log/nodepool
%attr(0755, nodepool, nodepool) %{_sharedstatedir}/nodepool
%{python3_sitelib}/nodepool
%{python3_sitelib}/nodepool-*.egg-info

%files launcher
%{_bindir}/nodepool-launcher
%{_unitdir}/nodepool-launcher.service
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/nodepool/launcher-logging.yaml

%files builder
%{_bindir}/nodepool-builder
%{_unitdir}/nodepool-builder.service
%{_sysconfdir}/sudoers.d/nodepool
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/nodepool/builder-logging.yaml
%attr(0755, nodepool, nodepool) %{_localstatedir}/cache/nodepool

%files doc
%doc LICENSE build/html


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.13.1-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Fabien Boucher <fboucher@redhat.com> - 3.13.1-1
- Bump to 3.13.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.12.0-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-1
- Rebuilt for Python 3.9

* Mon Mar 09 2020 Fabien Boucher <fboucher@redhat.com> - 3.12.0-1
- Bump to 3.12.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Fabien Boucher <fboucher@redhat.com> - 3.10.0-1
- Bump to 3.10.0

* Fri Oct 11 2019 Fabien Boucher <fboucher@redhat.com> - 3.9.0-1
- Import 3.9.0 packaging from Software Factory

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Mon Apr 02 2018 Tristan Cacqueray <tdecacqu@redhat.com> - 3.0.0-1
- Import from software factory repository
