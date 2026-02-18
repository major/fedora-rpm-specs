Name:           mopidy-mpd
Version:        4.0.0~a4
Release:        1%{?dist}
Summary:        Mopidy extension for controlling Mopidy from MPD clients

License:        Apache-2.0
URL:            https://mopidy.com/ext/mpd/
Source0:        https://files.pythonhosted.org/packages/source/m/mopidy-mpd/mopidy_mpd-4.0.0a4.tar.gz
# package has been renamed from Mopidy-MPD to mopidy_mpd, pypi_source can't handle that.
%dnl Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  tox
BuildRequires:  python3-tox-current-env
BuildRequires:  mopidy >= 4.0.0~a10
Requires:       mopidy >= 4.0.0~a10

%description
Frontend that provides a full MPD server implementation to make Mopidy
available from MPD clients.


%prep
%autosetup -n mopidy_mpd-4.0.0a4 -p1
#^TODO: revert to %%autosetup -n %%{name}-%%{version} -p1
rm -f setup.cfg # HACK: work around https://github.com/tox-dev/tox/issues/3602

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mopidy_mpd

%check
%tox

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sun Feb 15 2026 Tobias Girstmair <t-fedora@girst.at> - 4.0.0~a4-1
- Upgrade to latest prerelease (RHBZ#2416927) and rebuild due to FTBFS (RHBZ#2434829)

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~a1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 4.0.0~a1-5
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 4.0.0~a1-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~a1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jul 13 2025 Tobias Girstmair <t-fedora@girst.at> - 4.0.0~a1-2
- Fix changelog

* Fri Jul 4 2025 Tobias Girstmair <t-fedora@girst.at> - 4.0.0~a1-1
- Upgrade to latest prerelease

* Tue Jun 24 2025 Python Maint <python-maint@redhat.com> - 3.3.0^20241110git9c66c58-2
- Rebuilt for Python 3.14

* Tue Jan 21 2025 Tobias Girstmair <t-fedora@girst.at> - 3.3.0^20241110git9c66c58
- Upgrade to latest snapshot, for compatibility with mopidy-4.0.0~a2 (RHBZ#2336892)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Tobias Girstmair <t-fedora@girst.at> - 3.3.0-10
- move away from calling 'setup.py test' directly (RHBZ#2319635)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.11

* Fri Apr 29 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0 (#2080093)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 11 2021 Tobias Girstmair <t-fedora@girst.at> - 3.2.0-1
- Update to version 3.2.0, providing better MPD compatibility

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 5 2020 Tobias Girstmair <t-fedora@girst.at> - 3.1.0-1
- Update to version 3.1.0, providing better MPD compatibility

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 23 2020 Tobias Girstmair <t-rpmfusion@girst.at> - 3.0.0-4
- Explicitly BuildRequire setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Tobias Girstmair <t-rpmfusion@girst.at> - 3.0.0-1
- Initial RPM Release

