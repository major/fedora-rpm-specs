%global srcname spf-engine

Name:           pypolicyd-spf
Version:        3.1.0
Release:        2%{?dist}
Summary:        SPF Policy Server for Postfix (Python implementation)

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://launchpad.net/%{srcname}
Source0:        https://launchpad.net/%{srcname}/3.1/%{version}/+download/%{srcname}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Patch0:         pypolicyd-spf-3.0.4-service.patch

BuildArch:      noarch
Requires:       postfix
Requires:       python3-pyspf
Requires:       python3-authres

BuildRequires:  systemd
BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%package milter
Summary:        Milter for pypolicyd-spf (spf-engine).
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pymilter

%description
pypolicyd-spf (spf-engine) is a Postfix policy engine for Sender Policy
Framework (SPF) checking. It is implemented in pure Python and uses the
python-spf (pyspf) module.

This SPF policy server implementation provides flexible options for different
receiver policies and sender whitelisting to enable it to support a very wide
range of requirements.

%description milter
Milter for pypolicyd-spf.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Move doc files
%{__mv} data/share/doc/python-policyd-spf/README.per_user_whitelisting .
%{__mv} data/etc/python-policyd-spf/policyd-spf.conf.commented .

%build
%pyproject_wheel


%install
%pyproject_install

# We want the binary in Postfix libexec directory
%{__mkdir_p} %{buildroot}%{_libexecdir}/postfix
%{__mv} %{buildroot}%{_bindir}/policyd-spf %{buildroot}%{_libexecdir}/postfix

# Move etc
%{__mv} %{buildroot}%{_prefix}/etc %{buildroot}%{_sysconfdir}
%{__sed} -i -e 's/^HELO_reject = SPF_Not_Pass$/HELO_reject = Fail/' \
               %{buildroot}%{_sysconfdir}/python-policyd-spf/policyd-spf.conf

# Remove SysV init
%{__rm} -rf %{buildroot}%{_sysconfdir}/init.d

# Temporary files for milter
%{__mkdir_p} %{buildroot}%{_tmpfilesdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%pre
/usr/sbin/useradd -r -M -s /sbin/nologin -d /run/pyspf-milter \
    pyspf-milter &>/dev/null || :

 
%files
%doc README.txt README.per_user_whitelisting CHANGES COPYING
%doc policyd-spf.conf.commented
%dir %{_sysconfdir}/python-policyd-spf
%config(noreplace) %{_sysconfdir}/python-policyd-spf/policyd-spf.conf
%{_libexecdir}/postfix/policyd-spf
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{python3_sitelib}/spf_engine
%{python3_sitelib}/spf_engine-%{version}.dist-info/
%pycached %{python3_sitelib}/spf_engine/__init__.py
%pycached %{python3_sitelib}/spf_engine/policy*.py
%pycached %{python3_sitelib}/spf_engine/config.py


%files milter
%dir %{_sysconfdir}/pyspf-milter
%config(noreplace) %{_sysconfdir}/pyspf-milter/pyspf-milter.conf
%{_bindir}/pyspf-milter
%{_unitdir}/pyspf-milter.service
%{_mandir}/man8/*
%pycached %{python3_sitelib}/spf_engine/milter*.py
%pycached %{python3_sitelib}/spf_engine/util.py


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct  9 2024 Bojan Smojver <bojan@rexursive.com> 3.1.0-1
- Update to 3.1.0

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.4-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.4-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul  6 2023 Bojan Smojver <bojan@rexursive.com> 3.0.4-1
- Update to 3.0.4

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.9.3-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Bojan Smojver <bojan@rexursive.com> 2.9.3-4
- split milter into a sub-package

* Tue Nov 15 2022 Bojan Smojver <bojan@rexursive.com> 2.9.3-3
- require python3-pymilter (bug #2142743)

* Mon Nov 14 2022 Bojan Smojver <bojan@rexursive.com> 2.9.3-2
- require python3-authres (bug #2142476)

* Tue Jul 26 2022 Bojan Smojver <bojan@rexursive.com> 2.9.3-1
- bump up to 2.9.3 (spf-engine is now the source)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.2-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.2-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-2
- Rebuilt for Python 3.7

* Thu Feb 22 2018 Bojan Smojver <bojan@rexursive.com> 2.0.2-1
- bump up to 2.0.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Bojan Smojver <bojan@rexursive.com> 2.0.1-1
- bump up to 2.0.1
- drop ipaddress patch (this version works with python3 only)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-5
- Rebuild for Python 3.6

* Tue Nov 29 2016 Bojan Smojver <bojan@rexursive.com> 1.3.2-4
- try building with and for python3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec  5 2015 Bojan Smojver <bojan@rexursive.com> 1.3.2
- bump up to 1.3.2

* Tue Dec  1 2015 Bojan Smojver <bojan@rexursive.com> 1.3.1-4
- bump the release number to rebuild

* Thu Jun 18 2015 Bojan Smojver <bojan@rexursive.com> 1.3.1-3
- use python-ipaddress instead of python-ipaddr

* Wed Oct  1 2014 Bojan Smojver <bojan@rexursive.com> 1.3.1-2
- fix bug #1138206

* Fri Sep  5 2014 Bojan Smojver <bojan@rexursive.com> 1.3.1-1
- bump up to 1.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Bojan Smojver <bojan@rexursive.com> 1.2-3
- own the config dir

* Wed Aug  7 2013 Bojan Smojver <bojan@rexursive.com> 1.2-2
- address issues from package review
- specify python_sitelib only for EL5 or less
- explicitly depend on python2-devel
- remove CFLAGS
- do not specify the whole directory as noreplace, but config file instead

* Tue Aug  6 2013 Bojan Smojver <bojan@rexursive.com> 1.2-1
- bump up to 1.2

* Thu May 16 2013 Bojan Smojver <bojan@rexursive.com> 1.1.2-3
- fix changelog

* Tue May 14 2013 Bojan Smojver <bojan@rexursive.com> 1.1.2-2
- use macros in URLs

* Sun May 12 2013 Bojan Smojver <bojan@rexursive.com> 1.1.2-1
- bump up to 1.1.2
- use version macro in source
- require postfix

* Fri Mar 15 2013 Bojan Smojver <bojan@rexursive.com> 1.1-1
- initial release
