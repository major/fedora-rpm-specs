%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}

Summary: ModSecurity Core Ruleset
Name: mod_security_crs
Version: 4.15.0
Release: 2%{?dist}
License: Apache-2.0
URL: https://coreruleset.org/
Source: https://github.com/coreruleset/coreruleset/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch
Requires: mod_security >= 2.9.6
Obsoletes: mod_security_crs-extras < 3.0.0

# Patch0: mod_security_crs-XXX.patch

%description
This package provides the base rules for mod_security.

%prep
%autosetup -p1 -S gendiff -n coreruleset-%{version}

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/
%{__install} -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules
%{__install} -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/plugins
%{__install} -d %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules
%{__install} -d %{buildroot}%{_datarootdir}/mod_modsecurity_crs/plugins

%{__mv} rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
%{__mv} rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf

%{__install} -m0644 rules/*.conf %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/
%{__install} -m0644 rules/*.data %{buildroot}%{_datarootdir}/mod_modsecurity_crs/rules/
%{__install} -m0644 plugins/* %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/plugins/
%{__mv} crs-setup.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf

%post
if [ $1 == 1 ]; then
     # activate base_rules
     for f in `ls %{_datarootdir}/mod_modsecurity_crs/rules/` ; do 
         %{__ln_s} %{_datarootdir}/mod_modsecurity_crs/rules/$f %{_sysconfdir}/httpd/modsecurity.d/activated_rules/$f; 
     done
     %{__sed} -i '/IncludeOptional modsecurity\.d\/\*\.conf/ a\    IncludeOptional modsecurity.d\/plugins\/*-config.conf\n    IncludeOptional modsecurity.d\/plugins\/*-before.conf' %{_httpd_confdir}/mod_security.conf
     %{__sed} -i '/Include modsecurity\.d\/\*\.conf/a\    Include modsecurity.d/plugins/*-config.conf\n    Include modsecurity.d/plugins/*-before.conf' %{_httpd_confdir}/mod_security.conf
     %{__sed} -i '/IncludeOptional modsecurity\.d\/local_rules\/\*\.conf/a\    IncludeOptional modsecurity.d\/plugins\/*-after.conf' %{_httpd_confdir}/mod_security.conf
     %{__sed} -i '/Include modsecurity\.d\/local_rules\/\*\.conf/a\    Include modsecurity.d\/plugins\/*-after.conf' %{_httpd_confdir}/mod_security.conf
fi
exit 0

%preun
if [ $1 == 0 ]; then
     %{__sed} -i -E '/Include(Optional)? modsecurity\.d\/plugins/d' %{_httpd_confdir}/mod_security.conf
     for f in `ls %{_datarootdir}/mod_modsecurity_crs/rules/` ; do 
         %{__rm} %{_sysconfdir}/httpd/modsecurity.d/activated_rules/$f; 
     done
fi
exit 0

%files
%license LICENSE
%doc CHANGES.md README.md
%{_datarootdir}/mod_modsecurity_crs
%{_sysconfdir}/httpd/modsecurity.d/plugins
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/activated_rules/*
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/crs-setup.conf
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/plugins/*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Daniel Demus <daniel-fedoauth@demus.dk> - 4.15.0-2
- Prepare for plugins (see https://coreruleset.org/20220112/crs-plugin-mechanism/)

* Tue Jun 03 2025 Luboš Uhliarik <luhliari@redhat.com> - 4.15.0-1
- new version 4.15.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 02 2024 Luboš Uhliarik <luhliari@redhat.com> - 4.2.0-1
- new version 4.2.0
- switch to autosetup

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 06 2023 Luboš Uhliarik <luhliari@redhat.com> - 3.3.4-5
- SPDX migration

* Mon Mar 20 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.3.4-4
- Change URL to new official homepage

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Luboš Uhliarik <luhliari@redhat.com> - 3.3.4-2
- Add Early blocking feature patch again

* Fri Sep 30 2022 Luboš Uhliarik <luhliari@redhat.com> - 3.3.4-1
- new version 3.3.4

* Wed Sep 07 2022 Luboš Uhliarik <luhliari@redhat.com> - 3.3.0-6
- Fix application of early blocking patch

* Wed Aug 31 2022 Luboš Uhliarik <luhliari@redhat.com> - 3.3.0-5
- Backport early blocking feature

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 05 2021 Lubos Uhliarik <luhliari@redhat.com> - 3.2.0-1
- new version 3.2.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-4
- Exclude rule files should not be symlink

* Sat Apr 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-3
- Use versioned obsoletes
- Move away from /lib since rules are data

* Sat Apr 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-2
- Fix the install part since extra and experimental rules are not longer included in 3.x
- Remove EL5 bits since EL5/EPEL5 are OEL-ed
- Bump reqs

* Sat Apr 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0
- Clean up the spec

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9.20160414git-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.9.20160414git-1
- Update to 2.9.20160414git

* Tue Mar 08 2016 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.9.20160219git-1
- Update to 2.2.9
- Minor spec cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.8-1
- Update to 2.2.8
- Adapt the spec file to new github tarball schema.
- Correct bugus date in the spec file.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.6-4
- "extras" subpackage is not provided on RHEL7

* Wed Oct 17 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.6-3
- Remove the patch since we're requiring mod_security >= 2.7.0
- Require mod_security >= 2.7.0

* Mon Oct 01 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.6-2
- Add a patch to fix incompatible rules.
- Update to new git release

* Sat Sep 15 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.6-1
- Update to 2.2.6
- Update spec file since upstream moved to Github.

* Thu Sep 13 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.5-5
- Enable extra rules sub-package for EPEL.

* Tue Aug 28 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.5-4
- Fix spec for el5

* Tue Aug 28 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.5-3
- Add BuildRoot def for el5 compatibility

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.5-1
- upgrade

* Wed Jun 20 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.4-3
- "extras" subpackage is not provided on RHEL

* Thu May 03 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.4-2
- fix fedora-review issues (#816975)

* Thu Apr 19 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.4-1
- initial package


