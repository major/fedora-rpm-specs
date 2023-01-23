Name:		openssh-ldap-authkeys
Version:	0.2.0
Release:	1%{?dist}
Summary:	Python script to generate SSH authorized_keys files using an LDAP directory

License:	MIT
URL:		https://github.com/fuhry/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	systemd-rpm-macros
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools

# This is only for cases that we don't have a dependency generator active...
%if ! (%{defined python_enable_dependency_generator} || %{defined python_disable_dependency_generator})
Requires:	python%{python3_pkgversion}-ldap
Requires:	python%{python3_pkgversion}-dns
Requires:	python%{python3_pkgversion}-yaml
%endif


%description
openssh-ldap-authkeys is an implementation of AuthorizedKeysCommand for
OpenSSH 6.9 and newer that allows SSH public keys to be retrieved from
an LDAP source. It's provided for situations where a solution other
than 1:1 mapping is needed for users.

With SSH keys stored centrally in LDAP, revocation of a compromised
key is a quick and painless exercise for the user or IT department.

openssh-ldap-authkeys allows shared accounts to be fully auditable as
to who used them.


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install

# Make ghost entries for config files
touch %{buildroot}%{_sysconfdir}/%{name}/olak.yml
touch %{buildroot}%{_sysconfdir}/%{name}/authmap

# Delete example files, we'll docify them later
rm %{buildroot}%{_sysconfdir}/%{name}/*.example


%if 0%{?el7}
%post
%sysusers_create %{name}.sysusers.conf
%tmpfiles_create %{name}.tmpfiles.conf
%endif


%files
%license COPYING
%doc README.md
%doc *.example
%{python3_sitelib}/ldapauthkeys/
%{python3_sitelib}/openssh_ldap_authkeys*egg-info/
%{_bindir}/openssh-ldap-authkeys
%dir %{_sysconfdir}/%{name}
%ghost %config(noreplace) %{_sysconfdir}/%{name}/olak.yml
%ghost %config(noreplace) %{_sysconfdir}/%{name}/authmap
%{_tmpfilesdir}/openssh-ldap-authkeys.tmpfiles.conf
%{_sysusersdir}/openssh-ldap-authkeys.sysusers.conf


%changelog
* Sat Jan 21 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.0~git20200205.aee4c46-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0~git20200205.aee4c46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.0~git20200205.aee4c46-3
- Rebuilt for Python 3.10

* Tue Apr 06 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.0~git20200205.aee4c46-2
- Correctly guard out manual dependencies

* Mon Apr 05 2021 Neal Gompa <ngompa13@gmail.com> - 0.1.0~git20200205.aee4c46-1
- Build pre-release snapshot
