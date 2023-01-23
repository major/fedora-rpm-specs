Name:           tang
Version:        11
Release:        6%{?dist}
Summary:        Network Presence Binding Daemon

License:        GPLv3+
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        tang.sysusers

Patch: 0001-When-json_load_file-fails-report-the-error-details-i.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  git-core
BuildRequires:  jose >= 8
BuildRequires:  libjose-devel >= 8
BuildRequires:  libjose-zlib-devel >= 8
BuildRequires:  libjose-openssl-devel >= 8

BuildRequires:  http-parser-devel >= 2.7.1-3
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig

BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  curl

BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  grep
BuildRequires:  socat
BuildRequires:  sed

%{?systemd_requires}
Requires:       coreutils
Requires:       jose >= 8
Requires:       grep
Requires:       sed

Requires(pre):  shadow-utils

%description
Tang is a small daemon for binding data to the presence of a third party.

%prep
%autosetup -S git

%build
%meson
%meson_build

%install
%meson_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/tang.conf
%{__mkdir_p} $RPM_BUILD_ROOT/%{_localstatedir}/db/%{name}

%check
%meson_test

%pre
%sysusers_create_compat %{SOURCE1}
exit 0

%post
%systemd_post %{name}d.socket

# Let's make sure any existing keys are readable only
# by the owner/group.
if [ -d /var/db/tang ]; then
    for k in /var/db/tang/*.jwk; do
        test -e "${k}" || continue
        chmod 0440 -- "${k}"
    done
    for k in /var/db/tang/.*.jwk; do
        test -e "${k}" || continue
        chmod 0440 -- "${k}"
    done
    chown tang:tang -R /var/db/tang
fi

%preun
%systemd_preun %{name}d.socket

%postun
%systemd_postun_with_restart %{name}d.socket

%files
%license COPYING
%attr(0700, %{name}, %{name}) %{_localstatedir}/db/%{name}
%{_unitdir}/%{name}d@.service
%{_unitdir}/%{name}d.socket
%{_libexecdir}/%{name}d-keygen
%{_libexecdir}/%{name}d-rotate-keys
%{_libexecdir}/%{name}d
%{_mandir}/man8/tang.8*
%{_bindir}/%{name}-show-keys
%{_mandir}/man1/tang-show-keys.1*
%{_mandir}/man1/tangd-rotate-keys.1.*
%{_sysusersdir}/tang.conf

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Sergio Correia <scorreia@redhat.com> - 11-5
- Report error details when json_load_file() fails

* Wed Aug 17 2022 Sergio Arroutbi <sarroutb@redhat.com> - 11-4
- Adopt systemd-sysusers format

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Sergio Correia <scorreia@redhat.com> - 11-1
- New upstream release - v11.
  Resolves: CVE-2021-4076

* Mon Oct 04 2021 Sergio Arroutbi <sarroutb@redhat.com> - 10-5
- Fix scriptlet from previous commit

* Mon Oct 04 2021 Sergio Correia <scorreia@redhat.com> - 10-4
- Keys are created with 0440 mode
  Resolves rhbz#2008204

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Sergio Correia <scorreia@redhat.com> - 10-2
- Fix issues reported by shellcheck and a possible NULL pointer
  dereference reported by gcc static analyzer (3d770c6, 262d98f)

* Wed May 05 2021 Sergio Correia <scorreia@redhat.com> - 10-1
- New upstream release - v10.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 8-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 09 2021 Sergio Correia <scorreia@redhat.com> - 8-2
- Remove extra patches as they are already included in v8 release

* Mon Feb 08 2021 Sergio Correia <scorreia@redhat.com> - 8-1
- New upstream release - v8.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 1 2020 Sergio Correia <scorreia@redhat.com> - 7.8
- Move build system to meson
  Upstream commits (fed9020, 590de27)
- Move key handling to tang itself
  Upstream commits (6090505, c71df1d, 7119454)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 7-6
- Rebuild for http-parser 2.9.4

* Tue Feb 25 2020 Sergio Correia <scorreia@redhat.com> - 7-5
- Rebuilt after http-parser update

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Nathaniel McCallum <npmccallum@redhat.com> - 7-1
- New upstream release
- Retire tang-nagios package (now separate upstream)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Nathaniel McCallum <npmccallum@redhat.com> - 6-1
- New upstream release

* Wed Jun 14 2017 Nathaniel McCallum <npmccallum@redhat.com> - 5-2
- Fix incorrect dependencies

* Wed Jun 14 2017 Nathaniel McCallum <npmccallum@redhat.com> - 5-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Nathaniel McCallum <npmccallum@redhat.com> - 4-2
- Fix a race condition in one of the tests

* Thu Nov 10 2016 Nathaniel McCallum <npmccallum@redhat.com> - 4-1
- New upstream release
- Add nagios subpackage

* Wed Oct 26 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3-1
- New upstream release

* Wed Oct 19 2016 Nathaniel McCallum <npmccallum@redhat.com> - 2-1
- New upstream release

* Tue Aug 23 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1-1
- First release
