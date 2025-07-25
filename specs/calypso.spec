%global commit 7317d88263fb9658cd7f1174c6bbcfb0a7ae856a
%global shortcommit %%(c=%{commit}; echo ${c:0:7})
%global date 20190429

%bcond_without check

Name: calypso
Version: 2.0
Release: 0.22.%{date}git%{shortcommit}%{?dist}
Summary: Free and open-source CalDAV calendar server
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://keithp.com/blogs/calypso/
Source0: %{name}-%{commit}.tar.xz
Source1: %{name}-mktarball.sh
Source2: %{name}.config
Source3: %{name}.pam
Source4: %{name}.systemd
# fix python-daemon dependency name
Patch0: %{name}-daemon.patch
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros
%if %{with check}
BuildRequires: git-core
BuildRequires: python3-iniparse
BuildRequires: python3-pytest
%endif
Requires(post): git-core
Requires: git-core
Requires: python3-lockfile
Recommends: python3-kerberos
BuildArch: noarch

%description
Calypso is a python-based CalDAV/CardDAV server that started as a few small
patches to Radicale but was eventually split off as a separate project.

* Uses vObject for parsing and generating the data files
* Stores one event/contact per file
* Uses git to retain a history of the database

%prep
%autosetup -p1 -n %{name}-%{commit}

# Create a sysusers.d config file
cat >calypso.sysusers.conf <<EOF
u calypso - 'CalDAV/CardDAV server with git storage' %{_sharedstatedir}/calypso -
EOF

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l calypso
mkdir -p %{buildroot}%{_sharedstatedir}/calypso
install -Dpm644 calypso.1 %{buildroot}%{_mandir}/man1/calypso.1
install -Dpm644 %{S:2} %{buildroot}%{_sysconfdir}/calypso/config
install -Dpm644 %{S:3} %{buildroot}%{_sysconfdir}/pam.d/calypso
install -Dpm644 %{S:4} %{buildroot}%{_unitdir}/calypso.service

install -m0644 -D calypso.sysusers.conf %{buildroot}%{_sysusersdir}/calypso.conf

%if %{with check}
%check
%pyproject_check_import -t
%pytest
%endif


%preun
%systemd_preun calypso.service

%post
%systemd_post calypso.service
if [ $1 -eq 1 ] && ! [ -d %{_sharedstatedir}/calypso/default ]; then
    mkdir -p %{_sharedstatedir}/calypso/default
    pushd %{_sharedstatedir}/calypso/default
    cat > .calypso-collection << EOF
[collection]
is-calendar = 1
EOF
    git add .calypso-collection
    git commit -m'initialize new default calendar'
    popd
fi

%postun
%systemd_postun_with_restart calypso.service

%files -f %{pyproject_files}
%doc README collection-config config
%dir %attr(0750,root,calypso) %{_sysconfdir}/calypso
%config(noreplace) %{_sysconfdir}/calypso/config
%config(noreplace) %{_sysconfdir}/pam.d/calypso
%{_bindir}/calypso
%{_mandir}/man1/calypso.1*
%{_unitdir}/calypso.service
%dir %attr(0750,calypso,calypso) %{_sharedstatedir}/calypso
%{_sysusersdir}/calypso.conf

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.22.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 21 2025 Dominik Mierzejewski <dominik@greysector.net> 2.0-0.21.20190429git7317d88
- switch to modern python packaging macros (resolves rhbz#2377219)
- drop nonexistent Recommends:

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 2.0-0.20.20190429git7317d88
- Rebuilt for Python 3.14

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0-0.19.20190429git7317d88
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.18.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-0.17.20190429git7317d88
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.16.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0-0.15.20190429git7317d88
- Rebuilt for Python 3.13

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.14.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.13.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.12.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Python Maint <python-maint@redhat.com> - 2.0-0.11.20190429git7317d88
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.10.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.9.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.0-0.8.20190429git7317d88
- Rebuilt for Python 3.11

* Thu Feb 17 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.0-0.7.20190429git7317d88
- Utilize pytest instead of the deprecated nose test runner

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.6.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.5.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0-0.4.20190429git7317d88
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0-0.3.20190429git7317d88
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.2.20190429git7317d88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Mar 02 2020 Dominik Mierzejewski <dominik@greysector.net> 2.0-0.1.20190429git7317d88
- initial build
