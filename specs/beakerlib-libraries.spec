%global libraries_path %{_datadir}/beakerlib-libraries

Name: beakerlib-libraries
Version: 0.7
Release: 11%{?dist}
Summary: Beakerlib libraries

License: GPL-2.0-only
URL: https://pagure.io/beakerlib-libraries/
Source0: https://releases.pagure.org/beakerlib-libraries/%{name}-%{version}.tar.gz
BuildArch: noarch
AutoReq: no
Requires: beakerlib

%description
Beakerlib Libraries are used by beakerlib tests to encapsulate common complex
tasks such as configuring and starting a particular daemon in a single
function.

%prep
%autosetup

%build

%install
find . -maxdepth 2 -mindepth 2 '(' -path './bin/*' -o -path './.git*' ')' -prune -o -type d \
    -exec sh -c 'install -v -d $RPM_BUILD_ROOT%libraries_path/$(dirname "{}")/Library' ';' \
    -exec sh -c 'cp -v -a "{}" $RPM_BUILD_ROOT%libraries_path/$(dirname "{}")/Library'  ';'
install -d "$RPM_BUILD_ROOT/%_bindir"
install -m755 "bin/get-test-deps" "$RPM_BUILD_ROOT/%_bindir"

%files
%libraries_path
%_bindir/get-test-deps

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 10 2023 Andrei Stepanov <astepano@redhat.com> - 0.7-7
- Tune License entry.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Andrei Stepanov <astepano@redhat.com> - 0.7-1
- Build with the latest merged PRs.

* Fri Feb 12 2021 Andrei Stepanov <astepano@redhat.com> - 0.6-1
- Build with the latest merged PRs.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Andrei Stepanov <astepano@redhat.com> - 0.5-1
- Build with the latest merged PRs.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Andrei Stepanov <astepano@redhat.com> - 0.4-2
- Build with AutoReq: no

* Fri Mar 22 2019 Andrei Stepanov <astepano@redhat.com> - 0.4-1
- Build with the latest merged PRs.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Andrei Stepanov <astepano@redhat.com> - 0.3-1
- Build with the latest merged PRs.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Andrei Stepanov <astepano@redhat.com> - 0.2-1
- RPM package for Fedora/EPEL repo.
