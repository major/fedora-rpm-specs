%global homedir %{_sharedstatedir}/%{name}

Name:           mopidy
Version:        4.0.0~a2
Release:        3%{?dist}
Summary:        An extensible music server written in Python

License:        Apache-2.0
URL:            https://mopidy.com/
Source0:        %{pypi_source}
Source1:        mopidy.conf

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-tornado
BuildRequires:  python3-Pykka >= 4.0.0
BuildRequires:  python3-requests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  tox
BuildRequires:  python3-tox-current-env
BuildRequires:  python3-responses
BuildRequires:  python3-gstreamer1
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  libsoup3
BuildRequires:  systemd-rpm-macros
Requires:       python3-gstreamer1
Requires:       libsoup3
Requires:       gstreamer1-plugins-good
Requires:       python3-tornado
Requires:       python3-Pykka >= 4.0.0
Requires:       python3-requests
Requires(pre):  shadow-utils
Suggests:       mopidy-mpd

%description
Mopidy plays music from local disk, and a plethora of streaming services and
sources. You edit the playlist from any phone, tablet, or computer using a
variety of MPD and web clients.

%package doc
BuildRequires:  python3-graphviz
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-autodoc-typehints
Summary:        Documentation for Mopidy
BuildArch:      noarch

%description doc
Documentation for Mopidy, an extensible music server written in Python.


%prep
%autosetup -n %{name}-4.0.0a2 -p1
#HACK! revert to %%autosetup -n %%{name}-%%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

cd docs
PYTHONPATH=../src make SPHINXBUILD=sphinx-build-3 html man
rm _build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l %{name}

install -d -m 0755 %{buildroot}%{homedir}
install -d -m 0755 %{buildroot}%{_var}/cache/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -p -D extra/mopidyctl/mopidyctl %{buildroot}%{_sbindir}/mopidyctl
install -p -D -m 0644 docs/_build/man/mopidy.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -p -D -m 0644 extra/mopidyctl/mopidyctl.8 %{buildroot}%{_mandir}/man8/mopidyctl.8
install -p -D -m 0644 extra/systemd/mopidy.service %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/conf.d/mopidy.conf

%check
%tox

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{homedir} -s /sbin/nologin \
    -c "%{summary}" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
# Note: these directories needs to be writable by the mopidy service
%attr(-,%name,%name) %dir %{_var}/cache/%{name}
%attr(-,%name,%name) %dir %{homedir}
                     %dir %{_sysconfdir}/%{name}
                     %dir %{_datadir}/%{name}
                     %dir %{_datadir}/%{name}/conf.d
# Note: users are expected to put streaming service credentials here
%attr(0640,%name,%name) %ghost %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_sbindir}/mopidyctl
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man8/mopidyctl.8.*
%{_datadir}/%{name}/conf.d/mopidy.conf

%files doc
%doc docs/_build/html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~a2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 14 2024 Tobias Girstmair <t-fedora@girst.at> - 4.0.0~a2-2
- Fix test failures

* Fri Dec 06 2024 Tobias Girstmair <t-fedora@girst.at> - 4.0.0~a2-1
- Update to 4.0.0a2 (RHBZ#2330474) for Python 3.14 compatibility (RHBZ#2328700)

* Fri Oct 25 2024 Tobias Girstmair <t-fedora@girst.at> - 3.4.2-7
- Further fixes for setuptools 74 (RHBZ#2319634)

* Sun Oct 20 2024 Tobias Girstmair <t-fedora@girst.at> - 3.4.2-6
- Move away from calling 'setup.py test' for setuptools 74 compat (RHBZ#2319634)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4.2-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Tobias Girstmair <t-fedora@girst.at> - 3.4.2-1
- Update to 3.4.2 (#2247358)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Tobias Girstmair <t-fedora@girst.at> - 3.4.1-1
- Update to 3.4.1 (#2149151)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0 (#2080088)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Tobias Girstmair <t-fedora@girst.at> - 3.2.0-1
- Upgrade to Mopidy 3.2.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.1-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Tobias Girstmair <t-fedora@girst.at> - 3.1.1-1
- Upgrade to Mopidy 3.1.1, fixing a crash when extracting tags with gst 1.18

* Wed Dec 16 2020 Tobias Girstmair <t-fedora@girst.at> - 3.1.0-1
- Upgrade to Mopidy 3.1.0

* Thu Dec 3 2020 Tobias Girstmair <t-rpmfusion@girst.at> - 3.0.2-4
- Fix tests for Python 3.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-2
- Rebuilt for Python 3.9

* Fri Apr 3 2020 Tobias Girstmair <t-fedora@girst.at> - 3.0.2-1
- Upgrade to Mopidy 3.0.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Tobias Girstmair <t-rpmfusion@girst.at> - 3.0.1-1
- Initial RPM Release

