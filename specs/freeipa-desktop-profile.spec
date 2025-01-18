%global debug_package %{nil}
%global plugin_name desktop-profile

%global ipa_python3_sitelib %{python3_sitelib}

Name:           freeipa-%{plugin_name}
Version:        0.0.8
Release:        28%{?dist}
Summary:        FleetCommander integration with FreeIPA

BuildArch:      noarch

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/abbra/freeipa-desktop-profile
Source0:        freeipa-desktop-profile-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-ipaserver >= 4.6.0
Requires:      ipa-server-common >= 4.4.1

Requires(post): python3-ipa-%{plugin_name}-server
Requires: python3-ipa-%{plugin_name}-server
Requires: python3-ipa-%{plugin_name}-client

%description
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander.

%package -n freeipa-%{plugin_name}-common
Summary: Common package for client side FleetCommander integration with FreeIPA

%description  -n freeipa-%{plugin_name}-common
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander. This package adds common files needed by client-side packages


%package -n python3-ipa-%{plugin_name}-server
Summary: Server side of FleetCommander integration with FreeIPA for Python 3
Requires: python3-ipaserver

%description  -n python3-ipa-%{plugin_name}-server
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander. This package adds server-side support for Python 3
version of FreeIPA

%package -n python3-ipa-%{plugin_name}-client
Summary: Client side of FleetCommander integration with FreeIPA for Python 3
Requires: python3-ipaclient
Requires: freeipa-%{plugin_name}-common

%description  -n python3-ipa-%{plugin_name}-client
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander. This package adds client-side support for Python 3
version of FreeIPA

%prep
%autosetup

%build
touch debugfiles.list

%install
rm -rf $RPM_BUILD_ROOT
%__mkdir_p %buildroot/%{_sysconfdir}/ipa
%__mkdir_p %buildroot/%_datadir/ipa/schema.d
%__mkdir_p %buildroot/%_datadir/ipa/updates
#%__mkdir_p %buildroot/%_datadir/ipa/ui/js/plugins/deskprofile

%__cp plugin/etc/ipa/fleetcommander.conf %buildroot/%{_sysconfdir}/ipa/

for s in ipaclient ipaserver; do
    %__mkdir_p %{buildroot}%{ipa_python3_sitelib}/$s/plugins
    for j in $(find plugin/$s/plugins -name '*.py') ; do
        %__cp $j %{buildroot}%{ipa_python3_sitelib}/$s/plugins
    done
done

for j in $(find plugin/schema.d -name '*.ldif') ; do
    %__cp $j %buildroot/%_datadir/ipa/schema.d
done

for j in $(find plugin/updates -name '*.update') ; do
    %__cp $j %buildroot/%_datadir/ipa/updates
done

# Do not package web UI plugin yet
#for j in $(find plugin/ui/%{plugin_name} -name '*.js') ; do
#    %__cp $j %buildroot/%_datadir/ipa/js/plugins/%{plugin_name}
#done

%posttrans
python3 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    # This must be run in posttrans so that updates from previous
    # execution that may no longer be shipped are not applied.
    /usr/sbin/ipa-server-upgrade --quiet >/dev/null || :

    # Restart IPA processes. This must be also run in postrans so that plugins
    # and software is in consistent state
    # NOTE: systemd specific section

    /bin/systemctl is-enabled ipa.service >/dev/null 2>&1
    if [  $? -eq 0 ]; then
        /bin/systemctl restart ipa.service >/dev/null 2>&1 || :
    fi
fi

%files
%license COPYING
%doc plugin/Feature.mediawiki
%_datadir/ipa/schema.d/*
%_datadir/ipa/updates/*
#_datadir/ipa/ui/js/plugins/deskprofile/*

%files -n freeipa-%{plugin_name}-common
%{_sysconfdir}/ipa/fleetcommander.conf

%files -n python3-ipa-%{plugin_name}-client
%ipa_python3_sitelib/ipaclient/plugins/*

%files -n python3-ipa-%{plugin_name}-server
%ipa_python3_sitelib/ipaserver/plugins/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.8-27
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 0.0.8-25
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.0.8-21
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.0.8-18
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Oliver Gutierrez <ogutierrez@redhat.com> - 0.0.8-16
- Changed licensing in specfile to the correct one

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.8-14
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.8-11
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.8-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.8-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.8-5
- Remove python2 (#1634553)

* Sun Jul 22 2018 Alexander Bokovoy <abokovoy@redhat.com> 0.0.8-4
- Do not ship python2-ipa-deskprofile-server for Fedora 29 or later

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.8-2
- Rebuilt for Python 3.7

* Thu May 31 2018 Oliver Gutierrez <ogutierrez@redhat.com> 0.0.8-1
- Updated to version 0.0.8

* Mon May 21 2018 Oliver Gutierrez <ogutierrez@redhat.com> 0.0.7-1
- Updated to version 0.0.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Oliver Gutierrez <ogutierrez@redhat.com> 0.0.6-4
- Fixed dependencies for EPEL 7

* Thu Nov 23 2017 Oliver Gutierrez <ogutierrez@redhat.com> 0.0.6-3
- Moved context configuration file to a common package for client side packages

* Mon Nov 20 2017 Oliver Gutierrez <ogutierrez@redhat.com> 0.0.6-2
- Fixed errors in specfile

* Fri Nov 17 2017 Alexander Bokovoy <abokovoy@redhat.com> 0.0.6-1
- Allow loading JSON data from files only in interactive mode
- Package Python2 and Python3 versions separately
- Package client and server side separately

* Wed Feb  8 2017 Alexander Bokovoy <abokovoy@redhat.com> 0.0.4-1
- New release
- Added global desktop profile policy

* Wed Nov  2 2016 Alexander Bokovoy <abokovoy@redhat.com> 0.0.2-1
- New release

* Tue Nov  1 2016 Fabiano Fidêncio <fidencio@redhat.com> 0.0.1-2
- Use the same posttrans method used by FreeIPA

* Mon Sep  5 2016 Alexander Bokovoy <abokovoy@redhat.com> 0.0.1-1
- Initial release
