Name:           noggin
Version:        1.6.1
Release:        4%{?dist}
Summary:        Self-service user portal for FreeIPA for communities

License:        MIT
URL:            https://noggin-aaa.readthedocs.io/
Source0:        https://github.com/fedora-infra/noggin/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        noggin.service
Source2:        noggin.sysconfig

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros >= 0-14
BuildRequires:  systemd-rpm-macros
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
install -pm 0644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service
install -pm 0644 %{S:2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg
touch %{buildroot}%{_localstatedir}/log/noggin/access.log
touch %{buildroot}%{_localstatedir}/log/noggin/error.log

%files -f %{pyproject_files}
%license LICENSE
%doc README.md noggin.cfg.example
%{_bindir}/noggin-sar
%{_unitdir}/%{name}.service
%ghost %{_sysconfdir}/%{name}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_localstatedir}/log/noggin
%ghost %{_localstatedir}/log/noggin/*.log
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
