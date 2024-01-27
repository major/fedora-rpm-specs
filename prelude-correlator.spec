Name:           prelude-correlator
Version:        5.2.0
Release:        13%{?dist}
Summary:        Real time correlator of events received by Prelude Manager
License:        GPLv2+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
BuildRequires:  systemd
BuildRequires:  pkgconfig(libprelude) >= %{version}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%{?systemd_requires}
Requires:       python3-%{name} >= %{version}

# Since mass rebuild, debugpackage wont works for prelude-correlator
%define debug_package %{nil}

%description
Prelude-Correlator allows conducting multi-stream correlations
thanks to a powerful programming language for writing correlation
rules. With any type of alert able to be correlated, event
analysis becomes simpler, quicker and more incisive. This
correlation alert then appears within the Prewikka interface
and indicates the potential target information via the set of
correlation rules.

%package -n python3-%{name}
Summary:        Real time correlator of events received by Prelude Manager
Requires:       %{name} = %{version}-%{release}
Requires:       python3-prelude >= %{version}
Requires:       python3-netaddr
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Prelude-Correlator allows conducting multi-stream correlations
thanks to a powerful programming language for writing correlation
rules. With any type of alert able to be correlated, event
analysis becomes simpler, quicker and more incisive. This
correlation alert then appears within the Prewikka interface
and indicates the potential target information via the set of
correlation rules.

%prep
%autosetup -p1

%build
%py3_build

%install
install -d -m 0755 %{buildroot}%{_sbindir}
# We have to use this because py3_install do other things and siteconfig.py
# will be not installed
%{__python3} setup.py install --root=%{buildroot}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/%{name}-%{python3_version}

ln -s ./%{name}-%{python3_version} %{buildroot}%{_sbindir}/%{name}-3
ln -s ./%{name}-3 %{buildroot}%{_sbindir}/%{name}

# Systemd configuration file
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 

%files
%license COPYING
%doc AUTHORS NEWS HACKING.README
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%dir %{_sysconfdir}/%{name}/rules
%dir %{_sysconfdir}/%{name}/rules/python
%config(noreplace) %{_sysconfdir}/%{name}/rules/python/*.py*
%dir %{_sysconfdir}/%{name}/conf.d
%config %{_sysconfdir}/%{name}/conf.d/README
%{_localstatedir}/lib/%{name}/
%{_unitdir}/%{name}.service

%files -n python3-%{name}
%{_sbindir}/%{name}
%{_sbindir}/%{name}-3
%{_sbindir}/%{name}-%{python3_version}
%{python3_sitelib}/preludecorrelator/
%{python3_sitelib}/prelude_correlator-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.2.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.2.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.2.0-4
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.2.0-1
- Bump version 5.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.1.0-1
- Bump version 5.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.1-1
- Bump version 5.0.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.1-2
- Rebuilt for Python 3.7

* Wed Apr 25 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.1-1
- Bump version 4.1.1
- Remove Python2 support

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 4 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-1
- Bump version 4.0.0

* Thu Aug 10 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-4
- Temporary disable debugsource since Mass rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 04 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-1
- Bump version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun May 02 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.0-1
- New upstream release

* Tue Mar 09 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.0rc4-1
- New upstream release

* Mon Feb 01 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.0rc2-1
- New upstream release

* Tue Nov 03 2009 Steve Grubb <sgrubb@redhat.com> - 0.9.0-0.10.beta8
- New beta release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.9.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Steve Grubb <sgrubb@redhat.com> 0.9.0-0.8.beta6
- New beta release

* Mon Mar 02 2009 Steve Grubb <sgrubb@redhat.com> 0.9.0-0.7.beta3
- Fix bz#484361 Error message regarding missing arguments lua ruleset

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.6.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Steve Grubb <sgrubb@redhat.com> 0.9.0-0.5.beta3
- Fix bz#469824 Correct brute force correlation rules
- Add signal header to prelude-correlator.c so it builds correctly bz 474698
- Include unowned /usr/include/prelude-correlator directory

*Fri Jul 11 2008 Steve Grubb <sgrubb@redhat.com> 0.9.0-0.3.beta3
- New beta release

*Thu Jul 03 2008 Steve Grubb <sgrubb@redhat.com> 0.9.0-0.1.beta2
- Initial packaging
