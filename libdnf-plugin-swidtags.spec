
# Running rpmbuild --with test requires network access
%bcond_with test

Summary: Keeping SWID tags in sync with rpms installed via libdnf-based tools
Name: libdnf-plugin-swidtags
Version: 0.8.8
Release: 8%{?dist}
URL: https://github.com/swidtags/%{name}
Source0: https://github.com/swidtags/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
License: LGPLv2

BuildRequires: pkgconf
BuildRequires: make
BuildRequires: gcc
BuildRequires: libdnf-devel
# The following BuildRequires are only needed for check
%if %{with test}
BuildRequires: dnf
BuildRequires: tar
%endif

Requires: libdnf >= 0.24.1

%description
The libdnf plugin swidtags_plugin.so can be used to keep the SWID
information synchronized with SWID tags from dnf/yum repository
metadata for package installations, upgrades, and removals using
tools based on libdnf (for example microdnf).

%prep
%setup -q
%build

make %{?_smp_mflags} swidtags_plugin

%install

install -d %{buildroot}%{_libdir}/libdnf/plugins
install -m 755 swidtags_plugin.so %{buildroot}%{_libdir}/libdnf/plugins/

%check
%if %{with test}
make test
%endif

%files
%doc README.md
%license LICENSE
%{_libdir}/libdnf/plugins/swidtags_plugin.so

%changelog
* Fri May 19 2023 Petr Pisar <ppisar@redhat.com> - 0.8.8-8
- Rebuild against rpm-4.19 (https://fedoraproject.org/wiki/Changes/RPM-4.19)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.8-1
- Test fixes.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 22:13:20 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-3
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:02 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-2
- Rebuild for RPM 4.15

* Wed Jun 05 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.7-1
- Build and rpm dependency improvements.

* Tue Jun 04 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.6-1
- Make compatible with PackageKit.
- Fix memory leaks.

* Mon May 27 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.5-1
- 1711989 - bring comments from Fedora package review upstream.

* Tue May 21 2019 Jan Pazdziora <jpazdziora@redhat.com> - 0.8.4-1
- Initial release.
