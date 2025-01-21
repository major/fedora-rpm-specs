# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
%global macrosdir       %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global rrcdir          %_libexecdir

Name:           scl-utils-build-helpers
Version:        0
Release:        21%{?dist}
Summary:        RPM macros and scripts for SCL maintainers

BuildArch:      noarch

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/sclorg/scl-utils-build-helpers

Source0:        README.md
Source1:        COPYING
Source100:      scl-helper-wrap-bin.sh
Source101:      macros.scl-build-helpers

Requires:       scl-utils-build


%description
Several RPM macros and convenience scripts to make the maintenance of packages
for Software Collections easier.  The aim is to move as much duplicated code as
possible into one (dedicated) place.


%prep
%setup -c -T


%build


%install
# definitions
%global wrap_script %rrcdir/%(basename %SOURCE100)
%global macros %macrosdir/%(basename %SOURCE101)
substitutions=(
    -e 's|@SCRIPT_WRAP@|%wrap_script|g'
    -e 's|@MACROS@|%macros|g'
    -e 's|@GENERATOR@|%name-%version-%release|g'
)

# installation
install -p -m 644 %SOURCE0 .
install -p -m 644 %SOURCE1 .
mkdir -p %buildroot%rrcdir
mkdir -p %buildroot%macrosdir
sed "${substitutions[@]}" %{SOURCE100} > %buildroot%wrap_script
sed "${substitutions[@]}" %{SOURCE101} > %buildroot%macros


%files
%license COPYING
%doc README.md
%attr(755,-,-) %wrap_script
%macros


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 4 2024 Miroslav Suchý <msuchy@redhat.com> - 0-20
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Pavel Raiskup <praiskup@redhat.com> - 0-8
- package for Fedora, review fixes (rhbz#1679474)

* Fri Jun 23 2017 Honza Horak <hhorak@redhat.com> - 0-7
- use epoch if set for dependencies

* Wed Jun 21 2017 Pavel Raiskup <praiskup@redhat.com> - 0-6
- fix docs, by Lenka Špačková

* Wed Jun 21 2017 Pavel Raiskup <praiskup@redhat.com> - 0-5
- add metapackage macros and fix some wording

* Mon Jun 19 2017 Pavel Raiskup <praiskup@redhat.com> - 0-4
- bugfixes, don't install wrapper for the directory itself, fix one-hit macro

* Mon Jun 19 2017 Pavel Raiskup <praiskup@redhat.com> - 0-2
- more automation macros

* Fri Jun 16 2017 Pavel Raiskup <praiskup@redhat.com> - 0-1
- add license

* Fri Jun 16 2017 Pavel Raiskup <praiskup@redhat.com> - 0-0
- initial version
