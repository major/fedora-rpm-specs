%global oldpkg letsencrypt

# build docs on Fedora but not on RHEL (not all sphinx packages available)
%if 0%{?fedora}
%bcond_without docs
%else
%bcond_with docs
%endif
%bcond_without tests

%global         SPHINXBUILD sphinx-build-3

%global MODULES %{expand:certbot-dns-cloudflare certbot-dns-digitalocean certbot-dns-dnsimple certbot-dns-dnsmadeeasy certbot-dns-gehirn certbot-dns-linode certbot-dns-luadns certbot-dns-nsone certbot-dns-ovh certbot-dns-rfc2136 certbot-dns-route53 certbot-dns-sakuracloud}
%if 0%{?fedora} || 0%{?rhel} < 9
  %global MODULES %{expand:%MODULES certbot-dns-google}
%endif


Name:           certbot
Version:        3.0.1
Release:        1%{?dist}
Summary:        A free, automated certificate authority client

License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Source10:       certbot-renew-systemd.service
Source11:       certbot-renew-systemd.timer
Source12:       certbot-sysconfig-certbot
Source13:       certbot-cli.ini
Source14:       certbot-README.fedora
Source15:       certbot.logrotate

BuildArch:      noarch

BuildRequires:  python3-devel
# "test" extras also needs "python3dist(types-mock)", "python3dist(types-pyrfc3339)"
# which are not available on Fedora. Just require "pytest" here.
BuildRequires:  python3-pytest
# for docs
%if 0%{?fedora}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

# For the systemd macros
%{?systemd_requires}
BuildRequires:  systemd

# Need to label the httpd rw stuff correctly until base selinux policy updated
Requires(post): %{_sbindir}/restorecon

Requires: python3-certbot = %{version}-%{release}

Obsoletes: %{oldpkg} < 0.6.0
Provides: %{oldpkg} = %{version}-%{release}

%define _description() \%description -n %1\
\%{summary}

%define _package() \%package -n %1\
Summary:    %2 plugin for certbot\
\%if 0\%{?fedora}\
Provides:      %2 = \%{version}-\%{release}\
# adding these as manual requires because we nuke them with sed for the loop\
# of installing buildreqs and these would cause blocking since they aren't built yet\
Requires:      python3-acme = \%{version}-\%{release}\
Requires:      python3-certbot = \%{version}-\%{release}\
\%endif

%define _package_doc() \%package -n %1\
Summary:    Documenation for %1 libraries
Requires:   font(fontawesome)

%define _files() \%files -n python3-certbot-dns-%1\
\%license certbot-dns-%1/LICENSE.txt\
\%doc certbot-dns-%1/README.rst\
\%{python3_sitelib}/certbot_dns_%1/\
\%{python3_sitelib}/certbot_dns_%1-\%{version}.dist-info/

%define _files_doc() \%files -n python-%1-doc\
\%license %1/LICENSE.txt\
\%doc %1/README.rst\
\%doc %1/docs/_build/html


%description
certbot is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%package -n python3-certbot
Summary:    Python 3 libraries used by certbot
Requires:   python3-acme

%package -n python3-acme
Summary:    Python library for the ACME protocol

%package -n python3-certbot-apache
Summary:    The apache plugin for certbot
Requires:   mod_ssl
# adding these as manual requires because we nuke them with sed for the loop
# of installing buildreqs and these would cause blocking since they aren't built yet
Requires: python3-acme = %{version}-%{release}
Requires: python3-certbot = %{version}-%{release}
# Provide the name users expect as a certbot plugin
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} >= 8)
Provides:   certbot-apache = %{version}-%{release}
%endif

%package -n python3-certbot-nginx
Summary:     The nginx plugin for certbot
# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:      certbot-nginx = %{version}-%{release}
%endif
# adding these as manual requires because we nuke them with sed for the loop
# of installing buildreqs and these would cause blocking since they aren't built yet
Requires: python3-acme = %{version}-%{release}
Requires: python3-certbot = %{version}-%{release}
# Recommend the CLI as that will be the interface most use
Recommends:    certbot >= %{version}

%_package python3-certbot-dns-cloudflare certbot-dns-cloudflare
%if 0%{?fedora} || 0%{?rhel} < 9
# missing deps for el9
%_package python3-certbot-dns-google certbot-dns-google
%endif
%_package python3-certbot-dns-digitalocean certbot-dns-digitalocean
%_package python3-certbot-dns-dnsimple certbot-dns-dnsimple
%_package python3-certbot-dns-dnsmadeeasy certbot-dns-dnsmadeeasy
%_package python3-certbot-dns-gehirn certbot-dns-gehirn
%_package python3-certbot-dns-linode certbot-dns-linode
%_package python3-certbot-dns-luadns certbot-dns-luadns
%_package python3-certbot-dns-nsone certbot-dns-nsone
%_package python3-certbot-dns-ovh certbot-dns-ovh
%_package python3-certbot-dns-rfc2136 certbot-dns-rfc2136
%_package python3-certbot-dns-route53 certbot-dns-route53
%_package python3-certbot-dns-sakuracloud certbot-dns-sakuracloud
%if 0%{?fedora}
%_package_doc python-acme-doc
%_package_doc python-certbot-doc
%_package_doc python-certbot-dns-cloudflare-doc
%_package_doc python-certbot-dns-digitalocean-doc
%_package_doc python-certbot-dns-dnsimple-doc
%_package_doc python-certbot-dns-dnsmadeeasy-doc
%_package_doc python-certbot-dns-gehirn-doc
%_package_doc python-certbot-dns-google-doc
%_package_doc python-certbot-dns-linode-doc
%_package_doc python-certbot-dns-luadns-doc
%_package_doc python-certbot-dns-nsone-doc
%_package_doc python-certbot-dns-ovh-doc
%_package_doc python-certbot-dns-rfc2136-doc
%_package_doc python-certbot-dns-route53-doc
%_package_doc python-certbot-dns-sakuracloud-doc
%endif

%description -n python3-certbot
The python3 libraries to interface with certbot

%description -n python3-acme
Python 3 library for use of the Automatic Certificate Management Environment
protocol as defined by the IETF. It's used by the Let's Encrypt project.

%description -n python3-certbot-apache
Plugin for certbot that allows for automatic configuration of apache

%description -n python3-certbot-nginx
Plugin for certbot that allows for automatic configuration of ngnix

%_description python3-certbot-dns-cloudflare
%if 0%{?fedora} || 0%{?rhel} < 9
# missing el9 deps
%_description python3-certbot-dns-google
%endif
%_description python3-certbot-dns-digitalocean
%_description python3-certbot-dns-dnsimple
%_description python3-certbot-dns-dnsmadeeasy
%_description python3-certbot-dns-gehirn
%_description python3-certbot-dns-linode
%_description python3-certbot-dns-luadns
%_description python3-certbot-dns-nsone
%_description python3-certbot-dns-ovh
%_description python3-certbot-dns-rfc2136
%_description python3-certbot-dns-route53
%_description python3-certbot-dns-sakuracloud
%if 0%{?fedora}
%_description python-acme-doc
%_description python-certbot-doc
%_description python-certbot-dns-cloudflare-doc
%_description python-certbot-dns-digitalocean-doc
%_description python-certbot-dns-dnsimple-doc
%_description python-certbot-dns-dnsmadeeasy-doc
%_description python-certbot-dns-gehirn-doc
%_description python-certbot-dns-google-doc
%_description python-certbot-dns-linode-doc
%_description python-certbot-dns-luadns-doc
%_description python-certbot-dns-nsone-doc
%_description python-certbot-dns-ovh-doc
%_description python-certbot-dns-rfc2136-doc
%_description python-certbot-dns-route53-doc
%_description python-certbot-dns-sakuracloud-doc
%endif

%prep
%autosetup -n %{name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{name}.egg-info


%generate_buildrequires
for module in acme certbot %{MODULES} certbot-apache certbot-nginx
do
  cd $module
  sed -Ei '/(acme|certbot)>=\{version\}/d' setup.py
    %pyproject_buildrequires
  cd ..
done

%build
for module in acme certbot %{MODULES} certbot-apache certbot-nginx
do
  cd $module
    %pyproject_wheel
  cd ..
done

%install
%pyproject_install

%if 0%{?fedora}
# not all modules have docs
for module in acme certbot %{MODULES}
do
cd $module/docs && make html SPHINXBUILD=%{SPHINXBUILD}
rm -rf docs/_build/html/{.buildinfo,man,_sources}
cd ../..
done
%endif

mv %{buildroot}%{_bindir}/certbot{,-3}

# Add compatibility symlink as requested by upstream conference call
ln -s certbot %{buildroot}/usr/bin/%{oldpkg}
# Put the man pages in place
# install -pD -t %%{buildroot}%%{_mandir}/man1 docs/_build/man/*1*
# Use python3 for F26+ or if python2 is disabled
ln -s certbot-3 %{buildroot}%{_bindir}/certbot
install -Dm 0644 --preserve-timestamps %{SOURCE10} %{buildroot}%{_unitdir}/certbot-renew.service
install -Dm 0644 --preserve-timestamps %{SOURCE11} %{buildroot}%{_unitdir}/certbot-renew.timer
install -Dm 0644 --preserve-timestamps %{SOURCE12} %{buildroot}%{_sysconfdir}/sysconfig/certbot
install -Dm 0644 --preserve-timestamps %{SOURCE13} %{buildroot}%{_sysconfdir}/letsencrypt/cli.ini
install -Dm 0644 --preserve-timestamps %{SOURCE15} %{buildroot}%{_sysconfdir}/logrotate.d/certbot
cp -a %{SOURCE14} %{_builddir}/%{name}-%{version}/README.fedora

# project uses old letsencrypt dir for compatibility
install -dm 0755 %{buildroot}%{_sysconfdir}/%{oldpkg}
install -dm 0755 %{buildroot}%{_sharedstatedir}/%{oldpkg}
install -dm 0755 %{buildroot}%{_localstatedir}/log/letsencrypt

%if %{with tests}
%check
for module in acme certbot %{MODULES} certbot-apache certbot-nginx; do
pushd $module
%pytest -v
popd
done
%endif


# The base selinux policies don't handle the certbot directories yet so set them up manually
%post
%if 0%{?rhel} && 0%{?rhel} <= 7
semanage fcontext -a -t cert_t '%{_sysconfdir}/(letsencrypt|certbot)/(live|archive)(/.*)?'
%endif
restorecon -R %{_sysconfdir}/letsencrypt || :
%systemd_post certbot-renew.timer

# Remind users to start certbot-renew.timer if they need certbot to automatically renew certs
if [ "$1" -eq 1 ] ; then
  echo ""
  echo "Certbot auto renewal timer is not started by default."
  echo "Run 'systemctl start certbot-renew.timer' to enable automatic renewals."
fi


%preun
%systemd_preun certbot-renew.timer


%postun
%systemd_postun certbot-renew.timer


%files -n certbot
%license LICENSE.txt
%doc certbot/README.rst README.fedora certbot/CHANGELOG.md
%{_bindir}/certbot
%{_bindir}/%{oldpkg}
%dir %{_sysconfdir}/%{oldpkg}
%dir %{_sharedstatedir}/%{oldpkg}
%dir %{_localstatedir}/log/letsencrypt
%config(noreplace) %{_sysconfdir}/%{oldpkg}/cli.ini
%config(noreplace) %{_sysconfdir}/sysconfig/certbot
%config(noreplace) %{_sysconfdir}/logrotate.d/certbot
%{_unitdir}/certbot-renew.service
%{_unitdir}/certbot-renew.timer


%files -n python3-certbot
%license certbot/LICENSE.txt
%doc certbot/README.rst certbot/CHANGELOG.md
%{_bindir}/certbot-3
%{python3_sitelib}/certbot/
%{python3_sitelib}/certbot-%{version}.dist-info/


%files -n python3-acme
%license acme/LICENSE.txt
%doc acme/README.rst
%{python3_sitelib}/acme/
%{python3_sitelib}/acme-%{version}.dist-info/


%files -n python3-certbot-apache
%license certbot-apache/LICENSE.txt
%doc certbot-apache/README.rst
%{python3_sitelib}/certbot_apache/
%{python3_sitelib}/certbot_apache-%{version}.dist-info/


%files -n python3-certbot-nginx
%license certbot-nginx/LICENSE.txt
%doc certbot-nginx/README.rst
%{python3_sitelib}/certbot_nginx/
%{python3_sitelib}/certbot_nginx-%{version}.dist-info/


%_files cloudflare
%if 0%{?fedora} || 0%{?rhel} < 9
# missing el9 deps
%_files google
%endif
%_files digitalocean
%_files dnsimple
%_files dnsmadeeasy
%_files gehirn
%_files linode
%_files luadns
%_files nsone
%_files ovh
%_files rfc2136
%_files route53
%_files sakuracloud
%if 0%{?fedora}
%_files_doc acme
%_files_doc certbot
%_files_doc certbot-dns-cloudflare
%_files_doc certbot-dns-digitalocean
%_files_doc certbot-dns-dnsimple
%_files_doc certbot-dns-dnsmadeeasy
%_files_doc certbot-dns-gehirn
%_files_doc certbot-dns-google
%_files_doc certbot-dns-linode
%_files_doc certbot-dns-luadns
%_files_doc certbot-dns-nsone
%_files_doc certbot-dns-ovh
%_files_doc certbot-dns-rfc2136
%_files_doc certbot-dns-route53
%_files_doc certbot-dns-sakuracloud
%endif


%changelog
* Fri Jan 03 2025 Jonathan Wright <jonathan@almalinux.org> - 3.0.1-1
- update to 3.0.1 rhbz#2324360

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Python Maint <python-maint@redhat.com> - 2.11.0-2
- Rebuilt for Python 3.13

* Wed Jun 12 2024 Jonathan Wright <jonathan@almalinux.org> - 2.11.0-1
- update to 2.11.0 rhbz#2272763

* Tue Feb 13 2024 Jonathan Wright <jonathan@almalinux.org> - 2.9.0-1
- update to 2.9.0 rhbz#2263448

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Jonathan Wright <jonathan@almalinux.org> - 2.8.0-1
- Update to 2.8.0 rhbz#2246252

* Fri Oct 20 2023 Jonathan Wright <jonathan@almalinux.org> - 2.7.2-1
- Update to 2.7.2 rhbz#2242065

* Fri Oct 13 2023 Jonathan Wright <jonathan@almalinux.org> - 2.7.1-1
- Update to 2.7.1 rhbz#2242065

* Sat Sep 09 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.6.0-5
- Fix build with Python 3.12.0rc2 (warning message changed)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 15 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.6.0-3
- Fix build with Python 3.12
- Fix broken symbolic links

* Fri Jul 07 2023 Python Maint <python-maint@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.12

* Mon May 22 2023 Jonathan Wright <jonathan@almalinux.org> - 2.6.0-1
- Update to 2.6.0 rhbz#2196870
- Build python-certbot-dns-digitalocean on EPEL9

* Thu Apr 27 2023 rob thijssen <rthijssen@gmail.com> - 2.5.0-3
- Correct typo in logrotate configuration rhbz#2187543

* Thu Apr 13 2023 Jonathan Wright <jonathan@almalinux.org> - 2.5.0-2
- Include logrotate configuration rhbz#2102070

* Tue Apr 04 2023 Jonathan Wright <jonathan@almalinux.org> - 2.5.0-1
- Update to 2.5.0 rhbz#2155209

* Thu Mar 30 2023 Jerry James <loganjerry@gmail.com> - 2.2.0-3
- Change fontawesome-fonts R to match fontawesome 4.x

* Thu Mar 30 2023 Jonathan Wright <jonathan@almalinux.org> - 2.2.0-2
- add reminder about certbot-renew.timer during install

* Mon Mar 20 2023 Jonathan Wright <jonathan@almalinux.org> - 2.2.0-1
- build all certbot packages from a single source package rhbz#2132123
- update to 2.2.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Nick Bebout <nb@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Nov 09 2022 Nick Bebout <nb@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.30.0-1
- Update to 1.30.0 rhbz#2125049

* Tue Aug 09 2022 Jonathan Wright <jonathan@almalinux.org> - 1.29.0-1
- Update to 1.29.0 (#2094619)
- Update license to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.27.0-2
- Rebuilt for Python 3.11

* Wed May 04 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.27.0-1
- Update to 1.27.0 (#2081519)

* Thu Apr 07 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0 (#2064912)

* Mon Mar 14 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0 (#2052127)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.22.0-1
- Update to 1.22.0 (#2020069)

* Tue Oct 05 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0 (#2010952)

* Fri Sep 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0 (#2002040)

* Fri Sep 03 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.18.0-2
- enable "--preconfigured-renewal" also for EPEL8 (#1986205)

* Wed Aug 04 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0 (#1966771)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14.0-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0 (#1946804)
- also own /var/log/letsencrypt (#1946000)

* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0 (#1934815)

* Tue Feb 2 2021 Nick Bebout <nb@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0 (#1913017)

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#1904183)

* Wed Dec 02 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#1903310)

* Wed Oct 07 2020 Nick Bebout <nb@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Tue Oct 06 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Aug 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#1866066)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1854600)

* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843203)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831914)

* Sat Mar 21 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-3
- remove subpackage "python3-certbot-tests" which was committed by accident

* Mon Mar 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-2
- add subpackage "python3-certbot-tests" on EPEL8

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809807)

* Sun Feb 23 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.0-2
- re-added "python-mock" as runtime dependency

* Fri Feb 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (#1791087)

* Sun Feb 02 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.0-3
- do not strip "certbot.tests"

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.1.0-1
- Update to 1.1.0

* Thu Dec 05 2019 Felix Schwarz <fschwarz@fedoraproject.org> 1.0.0-2
- adapt conditions for EPEL8
- remove runtime dependency on mock

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769107)

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757575)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748612)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742577)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Sun Jun 30 2019 Miro Hrončok <mhroncok@redhat.com> - 0.35.1-2
- Rebuilt to update automatic Python dependencies

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717677)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-3
- Fix build on Python 2

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-2
- Update --renew-hook to --deploy-hook (#1665755)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686184) (#1705300)
- Run renew timer twice daily with 12-hour random delay

* Wed Feb 13 2019 Eli Young <elyscape@gmail.com> - 0.31.0-2
- Fix acme dependency

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673769)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669313)

* Thu Jan 03 2019 Eli Young <elyscape@gmail.com> - 0.29.1-2
- Disable certbot-level randomized delay on renew
- Run certbot renew non-interactively

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627569)

* Mon Aug 20 2018 Eli Young <elyscape@gmail.com> - 0.26.1-2
- Properly create config and state directories (#1485745, #1613138)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600292)

* Thu Jul 12 2018 Eli Young <elyscape@gmail.com> - 0.26.0-1
- Update to 0.26.0 (#1600292)

* Fri Jun 29 2018 Eli Young <elyscape@gmail.com> - 0.25.1-5
- Clean up some rpmlint violations

* Wed Jun 27 2018 Eli Young <elyscape@gmail.com> - 0.25.1-4
- Update remaining python2 requirements for F27

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-3
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Eli Young <elyscape@gmail.com> - 0.25.1-2
- Make certbot depend on same version of python-certbot

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591031)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588219)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574140)
- Remove unnecessary patches

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563899)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2 (#1558280)

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0 (#1552953)

* Thu Feb 08 2018 Eli Young <elyscape@gmail.com> - 0.21.1-5
- Remove SELinux policy management on Fedora
- Add temporary requirement on python-future

* Wed Feb 07 2018 Eli Young <elyscape@gmail.com> - 0.21.1-4
- Set permissions for certbot directories

* Wed Feb 07 2018 Eli Young <elyscape@gmail.com> - 0.21.1-3
- Regenerate dependencies from project (#1496291)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Update to 0.21.1 (#1535995)

* Tue Jan 02 2018 Eli Young <elyscape@gmail.com> - 0.20.0-2
- Unify Fedora and EPEL7 specs

* Wed Dec 20 2017 Eli Young <elyscape@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Fri Oct 06 2017 Eli Young <elyscape@gmail.com> - 0.19.0-1
- Update to 0.19.0 (bz#1499368)

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-2
- Fix deps

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2

* Mon Sep 18 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-2
- Fix BuildRequires and Requires to use python2-* where applicable

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-3
- Further tweaks after upstream feedback
- On F26+ use python3

* Wed May 17 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-2
- Tweaks to the renew service bz#1444814

* Tue May 16 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Fri May 12 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.0-1
- Update to 0.14.0
- Fix for bz#1444814

* Fri Apr 28 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-2
- Incorrect target for timer

* Wed Apr 19 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-1
* Update to 0.13.0
- Timer tweaks bz#1441846
* Tue Mar 07 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-4
- Up the timer to daily at the request of upstream
* Mon Mar 06 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-3
- Label the certificates generated by certbot with correct selinux context
- Include optional timer for automated renewal
* Mon Mar 06 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-2
- upstream request not to use py3 yet so switch to py2 for default
- include a py3 option for testing
* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-1
- update to 0.12.0
* Fri Feb 17 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-4
- change to python3 now certbot supports it
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-2
- parsedatetime needs future but doesn't declare it
* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-1
- Upgrade to 0.11.1
* Thu Jan 05 2017 Adam Williamson <awilliam@redhat.com> - 0.9.3-2
- Doc generation no longer needs sphinxcontrib-programoutput
- Work around Python dep generator dependency problem (#1410631)
* Fri Oct 14 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3
* Thu Oct 13 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Wed Jul 06 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.8.1-2
- Remove sed-replace that changes help output and code behavior, closes #1348391
* Wed Jun 15 2016 Nick Bebout <nb@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
* Fri Jun 03 2016 james <james.hogarth@gmail.com> - 0.8.0-1
- update to 0.8.0 release
* Tue May 31 2016 James Hogarth <james.hogarth@gmail.com> - 0.7.0-1
- Update to 0.7.0
* Thu May 12 2016 Nick Bebout <nb@fedoraproject.org> - 0.6.0-2
- Bump release to 2 since 1.0devXXX is greater than 1
* Thu May 12 2016 Nick Bebout <nb@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
* Thu May 12 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-1.0dev0git41f347d
- Update with compatibility symlink requested from upstream 
- Update with fixes from review
* Sun May 08 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-0.0dev0git38d7503
- Upgrade to 0.6.0 dev snapshot
- Rename to certbot to match upstream rename
* Wed Apr 06 2016 Nick Bebout <nb@fedoraproject.org> - 0.5.0-1
- Upgrade to 0.5.0
* Sat Mar 05 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-3
- Package does not require python-werkzeug anymore, upstream #2453
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-2
- Fix build on EL7 where no newer setuptools is available
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-1
- Upgrade to 0.4.2
* Tue Mar 1 2016 Nick Le Mouton <nick@noodles.net.nz> - 0.4.1-1
- Update to 0.4.1
* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
* Sat Jan 23 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.2.0-4
- Use acme dependency version consistently and add psutil min version
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-3
- Update the configargparse version in other places
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-2
- Update python-configargparse version requirement
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Apache plugin support for non-Debian based systems
- Relaxed PyOpenSSL version requirements
- Resolves issues with the Apache plugin enabling redirect
- Improved error messages from the client
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-2
- Fix packaging issues
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- fix a confusing UI path that caused some users to repeatedly renew their
- certs while experimenting with the client, in some cases hitting issuance rate limits
- numerous Apache configuration parser fixes
- avoid attempting to issue for unqualified domain names like "localhost"
- fix --webroot permission handling for non-root users
* Tue Dec 08 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.0-3
- Add python-sphinx_rtd_theme build requirement
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Add documentation from upstream
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-5.dev20151123
- Add missing build requirements that slipped through
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-4.dev20151123
- The python2 library should have the dependencies and not the bindir one
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3.dev20151123
- Separate out the python libraries from the application itself
- Enable python tests
* Tue Dec 01 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec to account for the runtime dependencies discovered
- Update spec to sit inline with current python practices
* Sun Apr 26 2015 Torrie Fischer <tdfischer@hackerbots.net> 0-1.git1d8281d.fc20
- Initial package
