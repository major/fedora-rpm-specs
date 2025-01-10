Name:           noggin
Version:        1.9.0
Release:        4%{?dist}
Summary:        Self-service user portal for FreeIPA for communities

License:        MIT
URL:            https://noggin-aaa.readthedocs.io/
Source0:        https://github.com/fedora-infra/noggin/archive/v%{version}/%{name}-%{version}.tar.gz

Source10:       noggin-README.Fedora

# Backports from upstream
## From:

# Proposed upstream
## From:

# Downstream Fedora changes

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros >= 0-14
BuildRequires:  systemd-rpm-macros
Requires:       nginx-filesystem
Requires:       (python3dist(gunicorn) with /usr/bin/gunicorn-3)


%description
Noggin is a self-service portal for FreeIPA.

The primary purpose of the portal is to allow users to sign up
and manage their account information and group membership.

%package theme-fas
Summary:        Fedora Account System theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-fas
Provides a theme for Noggin used for the Fedora Account System.

%package theme-centos
Summary:        CentOS Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-centos
Provides a theme for Noggin used for CentOS Accounts.

%package theme-openSUSE
Summary:        openSUSE Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}

%description theme-openSUSE
Provides a theme for Noggin used for openSUSE Accounts.


%prep
%autosetup -n %{name}-%{version} -p1

# Allow markupsafe 3 and newer
sed -i "/^markupsafe/s/\^/>=/" pyproject.toml

# Install README.Fedora file
install -pm 0644 %{SOURCE10} README.Fedora


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files noggin

mkdir -p %{buildroot}%{_bindir}
install -pm 0755 deployment/scripts/sar.py %{buildroot}%{_bindir}/noggin-sar
# Fix shebangs for noggin-sar
%py3_shebang_fix %{buildroot}%{_bindir}/noggin-sar

mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_localstatedir}/log/noggin
install -pm 0644 deployment/noggin.service %{buildroot}%{_unitdir}/%{name}.service
install -pm 0644 deployment/noggin.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg
touch %{buildroot}%{_localstatedir}/log/noggin/access.log
touch %{buildroot}%{_localstatedir}/log/noggin/error.log
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d
install -pm 0644 deployment/nginx.conf %{buildroot}%{_sysconfdir}/nginx/conf.d/noggin.conf
mkdir -p %{buildroot}%{_localstatedir}/log/nginx
touch %{buildroot}%{_localstatedir}/log/nginx/noggin.access.log
touch %{buildroot}%{_localstatedir}/log/nginx/noggin.error.log


%files -f %{pyproject_files}
%license LICENSE
%doc README.md deployment/noggin.cfg.example README.Fedora
%{_bindir}/noggin-sar
%{_unitdir}/%{name}.service
%ghost %{_sysconfdir}/%{name}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/nginx/conf.d/noggin.conf
%dir %{_localstatedir}/log/noggin
%ghost %{_localstatedir}/log/noggin/*.log
%dir %{_localstatedir}/log/nginx/
%ghost %{_localstatedir}/log/nginx/*.log
%exclude %{python3_sitelib}/%{name}/themes/fas
%exclude %{python3_sitelib}/%{name}/themes/centos
%exclude %{python3_sitelib}/%{name}/themes/openSUSE


%files theme-fas
%{python3_sitelib}/%{name}/themes/fas


%files theme-centos
%{python3_sitelib}/%{name}/themes/centos


%files theme-openSUSE
%{python3_sitelib}/%{name}/themes/openSUSE


%changelog
* Thu Oct 10 2024 Lumír Balhar <lbalhar@redhat.com> - 1.9.0-4
- Allow markupsafe 3 and newer

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.9.0-2
- Rebuilt for Python 3.13

* Tue Feb 06 2024 Aurelien Bompard <abompard@fedoraproject.org> - 1.9.0-1
- Update to 1.0.9
- Remove upstreamed patches

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8.0-1
- Rebase to 1.8.0 (Fixes RHBZ#2254144)

* Tue Sep 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.7.1-4
- Add patch to support flask-babel v3
- Reorganize patches to apply unconditionally

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.7.1-2
- Add patch for building in epel9

* Sat Feb 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.7.1-1
- Rebase to 1.7.1
- Add quick start documentation as README.Fedora

* Sat Feb 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.6.1-6
- Add sample no-op nginx configuration
- Fix noggin.service to use correct launch function call

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 08 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.6.1-4
- Fix noggin.service to use correct launch method

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.6.1-2
- Rebuilt for Python 3.11

* Mon Jun 06 2022 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 1.6.1-1
- Moved out the tests from the installed package
- Updated the dependencies

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1^git20210323.3b487ed-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1^git20210323.3b487ed-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.1^git20210323.3b487ed-2
- Rebuilt for Python 3.10

* Tue Mar 23 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1^git20210323.3b487ed-1
- Bump to new git snapshot

* Sun Mar 21 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20210319.511d606-1.1
- Bump to new git snapshot
- Refresh patches

* Fri Oct 30 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20201028.542001b-0.1
- Bump to new git snapshot

* Sat Oct 24 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20200923.6ed6757-0.2
- Add CentOS theme subpackage

* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20200923.6ed6757-0.1
- Bump to new git snapshot

* Sun Jul 26 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1+git20200722.fcba2d8-0.1
- Bump to new post-release git snapshot

* Sun Apr 19 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.1-0.1
- Initial packaging
