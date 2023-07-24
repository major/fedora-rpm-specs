
%global upstream_name rpm2swidtag

Summary: Tools for producing SWID tags for rpm packages and inspecting the SWID tags
Name: swid-tools
Version: 0.8.20
Release: 3%{?dist}
License: ASL 2.0
URL: https://github.com/swidtags/rpm2swidtag
Source0: https://github.com/swidtags/%{upstream_name}/releases/download/%{upstream_name}-%{version}/%{upstream_name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# The following BuildRequires are only needed for check
BuildRequires: python3
BuildRequires: python3-rpm
BuildRequires: python3-lxml
BuildRequires: openssl
BuildRequires: xmlsec1-openssl
BuildRequires: createrepo_c
BuildRequires: fakechroot
BuildRequires: fakeroot
BuildRequires: dnf
BuildRequires: python3-dnf-plugins-core
BuildRequires: gzip
BuildRequires: gnupg2

Requires: python3-rpm
Requires: python3-lxml
Requires: xmlsec1-openssl

Provides: rpm2swidtag = %{version}-%{release}
Obsoletes: rpm2swidtag < 0.7.2

%description
Utility for producing SWID tags for rpm packages and utility for listing
and inspecting SWID tags, including supplemental tag resolution.

%package -n dnf-plugin-swidtags
Summary: DNF plugin for keeping SWID tags up-to-date
Requires: python3-dnf-plugins-core
Requires: swid-tools = %{version}-%{release}
Recommends: dnf

%description -n dnf-plugin-swidtags
DNF plugin for retrieving SWID tags from repository metadata
or producing them locally.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
./test.sh

%files
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/rpm2swidtag
%config(noreplace) %{_sysconfdir}/rpm2swidtag/rpm2swidtag.conf
%dir %{_sysconfdir}/rpm2swidtag/rpm2swidtag.conf.d
%config(noreplace) %{_sysconfdir}/rpm2swidtag/rpm2swidtag.conf.d/*
%config(noreplace) %{_sysconfdir}/rpm2swidtag/*.xml
%config(noreplace) %{_sysconfdir}/rpm2swidtag/*.xslt
%dir %{_sysconfdir}/swid
%config(noreplace) %{_sysconfdir}/swid/swidq.conf
%dir %{_datarootdir}/swidq
%{_datarootdir}/swidq/stylesheets
%{python3_sitelib}/rpm2swidtag/
%{python3_sitelib}/%{upstream_name}-*.egg-info/
%{python3_sitelib}/swidq/
%{_bindir}/rpm2swidtag
%{_bindir}/swidq

%files -n dnf-plugin-swidtags
%config(noreplace) %{_sysconfdir}/dnf/plugins/swidtags.conf
%{python3_sitelib}/dnf-plugins/swidtags.py
%{python3_sitelib}/dnf-plugins/__pycache__/*
%{_bindir}/dnf-plugin-swidtags-update-from-0.7

%post -n dnf-plugin-swidtags

if rpm -q rpm2swidtag dnf-plugin-swidtags 2> /dev/null | grep -E -q '(rpm2swidtag|dnf-plugin-swidtags)-0\.[1-7]\.[0-9]-' ; then
	echo
	echo "Please run dnf-plugin-swidtags-update-from-0.7 to update the filename format."

	if echo "88d7506a4769d9402548cd9f0d242913cd46616f4fa755c52013094af33f5c1b /etc/dnf/plugins/swidtags.conf" | sha256sum -c > /dev/null 2>&1 ; then
		sed -i 's/^# rpm2swidtag_command = /rpm2swidtag_command = /' /etc/dnf/plugins/swidtags.conf
		echo
		echo "The rpm2swidtag_command in /etc/dnf/plugins/swidtags.conf enabled"
		echo "to keep the pre-0.8 behaviour."
	fi
fi

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.8.20-2
- Rebuilt for Python 3.12

* Tue Jun 06 2023 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.20-1
- 2211503 - rebased to 0.8.20.

* Thu May 04 2023 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.19-1
- 2193074 - rebased to 0.8.19.

* Thu Feb 16 2023 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.18-1
- 2170111 - rebased to 0.8.18.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 05 2022 Pazdziora <jpazdziora@redhat.com> - 0.8.17-1
- Rebased to 0.8.17 to address FTBFS on Fedora rawhide.

* Wed Aug 24 2022 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.16-1
- 2119074 - rebased to 0.8.16.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.8.15-2
- Rebuilt for Python 3.11

* Mon Feb 28 2022 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.15-1
- 2058819 - rebased to 0.8.15.

* Wed Feb 16 2022 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.14-1
- 2054857 - rebased to 0.8.14.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.13-1
- Rebased to 0.8.13.
- 2038924 - FTBFS related to dependencies, but new version needed to
  build on Fedora 36 anyway.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.12-2
- Rebuilt for Python 3.10

* Mon Mar 01 2021 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.12-1
- Rebased to 0.8.12.

* Mon Mar 01 2021 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.11-4
- Revert the 1900816 workaround.

* Sat Jan 30 2021 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.11-3
- 1900816 - we cannot test the dnf plugin due to fakechroot failing
  because of glibc changes.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.11-1
- 1884092 - rebased to 0.8.11.

* Fri Sep 25 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.10-1
- 1882162 - rebased to 0.8.10.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.9-2
- Rebuilt for Python 3.9

* Thu Feb 27 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.9-1
- Rebased to 0.8.9.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.8-1
- 1793504 - make ready for Python 3.9.
- Rebased to 0.8.8.

* Thu Sep 19 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.7-1
- Rebased to 0.8.7.

* Mon Aug 26 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.6-1
- 1743902 - align with code changes in dnf-4.2.8.
- Rebased to 0.8.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.4-2
- Rebuild to test Fedora CI.

* Mon May 20 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.4-1
- Rebased to 0.8.4.

* Wed May 15 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.3-1
- Rebased to 0.8.3.

* Mon May 06 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.2-1
- Rebased to 0.8.2.

* Tue Apr 23 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.1-1
- Rebased to 0.8.1.

* Tue Apr 16 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.0-1
- Rebased to 0.8.0.

* Tue Mar 26 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.7.4-1
- Rebased to 0.7.4.
- Added GPG key configuration for Fedora 30.
- Added handling of non-alphanum characters in regid and tagId.

* Fri Mar 15 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.7.3-1
- Rebased to 0.7.3.
- 1689169 - The libdnf 0.28 in Fedora 30 updates-testing changed the
  ConfigParser interfaces.
- 1684536 - Do not print error when running purge on purged setup.

* Fri Mar 01 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.7.2-1
- Rename package to swid-tools.
- Make templates config(noreplace) as well.
- 1683630 - python3-dnf-plugins-core is only needed by the dnf-plugin-swidtags
  subpackage.

* Mon Feb 18 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.7.1-1
- Initial Fedora rawhide release.

* Mon Feb 18 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.6.5-1
- Initial import.
