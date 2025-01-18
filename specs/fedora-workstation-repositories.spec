Name:		fedora-workstation-repositories
Version:	38
Release:	7%{?dist}
Summary:	Repository files for searchable repositories

License:	MIT
URL:		https://fedoraproject.org/wiki/Workstation/Third_Party_Software_Repositories
# Only available for x86_64
Source0:	_copr:copr.fedorainfracloud.org:phracek:PyCharm.repo
# Only available for x86_64
Source1:	google-chrome.repo
# Only available for aarch64, armfp, ppc64le, x86_64
Source2:	rpmfusion-nonfree-nvidia-driver.repo
# Only available for x86_64
Source3:	rpmfusion-nonfree-steam.repo

# For rpmfusions-nonfree repo keys
Requires:	distribution-gpg-keys

Requires:       fedora-third-party

# For /etc/yum.repos.d
Requires:	fedora-repos

%description
Repository files that make some select non-Fedora software available
via search in gnome-software.

%prep

%build
# Hook up the repositories to the global third-party enablement toggle
tee -a >> fedora-workstation.conf << EOF
%ifarch x86_64
[google-chrome]
type=dnf

[copr:copr.fedorainfracloud.org:phracek:PyCharm]
type=dnf

[rpmfusion-nonfree-steam]
type=dnf

%endif
%ifarch aarch64 ppc64le x86_64
[rpmfusion-nonfree-nvidia-driver]
type=dnf
%endif
EOF

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
%ifarch x86_64
cp %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
%endif
%ifarch aarch64 ppc64le x86_64
cp %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
%endif
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/fedora-third-party/conf.d
cp fedora-workstation.conf $RPM_BUILD_ROOT%{_prefix}/lib/fedora-third-party/conf.d/

%files
%ifarch x86_64
%config(noreplace) %{_sysconfdir}/yum.repos.d/_copr:copr.fedorainfracloud.org:phracek:PyCharm.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/google-chrome.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-steam.repo
%endif
%ifarch aarch64 ppc64le x86_64
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-nvidia-driver.repo
%endif
%{_prefix}/lib/fedora-third-party/conf.d/*.conf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Tomas Popela <tpopela@redhat.com> - 38-1
- Fix the PyCharm COPR repo file
- Resolves: rhbz#2063046
- Fix the license
- Resolves: rhbz#2036071
- Make the package archful as all of the repositories doesn't contain packages
  for all architectures that Fedora supports
- Resolves: rhbz#2093558

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 13 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 35-3
- Use HTTPS for google-chrome repository

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 2 2021 Owen Taylor <otaylor@redhat.com> - 35-1
- https://fedoraproject.org/wiki/Changes/Third_Party_Software_Mechanism

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 32-2
- Temporarily revert filtered flathub remote

* Fri Oct 04 2019 Matthias Clasen <mclasen@redhat.com> - 32-1
- Add a filtered flathub remote

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 31-1
- Add skip_if_unavailable=True to all third party repos (#1750414)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Stephen Gallagher <sgallagh@redhat.com> - 29-1
- Make repo files %%config(noreplace) so they aren't clobbered on upgrade if
  they have been modified (such as being enabled).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Kalev Lember <klember@redhat.com> - 28-1
- Add rpmfusion-nonfree-nvidia-driver.repo and rpmfusion-nonfree-steam.repo

* Thu Apr 05 2018 Kalev Lember <klember@redhat.com> - 25-5
- Add URL that points to a Workstation third party software wiki page

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 27 2016 Matthias Clasen <mclasen@redhat.com> - 25-1
- Add the Google Chrome repository

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun  8 2015 Matthias Clasen <mclasen@redhat.com>
- Initial packaging

